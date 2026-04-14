# 中文字数统计 MCP 服务

一个轻量的 MCP 服务，提供中文字符统计功能。

## 功能

### 工具 1：count_chinese_chars
统计文本中的纯中文字符数量（不含标点、英文、数字、空格）。

**参数：**
- `text` (string): 输入文本

**返回：** 纯中文字符的整数数量

**示例：**
```
输入: "你好，世界！Hello 123"
输出: 4
```

### 工具 2：count_chinese_chars_detail
返回详细的字符分类统计。

**参数：**
- `text` (string): 输入文本

**返回：**
```json
{
  "total": 总字符数,
  "chinese": 中文字符数,
  "letters": 英文字母数,
  "digits": 数字个数,
  "punctuation": 标点数,
  "spaces": 空格数
}
```

## 本地运行

```bash
pip install -r requirements.txt
python server.py
```

## 部署到魔塔社区

1. 将本仓库推送到 GitHub
2. 在魔塔「模型服务」→「MCP」中选择「从 GitHub 导入」
3. 填写仓库信息，平台自动拉取并部署

## 技术栈

- Python 3.10+
- MCP Python SDK (`mcp[server]`)
- 传输模式：SSE (Server-Sent Events)
