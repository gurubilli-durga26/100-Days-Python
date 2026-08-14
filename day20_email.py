'''
#smtplib module
--------------
-->this module is used to send a mail without using
mail or outlook by running the python code.
-->and here by using port(857)
'''
#Sending Basic Text Email
import smtplib
sender_email=("SENDER_EMAIL")
sender_app_password=("APP_PASSWORD")
receiver_email=("RECEIVER_EMAIL")
message='''
hello

regards,
python
'''

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.sendmail(sender_email,receiver_email,message)
server.quit()
print('succesfully')

#Sending Email with Subject using EmailMessage
import smtplib
from email.message import EmailMessage
msg=EmailMessage()
sender_email=("SENDER_EMAIL")
sender_app_password=("APP_PASSWORD")
receiver_email=("RECEIVER_EMAIL")
msg['from']=sender_email
msg['to']=receiver_email
msg['Subject']='Python Mail'


msg.set_content('''
hello,
python


regards,
python
''')

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('succesfully')

#Sending to Multiple Recipients with Attachment
import smtplib
from email.message import EmailMessage

msg=EmailMessage()
sender_email=("SENDER_EMAIL")
sender_app_password=("APP_PASSWORD")
receiver_email=[("RECEIVER_EMAIL_1"),("RECEIVER_EMAIL_2"),("RECEIVER_EMAIL_3"),...("RECEIVER_EMAIL_n")]
msg['from']=sender_email
msg['to']=receiver_email
msg['Subject']='Python Mail'


msg.set_content('''
hello,
python


regards,
python
''')
with open('Day3_str_list_methods.py','rb')as file:
    file_content=file.read()
    msg.add_attachment(file_content,maintype='application',subtype='py',filename='Day3_str_list_methods.py')

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_app_password)
server.send_message(msg)
server.quit()
print('succesfully')

