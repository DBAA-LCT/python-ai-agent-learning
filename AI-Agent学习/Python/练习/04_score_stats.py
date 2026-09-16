
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