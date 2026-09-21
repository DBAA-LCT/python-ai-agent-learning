"""模块 18：可复用成绩函数与安全模块导入

本次练习的需求：将成绩读取、校验和统计函数放入辅助模块，由运行脚本导入并调用；直接运行脚本时输出报告，被其他模块导入时不自动执行报告流程。
涉及的知识点：模块导入、函数复用、Path、JSON 读取、ValueError、函数返回值和入口判断。
复习重点：辅助模块只定义可复用函数；文件读取失败和数据校验失败通过异常传递给主流程；不要在模块顶层直接读取文件或打印报告。
常见错误：把读取或打印代码直接写在模块顶层，导致导入时产生副作用；异常后继续使用未成功赋值的数据；混淆 `Path` 类型和路径字符串。
"""

import json
from pathlib import Path

def load_scores(path: Path):
    '''读取json数据'''
    with path.open("r", encoding="utf-8") as file:
        json_data = json.load(file)
    return json_data


    

def validate_scores(json_data) -> list:
    '''
    判断从json文件读取到的数据是否合规，需要判断：
        数据是否为列表
        数据是否为空
        数据是否为纯数字
    '''
    # 判断1：数据是否为列表
    if not isinstance(json_data, list):
        raise ValueError("成绩文件格式不是列表")
    
    # 判断2：数据是否为空
    if not json_data:
        raise ValueError("成绩文件内容为空")
    
    # 判断3：数据是否为纯数字
    for score in json_data:
        if not isinstance(score, (int, float)):
            raise ValueError("成绩数据不是纯数字")
    # 全部检验通过，返回成绩列表
    return json_data

def get_score_stats(scores: list) -> dict:
    '''
        需求：
    - 提供可复用的成绩统计函数。
    - 接收成绩列表，返回总人数、及格人数、平均分、最高分和最低分。
    - 空列表时抛出 ValueError。
    - 被其他脚本导入时，不自动获取输入或打印报告。
    '''

    if not scores:
        raise ValueError("成绩列表不能为空")


    # 1：列表长度就是总人数
    total_people_num = len(scores)

    passed_people_num = 0
    total_score = 0

    max_score = scores[0]
    min_score = scores[0]

    for score in scores:
    #遍历所有成绩：
        # 2、判断是否及格,同时成绩还要是合法范围
        if score < 0 or score > 100:
            raise ValueError("成绩文件中的成绩不在百分制成绩的范围")
        if score >= 60:
            passed_people_num += 1
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
        total_score += score

    average_score = total_score / total_people_num
    report = {
        "总人数": total_people_num,
        "及格人数": passed_people_num,
        "平均分": average_score,
        "最高分": max_score,
        "最低分": min_score  
    }

    return report
