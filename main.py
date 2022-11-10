import pygame
import spritesheet
import PlayerSprite as ps

# screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
#hello
# loading images into pygame
bg_img = pygame.image.load('pictures/bg.jpg')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))  # resize the image to fit the screen




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
        self.player_base_image = player_spritesheet.image_at((-27, -703, 79, 113))
        #convert to alpha


        #create player
        self.player = ps.Player(0, 0, 79, 113, self.screen, self.player_base_image)

        #create a group for the player
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

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
        pass

    def draw(self):
        # set background to background image and draw it
       #set screen background white
        self.screen.fill(WHITE)
        self.player_group.draw(self.screen)
        pygame.display.flip()  # update a portion of the screen


    def quit(self):
        pygame.quit()


# main

if __name__ == '__main__':
    game = Game()
    game.run()
    game.quit()
