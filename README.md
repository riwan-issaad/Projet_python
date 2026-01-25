Projet Python : Mini-Jeu Pokémon
Voici mon projet de jeu d'aventure textuel codé en Python l'objectif principal finir les quetes. Le but était de créer un jeu où on peut se déplacer, gérer un inventaire et réaliser des quêtes, le tout avec une interface graphique pour ne pas jouer dans le terminal.

Ce que j'ai mis dans le jeu
Une interface graphique : J'ai utilisé tkinter pour avoir une vraie fenêtre avec une zone de texte et une barre pour écrire.

Une carte en 3D : On ne se déplace pas que au Nord ou au Sud, on peut aussi monter (go U) et descendre (go D) pour explorer des grottes ou des montagnes.

Des énigmes : Il faut trouver des clés pour débloquer certains chemins.

Un système de capture : On peut capturer un Pokémon si on a une Pokéball.

Comment lancer le jeu
Il faut juste avoir Python installé sur l'ordinateur.

Ouvrir le dossier du projet.

Lancer le fichier principal :

Bash

python game.py
Les commandes pour jouer
Une fois le jeu lancé, il suffit de taper les commandes dans la barre en bas et de faire Entrée.

Pour bouger : go N (Nord), go S (Sud), go E (Est), go O (Ouest).

Pour changer d'étage : go U (Monter), go D (Descendre).

Actions :

look : Pour voir ce qu'il y a dans la pièce.

take [objet] : Pour ramasser un truc (ex: take cle).

sac : Pour voir son inventaire.

talk [nom] : Pour parler à un personnage (ex: talk Chen).

capture [nom] : Pour attraper un Pokémon.

map : Affiche le plan du jeu.

quests : Affiche les missions en cours