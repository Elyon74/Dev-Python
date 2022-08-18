import pygame

from src.game import game
from src.player import player
from src.tilemap import mapmanager
from src.tilemap import tilemap

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
