from time import sleep

from libtestingtools.spam.models import User


class Session:
    def __init__(self) -> None:
        self.counter: int = 0
        self.users: list[User] = []

    def save_user(self, user: User) -> None:
        self.counter += 1
        user.id = self.counter
        self.users.append(user)

    def list_it(self) -> list[User]:
        return self.users

    def roll_back(self) -> None:
        self.users.clear()

    def close(self) -> None:
        pass


class Connection:
    def __init__(self) -> None:
        sleep(1)

    def generate_session(self) -> Session:
        return Session()

    def close(self) -> None:
        pass
