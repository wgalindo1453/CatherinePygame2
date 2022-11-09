import pygame
import spritesheet
import playersprite as ps

# screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900

spacebg = pygame.image.load("pictures/bg.jpg")

# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# game class
class Game:


    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.SysFont('arial', 16)
        self.i = 0
        #self.player = ps.Playerspr(SCREEN_WIDTH, SCREEN_HEIGHT, 'pictures/player.png', 0, 0)
        player_spritesheet = spritesheet.SpriteSheet('pictures/Morty.jpg')
        self.player_base_image = player_spritesheet.image_at((-27, -703, 79, 113))
        ps.Player(100, 100, 50, 50, self.screen, self.player_base_image)

        self.player_group = pygame.sprite.Group()
        self.player_group.add(ps.Player(100, 100, 50, 50, self.screen, self.player_base_image))

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        self.screen.blit(spacebg, (0, 0))
        self.player_group.draw(self.screen)

    def quit(self):
        pygame.quit()


# main
if __name__ == 'main':
    game = Game()
    game.run()
    game.quit()