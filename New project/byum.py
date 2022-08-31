import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    
except:
    print ('Something went wrong...')

gmail_user = 'nghiepha943@gmail.com'
gmail_password = 'urpayyiddswbopep'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print ('Something went wrong...')

sent_from = gmail_user
to = ['ong.hao.tranvan@gmail.com']
subject = 'OMG Super Important Message'
body = 'Hey, whats up?\n\n- Best friend'

email_text = """\
From:%s Newbie
To:%s
Subject:%s 

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