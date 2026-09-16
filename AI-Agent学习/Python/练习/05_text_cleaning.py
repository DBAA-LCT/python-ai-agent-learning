"""
模块 05：字符串处理

需求：
- 输入一段可能包含开头、结尾和连续空格的文本。
- 清理多余空白，使单词之间只保留一个空格。
- 输出清理后的文本和单词数量。

知识点：
- input() 获取文本
- str.split() 按空白拆分字符串
- str.join() 使用指定分隔符重新连接字符串
- len() 统计列表元素数量
- 字符串与列表之间的转换

复习重点：split() 不传参数时可以处理开头、结尾和连续空白；join() 由分隔符字符串调用。
"""

original = input("请输入要清理和统计的文本：")
words = original.split()
cleaned_text = " ".join(words)
print(f"清理后的字符串是：{cleaned_text}，一共{len(words)}个单词")
