"""
模块 10：成绩统计报告运行入口

需求：
- 动态录入指定数量的成绩。
- 导入成绩统计工具函数并调用。
- 输出统计报告。
- 通过入口判断控制脚本的直接运行。

知识点：
- from ... import ...
- input() 与 int() 类型转换
- for 循环和列表 append()
- 函数调用
- main() 主流程
- if __name__ == "__main__"

复习重点：
- 运行脚本负责输入和输出，工具模块负责统计逻辑。
- 导入工具模块时，不应该自动执行工具模块中的演示代码。
- 成绩数量必须是大于 0 的整数。

常见错误：
- import 语句中的模块名或函数名拼写错误。
- 忘记把输入的字符串转换为整数。
- 把 count <= 0 写成相反条件。
- 让运行脚本和工具模块承担相同职责。
"""

from t10_score_utils import get_score_stats

def main():
    scores  = []
    try:
        count = int(input("请输入要录入的成绩数量（大于0的整数）："))
    except ValueError:
        raise ValueError("要录入的数量输入有误，程序已退出")
    if count <= 0:
        raise ValueError("成绩数量必须大于0")

    print("请输入要录的成绩，没输入一个按回车提交")
    for i in range(count):
        scores.append(int(input("请输入成绩：")))
    
    result = get_score_stats(scores)

    print(result)

if __name__ == "__main__":
    main()