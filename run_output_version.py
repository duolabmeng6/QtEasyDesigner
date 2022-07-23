# -*- coding: utf-8 -*-
import os


def view_all_environment_variables():
    from icecream import ic
    for item in os.environ:
        name = item
        value = os.environ[item]
        ic(name, value)


# view_all_environment_variables()

tagName = os.environ.get('GITHUB_REF_NAME')
print("tagName:", tagName)
fileDir = os.path.dirname(__file__)
print("file dir:", fileDir)
versionFilePath = os.path.join(fileDir, "version.py")
print(f"edit file {versionFilePath} output: version = {tagName}")
with open(versionFilePath, 'w') as f:
    f.write(f'version = "{tagName}"')

exit()
