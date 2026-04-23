#!/usr/bin/env python3
"""MiMo V2.5 TTS — 预置音色语音合成。

模型: mimo-v2.5-tts
支持: 自然语言风格控制、音频标签控制、唱歌

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

PRESET_VOICES = [
    "冰糖",
    "茉莉",
    "苏打",
    "白桦",
    "Mia",
    "Chloe",
    "Milo",
    "Dean",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MiMo V2.5 TTS 预置音色语音合成")
    parser.add_argument("--text", required=True, help="要合成的文本")
    parser.add_argument(
        "--voice",
        required=True,
        choices=PRESET_VOICES,
        help="预置音色",
    )
    parser.add_argument(
        "--context",
        default="",
        help="自然语言风格控制指令",
    )
    parser.add_argument(
        "--output",
        default="tmp/mimo-v2.5-tts/output.wav",
        help="输出 wav 路径",
    )
    return parser.parse_args()


def build_client() -> OpenAI:
    api_key = os.environ.get("MIMO_API_KEY")
    if not api_key:
        print("MIMO_API_KEY is not set", file=sys.stderr)
        sys.exit(1)
    return OpenAI(api_key=api_key, base_url="https://api.xiaomimimo.com/v1")


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
        model="mimo-v2.5-tts",
        messages=messages,
        audio={"format": "wav", "voice": args.voice},  # voice: 预置音色 ID
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
