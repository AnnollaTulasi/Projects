import smtplib,ssl



def send_email(message="testing"):
    host = "smtp.gmail.com"
    port = 465

    username = "tulasi.tls.111@gmail.com"
    password = "quhtldmrndjtcebw"

    receiver = "tulasiannolla04@gmail.com"
    content = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=content) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
#send_email("Hello ,how are you?")
