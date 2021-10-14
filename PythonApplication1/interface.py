
import pygame

# Interface de Hub des points de vie du joueur
class interface(pygame.sprite.Sprite):
    def __init__(HPText, x, y):
                 super().__init__()
                 HPText.sprite_sheet = pygame.image.load('asset\HP\Sprite-HP.png')
                 HPText.image = HPText.get_image(0, 0)
                 HPText.image.set_colorkey([0, 0, 0])
                 HPText.rect = HPText.image.get_rect()
                 HPText.position = [x, y]
                 HPText.feet = pygame.Rect(0, 0, HPText.rect.width * 0.5, 12)

    def get_HPText1(HPText,x, y):
        HPText1 = pygame.Surface([32, 32])
        HPText1.blit(HPText.sprite_sheet, (0, 0), (x, y, 32, 32))
        return HPText1

    def update(HPText):
        HPText.rect.topleft = HPText.position

    def __init__(HPBar1, x, y):
                 super().__init__()
                 HPBar1.sprite_sheet = pygame.image.load('asset\HP\Sprite-HP1.png')
                 HPBar1.image = HPBar1.get_image(0, 0)
                 HPBar1.image.set_colorkey([0, 0, 0])
                 HPBar1.rect = HPBar1.image.get_rect()
                 HPBar1.position = [x, y]
                 HPBar1.feet = pygame.Rect(0, 0, HPBar1.rect.width * 0.5, 12)

    def get_HP1(HPBar1,x, y):
        HP1 = pygame.Surface([32, 32])
        HP1.blit(HPBar1.sprite_sheet, (0, 0), (x, y, 32, 32))
        return HP1

    def update(HPBar1):
        HPBar1.rect.topleft = HPBar1.position

    def __init__(HPBar2, x, y):
                 super().__init__()
                 HPBar2.sprite_sheet = pygame.image.load('asset\HP\Sprite-HP2.png')
                 HPBar2.image = HPBar2.get_image(0, 0)
                 HPBar2.image.set_colorkey([0, 0, 0])
                 HPBar2.rect = HPBar2.image.get_rect()
                 HPBar2.position = [x, y]
                 HPBar2.feet = pygame.Rect(0, 0, HPBar2.rect.width * 0.5, 12)

    def get_HP2(HPBar2,x, y):
        HP2 = pygame.Surface([32, 32])
        HP2.blit(HPBar2.sprite_sheet, (0, 0), (x, y, 32, 32))
        return HP2

    def update(HPBar2):
        HPBar2.rect.topleft = HPBar2.position

    def __init__(HPBar3, x, y):
                 super().__init__()
                 HPBar3.sprite_sheet = pygame.image.load('asset\HP\Sprite-HP3.png')
                 HPBar3.image = HPBar3.get_image(0, 0)
                 HPBar3.image.set_colorkey([0, 0, 0])
                 HPBar3.rect = HPBar3.image.get_rect()
                 HPBar3.position = [x, y]
                 HPBar3.feet = pygame.Rect(0, 0, HPBar3.rect.width * 0.5, 12)

    def get_HP3(HPBar3,x, y):
        HP3 = pygame.Surface([32, 32])
        HP3.blit(HPBar3.sprite_sheet, (0, 0), (x, y, 32, 32))
        return HP3

    def update(HPBar3):
        HPBar3.rect.topleft = HPBar3.position