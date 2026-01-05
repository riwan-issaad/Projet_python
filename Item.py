class Item:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

    def __str__(self):
        return f"{self.nom} : {self.description}"


#Essaie 1(Exemple)

pokeball =Item("Pokeball","Objet permettant de capturer un Pokémon")
print(pokeball)


