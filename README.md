# Daily Reports Archive 📰

一个利用 GitHub 仓库自动归档和分发每日简报（如 GitHub Trending、Simon Willison's Blog）的自动化中心。

## 目录结构
```text
.
├── 2026-03-26/                 # 每天生成一个日期文件夹
│   ├── github-trending.md      # 按主题分类的报告
│   └── simon-willison-blog.md
├── config.toml                 # 配置文件（收件人邮箱等）
├── scripts/                    # 存放发邮件等自动化脚本
└── .github/workflows/          # GitHub Actions 自动化工作流
```

## 使用方法

1. 修改 `config.toml` 中的 `recipients` 列表，指定你要发送的邮箱。
2. 配置仓库的 **Settings -> Secrets and variables -> Actions**，添加以下 Secret：
   - `SMTP_SERVER`: 如 smtp.qq.com
   - `SMTP_PORT`: 465 或 587
   - `SMTP_USERNAME`: 你的发件邮箱账号
   - `SMTP_PASSWORD`: 你的邮箱授权码
   - `SENDER_EMAIL`: (可选) 发件人地址，默认同 USERNAME
3. 每天向 `YYYY-MM-DD` 目录 push 相关的 markdown 报告，GitHub Actions 就会自动打包当天所有报告并通过邮件发送给你！
