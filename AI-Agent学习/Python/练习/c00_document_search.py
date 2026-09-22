'''
实现一个小工具：

    1从 UTF-8 的 documents.json 读取文档列表。
    2根据关键词匹配 title 或 content。
    3关键词需要：
        忽略大小写；
        去除首尾空格；
        空关键词给出明确提示。
    4返回匹配文档的 id 和 title。
    5保持原始输入顺序，默认最多返回 3 条。
    6没有匹配时返回空列表。
    7能区分以下错误：
        文件不存在；
        JSON 格式错误；
        最外层不是列表；
        文档缺少字段或字段类型错误。
'''
import json
from pathlib import Path

def load_json() -> list:
    data_dir = Path(__file__).parent / "data"
    try:
        json_path = data_dir / "documents.json"
        with json_path.open("r", encoding="utf-8") as file:
            content = json.load(file)
        
        if not isinstance(content, list):
            raise ValueError("json最外层必须是列表")

        return content
    except FileNotFoundError:
        print("文件未找到")
    except json.JSONDecodeError:
        print("文件不是json格式")
    except ValueError as e:
        print(f"文件数据有误：{e}")


def search_keyword( keyword: str, documents: list, limit: int = 3):

    keyword = keyword.strip().lower()

    if not keyword:
        print("关键词不能为空")
        return []

    results = []

    try:
        for document in documents:
            if document["title"]:
                title = document["title"]
            else:
                raise KeyError("文档中无title项")

            if document["content"]:
                text = document["content"]
            else:
                raise KeyError("文档中无content项")

            # 忽略大小写：将关键词和要搜索的文档都统一用小写查询
            if keyword in title.lower() or keyword in text.lower():
                print("匹配", document["id"], title)
                results.append({
                    "id": document["id"],
                    "title": title,
                })

                if len(results) >= limit:
                    break

        if not results:
            print("未匹配到关键词")

        return results
    except KeyError as e:
        print(f"文档数据有误：{e}")


def main():
    content = load_json()
    print("搜索到结果，原内容为：" , search_keyword("sql", content))

if __name__ == "__main__":
    main()