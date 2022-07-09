# 用于构建界面代码生成类
import re


class 界面代码生成类:
    头部导包代码 = []
    依赖包 = []
    类名 = "MainWin(QMainWindow)"
    事件绑定代码 = []
    事件绑定代码末尾 = []
    定义函数代码 = []
    末尾代码 = ""
    加载已存在的文件内容 = ""

    def __init__(self):
        pass
        self.依赖包 = []

    def 加入依赖包(self, 包名):
        # 过滤重复
        if 包名 in self.依赖包:
            return
        self.依赖包.append(包名)

    def 加入导包模块头部代码(self, 代码):
        # 过滤重复
        if 代码 in self.头部导包代码:
            return

        self.头部导包代码.append(代码)

    def 加入事件绑定代码(self, 代码, 插入到最后=False):
        if 插入到最后:
            self.事件绑定代码末尾.append(代码)
        else:
            self.事件绑定代码.append(代码)

    def 加入函数定义代码(self, 代码):
        # 获取函数名称 def 启动窗口创建完毕(
        函数名称 = re.search(r"def (.*)\(", 代码).group(1)
        # print("函数名称:", 函数名称)
        if self.加载已存在的文件内容:
            # 如果已经加载了文件内容，则检查是否已经存在该函数
            if 函数名称 in self.加载已存在的文件内容:
                # print(f"插入def并且检查是否存在 {函数名称} 已存在")
                return

        self.定义函数代码.append(代码)

    def 取类初始代码(self, ):
        return f"""
class {self.类名}:
    def __init__(self):
        super().__init__()
"""

    def 删除空行(self, 文本):
        pass
        代码 = re.sub(r"\n\s*\n", "\n", 文本)
        # print(代码)
        return 代码

    def 取头部代码(self):
        pass
        代码 = "# ==导入模块==\n"
        代码 += "\n".join(self.头部导包代码)
        代码 += "\n# ==导入模块==="

        return 代码

    def 删除空白行和空字符(self, 文本):
        代码 = re.sub(r"\n\s*\n", "\n", 文本)
        return 代码

    def 取事件绑定代码(self):
        pass
        # 事件绑定代码 与 事件绑定代码末尾合并
        新组合 = self.事件绑定代码 + self.事件绑定代码末尾
        新组合.insert(0, "# ==绑定事件==")
        新组合.append("# ==绑定事件===")
        新代码 = self.删除空白行和空字符("\n".join(新组合))
        # 在每一行文本前面加入空格
        新代码 = "\n".join(["        " + i for i in 新代码.split("\n")])

        return 新代码

    def 取函数定义代码(self):
        pass
        代码 = "\n".join(self.定义函数代码)
        代码 = self.删除空行(代码)
        代码 = "\n".join(["    " + i for i in 代码.split("\n")])
        return 代码

    def 取末尾代码(self):
        return self.末尾代码

    def 替换导入模块(self, 代码, 替换内容, 模块名称):
        # 使用正则表达式替换 "# ==导入模块开始==" 和 "# ==导入模块结束==" 之间的所有内容
        v = 代码
        开始 = f"\n# =={模块名称}=="
        结束 = f"# =={模块名称}==="

        # 替换内容 = 开始 + "\n" + 替换内容 + "\n" + 缩进 + 结束
        替换内容 = self.删除空行(替换内容)

        v = re.sub(开始 + r'.*' + 结束, 替换内容, v, flags=re.DOTALL)
        return v

    def 生成代码(self):
        print("生成代码")
        if self.加载已存在的文件内容 == "":
            代码 = ""

            代码 += self.取头部代码()  # 导入模块
            代码 += self.取类初始代码()
            代码 += self.取事件绑定代码()  # 绑定事件
            代码 += self.取函数定义代码()  # 函数定义
            代码 += self.取末尾代码()
            return 代码

        原来的内容 = self.加载已存在的文件内容
        原来的内容 = self.替换导入模块(原来的内容, self.取头部代码(), "导入模块")

        原来的内容 = self.替换导入模块(原来的内容, self.取事件绑定代码(), "绑定事件")

        # 找到 "# ==绑定事件===" 的位置
        开始位置 = 原来的内容.find("# ==绑定事件===") + len("# ==绑定事件===")
        # 从 开始位置这里插入文本 hello
        原来的内容 = 原来的内容[:开始位置] + self.取函数定义代码() + 原来的内容[开始位置:]

        return 原来的内容


if __name__ == "__main__":
    界面代码生成 = 界面代码生成类()
    界面代码生成.加载已存在的文件内容 = """
# ==导入模块==
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow
# ==导入模块===
class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        # ==绑定事件==
        self.ui = ui_启动窗口.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show() 
        self.启动窗口 = self 
        self.按钮1 = 按钮(self.ui.按钮1)
        self.按钮1.绑定事件被点击(self.按钮1被点击)
        self.{组件名称}创建完毕() 
        # ==绑定事件===    
    def 启动窗口创建完毕(self):
        print("启动窗口创建完毕")
    def 按钮1被点击(self):
        print("按钮1被点击")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
    

进程已结束,退出代码0

"""

    界面代码生成.加入导包模块头部代码("import sys")
    界面代码生成.加入导包模块头部代码("from PySide6.QtWidgets import QApplication")
    界面代码生成.加入导包模块头部代码("from PySide6.QtWidgets import QMainWindow")
    界面代码生成.加入导包模块头部代码("from qtefun.组件.按钮 import 按钮")
    界面代码生成.加入导包模块头部代码("from qtefun.组件.按钮 import 按钮")
    界面代码生成.加入导包模块头部代码("from qtefun.组件.按钮 import 按钮")
    界面代码生成.加入导包模块头部代码("from qtefun.组件.按钮 import 按钮")
    界面代码生成.类名 = "MainWin(QMainWindow)"

    界面代码生成.加入事件绑定代码("""
self.{组件名称}创建完毕() 
        """, True)
    界面代码生成.加入事件绑定代码("""
self.ui = ui_启动窗口.Ui_MainWindow()
self.ui.setupUi(self)
self.show() 
self.启动窗口 = self 
    """)

    界面代码生成.加入事件绑定代码("self.按钮1 = 按钮(self.ui.按钮1)")
    界面代码生成.加入事件绑定代码("self.按钮1.绑定事件被点击(self.按钮1被点击)")

    界面代码生成.加入函数定义代码(f"""
def 启动窗口创建完毕(self):
    print("启动窗口创建完毕")
    """)

    界面代码生成.加入函数定义代码(f"""
def 按钮1被点击(self):
    print("按钮1被点击")
    """)

    界面代码生成.加入函数定义代码(f"""
def 按钮2被点击(self):
    print("按钮1被点击")
        """)

    界面代码生成.末尾代码 = """
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
    """

    代码 = 界面代码生成.生成代码()
    print(代码)
