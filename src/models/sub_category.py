from src.models.category import Category

class SubCategory (Category):

    def __init__(self, id: int, name: str, top_category_id: int) -> None:
        super().__init__(id, name)
        self.top_category_id = top_category_id

