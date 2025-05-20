import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
'''
导入py自带的库，以下是正文
'''

mail=MIMEMultipart()#实例化一个邮件
mail['Subject']="test for mail"#这是邮件的标题
mail['From']="send@qq.com"#发件人的地址
mail['To']="recve@qq.com"#收件人的地址

body='''
<html>
  <body>
    <h1>HTML邮件测试</h1>
    <p>这是一封<strong>HTML格式</strong>的邮件和文件。</p>
    <p>由py脚本自动发出</p>
  </body>
</html>
'''#这是邮件的正文，支持html 等

content=MIMEText(body,'html','utf-8')#配置邮件正文的解析格式
mail.attach(content)#将内容追加到邮件中

'''
这是邮件附件的内容
'''
file=MIMEApplication(open('img/1.jpg','rb').read())#读取二进制文件内容，将结果放入
filename='1.jpg'
file.add_header('Content-Disposition','attachment',filename=filename)#为该附件添加其他信息，文件名，类型等
mail.attach(file)#将附件内容追加到mail

'''
建立连接，通信
'''
conn=smtplib.SMTP_SSL('smtp.qq.com',465)#像想要发送邮件的服务器建立连接，这里使用的是stml的ssl,即加密版本
conn.login('user@qq.com','password')#登录该邮件服务器
conn.sendmail(mail['From'],mail['To'],str(mail))#发送邮件，填入收发信息，字符串化的mail
conn.quit()#退出通信