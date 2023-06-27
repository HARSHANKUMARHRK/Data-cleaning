import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

body = f'''Hello team
we have attached Answer file for todays event.
Do check it out!!!

With Regards
Team Data Prosumers

'''
df=pd.read_csv("data.csv")
mailid = df["Email"]
for i in mailid:

    sender = 'cryptrix22@gmail.com'
    password = 'wajwjomyaockwokc'
    receiver = i

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Event'

    message.attach(MIMEText(body, 'plain'))

    qrimage = f'answer_notebook.ipynb'

    binary_pdf = open(qrimage, 'rb')

    payload = MIMEBase('application', 'octate-stream', Name=qrimage)
    payload.set_payload((binary_pdf).read())

    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=qrimage)
    message.attach(payload)

    session = smtplib.SMTP('smtp.gmail.com', 587)

    session.starttls()

    session.login(sender, password)

    text = message.as_string()
    session.sendmail(sender, receiver, text)
    session.quit()
    print('Mail Sent')
