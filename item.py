class Item:
    def __init__(self, nom, description):
        self.name = nom
        self.description = description

    def __str__(self):
        return f"{self.name} : {self.description}"