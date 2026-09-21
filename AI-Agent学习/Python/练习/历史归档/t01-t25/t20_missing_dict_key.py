"""模块 20：字典缺失键的读取与处理

本次练习的需求：读取字典中的必填字段，观察读取不存在键时的行为，并为可选字段提供默认值。
涉及的知识点：字典键读取、`dict[key]`、`dict.get()`、KeyError、try/except 和默认值。
复习重点：必填字段可以用 `record[key]` 直接读取；可选字段可以用 `record.get(key, default)` 安全读取；需要观察并处理不存在键引发的 KeyError。
常见错误：把 `[]` 和 `get()` 当成完全等价；忘记不存在键会引发 KeyError；捕获异常后仍继续使用未成功读取的变量；为不需要使用的读取结果创建无用变量。
"""


record = {
    "name": "小明",
    "score": 58,
    "passed": False,
}




print(record["name"])

try:
    record["class"]
except KeyError:
    print("字典中无此字段")


print(record.get("class", "class未设置"))