import pygame
import random
from os import path
pygame.init()
size = width, height =640, 480
screen = pygame.display.set_mode(size)
i =0
totoro =[]
for i in range(40):
    totoro.append(i+1)      
ball = pygame.image.load(path.join(
    path.dirname(__file__),
    "龍貓-0",
    "龍貓-"+ str(i)+".jpg"))
ballrect = ball.get_rect()
clock = pygame.time.Clock() 
back_ground = (255, 255, 230)
isRunning =True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning=False
    ball = pygame.image.load(path.join(
    path.dirname(__file__),
    "龍貓-0",
    "龍貓-"+ str(i)+".jpg"))
    i=i+1
    print(i)
    if i>39:
        i=0
    screen.fill(back_ground)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    clock.tick(30)
    if i==1:
        back_ground=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
pygame.quit()





