rimport time
import smtplib
from email.message import EmailMessage
from pythonping import ping
import json

user_data = {
    "website": input("Enter website: "), # input = json content
    "email": input("Enter email: "),
}

with open("data.json", "w") as file:
    json.dump(user_data, file, indent=4) #saves the json

url = user_data["website"]
email_address = user_data["email"]
error_counter = 0

def ping_website():
    try:
        response = ping(url,count=1)
        print(f"{url} is {response}")
    except Exception as e:
        print(f"Error, {url} is invalid")
        print(f"{url} didnt respond")
        global error_counter
        error_counter += 1
        if error_counter >= 5:
            error_counter = 0
            msg = EmailMessage()
            msg['Subject'] = 'Your website has gone down and requires immediate attention!'
            msg['From'] = 'enter-your-email'
            msg['To'] = user_data["email"]
            msg.set_content('this is an automated message to warn you that your website is currently down')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('enter-your-email', 'enter 2fa password key in app settings')
                smtp.send_message(msg)



while True:
    ping_website()
    time.sleep(60)ss