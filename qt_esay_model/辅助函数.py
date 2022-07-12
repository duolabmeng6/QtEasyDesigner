
import pyefun as efun
import requests


def 发送给ide插件(插件URL地址, 文件路径, 跳转位置):
    文件路径 = efun.文件_取文件名(文件路径)
    # 跳转URL = ide插件URL地址 + "/myserver?type=func&file=" + 文件路径 + "&def=" + 函数名 + "("
    # 文件路径 = urllib.parse.quote(文件路径)
    跳转URL = 插件URL地址 + "/myserver?type=target&file=" + 文件路径 + "&def=" + str(跳转位置)
    print("调用pycharm代码跳转", 跳转URL)
    try:
        content = requests.get(跳转URL, timeout=1)
        print("调用pycharm代码跳转", content.text)
        return True, ""
    except:
        pass
        return False, "调用pycharm跳转代码错误,请检查pycharm中易函数视窗编程系统插件是否安装成功"
