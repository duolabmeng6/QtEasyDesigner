# Qt Esay Designer

qt 窗口设计器 基于易函数的理念设计和开发

* 仍在开发中~

![](images/img1.png)
![](images/img2.png)


# 软件下载

由于在积极开发所以请及时关注新版本发布哦

支持 MacOS Window

[点击这里下载Qt视窗设计器](https://github.com/duolabmeng6/QtEsayDesigner/releases)

## 配置 pycharm 插件

提供 pycharm 插件以方便使用  [点击下载 QtEsayDesigner.IDE.jar](https://github.com/duolabmeng6/QtEsayDesigner/releases/download/0.0.13/QtEsayDesigner.IDE.jar
)

mac配置路径 `/Applications/QtEsayDesigner.app/Contents/MacOS/QtEsayDesigner`

window配置路径为 `exe文件路径`

# 使用帮助

本设计器所生成的 `ui_启动窗口.py` 可以兼容原版qt的按正常规则引入界面即可

qtefun 的模块下载后放置到项目目录 https://github.com/duolabmeng6/qtefun

后续会提供 `pip install qtefun` 或者直接写到项目目录的形式~

```text
.
├── app_启动窗口.py 主入口文件
├── qtefun  这是中文组件库
├── ui_启动窗口.py ui设计py文件
└── 启动窗口.json ui配置文件

```

# 参与开发 

## 开发环境 配置

```shell
git clone https://github.com/duolabmeng6/QtEsayDesigner.git --recurse-submodules
```

* 子模块 qtefun 这是组件库是中文的命令 https://github.com/duolabmeng6/qtefun
* 子模块 pyefun 这是各种功能类的中文命令 https://github.com/duolabmeng6/pyefun


需要开发的
* qt_esay_model/组件库 这里是指软件中的 组件箱 配置好即可出现在组件箱
* qtefun/组件 这里是组件的中文命令 这个库可以用于官方的qt设计器




