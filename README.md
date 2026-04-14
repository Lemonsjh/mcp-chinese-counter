# 中文字数统计 MCP 服务

一个轻量的 MCP 服务，提供中文字符统计功能。

## 功能

提供两个工具：

| 工具名 | 说明 |
|--------|------|
| `count_chinese_chars` | 统计文本中的纯中文字符数（不含标点、英文、数字、空格） |
| `count_chinese_chars_detail` | 详细统计，返回各类型字符的分类计数 |

## 安装

```bash
pip install -r requirements.txt
```

## 运行

```bash
python server.py
```

## 使用示例

调用 `count_chinese_chars`，输入：
```
今天天气不错，适合出门散步。
```

输出：
```
10
```

## 技术栈

- Python 3.10+
- MCP Python SDK (`mcp[server]`)
- 传输模式：SSE (Server-Sent Events)
