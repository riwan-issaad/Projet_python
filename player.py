from item import Item 

class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {} 

    def move(self, direction):
        # Sécurité : on utilise .get() pour éviter le crash si la direction n'existe pas
        next_room = self.current_room.exits.get(direction)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.check_history()
        return True

    def check_history(self):      
        if len(self.history) > 0:
            print(f"Déjà visité : {', '.join([r.name for r in set(self.history)])}")
            
    def back(self):
        if not self.history:
            print("\nImpossible de revenir en arrière.")
            return False
        self.current_room = self.history.pop()
        print(f"\nVous êtes revenu en arrière.")
        print(self.current_room.get_long_description())
        return True

    def look(self):
        print(self.current_room.get_long_description())
        print(self.current_room.get_inventory())

    def take(self, item_name):
        if item_name in self.current_room.inventory:
            item = self.current_room.inventory.pop(item_name)
            self.inventory[item_name] = item
            print(f"Vous avez pris {item.name}.")
            return True
        else:
            print(f"L'objet '{item_name}' n'existe pas ici.")
            return False

    def drop(self, item_name):
        if item_name in self.inventory:
            item = self.inventory.pop(item_name)
            self.current_room.inventory[item_name] = item
            print(f"Vous avez posé {item.name}.")
            return True
        else:
            print(f"Vous n'avez pas de '{item_name}'.")
            return False

    def get_inventory(self):
        if not self.inventory:
            print("Votre inventaire est vide.")
            return
        
        print("Vous disposez des items suivants :")
        for item in self.inventory.values():
            print(f"    - {item.name} : {item.description} ({item.weight} kg)")

    def talk(self, name):
        if name in self.current_room.characters:
            character = self.current_room.characters[name]
            print(f"\n{name}: {character.get_msg()}\n")
            return True
        else:
            print(f"\nIl n'y a pas de '{name}' ici.")
            return False

    def add_reward(self, reward):
        print(f"✨ Récompense reçue : {reward}")
        # On crée un item fictif pour la récompense
        if reward not in self.inventory:
            self.inventory[reward] = Item(reward, "Récompense de quête", 0)

    def capture(self, pokemon_name):
        # Vérifie la pokeball (en minuscule !)
        # Note : Dans ton setup game.py, tu as mis "Pokeball" avec majuscule dans l'inventaire
        # On va gérer les deux cas pour être sûr
        has_ball = "pokeball" in self.inventory or "Pokeball" in self.inventory
        
        if not has_ball:
            print("\n❌ Vous n'avez pas de Pokéball !")
            return False

        if pokemon_name in self.current_room.inventory:
            pokemon = self.current_room.inventory.pop(pokemon_name)
            print(f"\n🔴 Vous lancez une Pokéball sur {pokemon.name}...")
            print("...")
            print(f"✨ C'est attrapé ! {pokemon.name} est dans votre équipe !")
            
            # Retire la pokeball (on cherche la bonne clé)
            if "pokeball" in self.inventory: del self.inventory["pokeball"]
            elif "Pokeball" in self.inventory: del self.inventory["Pokeball"]
            
            self.inventory[pokemon_name] = pokemon
            return True
        else:
            print(f"\nIl n'y a pas de {pokemon_name} ici.")
            return False