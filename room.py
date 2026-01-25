class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {} # Changé en dictionnaire pour faciliter la recherche
        self.characters = [] # Liste des PNJ présents

    def get_exit(self, direction):
        if direction in self.exits:
            return self.exits[direction]
        return None

    def get_exit_string(self):
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        return exit_string.strip(", ")

    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"