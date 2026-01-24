# Description: Game class

# Import modules

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

#Village de départ


        Maison1 = Room("Maison_du_joueur", "dans votre Maison.")
        self.rooms.append(Maison1)
        Professeur1 = Room("Maison_du_professeur ", "dans la maison du professeur")
        self.rooms.append(Professeur1)
        Arène1 = Room("Arène du Souffle Naissant", "au sein de l’Arène du Souffle Naissant, là où chaque lumière marque le début d’un nouvel espoir et où les premiers pas d’un véritable champion prennent forme.")
        self.rooms.append(Arène1)
        Pilier1 = Room("Le Pilier de l’Aube Perdue", "au sein du Pilier de l’Aube Perdue, chaque jeune du village vient y déposer la main avant d’entamer son voyage, espérant recevoir la bénédiction silencieuse du Pilier.")
        self.rooms.append(Pilier1)
        Boutique = Room("Boutique", "au sein de la boutique")
        self.rooms.append(Boutique)

        Maison1.exits = {"N": Pilier1, "E" : None, "S" : None, "O" : None}
        Professeur1.exits = {"N" : Arène1, "E" : None, "S" :Pilier1, "O" :None}
        Arène1.exits = {"N" : None, "E" : None, "S" : None, "O" : None}
        Pilier1.exits = {"N" : None, "E" : Boutique , "S" : None, "O" : Professeur1}
        #Pilier2.exits = {"N" : None, "E" : None, "S" : None, "O" : None}
       
#OBJET DANS VILLAGE DE DEPART
        Carte = Item("Carte", "une carte mystérieuse", 0.1)
        Professeur1.inventory["Carte"] = Carte

        Xp = Item("XP","monnaie du jeu permettant d'achter des pokemon rare en boutique",1)
        Professeur1.inventory["XP"] = Xp
#Perosnnage dans le village de départ
        Historien = Character("Historien"," un historien ",Pilier1,["Bonjour je suis un historien et je suis la pour vous parler de ce pilier"])
        Professeur1.characters["Historien"] = Historien



# Village d'Eau
        Pilier2 = Room("Pilier 2 "," le deuxieme pilier")
        self.rooms.append(Pilier2)

        Maison_du_joueur_eau = Room("Maison_du_joueur ","dans votre maison bercée par le clapotis de l’eau.")
        self.rooms.append(Maison_du_joueur_eau)
        
        Maison_du_maitre_eau = Room("Maison_du_maitre_eau ","dans la demeure du Maître, imprégnée de sagesse et d’embruns.")
        self.rooms.append(Maison_du_maitre_eau)

        Arène_des_Flots_Murmurants = Room("Arène des Flots Murmurants","au cœur de l’Arène des Flots Murmurants, où chaque combat suit le rythme des marées.")
        self.rooms.append(Arène_des_Flots_Murmurants)

        La_Source_des_Profondeurs = Room("La Source des Profondeurs","devant une source cristalline où l’eau semble observer chaque voyageur.")
        self.rooms.append(La_Source_des_Profondeurs)

        Route2 = Room("Route Aquatique","sur un sentier bordé de canaux menant vers de nouvelles terres.")
        self.rooms.append(Route2)


        #Maison_du_joueur_eau.exits = {"N": None, "E": None, "S": None, "O": None}
        #Maison_du_maitre_eau.exits = {"N": None, "E": None, "S": None, "O": None}
        #Arene_eau.exits = {"N": Route2, "E": None, "S": None, "O": None}
       # La_Source_des_Profondeurs = {"N": Arene_eau, "E": None, "S": None, "O": Maison_du_maitre_eau}
       # Route1.exits = {"N": La_Source_des_Profondeurs , "E": None, "S": None, "O": None}


## Village Voltéria


        Maison_du_joueur_elec = Room("Maison de l’Étincelle","dans votre maison vibrante d’une énergie électrique constante.")
        self.rooms.append(Maison_du_joueur_elec)

        Maison_du_Maître_des_Courants= Room("Maison du Maître des Courants","dans la demeure du Maître, où l’air crépite d’électricité.")
        self.rooms.append(Maison_du_Maître_des_Courants)

        Arene_elec = Room("Arène de la Foudre Vive","au centre de l’Arène de la Foudre Vive, chaque affrontement fait jaillir des éclairs.")
        self.rooms.append(Arene_elec)

        Le_Conducteur_Ancestral= Room("Le Conducteur Ancestral","devant un pilier métallique captant la foudre depuis des générations.")
        self.rooms.append(Le_Conducteur_Ancestral)

        Route3 = Room("Route Orageuse","sur une route balayée par le vent et traversée d’arcs électriques.")
        self.rooms.append(Route3)

        #Maison_du_joueur_eau.exits = {"N": Le_Conducteur_Ancestral, "E": None, "S": None, "O": None}
        #Maison_du_maitre_eau.exits = {"N": Arene_eau, "E": None, "S": Le_Conducteur_Ancestral, "O": None}
       # Arene_eau.exits = {"N": Route2, "E": None, "S": None, "O": None}
       # Source_sacree.exits = {"N": Arene_eau, "E": None, "S": None, "O": Maison_du_maitre_eau}
       # Route2.exits = {"N": Le_Conducteur_Ancestral, "E": None, "S": None, "O": None}
    

    #Village de la ligue de Pokémon(Finale)

        Maison_du_joueur_elec = Room("Sanctuaire de l’Élu","dans le sanctuaire où vous avez grandi, désormais chargé d’une énergie électrique pure, ""chaque mur résonnant de votre destinée de Maître Pokémon.")
        self.rooms.append(Maison_du_joueur_elec)


        Maison_du_Maître_des_Courants = Room("Antre du Maître des Courants","dans la demeure du Maître Suprême, un lieu sacré où la foudre danse librement, ""témoignant des combats légendaires ayant forgé la Ligue.")
        self.rooms.append(Maison_du_Maître_des_Courants)


        Arene_elec = Room("Arène de l’Apothéose Foudroyante","au cœur de l’arène finale, suspendue entre ciel et terre, où chaque pas fait gronder le tonnerre ""et où seuls les véritables champions survivent à la foudre.")
        self.rooms.append(Arene_elec)


        Le_Conducteur_Ancestral = Room("Pilier du Conducteur Ancestral","devant l’ancien pilier de métal céleste, canal sacré de la foudre originelle, ""lieu où les Maîtres jurent fidélité à l’équilibre du monde Pokémon.")
        self.rooms.append(Le_Conducteur_Ancestral)


        #Route4 = Room("Voie du Jugement Orageux","sur la route menant à la Ligue, déchirée par des éclairs incessants, ""où chaque dresseur affronte ses peurs avant le combat final.")
        #self.rooms.append(Route4)
        #Maison_du_joueur_eau.exits = {"N": Source_sacree, "E": None, "S": None, "O": None}
        #Maison_du_maitre_eau.exits = {"N": Arene_eau, "E": None, "S": Source_sacree, "O": None}
        #Arene_eau.exits = {"N": Route2, "E": None, "S": None, "O": None}
       # Source_sacree.exits = {"N": Arene_eau, "E": None, "S": None, "O": Maison_du_maitre_eau}
       # Route3.exits = {"N": Le_Conducteur_Ancestral, "E": None, "S": None, "O": None}




        #Maison_du_joueur_elec.exits = {"N": Conducteur, "E": None, "S": None, "O": None}
        #Maison_du_maitre_elec.exits = {"N": Arene_elec, "E": None, "S": Conducteur, "O": None}
        #Arene_elec.exits = {"N": Route3, "E": None, "S": None, "O": None}
        #Conducteur.exits = {"N": Arene_elec, "E": None, "S": None, "O": Maison_du_maitre_elec}


        # Create exits for rooms


       

        #Maison_du_joueur.exits = {"N": Pilier, "E" : None, "S" : None, "O" : None}
        #Maison_du_professeur.exits = {"N" : Arène, "E" : None, "S" :Pilier, "O" :None}
        #Arène.exits = {"N" : Route1, "E" : None, "S" : None, "O" : None}
        #Pilier.exits = {"N" : Arène, "E" : None, "S" : None, "O" : Maison_du_professeur}
        #Boutique.exits = {"N" : Arène, "E" : None, "S" : Pilier, "O" : Maison_du_professeur}
       
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Maison1
        self.player.history.append(self.player.current_room)

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
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
   

def main():
    # Create a game object and play the game
    Game().play()
   

if __name__ == "__main__":
    main()
