import pygame

# On importe les class contenue dans les fichiers player.py game.py interface.py et la librairie pygame

from src.game import Game
from src.player import player
from src.interface import interface
from src.tilemap import mapmanager
from src.tilemap import tilemap1

# On lance le programme pygame
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
