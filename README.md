# 突然之间发现我已恋上你（Ren'Py 移植版）

视觉小说《突然之间发现我已恋上你》的 Ren'Py 重制版，由原 NScripter 脚本自动转换而来。

## 运行方式

1. 安装 [Ren'Py](https://www.renpy.org/) 8.5 或更高版本。
2. 用 Ren'Py 启动器打开本目录（`tulian/`），点击「启动项目」即可。

或者用命令行直接运行：

```bash
renpy.sh /path/to/tulian
```

## 目录结构

```
tulian/
├── game/
│   ├── script.rpy      # 转换后的剧情脚本（158 个标签、约 3 万句台词）
│   ├── screens.rpy     # 界面定义（主菜单、设置、存档、历史记录等）
│   ├── gui.rpy         # GUI 主题配置（配色、字体、尺寸）
│   ├── options.rpy     # 游戏选项（分辨率、语言、存档目录等）
│   ├── default.ttf     # 中文字体（MicroHei）
│   ├── images/         # 图片资源（7845 张）
│   ├── bgm/            # 背景音乐（34 首）
│   ├── voice/          # 角色语音（10699 条）
│   ├── se/             # 音效（600 个）
│   └── tl/chinese/     # 简体中文翻译（覆盖内置英文界面）
└── .gitignore
```

## 技术说明

### 资源转换

- 原游戏为 NScripter 引擎（`0.txt` + `arc.nsa` 系列）。
- 使用 `nsaout` 工具解包 `.nsa` 归档，得到图片、音频资源。
- 脚本由 Python 转换器（`convert.py`）自动翻译为 Ren'Py 格式。

### 关键实现细节

- **分辨率**：800×450（16:9），与原版一致。
- **立绘定位**：按 ONScripter `lsp2` 的中心坐标语义，用 `Transform` 精确还原。
- **背景**：4:3 素材在 16:9 屏幕居中裁剪显示。
- **语音**：`config.voice_filename_format` 自动补全 `voice/` 前缀。
- **字体**：全界面使用 `default.ttf`（支持简体中文、日文假名）。

### 已知问题

- 原脚本中 2 处 `goto *L_ry_ei_com06_goryu` 跳转目标未定义（原脚本自身 bug），已改为顺序执行。
- 原脚本有 2 处路线选择文字为 Shift-JIS 编码（其余为 GB18030），转换时已单独修正。
- 立绘坐标按原算法还原，个别复杂立绘叠加场景可能有细微偏移。

## 版权声明

游戏原作版权归原作者所有。本项目仅用于学习研究 Ren'Py 移植技术，请勿用于商业用途。
