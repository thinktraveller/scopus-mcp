# Scopus MCP Server: 构建流程与架构设计文档

本文档详细描述了 Scopus Model Context Protocol (MCP) 服务器项目的构建流程、架构设计思路、文件夹结构规范以及 MCP 工具集成指南。

## 1. 项目构建流程 (Build Process)

### 1.1 构建步骤

项目采用了现代 Python 包管理的最佳实践，从初始化到部署的完整流程如下：

1.  **环境初始化**:
    *   创建虚拟环境 (Virtual Environment) 以隔离项目依赖。
    *   使用 `uv` 或 `pip` 安装核心构建工具。
2.  **依赖安装**:
    *   解析 `pyproject.toml` 中的依赖项。
    *   安装生产环境依赖 (`mcp`, `httpx`, `python-dotenv`)。
    *   安装开发环境依赖 (`pytest`, `pytest-mock`)。
3.  **代码构建**:
    *   虽然本项目是纯 Python 脚本，不需要编译，但我们会打包成 Wheel (`.whl`) 格式以便分发。
    *   使用 `hatchling` 作为构建后端。
4.  **测试验证**:
    *   运行单元测试 (`pytest`) 验证核心逻辑。
    *   运行集成测试脚本 (`verify_refactor.py`) 验证 API 连接。
5.  **部署/运行**:
    *   配置 MCP 客户端（如 Claude Desktop）的 JSON 配置文件。
    *   通过标准输入/输出 (stdio) 启动服务。

### 1.2 技术选型依据

*   **语言**: Python 3.10+ (生态丰富，特别是在数据处理和网络请求方面)。
*   **构建后端**: `hatchling` (遵循 PEP 621 标准，配置简洁，支持现代 Python 打包)。
*   **包管理器**: `uv` (极速的 Python 包安装器和解析器，显著缩短 CI/CD 时间)。
*   **HTTP 客户端**: `httpx` (原生支持异步 `async/await`，性能优于同步的 `requests`，适合高并发的 MCP 服务)。
*   **协议**: Model Context Protocol (MCP) (标准化的 AI 模型上下文交互协议)。

### 1.3 依赖管理策略

所有依赖项均在 `pyproject.toml` 中严格定义：

*   **生产依赖**: 锁定最低版本号 (如 `httpx>=0.27.0`) 以确保 API 兼容性。
*   **开发依赖**: 分离在 `[project.optional-dependencies]` 中，避免生产环境臃肿。
*   **依赖更新**: 建议定期使用 `uv pip compile` 或类似工具审查依赖树。

### 1.4 环境变量处理方案

为了安全性和灵活性，配置加载遵循以下优先级（由高到低）：

1.  **系统环境变量**: `SCOPUS_API_KEY` (适合容器化部署或 CI/CD)。
2.  **`.env` 文件**: 自动加载项目根目录下的 `.env` 文件 (适合本地开发)。
3.  **`config.json`**: 传统的 JSON 配置文件 (兼容旧版本)。
4.  **默认值/报错**: 如果以上均未找到，抛出明确的 `ValueError`。

---

## 2. 架构设计思路 (Architecture Design)

### 2.1 系统分层设计

系统采用经典的分层架构，确保关注点分离 (Separation of Concerns)：

```mermaid
graph TD
    Client[MCP Client (Claude)] <--> Transport[Stdio Transport Layer]
    Transport <--> Server[MCP Server Layer]
    
    subgraph Core Logic
        Server --> Tools[Tool Definitions]
        Tools --> Service[ScopusClient Service]
        Service --> Cache[Caching Layer]
        Service --> Network[Network Layer (httpx)]
    end
    
    subgraph Data
        Network <--> ScopusAPI[Elsevier Scopus API]
        Cache <--> FileSystem[Local JSON Storage]
    end
    
    subgraph Config
        Service -.-> ConfigMgr[Config Manager]
        ConfigMgr -.-> EnvVars[Environment Variables]
    end
```

### 2.2 核心模块交互流程

1.  **请求接收**: `server.py` 通过 stdio 接收 JSON-RPC 格式的工具调用请求 (e.g., `search_scopus`)。
2.  **参数校验**: 验证请求参数（如 `query` 是否为空）。
3.  **服务调用**: `server.py` 调用 `ScopusClient` 的异步方法。
4.  **缓存检查**: `ScopusClient` 首先查询 `CacheManager`。
    *   **命中**: 直接返回本地 JSON 数据。
    *   **未命中**: 发起异步 HTTP 请求。
5.  **网络请求**: `httpx` 客户端发送请求到 Scopus API，自动处理：
    *   Authentication (添加 API Key Header)。
    *   Rate Limiting (遇到 429 自动休眠重试)。
6.  **数据清洗**: 获取的原始数据通过 `utils.py` 进行清洗和标准化。
7.  **响应返回**: 清洗后的数据被封装成 MCP 协议的 `TextContent` 格式返回给客户端。

### 2.3 关键设计决策

*   **异步优先**: 全链路采用 `async/await`，防止 I/O 阻塞导致服务无响应。
*   **文件级缓存**: 使用基于文件系统的 SHA-256 哈希缓存。相比内存缓存，它能持久化；相比 Redis，它无需额外部署组件，适合桌面端应用。
*   **防御性编程**: 在 API 调用层实现了指数退避 (Exponential Backoff) 重试机制，增强系统的鲁棒性。

### 2.4 扩展性考虑

*   **新工具添加**: 只需在 `server.py` 中注册新的 `@server.tool()` 并实现对应逻辑。
*   **新数据源**: `ScopusClient` 可以轻松扩展支持 Elsevier 的其他 API（如 ScienceDirect）。
*   **中间件**: 可以在 Server 和 Client 之间添加日志、监控或鉴权中间件。

---

## 3. 文件夹结构规范 (Folder Structure)

本项目遵循标准的 Python 项目结构，清晰区分源码、配置、文档和构建产物。

```
ScopusMCP/
├── src/                        # 源代码根目录
│   └── scopus_mcp/             # Python 包目录
│       ├── __init__.py         # 包标记
│       ├── server.py           # 核心业务代码：MCP 服务器入口
│       ├── client.py           # 核心业务代码：API 客户端
│       ├── cache.py            # 辅助模块：缓存逻辑
│       ├── utils.py            # 辅助模块：数据处理工具
│       └── config.py           # 配置管理
├── tests/                      # 单元测试与验证目录
│   ├── test_client.py          # 客户端逻辑测试
│   ├── test_parser.py          # 解析器逻辑测试
│   └── verify_refactor.py      # 集成测试脚本
├── config/                     # (逻辑概念) 配置文件存放
│   ├── config.json             # 实际配置文件
│   └── claude_desktop_config.json # 客户端集成配置
├── docs/                       # 项目文档
│   ├── README.md               # 概览文档
│   ├── PROJECT_STRUCTURE.md    # 详细结构文档
│   └── ARCHITECTURE_AND_BUILD.md # 本文档
├── build/                      # (自动生成) 构建输出目录
│   └── dist/                   # Wheel 包存放处
├── .env                        # 环境变量文件 (不应提交到 Git)
└── pyproject.toml              # 构建脚本与依赖配置
```

---

## 4. MCP 工具集成说明 (MCP Integration)

### 4.1 兼容性要求

*   **协议版本**: 兼容 Model Context Protocol Specification 1.0+。
*   **传输方式**: 必须支持 Standard Input/Output (stdio) 通信。
*   **客户端支持**: 经测试兼容 Claude Desktop App (macOS/Windows)。

### 4.2 必要的适配器接口

MCP 服务器必须实现以下 JSON-RPC 方法：

*   `tools/list`: 返回可用工具列表及其 JSON Schema 定义。
*   `tools/call`: 执行具体工具逻辑并返回结果。
*   `initialize`: 处理握手与能力协商。

### 4.3 配置映射规则

在 Claude Desktop 的配置文件 (`claude_desktop_config.json`) 中，需按以下格式映射：

```json
{
  "mcpServers": {
    "scopus-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/ScopusMCP", 
        "python",
        "-m",
        "scopus_mcp.server"
      ],
      "env": {
        "SCOPUS_API_KEY": "your-api-key-here" 
      }
    }
  }
}
```

*   **command**: 执行环境（推荐 `uv` 或绝对路径的 `python`）。
*   **args**: 启动参数，必须指向模块入口 `scopus_mcp.server`。
*   **env**: (可选) 可以在此处注入环境变量，覆盖默认配置。

### 4.4 扩展点说明

*   **自定义提示词 (Prompts)**: 未来可扩展 `prompts/list` 接口，提供预定义的 Scopus 搜索模板。
*   **资源 (Resources)**: 可扩展 `resources/list` 接口，直接将论文 PDF 或元数据作为资源暴露给 LLM 读取，而不仅仅是工具调用结果。
