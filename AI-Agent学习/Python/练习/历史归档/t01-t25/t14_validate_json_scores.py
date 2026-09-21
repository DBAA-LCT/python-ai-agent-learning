"""
练习 14：校验 JSON 读取后的成绩数据

需求：
- 从 JSON 文件读取成绩数据。
- 判断读取结果是否为非空列表。
- 数据有效时调用统计函数生成报告。
- 数据无效或文件不存在时输出对应提示，不继续统计。

知识点：
- isinstance()
- 列表非空判断
- raise ValueError
- 多个 except 分支
- JSON 文件读取
- main() 与入口判断

复习重点：
- 文件读取成功不代表数据内容有效，必须在 json.load() 后、统计前进行校验。
- 先判断数据类型，再判断列表是否为空；校验失败时不能继续调用统计函数。

有复习价值的常见错误：
- 把 isinstance(scores, list) 的条件方向写反，导致合法列表被判定为无效。
- 抛出 ValueError 却没有捕获，导致本来可以友好提示的数据错误显示 traceback。
"""
import json
from pathlib import Path

from t10_score_utils import get_score_stats

def main():
    data_dir = Path(__file__).parent / "data"
    data_dir.mkdir(exist_ok=True)
    try:
        json_path = data_dir / "t12_score.json"
        with json_path.open("r", encoding="utf-8") as file:
            scores = json.load(file)

        # 判断是否为列表
        if not isinstance(scores, list):
            raise ValueError("数据必须是列表")

        # 判断列表是否为空
        if not scores:
        # if len(scores) == 0:
            raise ValueError("成绩列表不能为空")

        print(get_score_stats(scores))

    except FileNotFoundError:
        print("成绩文件未找到")
    except ValueError as e:
        print(f"成绩数据无效{e}")

if __name__ == "__main__":
    main()