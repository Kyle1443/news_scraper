from requests_html import HTMLSession
import os
import smtplib
from email.message import EmailMessage
import time
import schedule


session = HTMLSession()
page = 'https://news.google.com/topstories?hl=en-GB&gl=GB&ceid=GB:en'

r = session.get(page)
r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')
link_list = []

key_words = 'Covid'

for article in articles:
    try: 
        newsitem = article.find('h3', first=True)
        title = newsitem.text
        links = newsitem.absolute_links
        if not key_words in title:continue
        link_list.append(links)
        print(str(link_list))
    except:
        pass

time.sleep(2)


EMAIL_ADRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Weather alert'
msg['From'] = EMAIL_ADRESS
msg['To'] = 'kyle1443@gmail.com'
msg.set_content(str(link_list))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)

print('message sent')


  