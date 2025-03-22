# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys


interval=8

def textbox():
    box=pygame.image.load("img/text_box.png")
    x,y=box.get_size()
    bairitu=640/x
    box=pygame.transform.scale(box,(x*bairitu,y*bairitu))
    return box

def main():
    pygame.init()                                   
    screen = pygame.display.set_mode((640, 480))    
    pygame.display.set_caption("Test")              
    font=pygame.font.Font("utils/ipaexm.ttf",30)
    box=textbox()
    text="操作方法/"
    textlist=list(text)
    timer=0
    Clock=pygame.time.Clock()
    

    while (1):
        Clock.tick(60)
        timer+=1
        screen.fill((0,0,0))  
        screen.blit(box,(0,205))
        count=0
        y=0
        if pygame.mouse.get_pressed()[0]:
            timer=40000000
        for temp in textlist[0:timer//interval]:
            count+=1
            text=font.render(temp,True,(255,255,255))
            if temp=="/":
                count=0
                y+=30
            else:
                screen.blit(text,(0+count*30,240+y))
        
        pygame.display.update() 

        for event in pygame.event.get():
            if event.type == QUIT:  
                pygame.quit()       
                sys.exit()


if __name__ == "__main__":
    main()

