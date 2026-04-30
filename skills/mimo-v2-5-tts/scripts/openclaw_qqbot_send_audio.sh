#!/usr/bin/env bash
# openclaw_qqbot_send_audio.sh — 将 WAV 音频复制到 OpenClaw QQ Bot 媒体目录并输出 <qqvoice> 标签
#
# OpenClaw QQBot 插件通过 <qqvoice> 标签机制发送语音消息：
#   - 安全策略要求本地文件必须在 ~/.openclaw/media/ 下才可上传
#   - WAV 格式由插件内部自动转换为 SILK 后上传，无需手动转码
#
# 位置参数：
#   $1  音频文件路径（wav）
#   $2  （可选）目标子目录名，默认 tts（文件将放入 ~/.openclaw/media/qqbot/<子目录>/）
#
# 用法：
#   bash openclaw_qqbot_send_audio.sh <audio.wav>
#   bash openclaw_qqbot_send_audio.sh <audio.wav> <subdir>
#
# 输出：
#   <qqvoice>/absolute/path/to/file.wav</qqvoice>
#   将此标签包含在回复内容中，OpenClaw QQBot 插件将自动上传并发送为语音消息。

set -euo pipefail

# ── 参数检查 ──────────────────────────────────────────────

if [[ $# -lt 1 ]]; then
  echo "用法: $0 <audio.wav> [subdir]" >&2
  exit 1
fi

AUDIO_FILE="$1"
SUBDIR="${2:-tts}"

if [[ ! -f "$AUDIO_FILE" ]]; then
  echo "错误: 文件不存在 — $AUDIO_FILE" >&2
  exit 1
fi

# ── 目标目录：~/.openclaw/media/qqbot/<subdir>/ ──────────

MEDIA_DIR="${HOME}/.openclaw/media/qqbot/${SUBDIR}"
mkdir -p "$MEDIA_DIR"

# ── 复制文件到媒体目录 ───────────────────────────────────

FILENAME="$(basename "$AUDIO_FILE")"
DEST="${MEDIA_DIR}/${FILENAME}"

# 若目标已存在且内容相同，则直接使用（避免重复复制）
if [[ -f "$DEST" ]] && cmp -s "$AUDIO_FILE" "$DEST"; then
  :  # 文件一致，无需复制
else
  cp "$AUDIO_FILE" "$DEST"
fi

# ── 输出 <qqvoice> 标签 ──────────────────────────────────

echo "<qqvoice>${DEST}</qqvoice>"
