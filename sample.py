import pygame
import numpy as np
width = 16 * 8
height = 16 * 20

def rgb_to_24bit(r, g, b):
    # 各色の値を8ビットとしてシフトして結合する
    return (r << 16) | (g << 8) | b

import pygame
import numpy as np

def chip_base(chip_array):
    base=pygame.image.load("img/base.png")
    width, height = base.get_size()
    # 画像のピクセルデータを取得
    # 画像の各ピクセルを取得してRGBの24ビットを配列に追加

    for y in range(height//16):
        for x in range(width//16):
            # ピクセルのRGB値を取得
            chip=[]
            for dy in range(16):
                #chip_x=[]
                for dx in range (16):
                    chip.append(base.get_at((x*16 + dx, y*16 + dy))[:3])
                #chip.append(chip_x)
            chip = np.array(chip).reshape((16,16,3))
            chip = np.transpose(chip, (1, 0, 2))
            chip_array.append(chip)
            #for d in chip:
            #    print(d)
    

            
if __name__=="__main__":
    chip_database = []
    chip_base(chip_database)


    pygame.init()   # Pygameを初期化
    screen = pygame.display.set_mode((1200, 700))    # 画面作成
    #image = pygame.image.load("image/icon.png")     # 画像読み込み
    running = True  # 実行継続フラグ
    font = pygame.font.Font(None, 10)               

    counter = 0
    chip_cnt = 0
    chip_cnt_x = 1
    chip_cnt_y = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with the image
        counter += 1
        
        if counter % 2 == 0:
            chip_cnt += 1
            chip_cnt_x += 1

        if chip_cnt_x % 70 == 0:
            chip_cnt_x = 1
            chip_cnt_y += 1

        try:
            test = chip_database[chip_cnt]
            image_surface = pygame.surfarray.make_surface(test)
            screen.blit(image_surface, (chip_cnt_x*16, chip_cnt_y*16))
            text = font.render( f"{chip_cnt}", True, (255, 255, 255))
            screen.blit(text, (chip_cnt_x*16, chip_cnt_y*16))
        except:
            pass
        #pygame.surfarray.blit_array(screen,  np.array(chip_database[0]))

        # Update the display
        pygame.display.update()

    # Quit pygame
    pygame.quit()
