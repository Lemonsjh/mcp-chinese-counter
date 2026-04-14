# 中文字数统计 MCP 服务

## 功能说明

提供中文字符统计能力，纯 Python 实现，部署轻量。

### 工具列表

#### count_chinese_chars
统计文本中的纯中文字符数量（不含标点、英文、数字、空格）。

- 输入参数：`text` (string)
- 返回：整数

#### count_chinese_chars_detail
返回字符详细分类统计。

- 输入参数：`text` (string)
- 返回：JSON 对象

## 环境要求

- Python 3.10+

## 依赖

```
mcp[server]>=1.0.0
```

## 本地运行

```bash
pip install -r requirements.txt
python server.py
```
