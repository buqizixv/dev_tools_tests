class User:
    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.id: int | None = None
