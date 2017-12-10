#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request , response,error
import urllib
import smtplib
from email.mime.text import MIMEText
import threading
import time

'''
service monitor
'''

def monitor(url):
    req = request.Request(url)
    response = None
    try:
        response = request.urlopen(req)
        return 1
    except error.URLError as e:
        print ('Reason:'+ str(e))
        return str(e)


def mail(content):
    sender = ""#sender email address
    receiver = [""]#receiver list
    host = ''#sender host
    port = 465#port
    mail_pass="" #sender password
    msg = MIMEText(content)
    msg['From'] = "" #from address
    msg['To'] = receiver[0]
    msg['Subject'] = "system error warning"

    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender,mail_pass) 
        smtp.sendmail(sender, receiver, msg.as_string())
    except Exception as  e:
        print (e)

def task():
    url = ''#test link
    while True:
        result = monitor(url)
        if result != 1 :
            mail(result)
        time.sleep(2*60)

if __name__  == "__main__" :
    task()