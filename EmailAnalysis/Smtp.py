import smtplib, ssl
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "mishraprayash00@gmail.com"
receiver_email = "mishraprayash11@gmail.com"
password = "vbwz uyzk mkxx aeka"
message = """\
Subject: Hi there
This message is sent from Python for testing purpose"""

context = ssl.create_default_context()
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email Sent Successfully')
except Exception as e:
    print(e)
