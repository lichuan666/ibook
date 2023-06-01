import smtplib
from email.mime.text import MIMEText

"""
reference:
https://zhuanlan.zhihu.com/p/24180606
"""

mail_host = "smtp.qq.com"
mail_user = "2997155472"
mail_pass = "ezmhvfexgkcrdfad"  # 这个是自己qq邮箱的授权码
sender = "2997155472@qq.com"


def send_email(to_email, mail_content=None):
    # 设置email信息
    # 邮件内容设置
    if mail_content is None:
        content = "You are late"
    else:
        content = mail_content

    receivers_list = [to_email]

    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'title'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers_list[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers_list, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误
