class Sender:
    def send(self, sender: str, addressee: str, subject: str, body: str) -> str:
        if '@' not in sender:
            raise InvalidMail(f'Invalid sender: {sender}')
        return sender


class InvalidMail(Exception):
    pass
