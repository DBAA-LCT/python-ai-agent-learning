"""
模块 04：函数与拆分

需求：
- 输入 5 个整数成绩并保存到列表。
- 使用函数计算总分和平均分。
- 函数接收整数列表，返回总分和平均分。
- 传入空列表时抛出明确的 ValueError。

知识点：
- def 定义函数
- 参数与返回值
- list[int] 参数类型标注
- tuple[int, float] 返回值类型标注
- sum() 和 len()
- if not 判断空列表
- raise 抛出异常
- 主流程与计算逻辑拆分

复习重点：函数负责计算，主流程负责输入和输出；函数不应依赖 input()。
"""


def calculate_stats(scores: list[int]) -> tuple[int, float]:
    if not scores:
        raise ValueError("成绩列表不能为空")
    total = sum(scores)
    average = total / len(scores)
    return total, average


scores = []
for _ in range(5):
    scores.append(int(input("请输入成绩：")))

total, average = calculate_stats(scores)
print(f"总分为：{total}")
print(f"平均分为：{average}")
