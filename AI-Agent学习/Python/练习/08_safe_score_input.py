"""
模块 08：异常处理与输入校验

需求：
- 输入一个成绩，并将输入内容转换为整数。
- 成绩在 0 到 100 之间时，输出输入的成绩。
- 成绩小于 0 或大于 100 时，输出范围错误提示。
- 输入不能转换为整数时，捕获异常并输出输入错误提示。

知识点：
- input() 获取用户输入
- int() 将字符串转换为整数
- try/except 捕获异常
- ValueError 表示值无法转换为目标类型
- if/else 条件分支
- Python 链式比较：0 <= score <= 100
- 变量的赋值与使用

复习重点：int(input(...)) 可能产生 ValueError；先处理类型转换，再判断数值范围；异常分支和正常分支的输出不能混淆。

常见错误：
- 忘记 input() 返回的是字符串，直接进行数值判断
- 使用 && 而不是 Python 的 and
- 使用 score > 0 导致成绩 0 被误判为非法
- 把 except ValueError 写成无效的 Exception ValueError
- 范围错误后仍继续输出“输入的成绩”
"""




def check_input_score(raw_score):
    try:
        score = int(raw_score)
    except ValueError:
        raise ValueError("请输入整数成绩")
    
    if not (0 <= score <= 100):
        raise ValueError ("成绩必须在0到100之间")
    return score



def main():
    raw_score = input("请输入成绩：")

    try:
        score = check_input_score(raw_score)
        print(f"你输入的成绩是：{score}")
    except ValueError as error:
        print(error)

if __name__ == "__main__":
    main()