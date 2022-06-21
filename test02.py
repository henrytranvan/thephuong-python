from sender import Mail, Message
mail = Mail(
"smtp.gmail.com",
port = 465,
username = "ong.hao.tranvan@gmail.com",
password = "Tranhao1948",
use_tls = False,
use_ssl = True,
debug_level = False
)
msg = Message("this is a test")
msg.fromaddr = ("unknown", "ong.hao.tranvan@gmail.com")
msg.to = "nickdungtor@gmail.com"
msg.body = "this is a msg plain text body"
msg.html = "<b>this is a msg text body</b>"
msg.reply_to = "ong.hao.tranvan@gmail.com"
msg.charset = "utf-8"
msg.extra_headers = {}
msg.mail_options = []
msg.rcpt_options = []
# Send message
mail.send('msg')