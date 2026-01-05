# Define the Character class.
class Character():
  
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self._msgs_buffer = msgs.copy()

    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        if not self._msgs_buffer:
            self._msgs_buffer = self.msgs.copy()
        return self._msgs_buffer.pop(0)
