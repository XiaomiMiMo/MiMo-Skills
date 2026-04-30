# mimo_tts.py — 预置音色语音合成

模型：`mimo-v2.5-tts`
功能：使用内置精品音色合成语音，支持自然语言风格控制、音频标签控制、唱歌。

## 参数

| 参数       | 必需 | 说明                                          |
| ---------- | ---- | --------------------------------------------- |
| `--text`   | 是   | 要合成的文本                                  |
| `--voice`  | 是   | 预置音色 ID（见下方音色列表）                 |
| `--context`| 否   | 自然语言风格控制指令（导演模式）              |
| `--output` | 否   | 输出 WAV 路径（默认：`tmp/mimo-v2.5-tts/output.wav`） |

### 可用音色

| Voice ID | 语言    | 性别   | 风格          |
| -------- | ------- | ------ | ------------- |
| `冰糖`   | 中文    | 女性   | 活泼少女      |
| `茉莉`   | 中文    | 女性   | 知性女声      |
| `苏打`   | 中文    | 男性   | 阳光少年      |
| `白桦`   | 中文    | 男性   | 成熟男声      |
| `Mia`    | English | Female | Lively girl   |
| `Chloe`  | English | Female | Sweet Dreamy  |
| `Milo`   | English | Male   | Sunny boy     |
| `Dean`   | English | Male   | Steady Gentle |

## 基础用法

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "你好，今天天气真不错。" \
  --voice "冰糖"
```

## 自然语言风格控制（--context）

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --context "用温柔的语气，语速稍慢" \
  --text "没关系，慢慢来，我等你。" \
  --voice "冰糖" \
  --output tmp/mimo-v2.5-tts/comfort.wav
```

## 音频标签控制

在文本中插入括号标签控制局部语气：

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "（紧张，深呼吸）呼……冷静，冷静。不就是一个面试吗……（小声）哎呀，领带歪没歪？" \
  --voice "冰糖" \
  --output tmp/mimo-v2.5-tts/interview.wav
```

## 唱歌

文本开头必须加 `(唱歌)` 标签，歌词要完整：

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "(唱歌)原谅我这一生不羁放纵爱自由，也会怕有一天会跌倒，Oh no。背弃了理想，谁人都可以，哪会怕有一天只你共我。" \
  --voice "冰糖" \
  --output tmp/mimo-v2.5-tts/singing.wav
```

## 英文 + 音频标签

```bash
python3 $SKILLS_PATH/mimo-v2-5-tts/scripts/mimo_tts.py \
  --text "I just... (sighs deeply) I don't know anymore. (suddenly firm) But I won't give up!" \
  --voice "Mia" \
  --output tmp/mimo-v2.5-tts/english.wav
```

## 长文本处理

V2.5 支持较长文本，**几乎所有场景都建议一次性生成**。仅当文本超过 **2500 字**时，才需分段合成后用 ffmpeg 拼接：

```bash
# 各段独立生成后拼接
echo "file '/tmp/mimo-v2.5-tts/part1.wav'" > /tmp/mimo-v2.5-tts/list.txt
echo "file '/tmp/mimo-v2.5-tts/part2.wav'" >> /tmp/mimo-v2.5-tts/list.txt
ffmpeg -y -f concat -safe 0 -i /tmp/mimo-v2.5-tts/list.txt -c copy /tmp/mimo-v2.5-tts/combined.wav
```

## 注意事项

- TTS 有随机性，同样输入效果可能不同，用户需要时可多生成几次供挑选。
- 唱歌歌词必须完整，残缺歌词会导致跑调、效果变差。
- 括号标签内只能写能发出声音的内容（语气、情绪、叹气等），不能写身体动作。
