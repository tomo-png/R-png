import sys
import pygame
from pygame.locals import *

class player:
    
    def __init__(self) :
        self.Animation={
            "ue":[],
            "sita":[],
            "migi":[],
            "hidari":[]
        }
        self.rects = []
        for y in range(4):
            for x in range(3):
                self.rects.append([x * 32, y * 32, 32, 32])

        self.speed=7
        self.index=0
        self.player_pos=[64,64]
        self.create_animation("sita",1)
        self.create_animation("sita", 0)
        self.create_animation("sita", 1)
        self.create_animation("sita", 2)
        self.create_animation("ue", 10)
        self.create_animation("ue", 9)
        self.create_animation("ue", 10)
        self.create_animation("ue", 11)
        self.create_animation("migi", 7)
        self.create_animation("migi", 6)
        self.create_animation("migi", 7)
        self.create_animation("migi", 8)
        self.create_animation("hidari", 4)
        self.create_animation("hidari", 3)
        self.create_animation("hidari", 4)
        self.create_animation("hidari", 5)
        self.muki="sita"
        # syougaibutu_rect=pygame.Rect(240,240,60,60)


    def create_animation(self,muki,index):
        self.Animation[muki].append(self.rects[index])

    def move_controler(self,hantei):
        keys= pygame.key.get_pressed()
        self.move=[0,0]
        if keys[pygame.K_s]:
            self.muki = "sita"
            self.move[1] += self.speed
            self.index+=1
        elif keys[pygame.K_w]:
            self.muki = "ue"
            self.move[1] -= self.speed
            self.index+=1
        elif keys[pygame.K_a]:
            self.muki = "hidari"
            self.move[0] -= self.speed
            self.index+=1
        elif keys[pygame.K_d]:
            self.muki = "migi"
            self.move[0] += self.speed
            self.index+=1

        shougaibutu_rects=[]
        x=0
        y=0
        self.player_pos[0]+=self.move[0]
        self.player_pos[1]+=self.move[1]
        if self.player_pos[0] > 608:
            self.player_pos[0]= 608
        
        if self.player_pos[0] < 0:
            self.player_pos[0]= 0

        if self.player_pos[1] < 0:
            self.player_pos[1]= 0

        if self.player_pos[1] > 450:
            self.player_pos[1]= 450
        self.player_rect=pygame.Rect(self.player_pos[0]+10,self.player_pos[1]+10,16,16)
        # プレイヤーの体のめり込み具合　　　↑　調整
        for hantei_chip in hantei:
            for temp in hantei_chip:
                #if temp == 0xffffff:
                if temp == 0xffdcff:#デバッグのため適当な数値割り当て

                    shougaibutu_rects.append(pygame.Rect((x*32,y*32,32,32)))
                x+=1
            x=0
            y+=1
        y=0

        for temp in shougaibutu_rects:
            if self.player_rect.colliderect(temp):
                self.player_pos[0]-=self.move[0]
                self.player_pos[1]-=self.move[1]
                return self.player_pos,self.index,self.muki,shougaibutu_rects
        

        return self.player_pos,self.index,self.muki,shougaibutu_rects
    
    def get_animation(self):
        return self.Animation
    
    def get_pc(self):
        return pygame.image.load("img/org_m01b.png")
    
