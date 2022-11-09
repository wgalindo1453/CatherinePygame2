import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def init(self, x, y, width, height, screen, image):
        pygame.sprite.Sprite.init(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5




