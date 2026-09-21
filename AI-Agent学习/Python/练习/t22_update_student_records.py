"""模块 22：遍历多条记录并更新成绩状态

本次练习的需求：遍历列表中的多条学生成绩字典记录，根据每条记录的成绩添加或更新 passed 字段，并输出更新后的记录列表。
涉及的知识点：列表中的字典、for 循环、循环变量、字典字段读取、字典字段更新、条件判断和布尔值。
复习重点：循环变量 record 表示当前字典；对 record 的字段赋值会直接修改列表中的对应记录；每条记录都必须根据自己的 score 单独判断 passed。
常见错误：只修改一个固定字典；把判断结果保存到列表外的临时变量；忘记处理成绩小于 60 的分支；修改 score 后忘记同步更新 passed；混淆列表和列表元素的类型。
"""


ming_record = {
    "name": "小明",
    "score": 58,
}
hong_record = {
    "name": "小红",
    "score": 85
}
gang_record = {
    "name": "小刚",
    "score": 60
}


records = [ming_record, hong_record, gang_record]

passed_num = 0
for record in records:
    if record["score"] >= 60:
        record["passed"] = True
        passed_num += 1
    else:
        record["passed"] = False

print(records)
print(passed_num)



