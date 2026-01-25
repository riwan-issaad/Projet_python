class Item:
    def __init__(self, nom, description, weight=0):
        self.name = nom
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"
