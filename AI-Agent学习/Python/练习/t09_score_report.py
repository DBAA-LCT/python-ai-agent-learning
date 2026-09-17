"""
模块 09：成绩统计与字典返回

需求：
- 接收一个成绩列表。
- 统计总人数、及格人数、平均分、最高分和最低分。
- 将统计结果整理成字典并返回。
- 空列表不允许进行统计，需要抛出 ValueError。

知识点：
- 函数参数与返回值
- 列表遍历
- 计数器与累加器
- 条件判断与边界值
- 字典的创建与返回
- ValueError 异常

复习重点：
- 先处理空列表，再使用第一个成绩初始化最高分和最低分。
- “及格”要使用大于等于 60 分的条件。
- 字典的键对应统计项目，字典的值对应已经计算出的变量。

常见错误：
- 忘记处理空列表，导致访问 scores[0] 时产生 IndexError。
- 使用 score > 60，导致 60 分未被计入及格人数。
- 字典键名和变量名不一致，导致返回结果含义不清。
"""


def get_score_stats(scores: list):
    if len(scores) == 0:
        raise ValueError("成绩表为空")

    total_people_num = len(scores)
    passed_people_num = 0
    total_score = 0
    max_score = scores[0]
    min_score = scores[0]

    for score in scores:
        total_score += score
        if score >= 60:
            passed_people_num += 1
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score

    average_score = total_score / total_people_num

    result = {
        "total_people_num": total_people_num,
        "passed_people_num": passed_people_num,
        "average_score": average_score,
        "max_score": max_score,
        "min_score": min_score,
    }
    return result


print(get_score_stats([59, 60, 85, 90, 30]))
