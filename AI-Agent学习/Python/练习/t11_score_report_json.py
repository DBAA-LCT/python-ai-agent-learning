"""
练习 11：成绩统计报告保存为 JSON

需求：
- 使用固定成绩生成统计报告。
- 将统计报告写入 JSON 文件。
- 再从 JSON 文件读取并打印。

知识点：
- pathlib.Path
- with 管理文件
- json.dump()
- json.load()
- 模块导入
- 入口判断
"""
import json
from pathlib import Path
from t10_score_utils import get_score_stats

def main():
    scores = [59, 60, 80]
    report = get_score_stats(scores)

    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)

    json_path = data_dir / "t11_score_report.json"

    with json_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)
    print("报告已经保存到json文件中")

    with json_path.open("r", encoding="utf-8") as file:
        read_report = json.load(file)


    print(read_report)

if __name__ == "__main__":
    main()

