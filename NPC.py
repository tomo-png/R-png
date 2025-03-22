import sys
import pygame
from pygame.locals import *

class npc:

    def __init__(self,img) :
        self.rect=[]
        self.img=pygame.image.load("img/npc1.png")

    def image(self):
        return self.img
    
    def turn(self,muki):
        pass
        