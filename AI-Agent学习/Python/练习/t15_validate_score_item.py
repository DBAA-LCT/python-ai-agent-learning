"""
练习 15：校验成绩列表中的元素类型

需求：
- 从 JSON 文件读取成绩列表。
- 确认成绩列表为非空列表。
- 确认列表中的每个元素都是整数或小数。
- 只有所有元素校验通过后，才调用统计函数生成报告。

知识点：
- for 循环遍历列表
- isinstance() 与类型元组
- raise ValueError
- JSON 文件读取
- 异常处理
- main() 与入口判断

复习重点：
- 元素级校验应放在列表整体校验之后、统计函数之前。
- isinstance(score, (int, float)) 可以同时接受整数和小数；发现无效元素时应立即停止并拒绝统计。

有复习价值的常见错误：
- isinstance() 的第二个参数应是类型或类型元组，不能写成 [int, float] 列表。
- raise 已经中断当前流程，后面不需要再写 break。
"""
import json
from pathlib import Path
from t10_score_utils import get_score_stats


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
    except ValueError as e:
        print(f"成绩数据无效{e}")

if __name__ == "__main__":
    main()