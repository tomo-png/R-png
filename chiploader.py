import pygame
import numpy as np

def base(chip_array):
    base=pygame.image.load("img/base.png")
    width, height = base.get_size()
    # 画像のピクセルデータを取得
    # 画像の各ピクセルを取得してRGBの24ビットを配列に追加

    for y in range(height//16):
        for x in range(width//16):
            # ピクセルのRGB値を取得
            chip=[]
            for dy in range(y*16):
                #chip_x=[]
                for dx in range (x*16):
                    chip.append(base.get_at((x*16+1 ,y*16+1)))
                #chip.append(chip_x)
            chip_array.append(chip)
        
            #for d in chip:
            #    print(d)
    

            
if __name__=="__main__":
    chip_database = []
    base(chip_database)


    pygame.init()   # Pygameを初期化
    screen = pygame.display.set_mode((1000, 600))    # 画面作成
    #image = pygame.image.load("image/icon.png")     # 画像読み込み
    running = True  # 実行継続フラグ
    print(chip_database[2])
    image_surface = pygame.surfarray.make_surface(np.array(chip_database[2]))
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill the screen with the image
        screen.blit(image_surface, (0, 0))
        
        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()
