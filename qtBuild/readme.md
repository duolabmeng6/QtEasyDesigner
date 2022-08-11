<h1 align="center">Auto PY to APP</h1>
<p align="center">一个.py到.exe或.app的可视化转换器，使用简单的图形界面和Python中的<a href="https://www.pyinstaller.org/">PyInstaller</a>。</p>

<p align="center">
<img src="https://myimages.25531.com/20220728/iShot_2022-07-28_20.48.17.png" style="zoom:50%;"  alt="Empty interface" />
</p>

<p align="center">
    <a href="https://github.com/jiayouzl/auto-py-to-app/releases"><img src="https://img.shields.io/github/release/jiayouzl/auto-py-to-app/all.svg" alt="GitHub version"></a>
    <a href="https://github.com/jiayouzl/auto-py-to-app/actions"><img src="https://img.shields.io/endpoint.svg?url=https://actions-badge.atrox.dev/atrox/sync-dotenv/badge" alt="GitHub Actions"></a>
    <a href="https://github.com/jiayouzl/auto-py-to-app/blob/master/LICENSE"><img src="https://img.shields.io/github/license/jiayouzl/auto-py-to-app.svg" alt="License"></a>
    <a href="https://pyinstaller.readthedocs.io/en/stable/requirements.html"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey" alt="Supported Platforms"></a>
</p>

## 程序简介

由于我定期要编译的软件比较多，一直在找一款图形化调用`PyInstaller`的软件方便管理，之前找到一款`auto-py-to-exe`我看用的人也挺多，但在苹果M1芯片下的macOS有个会导致无法使用的BUG，索性就自己抽空开发一个出来并开源与大家共享。

> 常用的几个命令参数都已经在v0.0.1版中做了支持，后续也会陆续新增其他参数的支持，也欢迎大家Fork一起改进升级。

> Windows与Linux版本会在近期马上发布。

## 功能简介
- 自定义程序名称、图标。
- 打包类型、窗口类型的两种模式的切换。
- 资源文件支持单文件与整个文件夹的导入。
- 自定义输出目录，方便管理。
- 配置文件支持导出、导入。
- 支持单独生成编译命令与直接在本程序内进行编译打包。

## 问题提交
如在使用中碰到bug请至[Issues](https://github.com/jiayouzl/auto-py-to-app/issues)提交。

## 开发环境

1. macOS `12.5` / Windows 10 `21H2` / Ubuntu Desktop `22.04`
2. Python `3.9.13`
3. PyCharm `2022.2`
4. PySide6 / Designer

## 编译环境
* macOS Monterey `12.5` `arm64`
* macOS Monterey `12.5` `intel 64-bit`
* Windows `10` `21H2`
* Ubuntu Desktop `22.04` `LTS`

## 下载/安装

- From release: [https://github.com/jiayouzl/auto-py-to-app/releases](https://github.com/jiayouzl/auto-py-to-app/releases)

## 注意事项
> 从2020年8月9日发布的 [PyInstaller V4.0](https://github.com/pyinstaller/pyinstaller/releases/tag/v4.0) 开始，不再支持Python2.7；不过，通过安装旧版本的PyInstaller，您仍然可以在Python2.7中使用该工具。
[PyInstaller V3.6](https://github.com/pyinstaller/pyinstaller/releases/tag/v3.6) 是支持Python2.7的最后一个版本；要安装此版本，请先卸载任何现有版本的PyInstaller，然后执行：`pip install pyinstaller==3.6`。

## 文件说明
```
.
├── main.py                         程序入口源代码
├── requirements.txt                依赖组件库
├── ui.py                           UI设计PY文件
└── ui.ui                           UI设计Designer文件
```

## License

MIT