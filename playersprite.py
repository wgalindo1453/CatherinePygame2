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
        self.jump = False  # boolean to check if the player is jumping
        self.jump_level = 10  # how high the player can jump
        self.bg_music = pygame.mixer.music.load('music/bg_music.mp3')
        pygame.mixer.music.play(-1)

        # create update function that allows the player to move

    # create a function that takes a list of images and flips them
    def flip_images(self, image_list):
        flipped_images = []  # create a list to hold the flipped images
        for image in image_list:  # loop through the list of images
            flipped_image = pygame.transform.flip(image, True, False)
            flipped_images.append(flipped_image)
        return flipped_images

    # create a gravity function

    def gravity(self):
        if self.rect.y < self.screenheight - self.rect.height: # if the player is not on the ground
            self.rect.y += 3  # add 1 to the y position of the player to simulate gravity

    # create a function to handle collision detection with the object group
    # def collisiondetection(self, object_group):
    #     if pygame.sprite.spritecollide(self, object_group, False):
    #         print("Collision detected")
    #         #find the object that the player collided with
    #         for object in object_group:
    #             if self.rect.colliderect(object.rect):
    #                 print("Collision detected with object: " + object.name)
    #                 if object.name == "platform":
    #
    #                     print("Collision detected with platform")
    #                 elif object.name == "spike":
    #                     print("Collision detected with spike")
    #                 elif object.name == "coin":
    #                     print("Collision detected with coin")
    #                     object_group.remove(object)
    #                     print("Coin removed")
    #                 elif object.name == "door":
    #                     print("Collision detected with door")
    def collisiondetection(self, object_group):
        for object in object_group:
            if self.rect.colliderect(object.rect):
                if object.name == "platform":
                    # Check the direction of the player's movement
                    if self.rect.bottom < object.rect.top:# if bottom of player is above top of platform
                        # Player is coming from above, move player on top of platform
                        self.rect.bottom = object.rect.top
                    elif self.rect.top > object.rect.bottom:# if top of player is below bottom of platform
                        # Player is coming from below, move player below platform
                        self.rect.top = object.rect.bottom
                    elif self.rect.centerx < object.rect.centerx:# if center of player is to the left of center of platform
                        # Player was coming from the left, move player to right of platform
                        self.rect.right = object.rect.left
                    elif self.rect.centerx > object.rect.centerx:
                        # Player was coming from the right, move player to left of platform
                        self.rect.left = object.rect.right



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
        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        #     self.image = self.up_images[0]

        # if the down key is pressed move the player down
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.image = self.base_image

        if self.jump == False:  # if the player is not jumping
            if keys[pygame.K_SPACE]:  # if the space bar is pressed
                self.jump = True  # set the jump boolean to true
        else:  # if the player is jumping
            if self.jump_level >= -10:  # if the jump level is greater than or equal to -10
                self.rect.y -= (self.jump_level * abs(self.jump_level)) * 0.5  # move the player up or down
                self.jump_level -= 2  # decrement the jump level
            else:
                self.jump = False  # set the jump boolean to false
                self.jump_level = 10  # set the jump level to 10

        # if player collides with a platform do not let them fall through

        # if the player goes off the screen, move them back on
        if self.rect.right > self.screenwidth:  # if the player goes off the right side of the screen
            self.rect.right = self.screenwidth  # move them back on
        if self.rect.left < 0:  # if the player goes off the left side of the screen
            self.rect.left = 0  # move them back on
        if self.rect.top < 0:  # if the player goes off the top of the screen
            self.rect.top = 0  # move them back on
        if self.rect.bottom > self.screenheight:  # if the player goes off the bottom of the screen
            self.rect.bottom = self.screenheight
