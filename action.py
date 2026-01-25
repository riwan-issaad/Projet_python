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
        # Dictionnaire robuste majuscules/minuscules
        Orientations = {"n": "N", "nord": "N", "NORD": "N", "N": "N",
                        "e": "E", "est": "E", "EST": "E", "E": "E",
                        "s": "S", "sud": "S", "SUD": "S", "S": "S",
                        "o": "O", "ouest": "O", "OUEST": "O", "O": "O",
                        "u": "U", "up": "U", "d": "D", "down": "D"}

        if direction in Orientations:
             direction = Orientations[direction]
        else:
            print("Direction inconnue.")
            return False
            
        player.move(direction)
        if game.quest_manager:
            game.quest_manager.check_room_objectives(player.current_room.name)
        return True

    def quit(game, list_of_words, number_of_parameters):
        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True
    
    def back(game, list_of_words, number_of_parameters):
        return game.player.back()

    def help(game, list_of_words, number_of_parameters):
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def look(game, list_of_words, number_of_parameters):
        game.player.look()
        return True

    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        item_name = list_of_words[1] # On garde la casse d'origine pour matcher les clés du dictionnaire
        if game.player.take(item_name):
            if game.quest_manager:
                game.quest_manager.check_action_objectives("prendre", item_name)
        return True

    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
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
                # On valide l'objectif de quête
                # Le format attendu par quest.py est "parler avec X" ou "parler X"
                game.quest_manager.check_action_objectives("parler", character_name)
                # On force aussi la validation spécifique si besoin
                game.quest_manager.complete_objective(f"Parler à {character_name}")
        return True

    def quests(game, list_of_words, number_of_parameters):
        if game.quest_manager:
            game.quest_manager.show_quests()
        return True

    def capture(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        pokemon_name = list_of_words[1] # Pas de lower() ici pour matcher les clés du dictionnaire comme "Rattata"
        game.player.capture(pokemon_name)
        return True
    
    def map(game, list_of_words, number_of_parameters):
        carte = """
                       [ Sommet Arène ]
                             ^
                             | (UP)
                             |
                       [ Route 1 ]  ----> (DOWN) ----> [ Grotte ]
                             |
                             | (N)
                             |
      [ Labo ] <---(O)--- [ Place ] ---(E)---> [ Boutique ]
                             |
                             | (S)
                             |
                        [ Maison ]
        """
        print(carte)
        return True