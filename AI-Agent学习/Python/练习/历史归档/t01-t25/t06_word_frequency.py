"""
模块 06：字典与数据建模

需求：
- 输入一段文本并拆分成单词列表。
- 统计每个单词出现的次数。
- 使用字典保存“单词 -> 出现次数”的映射。
- 保留 if/else 和 dict.get() 两种实现进行对照复习。

知识点：
- 字典的键和值
- 字典新增与更新：counts[word] = value
- in 判断键是否存在
- if/else 条件分支
- dict.get(key, default) 获取默认值
- for 遍历列表
- 字符串 split() 拆分

复习重点：字典键唯一；第一次出现时初始化为 1，重复出现时次数加 1。
"""

text = input("请输入要统计单词频率的文本：")
words = text.split()

# 写法一：使用 if/else 判断单词是否已经存在
counts_if_else = {}
for word in words:
    if word in counts_if_else:
        counts_if_else[word] += 1
    else:
        counts_if_else[word] = 1

# 写法二：使用 dict.get() 处理不存在的键
counts_get = {}
for word in words:
    counts_get[word] = counts_get.get(word, 0) + 1

print(f"if/else 写法：{counts_if_else}")
print(f"get() 写法：{counts_get}")
