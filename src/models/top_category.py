from src.models.category import Category

class TopCategory (Category):

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)
