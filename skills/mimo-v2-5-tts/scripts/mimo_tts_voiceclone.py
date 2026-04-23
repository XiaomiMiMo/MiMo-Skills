#!/usr/bin/env python3
"""MiMo V2.5 TTS — 音频样本复刻音色。

模型: mimo-v2.5-tts-voiceclone
支持: 通过音频样本精准复刻音色、自然语言风格控制（导演模式）

Requires:
    pip install openai
    export MIMO_API_KEY=...
"""

import argparse
import base64
import os
import sys
from pathlib import Path

from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MiMo V2.5 TTS 音频样本复刻音色")
    parser.add_argument("--text", required=True, help="要合成的文本")
    parser.add_argument(
        "--voice-file",
        required=True,
        help="音色样本音频文件路径（mp3/wav）",
    )
    parser.add_argument(
        "--context",
        default="",
        help="自然语言风格控制指令（导演模式）",
    )
    parser.add_argument(
        "--output",
        default="tmp/mimo-v2.5-tts/voiceclone.wav",
        help="输出 wav 路径",
    )
    return parser.parse_args()


def build_client() -> OpenAI:
    api_key = os.environ.get("MIMO_API_KEY")
    if not api_key:
        print("MIMO_API_KEY is not set", file=sys.stderr)
        sys.exit(1)
    return OpenAI(api_key=api_key, base_url="https://api.xiaomimimo.com/v1")


def encode_voice_file(file_path: str) -> str:
    """Encode a voice sample file to base64 with MIME prefix."""
    path = Path(file_path)
    if not path.exists():
        print(f"Voice file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    suffix = path.suffix.lower()
    mime_map = {".mp3": "audio/mpeg", ".wav": "audio/wav"}
    mime_type = mime_map.get(suffix)
    if not mime_type:
        print(f"Unsupported audio format: {suffix}. Use mp3 or wav.", file=sys.stderr)
        sys.exit(1)

    data = path.read_bytes()
    if len(data) > 10 * 1024 * 1024:
        print("Voice file too large (max 10 MB)", file=sys.stderr)
        sys.exit(1)

    b64 = base64.b64encode(data).decode("utf-8")
    return f"data:{mime_type};base64,{b64}"


def main() -> None:
    args = parse_args()
    client = build_client()

    messages = []
    if args.context:
        # 使用 user 文本来进行自然语言风格控制
        messages.append({"role": "user", "content": args.context})
    # role: assistant 中的文本会被合成
    messages.append({"role": "assistant", "content": args.text})

    completion = client.chat.completions.create(
        model="mimo-v2.5-tts-voiceclone",
        messages=messages,
        audio={
            "format": "wav",
            "voice": encode_voice_file(args.voice_file),
        },  # voice: DataURL 编码的音频样本
    )

    message = completion.choices[0].message
    if message.audio is None or not getattr(message.audio, "data", None):
        print("No audio data returned", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(base64.b64decode(message.audio.data))
    print(output_path)


if __name__ == "__main__":
    main()
