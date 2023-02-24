import pygame


class ObjectSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, NAME):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((100, 50))
        #change color of the surface
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = NAME
