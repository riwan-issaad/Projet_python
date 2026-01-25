"""Character module for the game."""


class Character:
    def __init__(self, name, description, current_room=None, msgs=None):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs if msgs is not None else []
        self.inventory = {}

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self.msgs:
            return f"{self.name} n'a rien à dire."

        # Récupérer et faire tourner les messages
        message = self.msgs.pop(0)
        self.msgs.append(message)
        return message

    def move(self):
        # Les personnages restent sur place pour l'instant
        pass
