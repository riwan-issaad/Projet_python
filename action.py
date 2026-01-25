"""Module for game actions and commands."""

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"


class Actions:
    """Container for all game action methods."""

    def go(game, list_of_words, _):
        """Move in a direction."""
        player = game.player
        length = len(list_of_words)
        if length != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]
        orientations = {"n": "N", "nord": "N", "NORD": "N", "N": "N",
                        "e": "E", "est": "E", "EST": "E", "E": "E",
                        "s": "S", "sud": "S", "SUD": "S", "S": "S",
                        "o": "O", "ouest": "O", "OUEST": "O", "O": "O",
                        "u": "U", "up": "U", "d": "D", "down": "D"}

        if direction in orientations:
            direction = orientations[direction]
        else:
            print("Direction inconnue.")
            return False

        # --- MECANIQUE DE LA CLE (NOUVEAU) ---
        if player.current_room.name == "Route 1" and direction == "U":
            if "cle" not in player.inventory:
                msg = "\n⛔ STOP ! Le chemin vers la Route 2 est fermé par une barrière.\n"
                msg += "Il vous faut la 'Cle' pour passer (Indice : Cherchez à la Boutique).\n"
                print(msg)
                return False
            print("\n🔓 Vous utilisez la Clé pour ouvrir la barrière !")
        player.move(direction)
        if game.quest_manager:
            game.quest_manager.check_room_objectives(player.current_room.name)
        return True

    def quit(game, _, __):
        """Quit the game."""
        player = game.player
        print(f"\nMerci {player.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    def back(game, _, __):
        """Go back to previous room."""
        return game.player.back()

    def help(game, _, __):
        """Display help for all commands."""
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def look(game, _, __):
        """Look around the current room."""
        game.player.look()
        return True

    def take(game, list_of_words, _):
        """Take an item from the current room."""
        length = len(list_of_words)
        if length != 2:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        if game.player.take(item_name):
            if game.quest_manager:
                game.quest_manager.check_action_objectives("prendre", item_name)
        return True
    def drop(game, list_of_words, _):
        """Drop an item from inventory."""
        length = len(list_of_words)
        if length != 2:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        game.player.drop(item_name)
        return True
    def check(game, _, __):
        """Check inventory."""
        game.player.get_inventory()
        return True

    def talk(game, list_of_words, _):
        """Talk to a character."""
        length = len(list_of_words)
        if length != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        character_name = list_of_words[1]
        if game.player.talk(character_name):
            if game.quest_manager:
                game.quest_manager.check_action_objectives("parler",
                                                          character_name)
                game.quest_manager.complete_objective(
                    f"Parler à {character_name}")
        return True
    def quests(game, _, __):
        """Display active quests."""
        if game.quest_manager:
            game.quest_manager.show_quests()
        return True

    def capture(game, list_of_words, _):
        """Capture a Pokémon."""
        length = len(list_of_words)
        if length != 2:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        pokemon_name = list_of_words[1]
        if game.player.capture(pokemon_name):
            if game.quest_manager:
                # On valide l'objectif de quête "capture rattata"
                game.quest_manager.check_action_objectives("capture",
                                                           pokemon_name)
        return True
    def map(game, _, __):
        """Display the game map."""
        # Nouvelle Carte Agrandie
        carte = """
                       [ Sommet Arène ] (FIN)
                             ^
                             | (UP)
                       [ Village 2 ]
                             ^
                             | (UP)
                       [ Route 2 ]
                             ^
                             | (UP - Il faut la Clé !)
                       [ Route 1 ]  ----> (DOWN) ----> [ Grotte ]
                             |
                             | (N)
      [ Labo ] <---(O)--- [ Place ] ---(E)---> [ Boutique ]
                             |
                             | (S)
                        [ Maison ]
        """
        print(carte)
        return True
