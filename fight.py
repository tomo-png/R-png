import pygame
from pygame.locals import *
import sys
import time
import random

class sentou():
    
    def __init__(self,name,HP,ATK,MP,TekiName,TekiHP,TekiATK,Tekiimg):
        pygame.init()
        pygame.display.set_caption("Fight")
        self.name = name
        self.HP = HP
        self.MP = MP
        self.ATK = ATK
        self.Tekiname = TekiName
        self.TekiMAXHP= TekiHP
        self.TekiHP = TekiHP
        self.TekiATK = TekiATK
        self.cmds = []
        self.atkcmds=[]
        self.magics=[]
        self.h,self.w = (640,480)
        self.screen = pygame.display.set_mode((self.h, self.w)) 
        self.Tekiimg =pygame.transform.scale(Tekiimg,(200,200))
        self.tekifullHP = 100
        self.command = ["こうげき","まほう","アイテム","にげる"]
        self.atkcommand = ["通常攻撃","ギガ","ギガンテ","もどる"]
        self.magic = ["ヘナトス","ためる","ホイミ","もどる"]
        self.font=pygame.font.Font("ipaexm.ttf",25)
        for temp in range(4):
            self.cmds.append(self.font.render(self.command[temp], True, (255,255,255)))
        for temp in range(4):
            self.atkcmds.append(self.font.render(self.atkcommand[temp], True, (255, 255, 255)))
        for temp in range(4):
            self.magics.append(self.font.render(self.magic[temp], True, (255,255,255)))
        self.point = self.font.render("▷", True, (255,255,255))
        

    def main(self):
        Clock = pygame.time.Clock()
        sentaku = 0
        page=1  
        step=0
        while True:
            running=True
            while running:
                Clock.tick(60)
                self.screen.fill((0,0,0))
                
                pygame.draw.rect(self.screen,(255,255,255),(20,300,160,160),3)
                pygame.draw.rect(self.screen,(255,255,255),(200,300,400,160),3)
                pygame.draw.rect(self.screen,(255,0,0),(0,0,640,40))
                pygame.draw.rect(self.screen,(0,255,0),(0,0,640 * (self.TekiHP/self.TekiMAXHP),40))
                self.screen.blit(self.Tekiimg,(220,90))
                if page==1:
                    for temp in range(4):
                        self.screen.blit(self.cmds[temp], (50,310 + temp * 30))
                if page == 2:
                    for temp in range(4):
                        self.screen.blit(self.atkcmds[temp], (50, 310 + temp * 30))
                if page ==3:
                    for temp in range(4):
                        self.screen.blit(self.magics[temp], (50, 310 + temp * 30))
                self.hp_text = self.font.render("HP "+str(self.HP)+"/100", True, (255,255,255))
                self.mp_text = self.font.render("MP "+str(self.MP)+"/100", True, (255,255,255))
                self.atk_text = self.font.render("Atack "+str(self.ATK), True, (255,255,255))
                self.screen.blit(self.point, (30,310 + sentaku%4 * 30))
                self.screen.blit(self.hp_text,(210,310))
                self.screen.blit(self.mp_text,(210,340))
                self.screen.blit(self.atk_text,(210,370))
                pygame.display.update()
            

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYUP:
                        if event.key==K_w:
                            sentaku-=1
                        if event.key==K_s:
                            sentaku+=1
                        if event.key==K_k:
                            if page==1 :
                                if sentaku%4==0:
                                    page=2
                                if sentaku%4==1:
                                    page=3

                            elif page==2 :
                                if sentaku%4==0:
                                    self.types="通常攻撃"
                                    running=False
                                if sentaku%4==1:
                                    self.types="ギガ"
                                    running=False
                                if sentaku%4==2:
                                    self.types="ギガンテ"
                                    running=False
                                if sentaku%4==3:
                                    page=1
                                    sentaku=0 

                            elif page==3 :
                                if sentaku%4==0:
                                    self.type="ヘナトス"
                                    running = False

                                if sentaku%4==1:
                                    self.type="ためる"
                                    running = False   

                                if sentaku%4==2:
                                    self.type="ホイミ"
                                    running = False

                                if sentaku%4==3:
                                    self.type="もどる"
                                    page=1
                                    sentaku=0 
            step=1
            text1=self.font.render("プレイヤーのターン！",True,(255,255,255))
            text2=self.font.render("ボスのターン！",True,(255,255,255))
            time = 0
            stepframe = 45
            self.haba=random.uniform(0.8,1.2)
            self.mphaba=random.randint(5,15)
            bairitu = 0
            koudou = True
            boss_koudou=True
            while True:
                Clock.tick(60)
                self.screen.fill((0,0,0))
                pygame.draw.rect(self.screen,(255,255,255),(20,300,160,160),3)
                pygame.draw.rect(self.screen,(255,255,255),(200,300,400,160),3)
                pygame.draw.rect(self.screen,(255,0,0),(0,0,640,40))
                pygame.draw.rect(self.screen,(0,255,0),(0,0,640 * (self.TekiHP/self.TekiMAXHP),40))
                self.screen.blit(self.Tekiimg,(220,90))
                self.mphaba=round(self.mphaba,1)
                if step==1:
                    self.screen.blit(text1,(210,310))
                    time = 0
                
                if step == 2:
                  if page == 2:
                    if koudou:
                        if self.types=="通常攻撃":
                            bairitu=1
                            damage = self.ATK * self.haba
                            self.MP+=self.mphaba
                           
                        if self.types=="ギガ":
                            if self.MP<10:
                               damage = 0

                            else:
                                bairitu = 1.2
                                self.MP -= 10
                                damage = self.ATK * self.haba * bairitu

                        if self.types == "ギガンテ":
                            if self.MP<50:
                               damage = 0
                            else:
                                bairitu = 2
                                self.MP-= 50
                                damage = self.ATK * self.haba * bairitu
                        damage=round(damage,1)
                        self.TekiHP -= damage
                        koudou = False

                               
                    time += 1
                    if page == 2:
                        temp=self.font.render(f"プレイヤーは{damage}ダメージを与えた！",True,(255,255,255))
                        self.screen.blit(temp,(210,310))
                
                  if page == 3:
                    if koudou:
                        if self.type == "ヘナトス":
                            if self.MP<10:
                                temp=self.font.render(f"MP不足",True,(255,255,255))
                            else:
                                self.TekiATK = self.TekiATK *0.7
                                temp=self.font.render(f"敵の攻撃力を下げた！",True,(255,255,255))
                                self.MP-=10
                        koudou=False
                        if self.type=="ためる":
                            if self.MP<15:
                                temp=self.font.render(f"MP不足",True,(255,255,255))
                            else:
                                self.ATK=self.ATK*1.2
                                temp=self.font.render(f"自身の攻撃力を上げた！",True,(255,255,255))
                                self.MP-=15
                        koudou=False
                        if self.type=="ホイミ":
                            if self.MP<35:
                                temp=self.font.render(f"MP不足",True,(255,255,255))
                            if self.HP>=100:
                                self.HP=100
                                temp=self.font.render(f"HPは100なので回復できなかった！",True,(255,255,255))
                            else:
                                self.HP=100
                                temp=self.font.render(f"自身のHPを全回復した！",True,(255,255,255))
                                self.MP-=35
                        koudou=False
                    self.screen.blit(temp,(210,310))
                        

                
                if step == 3:
                    self.screen.blit(text2,(210,310))

                if step==4:
                    if boss_koudou:
                        number=random.randint(0,100)
                        print(number)
                        haba=random.uniform(0.8,1.2)
                        if number<=50:
                            damage=self.TekiATK*haba
                            damage=round(damage,1)
                            self.HP-=damage
                            temp=self.font.render(f"プレイヤーは{damage}ダメージをくらった！",True,(255,255,255))
                        elif number<=70:
                            self.TekiATK=self.TekiATK*1.2
                            temp=self.font.render(f"敵の攻撃力が上がった！",True,(255,255,255))
                        elif number<=90:
                            self.TekiHP+=20
                            temp=self.font.render(f"敵が回復した！",True,(255,255,255))
                        elif number<=95:
                            temp=self.font.render(f"敵の攻撃を避けた！",True,(255,255,255))
                        elif number<=100:
                            self.MP-=20
                            if self.MP<0:
                                self.MP=0
                            temp=self.font.render(f"プレイヤーのMPが奪われて敵が/回復した！",True,(255,255,255))
                            self.TekiATK+=10
                        boss_koudou=False
                    step+=1
                
                if step==5:    
                    self.screen.blit(temp,(210,310))
                    koudou = True
                    
                if step==6:
                    self.HP = round(self.HP,1)
                    self.ATK = round(self.ATK,1)
                    if self.HP < 0:
                        return "player_lose"
                    if self.TekiHP<=0:
                        return "player_win"
                    break;

                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==KEYUP:
                        if event.key==K_k:
                            step+=1


if __name__ == "__main__":
    boss = pygame.image.load("img/knight12.png")
    Sentou= sentou("tomo",100,10,50,"Boss",200,15,Tekiimg=boss)
    Sentou.main()
