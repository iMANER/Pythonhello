from email.mime.text import MIMEText
msg=MIMEText('Hello,send by Python...','plain','utf-8')

from_addr=input('From:')
'''
laftfacdkybcbjfa
'''
passwd=input('Password:')

to_addr=input('To:')

smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,passwd)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()