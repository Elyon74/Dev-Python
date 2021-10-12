import pygame
import pyscroll
import pytmx

from player import player
#On importe les librairie de pygame

class Game:
    def __init__(self):
        #Créer la fenètre du jeux
        self.screen = pygame.display.set_mode((800, 600))
        ##On change le titre de la fenètre
        pygame.display.set_caption("PyGame World")
        #Chargez la carte entre les parentheses le nom de la carte dans le dossier de la solution python
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        #Zoom sur la carte map_layer.zoom = 0
        #On creer un joueur
        self.player = player(400, 400)
        self.walls = []
        #On creer un calque de la carte positionner en 1er dans la file de prioriter
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.moveup()
        elif pressed[pygame.K_DOWN]:
            self.player.movedown()
        elif pressed[pygame.K_LEFT]:
            self.player.moveleft()
        elif pressed[pygame.K_RIGHT]:
            self.player.moveright()
        
    def run(self):
        clock = pygame.time.Clock()
        ##Variable de boucle du jeux
        Running = True
        while Running:
            #On dessine le calque de la carte et on l' actualise dans la fenetre
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