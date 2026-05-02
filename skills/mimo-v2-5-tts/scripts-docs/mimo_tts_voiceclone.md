# mimo_tts_voiceclone.py — 音频样本复刻音色

模型：`mimo-v2.5-tts-voiceclone`
功能：通过上传音频样本精准复刻说话人的音色，可叠加自然语言风格控制（导演模式）。

## 参数

| 参数           | 必需 | 说明                                                         |
| -------------- | ---- | ------------------------------------------------------------ |
| `--text`       | 是   | 要合成的文本                                                 |
| `--voice-file` | 是   | 音色样本音频文件路径（mp3 或 wav，Base64 后不超过 10 MB）    |
| `--context`    | 否   | 自然语言风格控制指令（导演模式）                             |
| `--output`     | 否   | 输出 WAV 路径（默认：`tmp/mimo-v2.5-tts/voiceclone.wav`）    |

## 基础用法

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voiceclone.py \
  --voice-file voice.mp3 \
  --text "Yes, I had a sandwich." \
  --output tmp/mimo-v2.5-tts/voiceclone.wav
```

## 音色克隆 + 导演模式

在复刻音色的同时，用 `--context` 控制语气和情绪：

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voiceclone.py \
  --voice-file voice.mp3 \
  --context "用温柔的语气，语速稍慢" \
  --text "没关系，慢慢来，我等你。" \
  --output tmp/mimo-v2.5-tts/voiceclone_director.wav
```

## 导演模式完整示例

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voiceclone.py \
  --voice-file speaker.wav \
  --context "角色：百年门阀的现任大当家，冷硬、疏离、极具威压。
场景：在祠堂阴影里，用最冷硬的态度拒绝对方的告白。
指导：极慢语速，每个字像在舌尖滚过才吐出，句间留长空白。实音重且硬，某些尾音带极轻的气声收束。" \
  --text "你跑来这里……是觉得，凭一腔热血，就能改变什么吗。" \
  --output tmp/mimo-v2.5-tts/dramatic.wav
```

## 接收「设计 → 克隆」工作流输入

voicedesign 生成的音频可直接作为 voiceclone 的样本：

```bash
# 上游：用 voicedesign 生成音色样本
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voicedesign.py \
  --context "中年男性，播音员风格，沉稳清晰，字正腔圆。" \
  --text "这是一段音色样本。" \
  --output tmp/mimo-v2.5-tts/anchor_sample.wav

# 下游：用 voiceclone 将该音色应用到新文本
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voiceclone.py \
  --voice-file tmp/mimo-v2.5-tts/anchor_sample.wav \
  --text "各位晚上好，欢迎收看今天的节目。" \
  --output tmp/mimo-v2.5-tts/anchor_final.wav
```

## 注意事项

- 音色样本 Base64 编码后**不超过 10 MB**（约对应 3-5 分钟的 mp3/wav）。
- 仅支持 **mp3** 和 **wav** 格式。
- 样本时长建议 5-30 秒，内容清晰无背景噪音，效果最佳。
- `--context` 影响语气风格，不改变音色本身的音质。
- TTS 有随机性，同样参数效果可能不同，可多生成几次供挑选。
