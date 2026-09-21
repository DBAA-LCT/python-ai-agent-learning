"""模块 23：将及格人数统计提取为函数

本次练习的需求：接收多条学生成绩字典记录，统计 passed 字段为 True 的人数，并返回统计结果。
涉及的知识点：函数参数、函数返回值、列表中的字典、for 循环、条件判断、计数器和入口判断。
复习重点：统计函数只负责接收数据和返回结果；主流程负责准备数据、调用函数和输出；计数器应在函数内部初始化并返回最终结果。
常见错误：忘记传入 records；把计数器初始化在循环内部；只打印结果却不使用 return；在函数外依赖局部变量；混淆当前 record 和整个 records 列表。
"""


def count_passed_students(records: list[dict]) -> int:
    """统计 passed 字段为 True 的学生人数。"""
    passed_count = 0

    for record in records:
        if record["passed"]:
            passed_count += 1

    return passed_count


def main():
    records = [
        {"name": "小明", "score": 58, "passed": False},
        {"name": "小红", "score": 85, "passed": True},
        {"name": "小刚", "score": 60, "passed": True},
    ]

    passed_count = count_passed_students(records)
    print(f"及格人数：{passed_count}")


if __name__ == "__main__":
    main()
