"""
模块 03：列表与聚合

需求：
- 输入 5 个整数成绩并保存到列表。
- 计算所有成绩的总分。
- 计算所有成绩的平均分。
- 输出总分和平均分。

知识点：
- 列表收集数据
- for 循环与 range()
- sum() 计算总和
- len() 获取列表长度
- 除法计算平均值
- f-string 格式化输出

复习重点：聚合数据时，使用 sum(scores) 和 len(scores) 让计算跟列表实际长度关联。
"""

scores = []

for _ in range(5):
    scores.append(int(input("请输入成绩：")))

total = sum(scores)
# 另一种显式累加写法：
# for score in scores:
#     total += score
average = total / len(scores)

print(f"总分为：{total}")
print(f"平均分为：{average}")
