# MCP数学演示项目

这是一个使用MCP（Mathematical Computing Platform）的Python演示项目，旨在帮助初学者了解和学习数学计算的基本概念和应用。

## 项目简介

本项目展示了如何通过代码调用MCP（sse和stdio）
- MCP的sse方式
- MCP的stdio方式
- 如何结合大模型调用MCP

## 环境要求
安装uv https://docs.astral.sh/uv/getting-started/installation/

## 安装步骤

1. 克隆项目到本地：
```bash
git clone [项目地址]
cd mcp-math-demo
```

2. 创建并激活虚拟环境（推荐）：
```bash
# 创建虚拟环境（工程中会多一个.venv 文件），并激活环境
uv venv
# 激活环境，mac和window 有点差异，需注意下
source .venv/bin/activate
# 或
.\venv\Scripts\activate  # Windows
```

3. 安装依赖包：
```bash
uv pip install -e .
```

## 项目结构

```
mcp-math-demo/
├── README.md
├── requirements.txt
├── src/
│   └── main.py
└── examples/
    └── basic_math.py
```

## 使用说明

1. sse 启动
```bash
uv run src/example/server-math-sse.py
```

2. stdio调试
```bash
uv run mcp dev src/example/server-math-stdio.py
```

3. 启动客户
```bash
uv run src/example/client-langchain.py
```

4. 调试客户端
....

详情可以查看：
[https://mtqth1thwc.feishu.cn/wiki/TLyuw5GlziSL5Kk7xzScuEMgn1c?from=from_copylink](https://blog.csdn.net/weixin_53122830/article/details/148120229)

## 学习资源
- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [MCP官方文档](https://modelcontextprotocol.io/introduction) 

### 开发工具
- **Uv/Uvx**: 高效的Python虚拟环境管理工具
  - [官方文档](https://docs.astral.sh/uv/)

- **NPX**: 无需安装即可运行npm包命令的工具（Node 18+）
  - [使用说明](https://www.tkcnn.com/npm/commands/npx.html)
  - 用于启动调试工具：`npx @modelcontextprotocol/inspector@0.6.0`

- **NVM**: Node.js版本管理工具
  - [Unix/Linux版本](https://github.com/nvm-sh/nvm)
  - [Windows版本](https://github.com/coreybutler/nvm-windows)（需要管理员权限）

## 贡献指南

欢迎提交问题和改进建议！如果您想贡献代码，请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的更改
4. 推送到您的分支
5. 创建一个新的 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件
