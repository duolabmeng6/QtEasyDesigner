from pyefun import *
所有环境变量 = 取系统所有环境变量()
print(所有环境变量)

路径 = 读环境变量("env:GITHUB_ENV")
print(路径)
GITHUB_ENV = 读入文本("./GITHUB_ENV")
print("GITHUB_ENV:", GITHUB_ENV)
VERSION = 读入文本("./VERSION")
print("版本:", VERSION)
写到文件(路径, GITHUB_ENV + "\nVERSION={}".format(VERSION))
