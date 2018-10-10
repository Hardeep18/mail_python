#!/usr/bin/python
import sys
import smtplib

subject = sys.argv[1]
body = sys.argv[2]
recipients = sys.argv[3]
gmail_user = 'username@gmail.com'
gmail_pwd = 'password'

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)

header = 'To:' + recipients + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + subject + ' \n'
msg = header + '\n' + body + '\n\n'

smtpserver.sendmail(gmail_user, recipients.split(', '), msg)
smtpserver.close()
