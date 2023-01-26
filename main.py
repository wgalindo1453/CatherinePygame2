import pygame
import spritesheet
import playersprite as ps
import objectsprite as os
# screen size
SCREEN_WIDTH = 1000  # 500
SCREEN_HEIGHT = 900  # 450
# hello
# loading images into pygame
bg_img = pygame.image.load('pictures/bg.jpg')
# resize the image to fit the screen
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# create a class for the player


# game class
class Game:
    i = 0

    def __init__(self):
        pygame.init()  # initialize pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # create screen
        self.clock = pygame.time.Clock()  # create clock
        self.running = True  # game loop
        self.font = pygame.font.SysFont('comic sans', 16)  # create font
        self.i = 0
        player_spritesheet = spritesheet.SpriteSheet('pictures/Morty.png')
        # morty
        self.player_base_image = player_spritesheet.image_at((27, 703, 79, 113))  # dont forget to remove negative sign
        self.player_base_image.convert_alpha()
        self.left_images = []  # list of images for left and right movement
        self.player_left_image1 = player_spritesheet.image_at((9, 877, 93, 108))
        self.player_left_image2 = player_spritesheet.image_at((138, 876, 92, 108))
        self.player_left_image3 = player_spritesheet.image_at((267, 877, 93, 108))
        self.player_left_image4 = player_spritesheet.image_at((395, 876, 95, 109))
        self.left_images = [self.player_left_image1, self.player_left_image2,
                            self.player_left_image3, self.player_left_image4]
        #MORTY UP IMAGES
        self.up_images = []
        self.player_right_image1 = player_spritesheet.image_at((28, 1042, 78, 109))
        self.player_right_image2 = player_spritesheet.image_at((157, 1042, 78, 108))
        self.player_right_image3 = player_spritesheet.image_at((286, 1042, 78, 109))
        self.player_right_image4 = player_spritesheet.image_at((415, 1042, 78, 109))
        self.up_images = [self.player_right_image1, self.player_right_image2,
                          self.player_right_image3, self.player_right_image4]

        # create player
        self.player_group = pygame.sprite.Group()
        self.player = ps.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 79, 113, self.screen, self.player_base_image,
                                self.left_images, self.up_images)

        self.object_group = pygame.sprite.Group()
        self.test_object = os.ObjectSprite(self.player_base_image, 100, 800)
        # self.player = ps.Player(0, 0, 105, 109, self.screen, self.player1_img)
        # create a group for the player

        self.player_group.add(self.player)
        self.object_group.add(self.test_object)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()

            self.update()
            self.draw()

    # Handles events in the game such as key presses and mouse clicks
    def events(self):
        for event in pygame.event.get():  # event loop
            if event.type == pygame.QUIT:  # if user clicks X button
                self.running = False

    # Updates the game state such as player position and enemy position
    # This is where the game logic goes
    def update(self):
        self.player_group.update()

    def draw(self):
        # set background to background image and draw it
        self.screen.blit(bg_img, (0, 0))
        self.player_group.draw(self.screen) # draw player
        self.object_group.draw(self.screen) # draw object
        pygame.display.flip()  # update a portion of the screen

    def quit(self):
        pygame.quit()


# main

if __name__ == '__main__':
    game = Game()
    game.run()
    game.quit()
