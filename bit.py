# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *
import numpy as np
import time

"""
マップ編集用
https://www.photopea.com/

16色ビットマップフォーマット
カラーパレットの番号順にタイルを読み込む
https://apec.aichi-c.ed.jp/kyouka/jouho/contents/2018/jissyuu/043/gazou.files/filefmt.files/bmp16.htm

"""
SCREEN_SIZE = (640, 480)

def main():
    
    pygame.init() 
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("GAME TITLE")  

    while True:
        screen.fill((0, 0, 0))
        pygame.display.update()  

        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == QUIT:  
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

def get_map(filepath):
    return get_bmp_data_array(filepath)
    """
    bit=pygame.image.load(filepath)
    rawdata=pygame.image.tobytes(bit,"P")
    #print(rawdata)
    height = bit.get_height()
    width = bit.get_width()
    hantei=0
    map=[]
    index=0
    for i in range(height):
        buff=[]
        for n in range(width):
            buff.append(rawdata[index])
            index+=1
        map.append(buff)
    return map
    """
    

def get_8bit_bitmap(filepath):
    pygame.init()
    image=pygame.image.load("img/test.bmp")
    #image.convert(8)
    w,h=image.get_size()
    pixels = pygame.PixelArray(image)
    int_pixels = np.array(pixels,dtype=np.uint8)
    del pixels
    return int_pixels

def rgb_to_24bit(r, g, b):
    # 各色の値を8ビットとしてシフトして結合する
    return (r << 16) | (g << 8) | b

def get_bmp_data_array(image_path):

    # 画像を読み込み
    image = pygame.image.load(image_path)
    # 画像の幅と高さを取得
    width, height = image.get_size()
    # 画像のピクセルデータを取得
    rgb_array = []
    # 画像の各ピクセルを取得してRGBの24ビットを配列に追加
    for y in range(height):
        row = []
        for x in range(width):
            # ピクセルのRGB値を取得
            r, g, b, _ = image.get_at((x, y))  # アルファ値は無視してRGBのみ取得
            rgb_value = rgb_to_24bit(r,g,b)   #RGBの値を結合、HTML表記用に24bitの数値にする
            row.append(rgb_value)
        rgb_array.append(row)
    return rgb_array


if __name__ == "__main__":
    testmap = get_bmp_data_array("img/bmptest.bmp")
    x = list(testmap)
    #for d in x:
        #print(list(map(hex,d)))
        #time.sleep(1)