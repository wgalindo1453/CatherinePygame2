import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        #make sprite green

        self.rect = self.image.get_rect()
        #remove black background

        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen






