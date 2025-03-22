import pygame
from pygame.locals import *
import sys

class textcontroler:
    def __init__(self):
        self.box=pygame.image.load("img/text_box.png")
        x,y=self.box.get_size()
        bairitu=640/x
        self.box=pygame.transform.scale(self.box,(x*bairitu,y*bairitu))
        self.font=pygame.font.Font("utils/ipaexm.ttf",30)
        
    def draw(self,text,interval):             
        surf=pygame.display.get_surface()    
        textlist=list(text)                               
        running=True
        timer=0
        Clock=pygame.time.Clock()
    
        while running:
            Clock.tick(60)
            timer+=1
            surf.blit(self.box,(0,205))
            count=0
            y=0

            for temp in textlist[0:timer//interval]:
                count+=1
                text=self.font.render(temp,True,(255,255,255))
                if temp=="/":
                    count=0
                    y+=30
                else:
                    surf.blit(text,(0+count*30,240+y))
            
            pygame.display.update() 

            for event in pygame.event.get():
                if event.type == QUIT:  
                    pygame.quit()       
                    sys.exit()

                if event.type==KEYUP:
                    if event.key==K_k:
                        if timer//interval >100000:
                            running =False
                        timer=1000000





