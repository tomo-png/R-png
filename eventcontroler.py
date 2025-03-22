import sys
import pygame
import utils.mapchip
import textcontroler
from pygame.locals import *
import ending
import fight

class event:
    def __init__(self) :
        self.text=("操作説明/wasdキーで移動です")
        self.text2=("・・・")
        self.text2_1=("何かの鍵を落としていった")
        self.text3=("残念だったな、実は宝箱ではなく自分は魔王なのだ！！")
        self.text4=("私に勝ったら世界を平和にしてやろう")
        self.text5=("そしてKキーでアイテムを動かしたり/調べたりすることができます/試しに左にある木を調べてみましょう")
        self.text6=("木がじゃまだったので魔法で消した！")
        self.text7=("強くなって出直してこい")
        self.text8=("鍵がかかってて開けられない")
        self.text8_1=("鍵を使って宝箱を開けた！")
        self.text8_2=("q")
        self.events=utils.mapchip.events
        self.textcont=textcontroler.textcontroler()
        self.tasks=[]
        self.boss = pygame.image.load("img/knight12.png")
        self.bossgame = fight.sentou("tomo",100,10,50,"Boss",200,20,Tekiimg=self.boss)
        self.ending=ending.end()
        self.kagi=False

    def check(self,player_pos):
        x,y=player_pos
        if self.events[(y+16)//32][(x+16)//32]>0:
            self.start(self.events[(y+16)//32][(x+16)//32])
    
    def start(self,eventcode):
        if eventcode==1:
            self.textcont.draw(self.text,8)
            self.textcont.draw(self.text5,8)
        if eventcode==2:
            self.textcont.draw(self.text2,8)
            self.textcont.draw(self.text2_1,8)
            self.tasks.append(["items",6,2,0])
            self.tasks.append(["hantei",6,2,0])
            self.tasks.append(["events",7,2,0])
            self.kagi=True

        if eventcode==3:
            self.textcont.draw(self.text3,8)
            self.textcont.draw(self.text4,8)
            kekka=self.bossgame.main()
            if kekka=="player_lose":
                self.textcont.draw(self.text7,8)
            if kekka=="player_win":
                self.ending.main()

            

        if eventcode==4:
            self.textcont.draw(self.text6,8)
            self.tasks.append(["items",12,16,0])
            self.tasks.append(["hantei",12,16,0])
            self.tasks.append(["hantei",12,17,0])
            self.tasks.append(["hantei",13,16,0])
            self.tasks.append(["hantei",13,17,0])
            self.tasks.append(["events",12,18,0])
            self.tasks.append(["events",13,18,0])

        if eventcode==5:
            if self.kagi==False:
                self.textcont.draw(self.text8,8)
            else:
                self.tasks.append(["items",0,0,2])

            

    def update(self):
        update=self.tasks
        self.tasks=[]
        return update 
    