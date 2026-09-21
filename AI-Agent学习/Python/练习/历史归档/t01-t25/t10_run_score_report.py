"""
模块 10：成绩统计报告运行入口

模块 10 需求：
- 动态录入指定数量的成绩。
- 导入成绩统计工具函数并调用。
- 输出统计报告。
- 通过入口判断控制脚本的直接运行。

模块 11 改进：输入异常与用户体验
- 数量不是整数时，输出清晰提示并结束程序。
- 数量小于等于 0 时，输出清晰提示并结束程序。
- 成绩不是整数时，输出清晰提示并结束程序。
- 正常输入时，继续生成成绩统计报告。

知识点：
- from ... import ...
- input() 与 int() 类型转换
- for 循环和列表 append()
- 函数调用
- try/except 异常捕获
- ValueError 异常类型
- raise ValueError 主动抛出异常
- return 结束 main() 当前流程
- main() 主流程
- if __name__ == "__main__"

复习重点：
- 运行脚本负责输入和输出，工具模块负责统计逻辑。
- 导入工具模块时，不应该自动执行工具模块中的演示代码。
- 成绩数量必须是大于 0 的整数。
- except 捕获异常后，如果只 print() 而没有 return 或其他结束处理，程序会继续执行。
- raise 会抛出异常；如果没有外层 except 接住，程序会显示 traceback。
- 无效数据不能继续进入后续统计流程。

常见错误：
- import 语句中的模块名或函数名拼写错误。
- 忘记把输入的字符串转换为整数。
- 把 count <= 0 写成相反条件。
- 把成绩输入的 int() 转换放在 try 外面。
- 异常分支只打印错误，却忘记结束当前流程。
- 异常后继续使用没有成功赋值的变量。
- 捕获异常后再次 raise，导致程序显示 traceback。
- 让运行脚本和工具模块承担相同职责。
"""

from t10_score_utils import get_score_stats

def main():
    scores  = []
    try:
        count = int(input("请输入要录入的成绩数量（大于0的整数）："))
        if count <= 0:
            raise ValueError("成绩数量必须大于0")
    except ValueError as e:
        print(f"要录入的数量输入有误，程序已退出:{e}")
        return


    print("请输入要录的成绩，没输入一个按回车提交")
    for i in range(count):
        try:
            scores.append(int(input("请输入成绩：")))
        except ValueError:
            print("输入的成绩不合法")
            return
    
    result = get_score_stats(scores)

    print(result)

if __name__ == "__main__":
    main()