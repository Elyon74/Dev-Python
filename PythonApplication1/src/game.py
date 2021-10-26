import pygame

from src.player import player
from src.interface import interface
from src.tilemap import mapmanager

# On importe les librairies et les class necessaire a pygame

class Game:

    def __init__(self):
        # Créer la fenètre du jeux
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyGame World")
        # On creer un joueur et le place dans la map puis les interfaces
        self.player = player(0, 0)
        self.map_manager = mapmanager(self.screen, self.player)
        # self.HPText = interface(10,10)
        # self.HPBar1 = interface(60,10)
        # self.HPBar2 = interface(110,10)
        # self.HPBar3 = interface(160,10)
        # self.GoldText = interface(10,20)
        # self.LevelText = interface(60,20)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
        
    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()
        # Variable de boucle du jeux
        Running = True
        while Running:
            # On dessine le calque de la carte et on l' actualise dans la fenetre
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                    pygame.quit()
            clock.tick(60)
