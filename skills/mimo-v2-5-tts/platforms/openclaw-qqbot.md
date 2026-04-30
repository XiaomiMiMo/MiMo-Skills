# OpenClaw QQ Bot 语音消息发送

> **适用场景：** 将 TTS 生成的语音发送到 OpenClaw QQ Bot（私聊或群聊）。

OpenClaw QQBot 插件通过 `<qqvoice>` 标签机制发送语音消息：在回复内容中包含此标签，插件自动完成 WAV → SILK 转码、上传和发送。

> **安全策略：** 本地文件必须位于 `~/.openclaw/media/` 目录下才允许上传。直接将 TTS 输出到该目录即可，无需额外脚本。

## 用法

### 私聊 / 群聊发送

将 TTS 的 `--output` 直接指向 `~/.openclaw/media/qqbot/tts/`，然后在回复中写 `<qqvoice>` 标签：

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "好的，马上就好！" \
  --voice "冰糖" \
  --output ~/.openclaw/media/qqbot/tts/voice.wav
```

在回复内容中包含：

```
<qqvoice>/Users/xxx/.openclaw/media/qqbot/tts/voice.wav</qqvoice>
```

> **注意：** 路径必须是绝对路径。`~` 在标签内不会展开，需要替换为实际路径（如 `/Users/xxx`）。

### 与文字一起发送

```
好的，我来朗读这段内容：
<qqvoice>/Users/xxx/.openclaw/media/qqbot/tts/voice.wav</qqvoice>
```

> **注意：** 发送语音时不要在文字部分重复语音中已朗读的内容。

## OpenClaw 处理流程

`WAV → SILK (ffmpeg/WASM)` → `上传富媒体（file_data base64）` → `发送 media 消息（type=7）`
