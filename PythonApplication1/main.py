import pygame

# On importe les class contenue dans les fichiers player.py game.py interface.py et la librairie pygame

from game import Game
from player import player
from interface import interface

# On lance le programme pygame
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
