"""
中文字数统计 MCP 服务
用于统计文本中的纯中文字符数量（不含标点、英文、数字、空格）

依赖：mcp[server] >= 1.0.0
运行：python server.py
"""

from mcp.server.fastmcp import FastMCP
import re

# 初始化 MCP 服务，名称可自定义
mcp = FastMCP("中文字数统计")


@mcp.tool()
def count_chinese_chars(text: str) -> int:
    """
    统计文本中的纯中文字符数

    Args:
        text: 输入文本

    Returns:
        纯中文字符的数量（不含标点、英文、数字、空格）
    """
    if not text:
        return 0
    chars = re.findall(r"[\u4e00-\u9fff]", text)
    return len(chars)


@mcp.tool()
def count_chinese_chars_detail(text: str) -> dict:
    """
    统计文本中的中文字符详情

    Args:
        text: 输入文本

    Returns:
        包含总字符数、中文字符数、详细分类的字典
    """
    if not text:
        return {"total": 0, "chinese": 0, "others": 0}

    chinese = re.findall(r"[\u4e00-\u9fff]", text)
    letters = re.findall(r"[A-Za-z]", text)
    digits = re.findall(r"[0-9]", text)
    punctuation = re.findall(r"[^\u4e00-\u9fffA-Za-z0-9\s]", text)
    spaces = re.findall(r"\s", text)

    return {
        "total": len(text),
        "chinese": len(chinese),
        "letters": len(letters),
        "digits": len(digits),
        "punctuation": len(punctuation),
        "spaces": len(spaces),
    }


if __name__ == "__main__":
    # SSE 模式，支持远程 HTTP 访问，适合魔塔等平台部署
    mcp.run(transport="sse")
