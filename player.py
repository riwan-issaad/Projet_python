# Define the Player class.
class Player():
    """
    This class represents the player in the game. The player has a name and
    a current room, and can move between rooms.

    Attributes:
        name (str): The name of the player.
        current_room (Room): The room where the player is currently located.

    Methods:
        __init__(self, name): The constructor.
        move(self, direction): Moves the player to another room.

    Examples:

    >>> player = Player("Alice")
    >>> player.name
    'Alice'
    >>> player.current_room is None
    True
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {} 

       
    # Define the move method.
    def move(self, direction):
        """
        Moves the player in the specified direction.

        If no room exists in that direction, an error message is displayed.

        Args:
            direction (str): The direction to move to.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
       
        # Set the current room to the next room.
        self.current_room = next_room
        self.history.append(self.current_room)
       
        print(self.current_room.get_long_description())
       
        history_output =self.get_history()
        if history_output:
            print(history_output)
       
        return True
   
    def get_history(self):      
        # Si l'historique n'a qu'une seule pièce (la pièce actuelle), on ne liste rien.
        if len(self.history) <= 1:
            return ""

        # Exclure la dernière pièce (qui est la pièce actuelle)
        visited_rooms = self.history[:-1]

        history_string = "\nVous avez déjà visité les pièces suivantes:\n"
        for room in visited_rooms:
            # Nous utilisons la description de la pièce (ex: "un marécage sombre...")
            history_string += f"- {room.name}\n"
           
        return history_string
   
    def back(self):
        if len(self.history) <= 1:
            print("\n vous êtes revenu en arrière,donc vous êtes")
            return False
        self.history.pop()
        self.current_room=self.history[-1]
        print(f"\nVous êtes revenu en arrière.")
       
        print(self.current_room.get_long_description())
       
        history_output =self.get_history()
        if history_output:
            print(history_output)
        return True
       
    def history(self, history):
        history=[]
        history.append

    
    def get_inventory(self):
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_string = "Vous disposez des items suivants :\n"
        for item in self.inventory.values():
            inventory_string += f"    - {item.name} : {item.description} ({item.weight} kg)\n"
        return inventory_string
    
    def look(self):
        """
        Displays the description of the current room and its items.
        """
        print(self.current_room.get_long_description())
        print(self.current_room.get_inventory())

    # ...existing code...

    def take(self, item_name):
        """
        Permet au joueur de prendre un objet dans la pièce actuelle.

        Args:
            item_name (str): Le nom de l'objet à prendre.
        """
        if item_name in self.current_room.inventory:
            item = self.current_room.inventory[item_name]
            self.inventory[item_name] = item
            del self.current_room.inventory[item_name]
            print(f"Vous avez pris {item.name}.")
        else:
            print(f"L'objet '{item_name}' n'existe pas dans cette pièce.")

        

        