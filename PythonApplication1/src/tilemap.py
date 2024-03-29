import pygame
import pyscroll
import pytmx
from dataclasses import dataclass

@dataclass
class tilemap:

    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap

class mapmanager:

    def __init__(self, screen, player):
        self.maps = dict()
        self.screen = screen
        self.player = player
        self.current_map = "map"
        #Ajouter une tilemap
        self.register_map("map")
        #Spawn du joueur
        self.teleport_player("player")

    def check_collision(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name):
        # Chargez la carte entre les parentheses le nom de la carte dans le dossier de la solution python
        tmx_data = pytmx.util_pygame.load_pygame(f"tilemap/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # Zoom sur la carte map_layer.zoom = 2
        # map_layer.zoom = 0
        walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        # On creer un calque de la carte
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)
        # On Creer un objet map et on l' ajoute dans le dictionnaire
        self.maps[name] = tilemap(name, walls, group, tmx_data)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collision()