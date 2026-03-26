# 📰 Simon Willison 博客更新 (2026-03-26)

### 1. [datasette-files-s3 0.1a1](https://simonwillison.net/2026/Mar/25/datasette-files-s3/#atom-everything)
**初步总结与核心观点**：
发布了 `datasette-files` 的一个新 S3 后端插件 `datasette-files-s3 0.1a1`。这个插件为 Datasette 提供了将文件存储在 Amazon S3（或兼容 API）并从中检索文件的能力，进一步扩展了 Datasette 生态处理大规模文件存储的潜力。

---

### 2. [Thoughts on slowing the fuck down](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/#atom-everything)
**初步总结与核心观点**：
Simon 关注到了 Mario Zechner (Pi Agent 框架的创建者) 的一篇文章，探讨当前 AI 行业的“狂热与降速”问题。核心观点是：当前 AI 工具链和包管理系统的迭代速度过快，导致开发者严重焦虑。业界需要开始放慢脚步，专注于基础设施的稳定性和可靠性，而不是盲目追求新功能。

---

### 3. [datasette-llm 0.1a1](https://simonwillison.net/2026/Mar/25/datasette-llm/#atom-everything)
**初步总结与核心观点**：
发布了基础插件 `datasette-llm 0.1a1`，它可以将 LLM（大型语言模型）工具引入到 Datasette 生态中，使其他插件能够调用语言模型能力。这是 Simon 致力于将数据库与 AI 能力深度融合的持续工程。

---

### 4. [LiteLLM Hack: Were You One of the 47,000?](https://simonwillison.net/2026/Mar/25/litellm-hack/#atom-everything)
**初步总结与核心观点**：
文章讨论了最近发生的 LiteLLM 供应链安全事件（被黑客植入后门）。安全研究员 Daniel Hnyk 使用 Google Cloud 的 BigQuery PyPI 公开数据集，追踪并找出了受影响的 4.7 万名开发者。核心观点强调了开源供应链安全的脆弱性以及利用云端大数据对攻击面进行事后溯源的有效性。
