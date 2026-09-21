"""模块 21：使用列表保存多条学生成绩记录

本次练习的需求：创建多条学生成绩字典记录，将它们放入列表，并遍历列表读取每条记录的姓名和成绩。
涉及的知识点：列表、字典、列表中的字典、for 循环、字典键读取、KeyError 和 try/except。
复习重点：外层列表表示多条记录；列表中的每个元素是一条普通字典记录；遍历得到单条记录后，再使用 `record["name"]` 和 `record["score"]` 读取字段。
常见错误：把多条记录误写成一个字典；混淆列表和列表元素的类型；遍历后忘记通过键读取字典字段；f-string 外层引号与字典键引号冲突；使用 `get()` 后又期待捕获 KeyError。
"""


ming_record = {
    "name": "小明",
    "score": 58,
}
hong_record = {
    "name": "小红",
    "score": 85
}

records = [ming_record, hong_record ]

try:
    for record in records:
        print(f'{record["name"]}的成绩是：{record["score"]}')
except KeyError:
    print("成绩字典中的数据有误")

