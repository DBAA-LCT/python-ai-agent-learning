"""
练习 12：从 JSON 文件读取成绩列表并生成统计报告

需求：
- 从 data/t12_score.json 读取成绩列表。
- 使用读取出的成绩列表调用统计函数。
- 打印生成的成绩统计报告。
- 文件不存在时给出友好提示。

知识点：
- pathlib.Path
- with 管理文件
- json.load()
- JSON 数组与 Python 列表
- try/except FileNotFoundError
- 模块导入

复习重点：
- JSON 数组会被 json.load(file) 转换为 Python 列表，读取结果可以直接传给统计函数。
- try 应该包住真正可能失败的文件打开和读取操作；只有成功得到 scores 后，才能继续统计。

有复习价值的常见错误：
- 把读取结果误认为字符串，或者把 JSON 报告字典误当成原始成绩列表。
- 只捕获路径拼接而没有捕获文件打开；异常处理后仍继续使用没有成功赋值的 scores。
"""
import json
from pathlib import Path
from t10_score_utils import get_score_stats

data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)
try:
    json_path = data_dir / "t12_score.json"
    with json_path.open("r", encoding="utf-8") as file:
        scores = json.load(file)
    print(get_score_stats(scores))

except FileNotFoundError:
    print("成绩文件未找到")

