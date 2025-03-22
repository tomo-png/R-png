import utils.mapchip
import sys
import pygame
import utils.image
import utils.mapchip
import mapcontroler
import playercontroler
import textcontroler
import eventcontroler
import bit
from pygame.locals import *


"""
マップワープ



"""

class game:

    def __init__(self):     
        pygame.init()
        self.screen=pygame.display.set_mode((640,480))
        self.textcont=textcontroler.textcontroler()
        self.eventcont=eventcontroler.event()
        self.mapcont=mapcontroler.map()
        
        self.map=bit.get_map("img/new_map.bmp")
        self.mapchip=utils.mapchip
        # self.items=bit.map("img/new_map.bmp")
        self.items=bit.get_map("img/items_map.bmp")
        self.hantei=bit.get_map("img/hantei_map.bmp")
        self.events=utils.mapchip.events
        self.player_cont=playercontroler.player()
        self.player_image=self.player_cont.get_pc()
        self.Animation=self.player_cont.get_animation()
        self.Clock=pygame.time.Clock()
        self.timer=0
        self.main_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.map[self.mapcont.dy:self.mapcont.dy+15]]
        self.items_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.items[self.mapcont.dy:self.mapcont.dy+15]]
        self.hantei_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.hantei[self.mapcont.dy:self.mapcont.dy+15]]



    def main(self):
        self.mapcont.dx = 20
        self.mapcont.dy = 15
        #self.player_cont.player_pos = []
        while True:
            self.timer+=1
            self.Clock.tick(60)
            self.screen.fill((0,0,0))        
            self.screen.blit(self.mapcont.draw_maps(self.main_map),(0,0))
            self.screen.blit(self.mapcont.draw_items(self.items_map),(0,0))
            pos,index,muki,hantei=self.player_cont.move_controler(self.hantei_map)
            self.screen.blit(self.player_image, pos, self.Animation[muki][(index%32)//8])
            #self.mapcont.dx= self.player_cont.player_pos[0]//20
            #self.mapcont.dy= self.player_cont.player_pos[1]//15

            """
                マップ遷移の判定が緩いため、当たり判定があっても通り抜けられる現象アリ。後に修正せよ。
            
            """
            if (self.player_cont.player_pos[0]//32 )  % 20 == 19: #mod 21 == 20 にすればよりきれいかも
                self.mapcont.dx += 20
                # print(f"dx,dy={self.mapcont.dx},{self.mapcont.dy}\t{self.player_cont.player_pos} at {(self.player_cont.player_pos[0]//32)%20}")
                
                self.player_cont.player_pos[0] = 50

            if (self.player_cont.player_pos[1]//32  ) % 15 == 14:
                self.mapcont.dy += 15
                # print(f"dx,dy={self.mapcont.dx},{self.mapcont.dy}{self.player_cont.player_pos} at {(self.player_cont.player_pos[1]//32)%15}")
                
                self.player_cont.player_pos[1] = 40
            
            if (self.player_cont.player_pos[1]//32  ) % 15 == 0:
                self.mapcont.dy -= 15
                # print(f"dx,dy={self.mapcont.dx},{self.mapcont.dy}{self.player_cont.player_pos} at {(self.player_cont.player_pos[1]//32)%15}")
                
                self.player_cont.player_pos[1] = 420
            
            if (self.player_cont.player_pos[0]//32 )  % 20 == 0:
                self.mapcont.dx -= 20
                # print(f"dx,dy={self.mapcont.dx},{self.mapcont.dy}{self.player_cont.player_pos} at {(self.player_cont.player_pos[0]//32)%20}")
                
                self.player_cont.player_pos[0] = 590
            
            print(self.mapcont.dx,self.mapcont.dy,end="\r")

            for temp in hantei:
                #pygame.draw.rect(self.screen,(255,0,0),temp,1)
                pass
            self.main_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.map[self.mapcont.dy:self.mapcont.dy+15]]
            self.items_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.items[self.mapcont.dy:self.mapcont.dy+15]]
            self.hantei_map = [x[self.mapcont.dx:self.mapcont.dx+20] for x in self.hantei[self.mapcont.dy:self.mapcont.dy+15]]

            pygame.display.update()    

            for event in pygame.event.get():
                if event.type == QUIT:  
                    pygame.quit()       
                    sys.exit()
                if event.type==KEYUP:
                    if event.key==K_k:
                        self.eventcont.check(pos)
                        for update in self.eventcont.update():
                            if update[0]=="items":
                                self.items[update[1]][update[2]]=update[3]
                            if update[0]=="hantei":
                                self.hantei[update[1]][update[2]]=update[3]
                            if update[0]=="events":
                                self.events[update[1]][update[2]]=update[3]


Game = game()
Game.main()