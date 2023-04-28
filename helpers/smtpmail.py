# smtpmail.py
from smtplib import SMTP
from email.message import EmailMessage


class SMTPMail:
    __server = "smtp.example.com"
    __port = 25
    __from_address = "example@example.com"
    __to_addresses = ["example@example.com"]
    __subject = "Hello"
    __message = "Hello, This is a test message."
    __username = None
    __password = None

    def __init__(self,
                 from_address: str,
                 to_addresses: list[str],
                 subject: str, message: str,
                 server: str,
                 port: int = 25,
                 username: str = None,
                 password: str = None):
        """
        SMTPMail object that you can send via a server, using authentication if needed.
        :param from_address: Address to send the email from
        :param to_addresses: Addresses to send the email to
        :param subject: Subject of the email
        :param message: Body of the email
        :param server: SMTP server
        :param port: SMTP server port
        :param username: SMTP server username
        :param password: SMTP server password
        """

        self.__server = server
        self.__port = port
        self.__from_address = from_address
        self.__to_addresses = to_addresses
        self.__subject = subject
        self.__message = message
        self.__username = username
        self.__password = password

    def send(self):
        """
        Sends the SMTPMail object.
        :return: None
        """

        # Open a connection to the SMTP server
        with SMTP(self.__server, self.__port) as session:

            # If a username and password has been supplied, Authenticate with the SMTP server
            if self.__username is not None and self.__password is not None:
                session.login(self.__username, self.__password)

            # Send the email message
            session.send_message(self.__create_message_object())

    def __create_message_object(self):
        """
        Creates an EmailMessage object for use in smtplib.
        :return: EmailMessage
        """
        msg = EmailMessage()
        msg['Subject'] = self.__subject
        msg['From'] = self.__from_address
        msg['To'] = ', '.join(self.__to_addresses)
        msg.set_content(self.__message)

        return msg
