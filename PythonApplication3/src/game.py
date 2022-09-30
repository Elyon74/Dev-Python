
import pygame
from src.player import player
from src.tilemap import tilemap
from src.tilemap import mapmanager

class game:
    def __init__(self):
        self.running = True
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PythonRPG")
        background = pygame.image.load(r'D:\\asset\picture\Bigtree.png')
        self.player = player( 0, 0)
        self.map_manager = mapmanager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_Z]:
            self.player.move_up()
        elif pressed[pygame.K_S]:
            self.player.move_down()
        elif pressed[pygame.K_Q]:
            self.player.move_right()
        elif pressed[pygame.K_D]:
            self.player.move_left()
        
    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            screen.fill((0, 0, 0))
            screen.blit(background, (0, 0))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    clock.tick(60)