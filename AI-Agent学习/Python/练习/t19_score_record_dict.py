"""模块 19：使用字典表示一条成绩记录

本次练习的需求：创建一条学生成绩记录，读取姓名和成绩，添加 passed 字段，并在成绩更新后同步更新 passed 字段。
涉及的知识点：字典、键和值、字典字段读取、字典字段添加、字典字段更新、条件判断和布尔值。
复习重点：一条记录中的姓名、成绩和 passed 都是字段；通过 record[key] 读取字段，通过赋值添加或更新字段；更新相关数据后要检查依赖字段是否需要同步更新。
常见错误：把一条记录误写成嵌套字典；混淆添加字段和更新字段；只处理及格分支而忘记让 passed 与最新成绩保持一致；f-string 外层引号与字典键引号冲突。
"""


record = {
    "name": "小明",
    "score": 58,
    "passed": False,
}

print(f'此字典记录：{record["name"]}，成绩为：{record["score"]}')

record["score"] = 65
if record["score"] >= 60:
    record["passed"] = True
else:
    record["passed"] = False

print(record)


