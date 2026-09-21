"""模块 24：独立重写列表统计函数

本次练习的需求：定义一个接收分数列表的函数，统计分数大于等于 80 的人数并返回结果，由主流程调用并输出。
涉及的知识点：函数参数、函数返回值、列表、for 循环、条件判断、计数器和入口判断。
复习重点：参数应真正参与函数处理；计数器应在函数内部初始化；统计结果使用 `return` 返回，主流程负责输出。
常见错误：把计数器初始化在循环内部；只使用 `print()` 不使用 `return`；函数内部重新写死输入数据；函数名和实际统计规则不一致；使用不准确的类型标注。
"""


def count_excellent_students(scores: list[int]) -> int:
    excellent_count = 0

    for score in scores:
        if score >= 80:
            excellent_count += 1

    return excellent_count


def main():
    scores = [59, 60, 80, 95]

    excellent_count = count_excellent_students(scores)
    print(f"优秀人数：{excellent_count}")


if __name__ == "__main__":
    main()










