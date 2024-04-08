import smtplib
import getpass
from email.message import EmailMessage 
import os.path
import mimetypes

message = EmailMessage()

print(message)

sender = "anshusarkar1@gmail.com"
reciver = "anshusarkar2@gmail.com"

message['From'] = sender
message['To'] = reciver

print(message)

# From: anshusarkar1@gmail.com that's the translation of human understanding of the avobe code
# To: anshusarkar2@gmail.com 

message['Subject'] = 'Greetings from {} to {}!'.format(sender, reciver)

# print(message)

# Subject: Greetings from anshusarkar1@gmail.com to anshusarkar2@gmail.com

body = """Hey there!

I'm learning to send emails using Python!"""

attachment_path = "/home/zero/Python/Email-lib/Zero.jpg"

attachment_filename = os.path.basename(attachment_path)

message.set_content(body)

mime_type, _ = mimetypes.guess_type(attachment_path)

print(mime_type,"\n")

mime_type, mime_subtype = mime_type.split('/', 1)

print("The attachmanet's extension is : ",mime_type,"\n") # Would seperate image name and store them in mime type and would store the extension in mime_subtype

print("The attachment's namr is : ",mime_subtype,"\n")



with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(), # Reading thee contains of the file attachmanets and attaching it to the message 
                            maintype=mime_type, # Assinging the name of the attachment to maintype stating the attachments name
                            subtype=mime_subtype, # Assinging the extension name to the subtype stating the attachments extension name
                            filename=os.path.basename(attachment_path))
 

# mail_server = smtplib.SMTP('localhost')

mail_server = smtplib.SMTP_SSL('smtp.example.com')

mail_server.set_debuglevel(1)

mail_pass = getpass.getpass('Password? ')

print(mail_pass)

mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()

# I would have to know more about mailing IG .