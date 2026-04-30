# OpenClaw QQ Bot 语音消息发送

> **适用场景：** 将 TTS 生成的语音发送到 OpenClaw QQ Bot（私聊或群聊）。

OpenClaw QQBot 插件通过 `<qqvoice>` 标签机制发送语音消息：在回复内容中包含此标签，插件自动完成 WAV → SILK 转码、上传和发送。

> **安全策略：** 安全策略要求本地文件必须位于 `~/.openclaw/media/` 目录下才允许上传。`openclaw_qqbot_send_audio.sh` 会将音频文件复制到 `~/.openclaw/media/qqbot/tts/` 并输出正确的 `<qqvoice>` 标签。

## 环境依赖

无需额外环境变量（AppID 和 ClientSecret 由 OpenClaw QQBot 插件统一管理）。

| 依赖      | 说明         | 必需 |
| --------- | ------------ | ---- |
| `bash`    | 运行脚本     | 是   |

## 用法

### 私聊 / 群聊发送

```bash
# 1. 生成语音
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "好的，马上就好！" \
  --voice "冰糖" \
  --output /tmp/mimo-v2.5-tts/voice.wav

# 2. 复制到媒体目录，获取 <qqvoice> 标签
bash $SKILLS_PATH/mimo-v2-5-tts/scripts/openclaw_qqbot_send_audio.sh /tmp/mimo-v2.5-tts/voice.wav
```

脚本输出示例：

```
<qqvoice>/Users/xxx/.openclaw/media/qqbot/tts/voice.wav</qqvoice>
```

将此标签包含在回复内容中即可，OpenClaw 插件将自动发送为语音消息。

### 与文字一起发送

如需同时发送文字和语音，将文字与标签放在同一条回复里：

```
好的，我来朗读这段内容：
<qqvoice>/Users/xxx/.openclaw/media/qqbot/tts/voice.wav</qqvoice>
```

> **注意：** 发送语音时不要在文字部分重复语音中已朗读的内容。

## 脚本内部流程

`openclaw_qqbot_send_audio.sh` 内部流程：检查文件 → 复制到 `~/.openclaw/media/qqbot/tts/` → 输出 `<qqvoice>` 标签。

OpenClaw 收到标签后的流程：`WAV → SILK (ffmpeg/WASM)` → `上传富媒体（file_data base64）` → `发送 media 消息（type=7）`。
