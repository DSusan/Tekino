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
left, right, attack_1, attack_1_projectile, attack_2, attack_3, crouch, busy = False, False, False, False, False, False, False, False
x = 500
y = 240
x_projectile = x + 185 
y_projectile = 395
x_change = 0
t_elapsed = 0

class projectile:
    def __init__(self):
        anim.repukken_projectile.loop = False
    def move(self,x_pos,y_pos):
        anim.repukken_projectile.play()
        anim.repukken_projectile.blit(win,(x_pos,y_pos))

class backround:
    def __init__(self):
        anim.stage_idle.play()
    def idle(self):
        anim.stage_idle.blit(win,(0,0))

class fighter:
    def __init__(self):
        anim.crouch.loop = False
        anim.walkLeft.play()
        anim.walkRight.play()
        anim.idle.play()
        anim.repukken.loop = False
        anim.cutter.loop = False
        anim.punch_1.loop = False
        
    def walkLeft(self,x_pos,y_pos):
        anim.walkLeft.blit(win,(x_pos,y_pos))
    def walkRight(self,x_pos,y_pos):
        anim.walkRight.blit(win,(x_pos,y_pos))
    def idle(self,x_pos,y_pos):
        anim.idle.blit(win,(x_pos,y_pos))
    def crouch(self,x_pos,y_pos):
        if anim.crouch.currentFrameNum == 3:
            anim.crouch.pause()
        else:
            anim.crouch.play()
        anim.crouch.blit(win,(x_pos,y_pos+50))
    def attack_projectile_1(self,x_pos,y_pos):
        anim.repukken.play()
        anim.repukken.blit(win,(x_pos,y_pos-100))
    def attack_kick_1(self,x_pos,y_pos):
        anim.cutter.play()
        anim.cutter.blit(win,(x_pos,y_pos-100))
    def attack_punch_1(self,x_pos,y_pos):
        anim.punch_1.play()
        anim.punch_1.blit(win,(x_pos,y_pos))

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
    elif crouch:
        senshi.crouch(x,y)
    elif attack_1: 
        senshi.attack_projectile_1(x,y) 
    elif attack_2:  
        senshi.attack_kick_1(x,y) 
    elif attack_3:
        senshi.attack_punch_1(x,y)   
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                crouch = False
                anim.crouch.elapsed = 0

    keys = pygame.key.get_pressed()

    if  busy:
        x_change = 0
        right = False
        left = False
        crouch = False
    else:
        if keys[pygame.K_LEFT] :
            x_change = -10 
            left = True
            right = False
        elif keys[pygame.K_RIGHT] :
            x_change = 10
            left = False
            right = True
        elif keys[pygame.K_DOWN] :
            x_change = 0
            left = False
            right = False
            crouch = True
        elif keys[pygame.K_a] :
            x_change = 0
            attack_1 = True
            busy = True
        elif keys[pygame.K_s] :
            x_change = 0
            attack_3 = True
            busy = True
        elif keys[pygame.K_f] :
            x_change = 0
            attack_2 = True
            busy = True
        else:
            x_change = 0
            right = False
            left = False
            crouch = False
            
    
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
    
    if anim.punch_1.isFinished():
        anim.punch_1.elapsed = 0
        attack_3 = False
        busy = False

    x += x_change
    if x_change:
        x_projectile = x + 185
    
    
    redrawGameWindow()

