import random

# Define the Character class

class Character:
    """
    This class represents a non-player character (NPC) in the game.

    Attributes:
        name (str): The name of the character.
        description (str): A description of the character.
        current_room (Room): The room where the character is currently located.
        msgs (list): A list of messages to display when the player interacts with the character.
    """

    def __init__(self, name, description, current_room=None, msgs=None):
        """
        Initializes a new character.

        Args:
            name (str): The name of the character.
            description (str): Description of the character.
            current_room (Room, optional): The room where the character is located. Defaults to None.
            msgs (list, optional): List of messages for interaction. Defaults to empty list.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs is not None else []
        self.inventory = {}

        
    def __str__(self):
        """
        Returns a string representation of the character.

        Returns:
            str: A string in the format 'Name : description'.
        """
        return f"{self.name} : {self.description}"

    def get_msg(self):
        """
        Retourne le prochain message du personnage de manière cyclique.
        Les messages sont affichés dans l'ordre, puis recommencent depuis le début.
        
        Returns:
            str: Le prochain message du personnage.
        """
        from Game import DEBUG
        
        if not self.msgs:
            return f"{self.name} n'a rien à dire."
        
        # Récupérer et retirer le premier message de la liste
        message = self.msgs.pop(0)
        
        # Remettre le message à la fin de la liste pour le prochain cycle
        self.msgs.append(message)
        
        if DEBUG:
            print(f"DEBUG: {self.name} dit: {message}")
        
        return message

    def move(self):
        """
        Le personnage se déplace aléatoirement dans une salle voisine.
        DÉSACTIVÉ pour que les personnages restent à leur place.
        """
        # Les personnages ne se déplacent plus - ils restent dans leur salle initiale
        pass