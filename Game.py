import tkinter as tk
from tkinter import scrolledtext
from tkinter import font
import sys

from room import Room
from player import Player
from command import Command
from action import Actions  
from item import Item       
from character import Character
from quest import Quest, QuestManager

class _StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert('end', string)
        self.text_widget.see('end')

    def flush(self):
        pass

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Pokémon : L'Aventure Textuelle")
        self.root.geometry("800x600")

        self.custom_font = font.Font(family="Courier", size=12)
        
        self.text_area = scrolledtext.ScrolledText(self.root, state='normal', wrap='word', font=self.custom_font)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)
        
        sys.stdout = _StdoutRedirector(self.text_area)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var, font=self.custom_font)
        self.entry.pack(fill='x', padx=10, pady=5)
        self.entry.bind("<Return>", self.process_input)
        self.entry.focus_set()

        self.submit_button = tk.Button(self.root, text="Envoyer", command=self.process_input)
        self.submit_button.pack(pady=5)

    def process_input(self, event=None):
        user_input = self.entry_var.get()
        if user_input.strip():
            print(f"\n> {user_input}") 
            self.game.process_command(user_input)
            self.entry_var.set("")
            if self.game.finished:
                self.root.after(3000, self.root.destroy)

    def start(self):
        self.root.mainloop()

class Game:
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.quest_manager = None

    def setup(self):
        # ... (Garde tes commandes help, quit, go, take, capture... au début) ...
        # ... (Ne touche pas aux commandes, modifie juste à partir de "2. Setup rooms") ...

        # 2. Setup rooms (Configuration de la Carte)
        # ------------------------------------------

        # Création des lieux
        maison = Room("Maison", "dans ta chambre. C'est ici que tout commence.")
        place = Room("Place du Village", "sur la place principale de Bourg-Palette.")
        labo = Room("Labo de Chen", "dans le laboratoire rempli de livres et de machines.")
        route1 = Room("Route 1", "sur un chemin de terre entouré de hautes herbes.")
        arene = Room("Arène", "devant l'imposante Arène du Champion.")
        
        # On ajoute les salles au jeu
        self.rooms.extend([maison, place, labo, route1, arene])

        # Connexions (Définition des sorties)
        # Maison <-> Place
        maison.exits = {"N": place}
        place.exits = {"S": maison, "E": labo, "N": route1}
        
        # Place <-> Labo
        labo.exits = {"O": place}
        
        # Place <-> Route 1
        route1.exits = {"S": place, "N": arene}
        
        # Route 1 <-> Arène
        arene.exits = {"S": route1}


        # 3. Setup Items (Les Objets)
        # ---------------------------
        
        # Maison : Pokéball + Potion
        pokeball = Item("Pokeball", "Une balle rouge et blanche.")
        maison.inventory["pokeball"] = pokeball
        
        potion = Item("Potion", "Un spray pour soigner les blessures.")
        maison.inventory["potion"] = potion

        # Labo : Colis (Objet de quête)
        # Note : On met le colis au Labo pour l'exemple, ou à la Boutique si tu en crées une.
        # Disons que Chen l'a oublié sur son bureau pour l'instant, ou qu'il faut le chercher ailleurs.
        # Pour ta quête actuelle, mettons le colis dans la "Maison" pour que ce soit facile :
        colis = Item("Colis", "Le paquet pour le Professeur.")
        maison.inventory["colis"] = colis


        # 4. Setup Characters & Pokémon (PNJ et Sauvages)
        # -----------------------------------------------
        
        # Maman est à la maison
        maman = Character("Maman", "Ta mère", maison, ["Coucou mon chéri !", "N'oublie pas ta casquette."])
        maison.characters.append(maman)
        
        # Chen est au Labo
        chen = Character("Chen", "Le Professeur Pokémon", labo, ["Bonjour !", "Ah, tu as mon colis ?"])
        labo.characters.append(chen)

        # Rattata est sur la Route 1 (En tant qu'Item pour la capture)
        rattata = Item("Rattata", "Un Pokémon sauvage violet.")
        route1.inventory["rattata"] = rattata


        # 5. Setup Player & Quests
        # ------------------------
        name = input("\nEntrez votre nom: ")
        self.player = Player(name)
        self.player.current_room = maison  # On commence dans la maison

        self.quest_manager = QuestManager(self.player)
        
        # Quête 1 : Le Colis
        # Attention : Les objectifs doivent correspondre à tes actions !
        quest_colis = Quest(
            "Livraison Express", 
            "Prends le colis chez toi et apporte-le à Chen au Labo.",
            ["prendre colis", "parler avec Chen"], 
            "Pokédex"
        )
        self.quest_manager.add_quest(quest_colis)
        self.quest_manager.activate_quest("Livraison Express")
        
        # Quête 2 : L'Arène
        quest_arene = Quest(
            "Vers le sommet", 
            "Traverse la Route 1 et atteins l'Arène.",
            ["Visiter Arène"], 
            "Potion Max"
        )
        self.quest_manager.add_quest(quest_arene)
        self.quest_manager.activate_quest("Vers le sommet")
        
        map_cmd = Command("map", " : afficher la carte du monde", Actions.map, 0)
        self.commands["map"] = map_cmd

    def play(self):
        self.setup()
        self.print_welcome()

        try:
            self.gui = GameGUI(self)
            self.gui.start()
        except tk.TclError:
            print("\n⚠️  Impossible de lancer l'interface graphique (Pas d'écran détecté).")
            print("   -> Lancement en mode texte classique...\n")
            
            while not self.finished:
                try:
                    self.process_command(input("> "))
                except (KeyboardInterrupt, EOFError):
                    self.finished = True
                    print("\nAu revoir !")

    def process_command(self, command_string):
        if not command_string: return
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' inconnue. Tapez 'help'.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans le monde des Pokémon !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        self.player.look()

if __name__ == "__main__":
    Game().play()