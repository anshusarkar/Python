from email.message import EmailMessage 

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

print(message)


# Subject: Greetings from anshusarkar1@gmail.com to anshusarkar2@gmail.com

body = """Hey there!

I'm learning to send emails using Python!"""

message.set_content(body)

print(message)