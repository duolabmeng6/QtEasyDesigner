
def 删除每一个行的首尾空白字符(text):
    # 删除每一行的首尾空白字符
    text_  = text
    text_ = [line.strip() for line in text_.splitlines()]
    # 删除空白行
    text_ = [line for line in text_ if line]
    # 重新组合
    text_ = '\n'.join(text_)
    return text_