import pygame

# Interface de Hub des points de vie du joueur
class interface(pygame.sprite.Sprite):

   def __init__(self, x, y):
       super().__init__()
       self.sprite_sheet = pygame.image.load('asset/HP/Sprite-HP.png')
       self.image = self.get_image(0, 0)
       self.image.set_colorkey([0, 0, 0])
       self.rect = self.image.get_rect()
       self.position = [x, y]
       self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
       self.old_position = self.position.copy()

   def update(self):
       self.rect.topleft = self.position
       self.feet.midbottom = self.position

   def get_image(self, x, y):
       image = pygame.Surface([320, 320])
       image.blit(self.sprite_sheet, (0, 0), (x, y, 320, 320))
       return image
