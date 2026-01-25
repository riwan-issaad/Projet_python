from item import Item 

class Player():
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {} 

    def move(self, direction):
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
        if self.current_room.inventory:
            print("Objets visibles :")
            for item in self.current_room.inventory.values():
                print(f"    - {item}")
        if self.current_room.characters:
            print("Personnages présents :")
            for char in self.current_room.characters:
                print(f"    - {char}")

    def take(self, item_name):
        if item_name in self.current_room.inventory:
            item = self.current_room.inventory.pop(item_name)
            self.inventory[item_name] = item
            print(f"\nVous avez ramassé : {item_name}")
            return True
        else:
            print(f"\nIl n'y a pas de '{item_name}' ici.")
            return False

    def drop(self, item_name):
        if item_name in self.inventory:
            item = self.inventory.pop(item_name)
            self.current_room.inventory[item_name] = item
            print(f"\nVous avez posé : {item_name}")
            return True
        else:
            print(f"\nVous n'avez pas de '{item_name}' dans votre sac.")
            return False

    def get_inventory(self):
        if not self.inventory:
            print("\nVotre sac est vide.")
            return
        print("\nContenu de votre sac :")
        for item in self.inventory.values():
            print(f"    - {item}")

    def talk(self, name):
        found_char = None
        for char in self.current_room.characters:
            if char.name == name:
                found_char = char
                break
        
        if not found_char:
            print(f"\nIl n'y a pas de '{name}' ici.")
            return False

        if found_char.name == "Chen":
            if "colis" in self.inventory:
                print("\nChen : Oh ! Tu as rapporté mon Colis ! Merci.")
                print("Chen : Tiens, voici ton Pokédex !")
                del self.inventory["colis"]
                return True

        print(f"\n{found_char.name}: {found_char.get_msg()}")
        return True

    def add_reward(self, reward):
        print(f"✨ Vous avez reçu : {reward} !")
        item_recompense = Item(reward, f"Récompense obtenue.")
        self.inventory[reward.lower()] = item_recompense

    # --- FONCTION CAPTURE (ESSENTIELLE) ---
    def capture(self, pokemon_name):
        # Vérifie la pokeball (en minuscule !)
        if "pokeball" not in self.inventory:
            print("\n❌ Vous n'avez pas de Pokéball !")
            return False

        # Vérifie le pokemon
        if pokemon_name in self.current_room.inventory:
            pokemon = self.current_room.inventory.pop(pokemon_name)
            print(f"\n🔴 Vous lancez une Pokéball sur {pokemon.name}...")
            print("...")
            print(f"✨ C'est attrapé ! {pokemon.name} est dans votre équipe !")
            
            # Retire la pokeball
            del self.inventory["pokeball"]
            
            # Ajoute le pokémon
            self.inventory[pokemon_name] = pokemon
            return True
        else:
            print(f"\nIl n'y a pas de {pokemon_name} ici.")
            return False