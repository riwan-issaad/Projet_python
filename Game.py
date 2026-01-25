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
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Pokémon : L'Aventure Étendue")
        self.root.geometry("800x600")
        self.custom_font = font.Font(family="Courier", size=11)

        self.text_area = scrolledtext.ScrolledText(
            self.root, state='normal', wrap='word', font=self.custom_font)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)
        sys.stdout = _StdoutRedirector(self.text_area)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var, font=self.custom_font)
        self.entry.pack(fill='x', padx=10, pady=5)
        self.entry.bind("<Return>", self.process_input)
        self.entry.focus_set()

        self.btn = tk.Button(self.root, text="Envoyer",
                              command=self.process_input)
        self.btn.pack(pady=5)

        # On lance l'intro une fois la fenêtre prête
        self.game.print_welcome()

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
        # NOUVEAU : Une variable pour savoir si on attend le nom
        self.waiting_for_name = True

    def setup(self):
        # Commandes
        self.commands["help"] = Command("help", " : aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter", Actions.quit, 0)
        self.commands["go"] = Command("go", " <dir> : bouger (N, E, S, O, U, D)",
                                      Actions.go, 1)
        self.commands["back"] = Command("back", " : retour", Actions.back, 0)
        self.commands["look"] = Command("look", " : observer", Actions.look, 0)
        self.commands["take"] = Command("take", " <item> : prendre",
                                        Actions.take, 1)
        self.commands["drop"] = Command("drop", " <item> : poser",
                                        Actions.drop, 1)
        self.commands["sac"] = Command("sac", " : inventaire",
                                       Actions.check, 0)
        self.commands["talk"] = Command("talk", " <nom> : parler",
                                        Actions.talk, 1)
        self.commands["quests"] = Command("quests", " : quêtes",
                                          Actions.quests, 0)
        self.commands["capture"] = Command("capture", " <nom> : capturer",
                                           Actions.capture, 1)
        self.commands["map"] = Command("map", " : carte", Actions.map, 0)

        # --- CREATION DE LA CARTE ---
        maison = Room("Maison du Héros", "dans ta chambre.")
        place = Room("Place du Village", "au centre du village.")
        labo = Room("Labo de Chen", "dans le laboratoire.")
        boutique = Room("Boutique",
                        "dans le magasin général. Une clé brille sur le comptoir.")
        route1 = Room("Route 1",
                      "au pied de la montagne. Une barrière bloque le chemin montant.")
        grotte = Room("Grotte Souterraine", "dans une grotte sombre (Niveau -1).")
        route2 = Room("Route 2", "sur un chemin escarpé en altitude.")
        village2 = Room("Village Céleste",
                        "dans un petit village perdu dans les nuages.")
        sommet = Room("Sommet de l'Arène",
                      "tout en haut, devant le Champion (FIN).")

        self.rooms.extend([maison, place, labo, boutique, route1, grotte,
                           route2, village2, sommet])

        # Connexions
        maison.exits = {"N": place}
        place.exits = {"S": maison, "E": boutique, "O": labo, "N": route1}
        labo.exits = {"E": place}
        boutique.exits = {"O": place}
        route1.exits = {"S": place, "D": grotte, "U": route2}
        grotte.exits = {"U": route1}
        route2.exits = {"D": route1, "U": village2}
        village2.exits = {"D": route2, "U": sommet}
        sommet.exits = {"D": village2}

        # Objets
        maison.inventory["Pokeball"] = Item("Pokeball", "Pour capturer !", 0.1)
        maison.inventory["colis"] = Item("Colis", "Le paquet pour Chen.", 1.0)
        boutique.inventory["cle"] = Item("Cle", "La clé de la barrière Route 2.", 0.1)
        grotte.inventory["rattata"] = Item("Rattata", "Un petit Pokémon violet.", 0.5)
        sommet.inventory["Badge"] = Item("Badge", "Le Badge Roche.", 0.1)

        # Personnages
        labo.characters["Chen"] = Character("Chen", "Le Professeur.", labo,
                                           ["Bonjour !",
                                            "J'attends mon colis."])
        boutique.characters["Vendeur"] = Character("Vendeur", "Le gérant.",
                                                   boutique,
                                                   ["Cette clé ouvre la Route 2."])
        sommet.characters["Pierre"] = Character("Pierre", "Champion d'Arène.",
                                                sommet,
                                                ["Te voilà enfin au sommet !"])

        # --- JOUEUR (Nom temporaire) ---
        # On ne demande plus le nom ici ! On met un nom vide pour l'instant.
        self.player = Player("")
        self.player.current_room = maison
        self.player.history.append(maison)

        # Quêtes
        self.quest_manager = QuestManager(self.player)
        self.quest_manager.add_quest(
            Quest("Livraison", "Apporte le colis à Chen.",
                  ["prendre colis", "parler avec Chen"], "Pokédex"))
        self.quest_manager.activate_quest("Livraison")
        self.quest_manager.add_quest(
            Quest("Chasse au Rattata", "Capture le Rattata dans la Grotte.",
                  ["capture rattata"], "Super Potion"))
        self.quest_manager.activate_quest("Chasse au Rattata")
        self.quest_manager.add_quest(
            Quest("Vers le Sommet", "Grimpe tout en haut.",
                  ["Visiter Sommet de l'Arène"], "Victoire"))
        self.quest_manager.activate_quest("Vers le Sommet")

    def play(self):
        self.setup()
        try:
            self.gui = GameGUI(self)
            self.gui.start()
        except tk.TclError:
            print("\n⚠️  Pas d'écran détecté (Mode Cloud).\n")
            # En mode texte, on demande le nom manuellement
            self.player.name = input("Entrez votre nom : ")
            self.waiting_for_name = False
            self.print_welcome()
            while not self.finished:
                self.check_victory_defeat()
                try:
                    user_input = input("> ")
                    self.process_command(user_input)
                except (KeyboardInterrupt, EOFError):
                    self.finished = True
                    print("\nAu revoir !")
    
    def check_victory_defeat(self):
        if self.win():
            print("\n🏆 VICTOIRE ! Tu as atteint le sommet et fini les quêtes ! 🏆")
            self.finished = True

    def process_command(self, command_string):
        if not command_string:
            return

        # --- NOUVEAU : GESTION DU NOM ---
        # Si on est en train d'attendre le nom, on le récupère ici
        if self.waiting_for_name:
            self.player.name = command_string
            self.waiting_for_name = False
            print(f"\nEnchanté {self.player.name} ! L'aventure commence...")
            print("-" * 40)
            self.player.look()
            return
        # -------------------------------

        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' inconnue. Tapez 'help'.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words,
                          command.number_of_parameters)
            self.check_victory_defeat()

    def print_welcome(self):
        # On change le message d'accueil pour poser la question
        print("\n=== POKEMON : L'AVENTURE PYTHON ===")
        print("Bienvenue dans le monde des Pokémon !")
        print("Veuillez entrer votre nom pour commencer :")

    def win(self):
        if self.quest_manager is None:
            return False
        all_quests = self.quest_manager.get_all_quests()
        if not all_quests:
            return False
        for quest in all_quests:
            if not quest.is_completed:
                return False
        return True

if __name__ == "__main__":
    Game().play()
