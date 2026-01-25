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

# --- 1. CLASSE _StdoutRedirector (Celle du prof) ---
class _StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert('end', string)
        self.text_widget.see('end')

    def flush(self):
        pass

# --- 2. CLASSE GameGUI (Version standard) ---
class GameGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Jeu d'Aventure")
        self.root.geometry("600x400") # Taille standard

        # Zone de texte (ScrolledText)
        self.text_area = scrolledtext.ScrolledText(self.root, state='normal', wrap='word')
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Redirection des print() vers la zone de texte
        sys.stdout = _StdoutRedirector(self.text_area)

        # Zone de saisie (Entry)
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.pack(fill='x', padx=10, pady=5)
        
        # Validation avec la touche Entrée
        self.entry.bind("<Return>", self.process_input)
        self.entry.focus_set()

    def process_input(self, event=None):
        user_input = self.entry_var.get()
        if user_input.strip():
            print(f"\n> {user_input}") # Affiche la commande
            self.game.process_command(user_input)
            self.entry_var.set("") # Vide le champ
            
            if self.game.finished:
                self.root.after(3000, self.root.destroy)

    def start(self):
        self.root.mainloop()

# --- 3. CLASSE GAME ---
class Game:
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.quest_manager = None

    def setup(self):
        # Configuration des commandes
        self.commands["help"] = Command("help", " : aide", Actions.help, 0)
        self.commands["quit"] = Command("quit", " : quitter", Actions.quit, 0)
        self.commands["go"] = Command("go", " <dir> : bouger (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["back"] = Command("back", " : retour", Actions.back, 0)
        self.commands["look"] = Command("look", " : observer", Actions.look, 0)
        self.commands["take"] = Command("take", " <item> : prendre", Actions.take, 1)
        self.commands["drop"] = Command("drop", " <item> : poser", Actions.drop, 1)
        self.commands["sac"] = Command("sac", " : inventaire", Actions.check, 0)
        self.commands["talk"] = Command("talk", " <nom> : parler", Actions.talk, 1)
        self.commands["quests"] = Command("quests", " : quêtes", Actions.quests, 0)
        self.commands["capture"] = Command("capture", " <nom> : capturer", Actions.capture, 1)
        self.commands["map"] = Command("map", " : carte", Actions.map, 0)

        # --- CARTE (Avec exigence Monter/Descendre) ---
        
        Maison = Room("Maison du Héros", "dans ta chambre.")
        Place = Room("Place du Village", "au centre du village.")
        Labo = Room("Labo de Chen", "dans le laboratoire.")
        Boutique = Room("Boutique", "dans le magasin.")
        Route1 = Room("Route 1", "au pied de la montagne.")
        
        # Niveau Bas (Down)
        Grotte = Room("Grotte Souterraine", "dans une grotte sombre (Niveau -1).")
        # Niveau Haut (Up)
        Sommet = Room("Sommet de l'Arène", "tout en haut de la montagne (Niveau +1).")

        self.rooms.extend([Maison, Place, Labo, Boutique, Route1, Grotte, Sommet])

        # Connexions
        Maison.exits = {"N": Place}
        Place.exits = {"S": Maison, "E": Boutique, "O": Labo, "N": Route1}
        Labo.exits = {"E": Place}
        Boutique.exits = {"O": Place}
        
        # Le carrefour 3D (Route 1)
        Route1.exits = {"S": Place, "U": Sommet, "D": Grotte}
        Grotte.exits = {"U": Route1} # On remonte
        Sommet.exits = {"D": Route1} # On redescend

        # Objets
        Pokeball = Item("Pokeball", "Pour capturer !", 0.1)
        Maison.inventory["Pokeball"] = Pokeball
        
        Rattata = Item("Rattata", "Un petit Pokémon violet.", 0.5)
        Grotte.inventory["rattata"] = Rattata # Caché dans la grotte !

        Colis = Item("Colis", "Le paquet pour Chen.", 1.0)
        Maison.inventory["colis"] = Colis 

        # Personnages
        Chen = Character("Chen", "Le Professeur.", Labo, ["Bonjour !", "J'attends mon colis."])
        Labo.characters["Chen"] = Chen
        
        Maman = Character("Maman", "Ta mère.", Maison, ["Fais attention dans la Grotte !"])
        Maison.characters["Maman"] = Maman
        
        Champion = Character("Pierre", "Champion d'Arène.", Sommet, ["Prouve ta valeur !"])
        Sommet.characters["Pierre"] = Champion

        # Joueur & Quêtes
        # name = input("\nEntrez votre nom: ") # En GUI, input() bloque tout.
        self.player = Player("Sacha") 
        self.player.current_room = Maison
        self.player.history.append(Maison)

        self.quest_manager = QuestManager(self.player)
        self.quest_manager.add_quest(Quest("Livraison", "Apporte le colis à Chen.", ["prendre colis", "parler avec Chen"], "Pokédex"))
        self.quest_manager.activate_quest("Livraison")
        self.quest_manager.add_quest(Quest("Sommet", "Grimpe au Sommet.", ["Visiter Sommet de l'Arène"], "Potion Max"))
        self.quest_manager.activate_quest("Sommet")

    def play(self):
        self.setup()
        self.print_welcome()
        
        # Lancement de l'interface
        # Note : Je garde le try/except car sur Codespaces (Cloud), 
        # lancer Tkinter sans écran fait planter le script immédiatement.
        # Cela permet au prof de voir la GUI, et à toi de tester sans crash.
        try:
            self.gui = GameGUI(self)
            self.gui.start()
        except tk.TclError:
            print("\n⚠️  Pas d'écran détecté (Mode Cloud).