"""模块 18：运行成绩报告并验证安全导入

本次练习的需求：导入辅助模块中的成绩函数，读取成绩数据并输出报告；直接运行本脚本时执行 main()，被其他模块导入时不自动执行。
涉及的知识点：模块导入、main()、if __name__ == "__main__"、try/except、JSONDecodeError 和函数调用顺序。
复习重点：main() 负责流程编排和错误提示；只有读取、校验和统计全部成功后才打印报告；入口判断控制直接运行与被导入两种场景。
常见错误：遗漏入口判断导致导入时自动执行；异常处理后继续使用未赋值的 json_data；捕获 `json.JSONDecodeError` 却忘记导入 `json`。
"""

from pathlib import Path
import json
from t18_score_helper import load_scores, validate_scores, get_score_stats


def main():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    json_path = data_dir / "t12_score.json"

    try:
        json_data = load_scores(json_path)
        scores = validate_scores(json_data)
        report = get_score_stats(scores)
        print(report)
    except FileNotFoundError:
        print("成绩文件未找到")
    except json.JSONDecodeError:
        print("成绩文件不是json格式")
    except ValueError as e:
        print(f"成绩数据无效{e}")
    

if __name__ == "__main__":
    main()