<div align="center">
  <picture>
    <source srcset="https://github.com/XiaomiMiMo/MiMo/raw/main/figures/Xiaomi_MiMo_darkmode.png?raw=true" media="(prefers-color-scheme: dark)">
    <img src="https://github.com/XiaomiMiMo/MiMo/raw/main/figures/Xiaomi_MiMo.png?raw=true" width="60%" alt="Xiaomi-MiMo" />
  </picture>
</div>

> 小米 MiMo 系列 Agent Skills。请在 <a href="https://platform.xiaomimimo.com/" target="_blank">🎨 Xiaomi MiMo 开放平台</a> 获取 API KEY。

## Skills

| Skill | 描述 | 许可证 |
|-------|------|--------|
| `mimo-v2-5-tts` | MiMo V2.5 TTS 语音合成。支持预置音色、音色设计、音色克隆、情绪风格、方言、唱歌。所有模式支持自然语言控制（导演模式）和音频标签控制。 | MIT |

## 安装

### npx（推荐）

```bash
npx skills add XiaomiMiMo/MiMo-Skills
```

常用选项：

```bash
# 列出可用的 skills（不安装）
npx skills add XiaomiMiMo/MiMo-Skills --list

# 安装到指定 agent
npx skills add XiaomiMiMo/MiMo-Skills -a claude-code -a opencode

# 全局安装（用户级）
npx skills add XiaomiMiMo/MiMo-Skills -g

# 安装指定 skill
npx skills add XiaomiMiMo/MiMo-Skills --skill mimo-v2-5-tts

# 非交互模式（适用于 CI/CD）
npx skills add XiaomiMiMo/MiMo-Skills -g -a claude-code -y
```

### 手动安装

```bash
git clone https://github.com/XiaomiMiMo/MiMo-Skills.git
ln -s MiMo-Skills/skills/* ~/.openclaw/skills/
# ln -s MiMo-Skills/skills/* ~/.hermes/skills/
# ln -s MiMo-Skills/skills/* ~/.config/opencode/skills/
# ln -s MiMo-Skills/skills/* ~/.claude/skills/
# ...
```

## 环境变量

| 变量 | 描述 | 必需 |
|------|------|------|
| `MIMO_API_KEY` | MiMo API 密钥 | 是 |
| `FEISHU_APP_ID` | 飞书 App ID（用于语音消息发送） | 否 |
| `FEISHU_APP_SECRET` | 飞书 App Secret（用于语音消息发送） | 否 |

## 许可证

[MIT](./LICENSE)
