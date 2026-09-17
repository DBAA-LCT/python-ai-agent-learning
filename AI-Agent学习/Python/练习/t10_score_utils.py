"""
模块 10：成绩统计工具模块

需求：
- 提供可复用的成绩统计函数。
- 接收成绩列表，返回总人数、及格人数、平均分、最高分和最低分。
- 空列表时抛出 ValueError。
- 被其他脚本导入时，不自动获取输入或打印报告。

知识点：
- 函数参数与返回值
- 列表遍历和字典返回值
- ValueError 异常
- 模块导入
- if __name__ == "__main__"

复习重点：
- 工具模块只负责可复用的处理逻辑。
- 顶层演示代码需要放在入口判断中，避免导入时自动执行。

常见错误：
- 在模块顶层直接调用函数并打印，导致导入模块时产生额外输出。
- 忘记处理空列表，导致访问第一个元素时出错。
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


if __name__ == "__main__":
    print(get_score_stats([59,69,85,90,30]))