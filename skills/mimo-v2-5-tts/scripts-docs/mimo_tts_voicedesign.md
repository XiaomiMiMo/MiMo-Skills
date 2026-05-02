# mimo_tts_voicedesign.py — 文本描述定制音色

模型：`mimo-v2.5-tts-voicedesign`
功能：通过文本描述自动生成音色，无需预置音色 ID，风格完全由描述驱动。

## 参数

| 参数        | 必需 | 说明                                                   |
| ----------- | ---- | ------------------------------------------------------ |
| `--text`    | 是   | 要合成的文本                                           |
| `--context` | 是   | 音色描述 / 自然语言风格控制指令（同时控制音色和风格）  |
| `--output`  | 否   | 输出 WAV 路径（默认：`tmp/mimo-v2.5-tts/voicedesign.wav`） |

> **注意：** `--context` 对 voicedesign 是**必需参数**，既描述音色本身，也可描述风格。

## 基础用法

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voicedesign.py \
  --context "Give me a young male tone." \
  --text "Yes, I had a sandwich." \
  --output tmp/mimo-v2.5-tts/voicedesign.wav
```

## 音色描述写作指南

音色描述是嗓子的身份卡。**只描写声音本身**，不写场景、不写动作。

**必写项：**
1. 年龄段 + 性别（决定基频）
2. 声音质感（气息、共鸣、音色底色）
3. 语速节奏
4. 情绪底色

**写作样例：**

```
中年男性，节奏极快，情绪高亢，拍卖师风格。吐字连珠，带抑扬顿挫与紧迫感。

青年男性，电竞解说风格，语速极快且连贯，带明显气口和爆发性强调，兴奋时声音上扬尖锐。

中年男性，法庭陈词风格，声线沉稳偏正式，吐字工整字字顿挫，情绪克制但每个词都很重。
```

**中文详细示例：**

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voicedesign.py \
  --context "中年女性，美食评论家风格，语调绵柔富感染力，描述时带夸张的回味与陶醉感，偶尔闭眼吸气。" \
  --text "[吸气]唔——这一口下去…[停顿]整个舌尖都被包住了。先是焦糖的甜，紧接着[强调]一点点[停顿]刚好的咸，在后味里慢慢铺开。[叹气]说真的，我已经[轻声]好久[停顿]没吃到这么用心的甜点了。" \
  --output tmp/mimo-v2.5-tts/foodcritic.wav
```

## 「设计 → 克隆」工作流

先用 voicedesign 生成满意的音色，再将该音频用 `mimo_tts_voiceclone.py` 复刻到其他文本：

```bash
# Step 1：设计音色
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voicedesign.py \
  --context "青年女性，动漫配音风格，声音清甜明亮，语速稍快，语调活泼跳跃。" \
  --text "你好，很高兴认识你！" \
  --output tmp/mimo-v2.5-tts/design_sample.wav

# Step 2：将设计音色克隆到新文本
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts_voiceclone.py \
  --voice-file tmp/mimo-v2.5-tts/design_sample.wav \
  --text "今天的天气真好，我们去公园走走吧！" \
  --output tmp/mimo-v2.5-tts/cloned_result.wav
```

## 注意事项

- voicedesign **不支持音频标签控制**（如 `[停顿]`、`[叹气]` 等），如需精细控制请改用更详细的 `--context` 描述。
- 描述不要用真实演员或 IP 角色名（版权 + 泛化效果差）。
- 描述不写场景（"在发布会"）或身体动作（"她走上舞台"）。
- TTS 有随机性，同样描述每次生成效果可能不同。
