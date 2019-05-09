import pygame
import pyganim
import anim
from pygame_functions import *
pygame.init()
pygame.display.set_caption("Tekino")

clock = pygame.time.Clock()
run = True
win = pygame.display.set_mode((1350,700))
size = width ,height = 1350,700
left, right, attack_1, attack_1_projectile, attack_2, busy = False, False, False, False, False, False
x = 500
y = 240
x_projectile = x + 185 
y_projectile = 395
x_change = 0
t_elapsed = 0

class projectile:
    def move(self,x_pos,y_pos):
        anim.repukken_projectile.loop = False
        anim.repukken_projectile.play()
        anim.repukken_projectile.blit(win,(x_pos,y_pos))

class backround:
    def idle(self):
        anim.stage_idle.play()
        anim.stage_idle.blit(win,(0,0))

class fighter:
    def walkLeft(self,x_pos,y_pos):
        anim.walkLeft.play()
        anim.walkLeft.blit(win,(x_pos,y_pos))
    def walkRight(self,x_pos,y_pos):
        anim.walkRight.play()
        anim.walkRight.blit(win,(x_pos,y_pos))
    def idle(self,x_pos,y_pos):
        anim.idle.play()
        anim.idle.blit(win,(x_pos,y_pos))
    def attack_projectile_1(self,x_pos,y_pos):
        anim.repukken.loop = False        
        anim.repukken.play()
        anim.repukken.blit(win,(x_pos,y_pos-100))
    def attack_kick_1(self,x_pos,y_pos):
        anim.cutter.loop = False
        anim.cutter.play()
        anim.cutter.blit(win,(x_pos,y_pos-100))

senshi = fighter()
stage = backround()
projectile_ = projectile()

def redrawGameWindow():
    global x_projectile
    stage.idle()
    if left:
        senshi.walkLeft(x,y)
    elif right:
        senshi.walkRight(x,y)
    elif attack_1: 
        senshi.attack_projectile_1(x,y) 
    elif attack_2:  
        senshi.attack_kick_1(x,y)    
    else:
        senshi.idle(x,y)

    if attack_1_projectile:
        projectile_.move(x_projectile, y_projectile)
        x_projectile += 15            

    pygame.display.update()

while run:

    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if  busy:
        x_change = 0
        right = False
        left = False
    else:
        if keys[pygame.K_LEFT] :
            x_change = -10 
            left = True
            right = False
        elif keys[pygame.K_RIGHT] :
            x_change = 10
            left = False
            right = True
        elif keys[pygame.K_a] :
            x_change = 0
            attack_1 = True
            busy = True
        elif keys[pygame.K_d] :
            x_change = 0
            attack_2 = True
            busy = True
        else:
            x_change = 0
            right = False
            left = False
            
    
    if anim.repukken.isFinished():
        attack_1 = False
        anim.repukken.elapsed = 0
    
    if anim.repukken.currentFrameNum > 5:
        attack_1_projectile =True

    if anim.repukken_projectile.isFinished():
        attack_1_projectile = False
        x_projectile = x + 185
        anim.repukken_projectile.elapsed = 0
        busy = False

    if anim.cutter.isFinished():
        anim.cutter.elapsed = 0
        attack_2 = False
        busy = False

    x += x_change
    if x_change:
        x_projectile = x + 185
    
    
    redrawGameWindow()

