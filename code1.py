import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
notifications = []  # 通知列表 
# 导入成绩表
def import_excel(file_path):
    data = pd.read_excel(file_path,skiprows=1)
    return data

# 生成通知
def create_notification(data,student_name1):

    notifications0 = []  # 通知列表
    # notifications1 = []  # 通知列表
    # notifications2 = []  # 通知列表
    #column = data['姓名']
    #print(column)
    text="亲爱的["+student_name1+"]同学:\n祝贺您顺利完成本学期的学习！教务处在此向您发送最新的成绩单。"

    for index, row in data.iterrows():
        student_name = row['姓名']
        student_id = row['学号']
        grade = row['百分成绩']
        subject = row['课程名称']
        #notification = f'姓名：{student_name}\n学号：{student_id}\n成绩：{grade}\n课程名称:{subject}\n'

        if student_name ==student_name1:
            text=text+'['+subject+']'+ '：['+str(grade)+']\n'
        # elif student_name == '李四':
        #     notifications1.append({'name': student_name, 'notification': notification})
        # elif student_name == '王五':
        #     notifications2.append({'name': student_name, 'notification': notification})
        
    text=text+'希望您能够对自己的成绩感到满意，并继续保持努力和积极的学习态度。如果您在某些科目上没有达到预期的成绩，不要灰心，这也是学习过程中的一部分。我们鼓励您与您的任课教师或辅导员进行交流，他们将很乐意为您解答任何疑问并提供帮助。请记住，学习是一个持续不断的过程，我们相信您有能力克服困难并取得更大的进步。再次恭喜您，祝您学习进步、事业成功！教务处'
    return text

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



# # 发送通知
# def send_notifications(notifications, sender_email, sender_password):
#     smtp_server = "2993622856@qq.com"
#     port = 587

#     context = ssl.create_default_context()
#     server = smtplib.SMTP(smtp_server,port)
#     try:
        
#         server.starttls(context=context)
#         server.login(sender_email, sender_password)

#         for notification in notifications:
#             receiver_email = notification['email']
#             message = MIMEMultipart("alternative")
#             message["Subject"] = "你的成绩通知"
#             message["From"] = sender_email
#             message["To"] = receiver_email

#             text = notification['notification']
#             part1 = MIMEText(text, "plain")
#             message.attach(part1)
            
#             server.sendmail(
#                 sender_email, receiver_email, message.as_string()
#             )
#     except Exception as e:
#         print(e)
#     finally:
#         server.quit()

# 主函数
def main():
    file_path = "grade.xlsx" 
    data = import_excel(file_path)
    namelist=[]

    for index,row in data.iterrows():
        student_name = row['姓名']
        if index == 0:
            namelist.append(student_name)
            continue
        flag=1
        for row2 in namelist:
            if student_name == row2:
                flag=0
                #print(1)
        if(flag==1 and index!=1):
            namelist.append(student_name)
    for row3 in namelist:
        text = create_notification(data,row3)
         # 设置邮箱服务器和登录信息
        print(text)
        smtp_server = "smtp.qq.com"
        smtp_port = 587
        smtp_username = "2473273950@qq.com"#邮件名
        smtp_password = "fenogtazvwsjdjga"#授权码

        # 创建SMTP客户端
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # 构建邮件
        msg = MIMEMultipart()
        msg["From"] = smtp_username
        msg["To"] = "2947753930@qq.com"#收件人
        msg["Subject"] = "邮件主题"

        body = text
        msg.attach(MIMEText(body, "plain"))

        # 发送邮件
        server.sendmail(smtp_username, "2947753930@qq.com", msg.as_string())

        # 关闭SMTP客户端
        server.quit() #这个可以发邮件，刚才试过了

if __name__ == "__main__":
    main()