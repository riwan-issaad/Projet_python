# Description: Game class

# Import modules
from quest import Quest, QuestManager
from room import Room
from player import Player
from command import Command
from action import Actions
from Item import Item
from character import Character


# Variable de débogage
DEBUG = False

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.quest_manager = None



   
    def setup(self):


        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back"," : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look","Permet d'observer la pièce.",Actions.look,0)
        self.commands["look"]= look
        take = Command("take","Permet de prendre un item de la pièce.",Actions.take,1)
        self.commands["take"] = take
        drop = Command("drop","Permet de reposer un item dans la pièce.",Actions.drop,1)
        self.commands["drop"] = drop
        check = Command("check","Permet de vérifier le contenu de l'inventaire.",Actions.check,0)
        self.commands["ckeck"] = check
        talk = Command("talk", " <someone> : parler avec un personnage", Actions.talk, 1)
        self.commands["talk"] = talk

       
#Setup Room


#Création des piliers (lien entre les différentes arènes)
        Pilier1 = Room("Le Pilier de l'Aube Perdue", "là où chaque jeune du village vient y déposer la main avant d'entamer son voyage, espérant recevoir la bénédiction silencieuse du Pilier")
        self.rooms.append(Pilier1)
        Pilier2 = Room("Pilier des Marées Anciennes","devant le Pilier des Marées Anciennes, vestige sacré où l'eau et le temps semblent s'entrelacer.")
        self.rooms.append(Pilier2)
        Pilier3 = Room("Pilier du Conducteur Ancestral","devant l'ancien pilier de métal céleste, canal sacré de la foudre originelle, lieu où les Maîtres jurent fidélité à l'équilibre du monde Pokémon.")
        self.rooms.append(Pilier3)

#Village de départ


        Maison1 = Room("Maison du Héros", "dans votre maison chaleureuse, où les souvenirs de l'enfance flottent encore")
        self.rooms.append(Maison1)
        Professeur1 = Room("Demeure du Professeur Eldor ", "dans la maison du professeur, remplie de parchemins et d'objets mystérieux")
        self.rooms.append(Professeur1)
        Arène1 = Room("Arène du Souffle Naissant", "là où chaque lumière marque le début d'un nouvel espoir et où les premiers pas d'un véritable champion prennent forme")
        self.rooms.append(Arène1)
        Boutique = Room("Boutique d'Alchimie de Liora", "étalée de fioles, herbes et objets magiques")
        self.rooms.append(Boutique)

        Maison1.exits = {"N": Pilier1, "E" : None, "S" : None, "O" : None}
        Professeur1.exits = {"N" : Arène1, "E" : Boutique, "S" :Pilier1, "O" :None}
        Arène1.exits = {"N" : Pilier2, "E" : None, "S" : None, "O" : None}
        Pilier1.exits = {"N" : None, "E" : Boutique , "S" : None, "O" : Professeur1}
        Boutique.exits = {"N" : Arène1, "E" : None, "S" : Pilier1, "O" : Professeur1}
       
#OBJET DANS VILLAGE DE DEPART
        Carte = Item("Carte", "une carte mystérieuse", 0.1)
        Professeur1.inventory["Carte"] = Carte
        Cle_Magique = Item("Clé Magique", "une clé ancienne qui permet d'accéder à des objets rares en boutique", 0.05)
        Professeur1.inventory["Clé Magique"] = Cle_Magique
        Xp = Item("XP","monnaie du jeu permettant d'achter des pokemon rare en boutique",1)
        Professeur1.inventory["XP"] = Xp

#PERSONNAGE DANS LE VILLAGE DE DEPART

        Eldor = Character("Professeur Eldor", "un sage professeur au regard perçant.", Professeur1, ["Étudie bien ces sorts !"])
        Professeur1.characters["Professeur Eldor"] = Eldor
        
        Ancien = Character("Ancien", "un vieil homme sage qui veille sur le Pilier.", Pilier1, ["Que la lumière t'accompagne, jeune voyageur."])
        Pilier1.characters["Ancien"] = Ancien
        
        Liora = Character("Liora", "la boutiqueuse aux mille potions.", Boutique, ["Bienvenue dans ma boutique !"])
        Boutique.characters["Liora"] = Liora



# Village d'Eau

        Professeur2 = Room("Sanctuaire du Maître Ondin","dans la demeure du Maître Ondin, imprégnée de sagesse, de coquillages anciens et d'embruns.")
        self.rooms.append(Professeur2)
        Arène2= Room("Arène des Flots Murmurants","au cœur de l'Arène des Flots Murmurants, où chaque combat suit le rythme des marées et du courage.")
        self.rooms.append(Arène2)
        Boutique2 = Room("Boutique des Courants","dans la Boutique des Courants, où fioles, filets et objets aquatiques reposent au rythme de l'eau.")
        self.rooms.append(Boutique2)



        Professeur2.exits = {"N": Arène2, "E": Boutique2, "S": Pilier2, "O": None}
        Arène2.exits = {"N":Pilier3, "E": None, "S": None, "O": None}
        Pilier2.exits = {"N": None, "E": Boutique2, "S": None, "O": Professeur2}
        Boutique2.exits = {"N": Arène2, "E": None, "S": Pilier2, "O": Professeur2}

#OBJET DANS VILLAGE D'EAU

        Potion = Item("Potion", "Restaure un peu de PV.", 0.1)
        Boutique2.inventory["Potion"] = Potion
        Super_Potion = Item("Super Potion", "Restaure beaucoup de PV.", 0.2)
        Boutique2.inventory["Super_Potion"] = Super_Potion

#PERONNAGE DANS VILLAGE D'EAU

        Mira = Character("Mira","une marchande spécialisée dans les objets liés aux Pokémon de type Eau.",Boutique2,["Bienvenue ! L'eau cache toujours quelque chose d'utile.","Les dresseurs avisés ne partent jamais sans potions.","Ces objets viennent des profondeurs … choisis bien."])
        Boutique2.characters["Mira"] = Mira
        Aurelion = Character("Aurelion","le Champion de l'Arène Eau, calme et implacable comme l'océan.",Arène2,["L'eau s'adapte à tout… comme un bon dresseur.","Chaque vague peut renverser un combat.","Montre-moi que tu sais suivre le rythme des marées."])
        Arène2.characters["Aurelion"] = Aurelion
        Ondin = Character("Maître Ondin","le Maître des Pokémon Eau, aussi calme que l'océan et aussi redoutable qu'une tempête soudaine.",Professeur2,["L'eau enseigne la patience, mais punit la précipitation.","Un dresseur doit apprendre à s'adapter, comme la mer.","Avant d'affronter l'arène, écoute ce que murmure l'eau."])
        Professeur2.characters["Ondin"] = Ondin


#Village de la ligue de Pokémon(Finale)

        Professeur3 = Room("Maître des Courants","dans la demeure du Maître Suprême, un lieu sacré où la foudre danse librement, témoignant des combats légendaires ayant forgé la Ligue.")
        self.rooms.append(Professeur3)
        Arène3 = Room("Arène de l'Apothéose Foudroyante","au cœur de l'arène finale, suspendue entre ciel et terre, où chaque pas fait gronder le tonnerre et où seuls les véritables champions survivent à la foudre.")
        self.rooms.append(Arène3)
        Boutique3 = Room("Boutique du Panthéon Pokémon","dans la boutique légendaire de la Ligue Pokémon, réservée aux dresseurs d'élite.")
        self.rooms.append(Boutique3)



#Création des sorties entre les pièces du village de la ligue

        Professeur3.exits = {"N": Arène3, "E": Boutique3, "S": Pilier3, "O": None}
        Arène3.exits = {"N": None, "E": None, "S": None, "O": None}
        Pilier3.exits = {"N": None, "E": Boutique3, "S": None, "O": Professeur3}
        Boutique3.exits = {"N": Arène3, "E": None, "S": Pilier3, "O": Professeur3}

#OBJET DANS VILLAGE DE LA LIGUE

        Amulette = Item("Amulette du Champion", "Symbole ultime de victoire.", 0.1)
        Arène3.inventory["Amulette"] = Amulette

#PERSONNAGE DANS VILLAGE DE LA LIGUE

        Aegiron = Character("Aegiron","le Maître de la Ligue Pokémon, stratège légendaire dont la présence impose le respect.",Arène3,["Tu as parcouru un long chemin pour arriver ici.","La victoire appartient à ceux qui comprennent leurs Pokémon.","Montre-moi si tu mérites le titre de Champion."])
        Professeur3.characters["Aegiron"] = Aegiron
        Maitre_des_Courants = Character("Maître des Courants"," un professeur impassible capable de lire le moindre mouvement comme un courant marin.",Professeur3,["L'eau ne s'oppose jamais… elle contourne.","Un bon dresseur sait quand attaquer et quand attendre.","Si tu comprends les courants, alors tu peux me défier."])
        Professeur3.characters["Maitre_des_Courants"] = Maitre_des_Courants
       
        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Maison1
        self.player.history.append(self.player.current_room)

        # Setup Quests
        self.quest_manager = QuestManager(self.player)

        quest1 = Quest("Cherche la réponse à l'énigme", "", ["Prendre les XP"], "100 XP")
        self.quest_manager.add_quest(quest1)
        self.quest_manager.activate_quest("Cherche la réponse à l'énigme")

        #quest2 = Quest("Obtiens la Clé Magique", "Parle au Professeur Eldor pour obtenir la Clé Magique qui te permettra d'accéder à des objets rares en boutique", ["Parler à Professeur Eldor", "Échanger la Clé à la boutique"], "Accès aux objets rares")
        #self.quest_manager.add_quest(quest2)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            if self.win():
                print("\n" + "="*60)
                print("🏆 VICTOIRE! 🏆")
                print("="*60)
                print(f"Félicitations {self.player.name}!")
                print("Vous avez complété toutes les quêtes et remporté la victoire!")
                print("="*60 + "\n")
                self.finished = True
                break
            
            if self.loose():
                print("\n" + "="*60)
                print("💀 DÉFAITE! 💀")
                print("="*60)
                print(f"Désolé {self.player.name}!")
                print("Vous êtes entré dans l'Arène Finale sans la Carte protectrice.")
                print("Vous avez été foudroyé par l'énergie du lieu!")
                print("="*60 + "\n")
                self.finished = True
                break

            for room in self.rooms:
                for character in list(room.characters.values()):
                    character.move()

            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print()
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

        
    def win(self):
        """
        Vérifie si le joueur a gagné la partie.
        Le joueur gagne quand toutes les quêtes sont complétées.
        
        Returns:
            bool: True si toutes les quêtes sont complétées, False sinon.
        """
        if self.quest_manager is None:
            return False
        
        all_quests = self.quest_manager.get_all_quests()
        
        if len(all_quests) == 0:
            return False
        
        for quest in all_quests:
            if not quest.is_completed:
                return False
        
        return True
   
    def loose(self):
        """
        Vérifie si le joueur a perdu la partie.
        Le joueur perd s'il entre dans l'Arène Finale sans posséder la Carte.
        
        Returns:
            bool: True si le joueur a perdu, False sinon.
        """
        if self.player.current_room.name == "Arène de l'Apothéose Foudroyante":
            if "Carte" not in self.player.inventory:
                return True
        
        return False

        
def main():
    # Create a game object and play the game
    Game().play()
   

if __name__ == "__main__":
    main()