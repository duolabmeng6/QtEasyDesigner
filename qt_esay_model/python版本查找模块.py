import os


def 查看当前环境的所有包():
    from importlib import metadata
    数组 = []
    for dist in metadata.distributions():
        数组.append(dist.metadata["Name"] + " " + dist.metadata["Version"])
    return 数组


# 获取系统的python
def 查找MacOS的python虚拟环境():
    # /Users/用户名/.local/share/virtualenvs/QtEasyDesigner-NJQRvDGp
    # 获取系统的用户目录然后搜索.local/share/virtualenvs/
    用户目录 = os.path.expanduser("~")
    搜索目录 = f"{用户目录}/.local/share/virtualenvs/"
    虚拟环境数组 = []
    for 目录 in os.listdir(搜索目录):
        # 检查是否为目录
        虚拟环境目录 = f"{搜索目录}{目录}"
        if os.path.isdir(虚拟环境目录):
            python路径 = f"{虚拟环境目录}/bin/python"
            pip路径 = f"{虚拟环境目录}/bin/pip"
            pyinstaller路径 = f"{虚拟环境目录}/bin/pyinstaller"
            # 查询python的版本
            python版本 = "没有检查到"
            pyinstaller版本 = "没有检查到"
            pip版本 = "没有检查到"
            try:
                python版本 = os.popen(f"{python路径} -V").read().strip()
                pyinstaller版本 = os.popen(f"{pyinstaller路径} -v").read().strip()
                pip版本 = os.popen(f"{pip路径} -V").read().strip()
                # pip 22.2.2 from 获取版本
                pip版本 = pip版本.split(" ")[1]
                # Python 3.9.13 获取版本
                python版本 = python版本.split(" ")[1]
            except:
                pass
            虚拟环境数组.append({
                "虚拟环境目录": 虚拟环境目录,
                "python路径": python路径,
                "pip路径": pip路径,
                "pyinstaller路径": pyinstaller路径,
                "python版本": python版本,
                "pip版本": pip版本,
                "pyinstaller版本": pyinstaller版本
            })

    return 虚拟环境数组

def 查找系统的python路径():
    # which python3
    python路径 = os.popen(f"which python").read().strip()
    pip路径 = os.popen(f"which pip").read().strip()
    pyinstaller路径 = os.popen(f"which pyinstaller").read().strip()
    # 查询python的版本
    python版本 = "没有检查到"
    pyinstaller版本 = "没有检查到"
    pip版本 = "没有检查到"
    try:
        python版本 = os.popen(f"{python路径} -V").read().strip()
        pyinstaller版本 = os.popen(f"{pyinstaller路径} -v").read().strip()
        pip版本 = os.popen(f"{pip路径} -V").read().strip()
        pip版本 = pip版本.split(" ")[1]
        python版本 = python版本.split(" ")[1]
    except:
        pass
    return {
        "python路径": python路径,
        "pip路径": pip路径,
        "pyinstaller路径": pyinstaller路径,
        "python版本": python版本,
        "pip版本": pip版本,
        "pyinstaller版本": pyinstaller版本
    }



if __name__ == "__main__":
    # 模块列表 = 查看当前环境的所有包()
    # print(模块列表)
    # from subprocess import call
    # call(["pip", "list"])

    # 模块列表 = 查看当前环境的所有包()
    # print(模块列表)
    # print(查找MacOS的python虚拟环境())
    print(查找系统的python路径())
    # from subprocess import call
    # call(["pip", "list"])
    # # print("pyinstaller")
    # # call(["pyinstaller", "-v"])
    # print("python")
    # call(["python", "-V"])
    # print("python")
    # call(["python3", "-V"])
    # print("pip")
    # call(["pip", "-V"])
    #