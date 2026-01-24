class Item:
    def __init__(self, name, description,weight):
        self.name = name
        self.description = description
        self.weight =weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight}kg)"


#Essaie 1(Exemple)

pokeball =Item("Pokeball","Objet permettant de capturer un Pokémon",50)
Xp = Item("XP","monnaie du jeu permettant d'achter des pokemon rare en boutique",1)
Carte = Item("Carte","une carte indiquant ou se trouve les pokemons",0.750)


