import pygame
from pygame.locals import *
import sys
import time
import random

class end:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fight")
        self.screen = pygame.display.set_mode((640,480))
        
    def main(self):
        Clock = pygame.time.Clock()
        while True:
                self.screen.fill((0, 0, 0))
                Clock.tick(60)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

if __name__ == "__main__":
    Ending = end()
    Ending.main()
