
"""
练习 16：处理 JSON 文件格式错误

需求：
- 从 JSON 文件读取成绩列表。
- 区分文件不存在、JSON 格式错误和数据内容无效。
- JSON 格式错误时输出友好提示，不显示 traceback。
- JSON 数据结构和元素校验通过后，调用统计函数生成报告。

知识点：
- json.load()
- json.JSONDecodeError
- 异常继承关系
- 多个 except 分支的顺序
- JSON 数据校验
- main() 与入口判断

复习重点：
- JSON 语法错误发生在 json.load(file) 解析阶段，早于 isinstance() 等数据校验。
- JSONDecodeError 是 ValueError 的子类，所以必须放在 ValueError 分支之前捕获。

有复习价值的常见错误：
- 把 JSON 解析错误误认为会在 isinstance() 校验处发生。
- 先捕获 ValueError 会让 JSONDecodeError 被宽泛分支捕获，失去专门的错误提示。
"""
import json
from pathlib import Path
from t10_score_utils import get_score_stats


"""模块 16：处理 JSON 文件格式错误

本次练习的需求：读取 JSON 成绩文件，区分文件不存在、JSON 格式错误和成绩数据内容无效。
涉及的知识点：Path 文件路径、json.load()、JSONDecodeError、ValueError、列表与元素类型校验、异常捕获顺序。
复习重点：先完成 JSON 文本解析，再校验解析结果；JSONDecodeError 必须放在 ValueError 之前；异常处理后不能继续使用无效数据。
常见错误：把 JSON 格式错误误认为数据类型错误，或把 JSONDecodeError 放在 ValueError 之后导致分支被提前捕获。
"""


def main():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    try:
        json_path = data_dir / "t12_score.json"
        with json_path.open("r",encoding="utf-8") as file:
            scores = json.load(file)
        
        # 判断是否为列表
        if not isinstance(scores, list):
            raise ValueError("数据必须是列表")

        # 判断列表是否为空
        if not scores:
        # if len(scores) == 0:
            raise ValueError("成绩列表不能为空")
        

        for score in scores:
            if not isinstance(score, (int, float)):
                raise ValueError("数据必须是纯数字")
                

        print(get_score_stats(scores))

    except FileNotFoundError:
        print("成绩文件未找到")

    except json.JSONDecodeError:
        print("JSON 文件格式错误")

    except ValueError as e:
        print(f"成绩数据无效{e}")


if __name__ == "__main__":
    main()