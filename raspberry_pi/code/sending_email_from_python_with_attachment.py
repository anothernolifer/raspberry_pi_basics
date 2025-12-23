# sending_email_from_python_with_attachment

import yagmail

password = ""

with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

yag = yagmail.SMTP('email_address', password)

yag.send( to="recipient_address",
          subject="Test Email",
          contents="This is a test email sent from a Python script using yagmail.",
          attachments="/path/to/attachment_file")

print("Email sent successfully.")