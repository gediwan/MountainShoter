import pygame



class Game:

    def __init__(self):
        self.window = None

    def run(self,):
        print('setup start')
        pygame.init()
        window = pygame.display.set_mode(size=(1200, 400))
        print('Setup End')

        print('Loop Start')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                quit()
