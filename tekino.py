import pygame
import pyganim
import anim
import anim2
from pygame_functions import *
#testing VSCODE GIT
pygame.init()
pygame.display.set_caption("Tekino")

clock = pygame.time.Clock()
run = True
win = pygame.display.set_mode((1350,700))
size = width ,height = 1350,700
left, right, attack_1, attack_1_projectile, attack_2, attack_3, attack_4, crouch, busy = False, False, False, False, False, False, False, False, False
left_2, right_2, attack_1_2, attack_1_projectile_2, attack_2_2, attack_3_2, attack_4_2, crouch_2, busy_2 = False, False, False, False, False, False, False, False, False
x = 500
y = 240
x2 = 1000

x_projectile = x + 185
x_projectile2 = x2 - 185 
y_projectile = 395
x_change = 0
x2_change = 0
t_elapsed = 0

class projectile:
    def __init__(self):
        anim.repukken_projectile.loop = False
    def move(self,x_pos,y_pos):
        anim.repukken_projectile.play()
        anim.repukken_projectile.blit(win,(x_pos,y_pos))

class projectile2:
    def __init__(self):
        anim2.repukken_projectile.loop = False
        anim2.repukken_projectile.flip(True, False)
    def move(self,x_pos,y_pos):
        anim2.repukken_projectile.play()
        anim2.repukken_projectile.blit(win,(x_pos,y_pos))

class backround:
    z=0
    def __init__(self):
        anim.stage_idle.play()
    def idle(self):
        rel_z= self.z % anim.bckg[0]
        anim.stage_idle.blit(win,(rel_z - anim.bckg[0] ,0))
        # 1800-1350 = 450
        if (rel_z < size[0]+450):
            anim.stage_idle.blit(win,(rel_z-450,0))
        self.z-=1

class fighter:
    def __init__(self):
        anim.crouch.loop = False
        anim.walkLeft.play()
        anim.walkRight.play()
        anim.idle.play()
        anim.repukken.loop = False
        anim.cutter.loop = False
        anim.punch_1.loop = False
        anim.kick_1.loop = False
        
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
    def attack_kick_2(self,x_pos,y_pos):
        anim.kick_1.play()
        anim.kick_1.blit(win,(x_pos,y_pos))
    def attack_punch_1(self,x_pos,y_pos):
        anim.punch_1.play()
        anim.punch_1.blit(win,(x_pos,y_pos))

class fighter2:
    def __init__(self):
        anim2.crouch.flip(True,False)
        anim2.crouch.loop = False
        anim2.walkLeft.play()
        anim2.walkRight.play()
        anim2.idle.flip(True,False)
        anim2.idle.play()
        anim2.repukken.flip(True,False)
        anim2.repukken.loop = False
        anim2.cutter.flip(True,False)
        anim2.cutter.loop = False
        anim2.punch_1.flip(True,False)
        anim2.punch_1.loop = False
        anim2.kick_1.flip(True,False)
        anim2.kick_1.loop = False
        
    def walkLeft(self,x_pos,y_pos):
        anim2.walkLeft.blit(win,(x_pos,y_pos))
    def walkRight(self,x_pos,y_pos):
        anim2.walkRight.blit(win,(x_pos,y_pos))
    def idle(self,x_pos,y_pos):
        anim2.idle.blit(win,(x_pos,y_pos))
    def crouch(self,x_pos,y_pos):
        if anim2.crouch.currentFrameNum == 3:
            anim2.crouch.pause()
        else:
            anim2.crouch.play()
        anim2.crouch.blit(win,(x_pos,y_pos+50))
    def attack_projectile_1(self,x_pos,y_pos):
        anim2.repukken.play()
        anim2.repukken.blit(win,(x_pos,y_pos-100))
    def attack_kick_1(self,x_pos,y_pos):
        anim2.cutter.play()
        anim2.cutter.blit(win,(x_pos,y_pos-100))
    def attack_kick_2(self,x_pos,y_pos):
        anim2.kick_1.play()
        anim2.kick_1.blit(win,(x_pos,y_pos))
    def attack_punch_1(self,x_pos,y_pos):
        anim2.punch_1.play()
        anim2.punch_1.blit(win,(x_pos,y_pos))

senshi = fighter()
senshi2  = fighter2()
stage = backround()
projectile_ = projectile()
projectile_2 = projectile2()

def redrawGameWindow():
    global x_projectile, x_projectile2
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
    elif attack_4:
        senshi.attack_kick_2(x,y)  
    else:
        senshi.idle(x,y)

    if left_2:
        senshi2.walkLeft(x2,y)
    elif right_2:
        senshi2.walkRight(x2,y)
    elif crouch_2:
        senshi2.crouch(x2,y)
    elif attack_1_2: 
        senshi2.attack_projectile_1(x2,y) 
    elif attack_2_2:  
        senshi2.attack_kick_1(x2,y) 
    elif attack_3_2:
        senshi2.attack_punch_1(x2,y) 
    elif attack_4_2:
        senshi2.attack_kick_2(x2,y)  
    else:
        senshi2.idle(x2,y)

    if attack_1_projectile:
        projectile_.move(x_projectile, y_projectile)
        x_projectile += 15

    if attack_1_projectile_2:            
        projectile_2.move(x_projectile2, y_projectile)
        x_projectile2 -= 15

    pygame.display.update()

while run:

    clock.tick(29)
    
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
        if anim.kick_1.isFinished():
            anim.kick_1.elapsed = 0
            attack_4 = False
            busy = False
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
        elif keys[pygame.K_h] :
            x_change = 0
            attack_1 = True
            busy = True
        elif keys[pygame.K_j] :
            x_change = 0
            attack_3 = True
            busy = True
        elif keys[pygame.K_k] :
            x_change = 0
            attack_4 = True
            busy = True
        elif keys[pygame.K_l] :
            x_change = 0
            attack_2 = True
            busy = True
        else:
            x_change = 0
            right = False
            left = False
            crouch = False

    if  busy_2:
        x2_change = 0
        right_2 = False
        left_2 = False
        crouch_2 = False
        if anim2.repukken.isFinished():
            attack_1_2 = False
            anim2.repukken.elapsed = 0
        if anim2.repukken.currentFrameNum > 5:
            attack_1_projectile_2 =True
        if anim2.repukken_projectile.isFinished():
            attack_1_projectile_2 = False
            x2_projectile = x2 - 185
            anim2.repukken_projectile.elapsed = 0
            busy_2 = False
        if anim2.cutter.isFinished():
            anim2.cutter.elapsed = 0
            attack_2_2 = False
            busy_2 = False
        if anim2.punch_1.isFinished():
            anim2.punch_1.elapsed = 0
            attack_3_2 = False
            busy_2 = False
        if anim2.kick_1.isFinished():
            anim2.kick_1.elapsed = 0
            attack_4_2 = False
            busy_2 = False
    else:
        if keys[pygame.K_c] :
            x2_change = 10 
            left_2 = True
            right_2 = False
        elif keys[pygame.K_b] :
            x2_change = -10
            left_2 = False
            right_2 = True
        elif keys[pygame.K_v] :
            x2_change = 0
            left_2 = False
            right_2 = False
            crouch_2 = True
        elif keys[pygame.K_a] :
            x2_change = 0
            attack_1_2 = True
            busy_2 = True
        elif keys[pygame.K_s] :
            x2_change = 0
            attack_3_2 = True
            busy_2 = True
        elif keys[pygame.K_z] :
            x2_change = 0
            attack_4_2 = True
            busy_2 = True
        elif keys[pygame.K_x] :
            x2_change = 0
            attack_2_2 = True
            busy_2 = True
        else:
            x2_change = 0
            right_2 = False
            left_2 = False
            crouch_2 = False       

    x += x_change
    x2 -= x2_change
    if x_change:
        x_projectile = x + 185
    if x2_change:
        x_projectile2 = x2 - 185
    
    redrawGameWindow()

