import pygame
import pyscroll
import pytmx

from player import player
from interface import interface

# On importe les librairies et les class necessaire a pygame

class Game:
    def __init__(self):
        # Créer la fenètre du jeux
        self.screen = pygame.display.set_mode((800, 600))
        ## On change le titre de la fenètre
        pygame.display.set_caption("PyGame World")
        # Chargez la carte entre les parentheses le nom de la carte dans le dossier de la solution python
        tmx_data = pytmx.util_pygame.load_pygame('tilemap\map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2
        # Zoom sur la carte map_layer.zoom = 2
        # On creer un joueur et le place dans la map puis les interfaces
        player_position = tmx_data.get_object_by_name("player")
        self.player = player(player_position.x, player_position.y)
        # self.HPText = interface(10,10)
        # self.HPBar1 = interface(60,10)
        # self.HPBar2 = interface(110,10)
        # self.HPBar3 = interface(160,10)
        # self.GoldText = interface(10,20)
        # self.LevelText = interface(60,20)

        # On creer un calque de la carte
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

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
        
    def run(self):
        clock = pygame.time.Clock()
        # Variable de boucle du jeux
        Running = True
        while Running:
            # On dessine le calque de la carte et on l' actualise dans la fenetre
            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                    pygame.quit()
            clock.tick(60)
