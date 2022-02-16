import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password123"
subject = "Python Email Test"
body = "This Is Testing Of Code Python :D"

message = f"""Sender: {sender}
receiver: {receiver}
subject: {subject}\n
{body}
"""
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    print("logged in......")
    server.sendmail(sender, receiver, message)
    print("Email sent :)")

except smtplib.SMTPAuthenticationError:
    print("Logging failed")
