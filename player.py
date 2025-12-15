# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []

       

   
    # Define the move method.
    def move(self, direction):
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
