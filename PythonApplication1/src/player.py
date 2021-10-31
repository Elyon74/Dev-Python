import pygame

# Sprite du joueur et gestion du joueur
class player(pygame.sprite.Sprite):

     def __init__(self, x, y):
         super().__init__()
         # Sprite du joueur a charger
         self.sprite_sheet = pygame.image.load('asset/Sprite/player.png')
         # Dimension de l' image
         self.image = self.get_image(0, 0)
         # Fond derriere limage vide
         self.image.set_colorkey([0, 0, 0])
         # Position de l' image
         self.rect = self.image.get_rect()
         self.position = [x, y]
         self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
         self.old_position = self.position.copy()
         # Vitesse de déplacement de l' image
         self.speed = 3

     def save_location(self): self.old_position = self.position.copy()

     def move_right(self): self.position[0] += self.speed
     
     def move_left(self): self.position[0] -= self.speed

     def move_up(self): self.position[1] -= self.speed

     def move_down(self): self.position[1] += self.speed

     def update(self):
         self.rect.topleft = self.position
         self.feet.midbottom = self.position
     
     def move_back(self):
         self.position = self.old_position
         self.rect.topleft = self.position
         self.feet.midbottom = self.rect.midbottom

     def get_image(self, x, y):
         image = pygame.Surface([320, 320])
         image.blit(self.sprite_sheet, (0, 0), (x, y, 320, 320))
         return image
