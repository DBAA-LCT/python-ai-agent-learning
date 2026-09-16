"""
模块 07：文件与 JSON

====================
一、需求
====================
1. 输入一段文本；
2. 统计每个单词出现的次数；
3. 将统计结果保存到 JSON 文件；
4. 再从 JSON 文件读取结果并输出。

====================
二、知识点
====================
1. import：导入标准库模块；
2. pathlib.Path：用对象表示和处理文件路径；
3. __file__：当前 Python 文件的路径；
4. Path.parent：获取当前文件所在的目录；
5. Path / "目录或文件名"：拼接路径；
6. Path.mkdir()：创建目录；
7. Path.open()：打开文件；
8. with：管理文件资源，代码块结束后自动关闭文件；
9. "w"：以写入模式打开文件；
10. "r"：以读取模式打开文件；
11. json.dump()：把 Python 数据写入 JSON 文件；
12. json.load()：从 JSON 文件读取数据，转换成 Python 数据；
13. ensure_ascii=False：让中文以正常文字保存，而不是 Unicode 转义；
14. indent=2：让 JSON 文件缩进显示，更容易阅读；
15. 序列化：把 Python 数据转换成 JSON 文本；
16. 反序列化：把 JSON 文本转换回 Python 数据。

====================
三、关键数据流
====================
输入文本
    ↓
split() 拆分成单词列表
    ↓
使用字典统计单词频率
    ↓
json.dump() 写入 JSON 文件
    ↓
json.load() 从文件读取
    ↓
输出读取后的字典

====================
四、常见错误
====================
1. 父目录不存在：open() 不能自动创建多级目录，需要先 mkdir()；
2. 写入时使用了 "r"：读取模式不能用于写入；
3. 读取时使用了 "w"：会覆盖原文件内容；
4. 忘记使用 with：文件可能没有被正确关闭；
5. 把 json.dump() 和 json.load() 混淆；
6. 运行目录和脚本目录不同，导致相对路径指向错误位置；
7. 文件名拼写错误，写入和读取的路径必须保持一致。

复习重点：
- dump = Python 数据写入 JSON；
- load = JSON 文件读取为 Python 数据；
- w = write，r = read；
- 使用 Path(__file__).parent 可以让路径相对于当前脚本更加稳定。
"""

import json
from pathlib import Path


# 获取当前 Python 文件所在目录，再拼接 data 子目录。
data_dir = Path(__file__).parent / "data"

# 如果 data 目录不存在就创建；如果已经存在，不报错。
data_dir.mkdir(exist_ok=True)

# 拼接 JSON 文件路径。
json_path = data_dir / "07_word_frequency.json"


# 读取文本，并统计每个单词的出现次数。
text = input("请输入要统计单词频率的文本：")
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1


# 使用写入模式，把字典序列化为 JSON 文本并保存到文件。
with json_path.open("w", encoding="utf-8") as file:
    json.dump(counts, file, ensure_ascii=False, indent=2)

print("单词频率写入成功")


# 使用读取模式，从 JSON 文件反序列化出 Python 字典。
with json_path.open("r", encoding="utf-8") as file:
    loaded_counts = json.load(file)

print(f"单词频率读取成功：{loaded_counts}")
