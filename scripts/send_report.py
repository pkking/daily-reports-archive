import os
import smtplib
from email.message import EmailMessage
import glob
import sys
import toml

def main():
    try:
        config = toml.load('config.toml')
    except Exception as e:
        print(f"Error loading config.toml: {e}")
        sys.exit(1)
    
    recipients = config.get('email', {}).get('recipients', [])
    if not recipients:
        print("No recipients configured in config.toml")
        sys.exit(0)
        
    # 查找最新的日期文件夹 (格式 YYYY-MM-DD)
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and len(d) == 10 and d.count('-') == 2 and d[0].isdigit()]
    if not dirs:
        print("No report directories found.")
        sys.exit(0)
        
    latest_dir = sorted(dirs)[-1]
    
    # 读取该目录下的所有 markdown 文件
    md_files = sorted(glob.glob(os.path.join(latest_dir, '*.md')))
    if not md_files:
        print(f"No markdown files found in {latest_dir}")
        sys.exit(0)
        
    body = f"🚀 这是 {latest_dir} 的每日简报合集：\n\n"
    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        topic = os.path.basename(md_file).replace('.md', '').replace('-', ' ').title()
        body += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        body += f" 📌 {topic}\n"
        body += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        body += f"{content}\n\n"
        
    # 获取环境变量中的 SMTP 配置 (从 GitHub Secrets 注入)
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = int(os.environ.get('SMTP_PORT', 465))
    smtp_user = os.environ.get('SMTP_USERNAME')
    smtp_pass = os.environ.get('SMTP_PASSWORD')
    sender_email = os.environ.get('SENDER_EMAIL', smtp_user)
    
    if not all([smtp_server, smtp_user, smtp_pass]):
        print("SMTP secrets missing. Please check GitHub Actions secrets.")
        sys.exit(1)
        
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = f"📰 每日简报归档 - {latest_dir}"
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    
    try:
        # 支持 SSL 或 TLS
        if smtp_port == 465:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {recipients}")
    except Exception as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
