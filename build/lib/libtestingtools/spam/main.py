from libtestingtools.spam.db import Session
from libtestingtools.spam.email_sender import Sender


class SpamSender:
    def __init__(self, session: Session, sender: Sender) -> None:
        self.session = session
        self.sender = sender

    def send_emails(self, sender: str, subject: str, body: str) -> None:
        for user in self.session.list_it():
            self.sender.send(
                sender,
                user.email,
                subject,
                body
            )
