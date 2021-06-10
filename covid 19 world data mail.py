#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
import requests

from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/#countries'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
data = soup.find_all("div", class_="maincounter-number")
x = (data[0].text)
y = (data[1].text)
z = (data[2].text)

def sendingmail():
    gmail_user = "" #Write your gmail address
    gmail_password = "" #Write your password

    sent_from = gmail_user
    to = [""] # Write mail adress
    subject = ""
    body = f"""


    Toplam Covid-19 Vaka Sayisi: {x}
    Toplam Olum Sayisi :{y} 
    Toplam Iyilesen Vaka Sayisi:{z}
         Saygilar Robot,  """

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
sendingmail()



