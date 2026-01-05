# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from Item import Item

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
       
       
        # Setup rooms

#Village de départ


        Maison_du_joueur = Room("Maison_du_joueur", "dans votre Maison.")
        self.rooms.append(Maison_du_joueur)
        Maison_du_professeur = Room("Maison_du_professeur ", "dans la maison du professeur")
        self.rooms.append(Maison_du_professeur)
        Arène = Room("Arène du Souffle Naissant", "au sein de l’Arène du Souffle Naissant, là où chaque lumière marque le début d’un nouvel espoir et où les premiers pas d’un véritable champion prennent forme.")
        self.rooms.append(Arène)
        Pilier = Room("Le Pilier de l’Aube Perdue", "au sein du Pilier de l’Aube Perdue, chaque jeune du village vient y déposer la main avant d’entamer son voyage, espérant recevoir la bénédiction silencieuse du Pilier.")
        self.rooms.append(Pilier)
        Route1 = Room("Route1", "sur le chemin où la biodiversité est plus que développée et vous enmenera jusqu'à la prochaine arène.")
        self.rooms.append(Route1)

        Maison_du_joueur.exits = {"N": Pilier, "E" : None, "S" : None, "O" : None}
        Maison_du_professeur.exits = {"N" : Arène, "E" : None, "S" :Pilier, "O" :None}
        Arène.exits = {"N" : Route1, "E" : None, "S" : None, "O" : None}
        Pilier.exits = {"N" : Arène, "E" : None, "S" : None, "O" : Maison_du_professeur}
       
        # history_cmd = Command("history", " : afficher les lieux déjà visités", Actions.history, 0)
        #self.commands["history"] = history_cmd


# Village d'Eau


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


        Maison_du_joueur_eau.exits = {"N": Source_sacree, "E": None, "S": None, "O": None}
        Maison_du_maitre_eau.exits = {"N": Arene_eau, "E": None, "S": Source_sacree, "O": None}
        Arene_eau.exits = {"N": Route2, "E": None, "S": None, "O": None}
        Source_sacree.exits = {"N": Arene_eau, "E": None, "S": None, "O": Maison_du_maitre_eau}


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


        Maison_du_joueur_elec.exits = {"N": Conducteur, "E": None, "S": None, "O": None}
        Maison_du_maitre_elec.exits = {"N": Arene_elec, "E": None, "S": Conducteur, "O": None}
        Arene_elec.exits = {"N": Route3, "E": None, "S": None, "O": None}
        Conducteur.exits = {"N": Arene_elec, "E": None, "S": None, "O": Maison_du_maitre_elec}


        # Create exits for rooms


       

        #Maison_du_joueur.exits = {"N": Pilier, "E" : None, "S" : None, "O" : None}
        #Maison_du_professeur.exits = {"N" : Arène, "E" : None, "S" :Pilier, "O" :None}
        #Arène.exits = {"N" : Route1, "E" : None, "S" : None, "O" : None}
        #Pilier.exits = {"N" : Arène, "E" : None, "S" : None, "O" : Maison_du_professeur}
        #Boutique.exits = {"N" : Arène, "E" : None, "S" : Pilier, "O" : Maison_du_professeur}
        #castle.exits = {"N" : forest, "E" : swamp, "S" : None, "O" : None}
       
       
        Arcktan = Item("Arcktan","Pokémon de type Plante",Arène,"...")
        #Obalie=Character("Obalie","Pokémon de type ...",Arène,"...")
        #Terhal=Character("Terhal","Pokémon de type Plante", Arène,"...")
        #Poussifeu=Character("Poussifeu","Pokémon de type Feu",Arène,"...")
        #Tarsal=Character("Tarsal","Pokémon de type Psy",Arène,"...")
        #Ouisticram=Character("Ouisticram","Pokémonde type Feu","...")
       
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = Maison_du_joueur
        self.player.history.append(self.player.current_room)
       

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
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
