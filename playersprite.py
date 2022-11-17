import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        # remove black background
        self.image.set_colorkey((0, 0, 0))
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen

        # create update function that allows the player to move

    def update(self):
        # get the keys pressed
        keys = pygame.key.get_pressed()
        # if the right key is pressed move the player right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        # if the left key is pressed move the player left
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        # if the up key is pressed move the player up
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        # if the down key is pressed move the player down
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # if the player goes off the screen, move them back on
        if self.rect.right > self.screenwidth: # if the player goes off the right side of the screen
            self.rect.right = self.screenwidth # move them back on
        if self.rect.left < 0: # if the player goes off the left side of the screen
            self.rect.left = 0 # move them back on
        if self.rect.top < 0:    # if the player goes off the top of the screen
            self.rect.top = 0 # move them back on
        if self.rect.bottom > self.screenheight: # if the player goes off the bottom of the screen
            self.rect.bottom = self.screenheight


