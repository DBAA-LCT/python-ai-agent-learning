scores = []

for _ in range(5):
    scores.append(int(input("请输入成绩：")))

total = sum(scores)
# for score in scores:
#     total += score
average = total / len(scores)

print(f"总分为：{total}")
print(f"平均分为：{average}")