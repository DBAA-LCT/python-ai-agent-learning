"""模块 17：将成绩数据校验提取为独立函数

本次练习的需求：读取 JSON 成绩数据，使用独立函数校验数据内容，并在校验成功后生成统计报告。
涉及的知识点：函数参数、返回值、raise ValueError、列表与元素类型校验、JSON 读取、异常处理、模块导入。
复习重点：validate_scores() 只负责数据校验；main() 负责文件读取、异常处理和流程编排；统计函数负责生成报告。
常见错误：把文件路径传给数据校验函数，校验成功后忘记 return，或从带有顶层执行代码的脚本导入函数。
"""

import json
from pathlib import Path

from t10_score_utils import get_score_stats


def validate_scores(scores):
    '''
    判断成绩列表是否有效:
        数据是否为列表
        数据是否为空
        数据是否为纯数字
    '''

    if not isinstance(scores, list):
        raise ValueError("成绩数据不是列表格式")
    
    if not scores:
        raise ValueError("成绩数据为空")
    
    for score in scores:
        if not isinstance(score, (int, float)):
            raise ValueError("成绩数据必须为纯数字")

    return scores



def main():
    '''从json文件中提取成绩，调用两个函数，最终生成成绩报告'''
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    try:
        json_path = data_dir / "t12_score.json"

        '''获取json中的数据'''
        with json_path.open("r", encoding="utf-8") as file:
            json_data = json.load(file)

        scores = validate_scores(json_data)
        report = get_score_stats(scores)
        print(report)
    except FileNotFoundError:
        print("成绩文件未找到")
    except json.JSONDecodeError:
        print("成绩文件不是json格式")
    except ValueError as e:
        print(f"成绩数据错误：{e}")
    

if __name__ == "__main__":
    main()