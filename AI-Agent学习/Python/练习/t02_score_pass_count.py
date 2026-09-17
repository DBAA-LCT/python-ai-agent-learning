"""
模块 02：循环与计数

需求：
- 输入 5 个整数成绩。
- 判断每个成绩是否及格。
- 统计并输出及格人数。

知识点：
- list 列表
- append() 追加元素
- range() 控制重复次数
- for 循环遍历
- 计数器变量
- if 条件判断
- >= 边界判断

复习重点：先收集一组数据，再遍历数据并更新计数器。
"""

scores = []
for i in range(5):
    scores.append(int(input("")))
count = 0
for score in scores:
    if score >= 60:
        count+=1

print(f"及格的人数为：{count}")
