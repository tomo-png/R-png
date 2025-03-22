import sys
import pygame
import utils.NPC as npc
from pygame.locals import *

class map:

    def __init__(self):     
        tuti_chip=pygame.image.load("img/tuti.png")
        kusa_chip=pygame.image.load("img/kusa.png")
        kawa_chip=pygame.image.load("img/kawa.png")
        iwa_chip=pygame.image.load("img/iwa.png")
        mizu_chip=pygame.image.load("img/mizu.png")
        bridge_chip=pygame.image.load("img/bridge.png")
        hashi_chip=pygame.image.load("img/hashi.png")
        self.bridge_chip2=pygame.image.load("img/bridge2.png")
        otakara_chip=pygame.image.load("img/otakara.png")
        otakaraake_chip=pygame.image.load("img/otakara_ake.png")
        kareki_chip=pygame.image.load("img/kareki.png")
        kannbann_chip=pygame.image.load("img/Kannbann.png")
        kawa_half=pygame.image.load("img/kawa_half.png")
        self.npc=npc.npc("img/npc1.png")

        self.tuti_chip=pygame.transform.scale(tuti_chip,(32,32))
        self.kusa_chip=pygame.transform.scale(kusa_chip,(32,32))
        self.kawa_chip=pygame.transform.scale(kawa_chip,(32,32))
        self.iwa_chip=pygame.transform.scale(iwa_chip,(32,32))
        self.mizu_chip=pygame.transform.scale(mizu_chip,(32,32))
        self.bridge_chip=pygame.transform.scale(bridge_chip,(34,40))
        self.hashi_chip=pygame.transform.scale(hashi_chip,(32,32))
        self.bridge_chip=pygame.transform.scale(bridge_chip,(64,92))
        self.otakara_chip=pygame.transform.scale(otakara_chip,(32,32))
        self.otakaraake_chip=pygame.transform.scale(otakaraake_chip,(32,32))
        self.kareki_chip=pygame.transform.scale2x(kareki_chip)
        self.kannbann_chip=pygame.transform.scale2x(kannbann_chip)
        self.kawa_half=pygame.transform.scale(kawa_half,(32,32))
        self.dx = 0 #ここでマップの移動できそう！！！！
        self.dy = 0 #


 
    def draw_maps(self,map):
        surf = pygame.Surface((640,480))
        surf.fill((0,0,0))
        x=0
        y=0
        
        for chips in map:
            for chip in chips:
                if chip==0x000000:
                    surf.blit(self.tuti_chip,((x)*32,(y )*32))
                if chip==0x800000:
                    surf.blit(self.kusa_chip,((x)*32,(y )*32))
                if chip==0x00ff00:
                    surf.blit(self.mizu_chip,((x)*32,(y )*32))
                if chip==3:
                    surf.blit(self.kusa_chip,((x)*32,(y )*32))
                    surf.blit(self.kawa_chip,((x)*32,(y)*32))
                if chip==4:
                    surf.blit(self.tuti_chip,((x)*32,(y )*32))
                    surf.blit(self.kawa_chip,((x)*32,(y )*32))
                if chip==5:
                    surf.blit(self.mizu_chip,((x)*32,(y )*32))
                    surf.blit(self.hashi_chip,((x)*32,(y )*32))
                if chip==6:
                    surf.blit(self.tuti_chip,((x)*32,(y )*32))
                    surf.blit(self.kawa_half,((x)*32,(y )*32))

                x+=1
            x=0
            y+=1
        y=0

        return surf

    def draw_items(self,items):
        surf=pygame.Surface((640,480),flags=pygame.SRCALPHA)
        x=0
        y=0
        for item in items:
            for chip in item :
                if chip==0:
                    pass
                if chip==1:
                    surf.blit(self.otakara_chip,((x)*32,(y )*32))
                if chip==0x00ffff:
                    surf.blit(self.otakaraake_chip,((x)*32,(y )*32))
                if chip==0xffff00:
                    surf.blit(self.kareki_chip,((x)*32,(y )*32))
                if chip==0xff8000:
                    surf.blit(self.kannbann_chip,((x)*32,(y )*32))
                if chip==5:
                    surf.blit(self.kawa_half,((x)*32,(y )*16))
                if chip==0xff00cc:
                    surf.blit(self.npc.image(),((x)*32,(y )*32))
                if chip == 0x808080:
                    surf.blit(self.iwa_chip,((x)*32,(y )*32))

                x+=1
            x=0
            y+=1
        y=0


        #surf.blit(self.bridge_chip2,(64,214))
        #surf.blit(self.bridge_chip,(464,9))
        return surf