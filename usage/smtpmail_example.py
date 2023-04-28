from helpers.smtpmail import SMTPMail


def main():
    SMTPMail("from@example.com",
             ["to1@example.com", "to2@example.com"],
             "This is a test message",
             "Hi there!\nSending a quick test email from the smtpmail helper!",
             "server.example.com",
             25,
             "Username@example.com",
             "MySuperStrongPassword").send()


if __name__ == '__main__':
    main()
