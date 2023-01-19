import pygame
import spritesheet


# create a class for the player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen, image, left_images_list, up_images_list):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.base_image = image
        self.rect = self.image.get_rect()
        # remove black background
        self.image.set_colorkey((0, 0, 0))
        self.screenwidth = screen.get_width()
        self.screenheight = screen.get_height()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.screen = screen
        self.left_images = left_images_list
        self.up_images = up_images_list
        self.image_index = 0

        # create update function that allows the player to move

    # create a function that takes a list of images and flips them
    def flip_images(self, image_list):
        flipped_images = []  # create a list to hold the flipped images
        for image in image_list:  # loop through the list of images
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_images.append(flipped_image)
        return flipped_images

    def update(self):

        self.image.set_colorkey((0, 0, 0))
        # get the keys pressed
        keys = pygame.key.get_pressed()
        # if the right key is pressed move the player right
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            flipped_images = self.flip_images(self.left_images)
            self.image_index = self.image_index + 1
            if self.image_index > 3:
                self.image_index = 0

            self.image = flipped_images[self.image_index]

        # if the left key is pressed move the player left
        if keys[pygame.K_LEFT]:

            print(self.image_index)  # print the image index
            self.rect.x -= self.speed  # move the player left
            self.image_index = self.image_index + 1
            if self.image_index > 3:  # if the image is the last image in the list
                self.image_index = 0  # set the image index to 0
                # increment the image index
            self.image = self.left_images[self.image_index]  # set the image to the image at the image index

        # if the up key is pressed move the player up
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.image = self.up_images[0]

        # if the down key is pressed move the player down
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.base_image

        # if the player goes off the screen, move them back on
        if self.rect.right > self.screenwidth:  # if the player goes off the right side of the screen
            self.rect.right = self.screenwidth  # move them back on
        if self.rect.left < 0:  # if the player goes off the left side of the screen
            self.rect.left = 0  # move them back on
        if self.rect.top < 0:  # if the player goes off the top of the screen
            self.rect.top = 0  # move them back on
        if self.rect.bottom > self.screenheight:  # if the player goes off the bottom of the screen
            self.rect.bottom = self.screenheight
