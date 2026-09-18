"""
练习 13：使用 main() 和入口判断组织 JSON 读取流程

需求：
- 将 t12 的 JSON 文件读取和成绩统计流程放入 main()。
- 直接运行脚本时执行 main() 并打印统计报告。
- 被其他模块导入时不自动读取文件或打印报告。

知识点：
- 函数定义与调用
- main() 主流程
- if __name__ == "__main__":
- 模块导入行为
- JSON 文件读取与异常处理

复习重点：
- import 和函数定义可以在模块导入时执行，但主流程应由入口判断控制。
- 直接运行脚本时 __name__ 的值是 "__main__"；导入模块时不是这个值。

有复习价值的常见错误：
- 把 "__main__" 写成 "main"，导致条件为假，main() 不会被调用；这种错误可能语法正确但运行时没有输出。
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
        print(get_score_stats(scores))

    except FileNotFoundError:
        print("成绩文件未找到")

if __name__ == "__main__":
    main()
