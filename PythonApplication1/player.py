import pygame

class player(pygame.sprite.Sprite):
     def __init__(self, x, y):
         super().__init__()
         #image a charger
         self.sprite_sheet = pygame.image.load('player.png')
         #dimension de l' image
         self.image = self.get_image(0, 0)
         #fond derriere limage vide
         self.image.set_colorkey([0, 0, 0])
         #position de l' image
         self.rect = self.image.get_rect()
         self.position = [x, y]
         self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
         self.old_position = self.position.copy()
         self.speed = 2
     def move_right(self): self.position[0] += self.speed
     
     def move_left(self): self.position[0] -= self.speed

     def move_up(self): self.position[1] -= self.speed

     def move_down(self): self.position[1] += self.speed

     def update(self):
         self.rect.topleft =self.position

     def get_image(self,x, y):
         image = pygame.Surface([32, 32])
         image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
         return image