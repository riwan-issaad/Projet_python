MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    def go(game, list_of_words, number_of_parameters):
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]
        Orientations = {"n": "N", "nord": "N", "NORD": "N", "N": "N",
                        "e": "E", "est": "E", "EST": "E", "E": "E",
                        "s": "S", "sud": "S", "SUD": "S", "S": "S",
                        "o": "O", "ouest": "O", "OUEST": "O", "O": "O"}

        if direction in Orientations:
             direction = Orientations[direction]
        else:
            print("Direction inconnue.")
            return False
            
        player.move(direction)
        # Vérification quête exploration
        if game.quest_manager:
            game.quest_manager.check_room_objectives(player.current_room.name)
        return True

    def quit(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    
    def back(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.back()

    def help(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def look(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.look()
        return True

    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1].lower()
        if game.player.take(item_name):
            # Quête
            if game.quest_manager:
                game.quest_manager.check_action_objectives("prendre", item_name)
        return True

    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1].lower()
        game.player.drop(item_name)
        return True

    def check(game, list_of_words, number_of_parameters):
        game.player.get_inventory()
        return True

    def talk(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        character_name = list_of_words[1]
        if game.player.talk(character_name):
            if game.quest_manager:
                game.quest_manager.check_action_objectives("parler", character_name)
        return True

    def quests(game, list_of_words, number_of_parameters):
        if game.quest_manager:
            game.quest_manager.show_quests()
        return True

    # --- C'EST ICI QUE CA MANQUAIT PEUT-ÊTRE ---
    def capture(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        pokemon_name = list_of_words[1].lower()
        # Appel obligatoire vers le joueur
        game.player.capture(pokemon_name)
        return True
    
    def map(game, list_of_words, number_of_parameters):
        # Un dessin en ASCII art
        carte = """
      [ Arène ]
          |
          | (N)
          |
      [ Route 1 ]
          |
          | (N)
          |
      [ Place ] --- (E) --- [ Labo ]
          |
          | (S)
          |
      [ Maison ]
        """
        print(carte)
        return True