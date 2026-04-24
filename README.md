<div align="center">
  <picture>
    <source srcset="https://github.com/XiaomiMiMo/MiMo/raw/main/figures/Xiaomi_MiMo_darkmode.png?raw=true" media="(prefers-color-scheme: dark)">
    <img src="https://github.com/XiaomiMiMo/MiMo/raw/main/figures/Xiaomi_MiMo.png?raw=true" width="60%" alt="Xiaomi-MiMo" />
  </picture>
</div>

> Agent skills for Xiaomi MiMo series. Get your API key at <a href="https://platform.xiaomimimo.com/" target="_blank">🎨 Xiaomi MiMo Open Platform</a>.

[中文版](./README_zh.md)

## Skills

| Skill | Description | License |
|-------|-------------|---------|
| `mimo-v2-5-tts` | MiMo V2.5 TTS voice synthesis. Supports preset voices, voice design, voice cloning, emotion styles, dialects, and singing. Supports natural language control, Director Mode, and audio tag control. | MIT |

## Installation

### npx (Recommended)

```bash
npx skills add XiaomiMiMo/MiMo-Skills
```

Options:

```bash
# List available skills without installing
npx skills add XiaomiMiMo/MiMo-Skills --list

# Install to specific agents
npx skills add XiaomiMiMo/MiMo-Skills -a claude-code -a opencode

# Install globally (user-level)
npx skills add XiaomiMiMo/MiMo-Skills -g

# Install specific skills by name
npx skills add XiaomiMiMo/MiMo-Skills --skill mimo-v2-5-tts

# Non-interactive (CI/CD friendly)
npx skills add XiaomiMiMo/MiMo-Skills -g -a claude-code -y
```

### Manual

```bash
git clone https://github.com/XiaomiMiMo/MiMo-Skills.git ~/.mimo-skills
ln -s ~/.mimo-skills/skills/* ~/.hermes/skills/
# ln -s ~/.mimo-skills/skills/* ~/.openclaw/skills/
# ln -s ~/.mimo-skills/skills/* ~/.config/opencode/skills/
# ln -s ~/.mimo-skills/skills/* ~/.claude/skills/
# ...
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `MIMO_API_KEY` | MiMo API key | Yes |
| `FEISHU_APP_ID` | Feishu App ID (for voice message sending) | Optional |
| `FEISHU_APP_SECRET` | Feishu App Secret (for voice message sending) | Optional |

## License

[MIT](./LICENSE)
