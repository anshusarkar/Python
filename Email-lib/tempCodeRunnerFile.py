
mail_server = smtplib.SMTP_SSL('smtp.example.com')

mail_server.set_debuglevel(1)

mail_pass = getpass.getpass('Password? ')

print(mail_pass)

mail_server.login(sender, mail_pass)

mail_server.send_message(message)

mail_server.quit()