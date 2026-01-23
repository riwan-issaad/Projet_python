# Define the Room class.

class Room:
    """
    This class represents a room in the game. A room has a name, a description,
    exits, and an inventory containing items.

    Attributes:
        name (str): The name of the room.
        description (str): The description of the room.
        exits (dict): A dictionary mapping directions (str) to rooms (Room or None).
        inventory (list): A list of items contained in the room.

    Methods:
        __init__(self, name, description): The constructor.
        get_exit(self, direction): Returns the room in the given direction.
        get_exit_string(self): Returns a string describing the available exits.
        get_long_description(self): Returns a full description of the room.
        get_inventory(self): Returns a string describing the room inventory.
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = []

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Returns the room corresponding to the given direction.

        Args:
            direction (str): The direction to look for.

        Returns:
            Room or None: The room in that direction if it exists, otherwise None.
        """
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Returns a string listing all available exits of the room.

        Returns:
            str: A string describing the exits.
        """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Returns a full description of the room, including exits.

        Returns:
            str: The long description of the room.
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    # Return a string describing the room inventory.
    def get_inventory(self):
        """
        Returns a string describing the items contained in the room.

        Returns:
            str: The inventory description.
        """
        if len(self.inventory) == 0:
            return "Il n'y a rien ici."

        inventory_string = "La pièce contient :\n"
        for item in self.inventory:
            inventory_string += (
                f"    - {item.name} : {item.description} ({item.weight} kg)\n"
            )

        return inventory_string
