import pygame
import random
from pygame import Rect
from os import path
pygame.init()
size = width, height =640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
image = pygame.image.load(path.join(path.dirname(__file__),"unnamed.jpg"))
image_rect = image.get_rect()
origin_image = image 
back_ground = (255, 255, 230)
pos_x =0 
pos_y =0
angle = 0
isRunning =True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pos_y=pos_y-1
    elif keys[pygame.K_DOWN]:
        pos_y=pos_y+1
    if keys[pygame.K_RIGHT]:
        pos_x=pos_x+1
        angle =angle-1
    elif keys[pygame.K_LEFT]:
        pos_x=pos_x-1
        angle =angle+1
    screen.fill(back_ground)
    screen.blit(image,image_rect)
    image = pygame.transform.scale(origin_image,(300+pos_y,300+pos_y))
    image = pygame.transform.rotate(image,angle)
    pygame.display.flip()
    clock.tick(30)
    