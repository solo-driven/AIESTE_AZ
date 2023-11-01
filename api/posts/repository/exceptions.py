class PostNotFoundError(Exception):
    def __init__(self, id: int):
        self.id = id
        super().__init__(f"Post with id {self.id} not found")
