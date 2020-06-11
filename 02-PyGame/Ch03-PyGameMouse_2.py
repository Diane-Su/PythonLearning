import sys
import pygame
from pygame import Rect
from os import path
# 初始化 initialize
pygame.init()
pygame.font.init()
font_name = pygame.font.match_font('arial')
size = width, height = 640, 480
background_color = 204, 255, 204
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pos = (0, 0)
pos_x = 0
pos_y = 0
radius = 10
circle_box = []
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,(255,255,255))
    text_rect =text_surface.get_rect()
    text_rect.midtop =(x,y)
    surf.blit(text_surface,text_rect)
while 1:
    # 偵測事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse = pygame.mouse.get_pressed()
    # print(mouse)
    if mouse[0]:
        # 製造一顆圓 泡泡
        pos_x, pos_y = pygame.mouse.get_pos()
        radius = 5
        circle = {}
        circle['pos_x'] = pos_x
        circle['pos_y'] = pos_y
        circle['r'] = 5
        circle['color'] =(0, 128, 255)
        circle_box.append(circle)
        # print("Pos :", pos)
        pass
    # 更新遊戲資料
    for c in circle_box:
        c['pos_y'] = c['pos_y']-15
        c['r'] = c['r']+1
        c['color'] = (c['color'][0]+5,c['color'][1]+5,c['color'][2])
        if c['color'][0]>255 or c['color'][1]>255:
            c['color']=(255,255,255)
            circle_box.remove(c)
    print("泡泡的數量", len(circle_box))
    screen.fill(background_color)
    # 畫圓
    draw_text(screen,'Ball number'+str(len(circle_box)),36,500,300)
    for c in circle_box:
        print(c['color'])
        pygame.draw.circle(
            screen,
            (204, 255, 255),
            (c['pos_x'], c['pos_y']),
            c['r'],
            0
        )
        pygame.draw.circle(
            screen,
            c['color'],
            (c['pos_x'], c['pos_y']),
            c['r'],
            3
        )
    pygame.display.flip()
    clock.tick(10)
