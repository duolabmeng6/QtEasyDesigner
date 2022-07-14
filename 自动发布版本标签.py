# 在github中自动发布版本标签
import os

from github import Github


def 版本号格式加一(版本号):
    版本号 = 版本号.split('.')
    版本号[-1] = str(int(版本号[-1]) + 1)
    版本号 = '.'.join(版本号)
    return 版本号


# print("版本号格式加一:", 版本号格式加一("1.0.0"))
# def 版本号大小比较(版本号1, 版本号2):
#     版本号1 = 版本号1.split('.')
#     版本号2 = 版本号2.split('.')
#     for i in range(len(版本号1)):
#         if int(版本号1[i]) > int(版本号2[i]):
#             return True
#         elif int(版本号1[i]) < int(版本号2[i]):
#             return False
#     return False
#
#
# print("版本号大小比较:", 版本号大小比较("1.0.0", "1.0.1"))
# print("版本号大小比较:", 版本号大小比较("1.0.0", "2.0.1"))
# print("版本号大小比较:", 版本号大小比较("3.0.0", "2.0.1"))


def 版本号从大小写排序(tags):
    # 删除非数字的版本号
    tags = [tag for tag in tags if tag.replace('.', '').isdigit()]
    tags_dict = []
    for tag in tags:
        # 获取数值
        tag_value = int("".join(tag.split('.')))
        tags_dict.append({
            "tag": tag,
            'tagint': tag_value
        })
    tags_dict.sort(key=lambda student: student['tagint'])
    tags_dict.reverse()
    # 重新组装
    tags = []
    for tag in tags_dict:
        tags.append(tag['tag'])
    return tags


# print("版本号从大小写排序:", 版本号从大小写排序(['0.0.10', '0.0.9', '3.2.8', '0.1.7', "v1.0", "latest"]))


# tags = ['latest', '0.0.10', '0.0.9', '0.0.8', '0.0.7']
# tags = 版本号从大小写排序(tags)
# print("使用 版本号大小比较 排序:", tags)
#
# exit()

def 检查当前项目并且将版本号码加一(token, project_name):
    # token = "token"
    # project_name = "duolabmeng6/QtEsayDesigner"

    g = Github(token)
    # print("用户名",g.get_user().name)
    repo = g.get_repo(project_name)
    # print("项目名称",repo.name)
    print("标签数量", repo.get_tags().totalCount)
    if repo.get_tags().totalCount == 0:
        # 没有标签的话 创建标签 0.0.1
        sha = repo.get_commits()[0].sha
        新版本号 = "0.0.1"
        repo.create_git_ref(f"refs/tags/{新版本号}", sha)
        return 新版本号

    # 版本号对比
    tags = []
    k = 0
    for tag in repo.get_tags():
        print(tag.name)
        tags.append(tag.name)
        k += 1
        if k == 5:
            break  # 取前5个标签
    print("原来的 tags", tags)

    # 版本号排序
    tags = 版本号从大小写排序(tags)
    # print("版本号排序:", tags)
    新版本号 = 版本号格式加一(tags[0])
    # print("新版本号:", 新版本号)
    print("创建新版本", 新版本号)
    sha = repo.get_commits()[0].sha
    repo.create_git_ref(f"refs/tags/{新版本号}", sha)

    return 新版本号


def main():
    GITHUB_REPOSITORY = os.environ.get('GITHUB_REPOSITORY')
    INPUT_TOKEN = os.environ.get('INPUT_TOKEN')
    # GITHUB_REPOSITORY = "duolabmeng6/QtEsayDesigner"
    新版本号 = 检查当前项目并且将版本号码加一(INPUT_TOKEN, GITHUB_REPOSITORY)
    print(f"::set-output name=NewVersion::{新版本号}")


if __name__ == "__main__":
    main()
