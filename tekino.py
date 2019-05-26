import pygame
import pyganim
import anim
import anim2
from pygame_functions import *
from classes import *

senshi = fighter()
senshi2  = fighter2()
stage = backround()
projectile_ = projectile()
projectile_2 = projectile2()

def redrawGameWindow():
    global busy, busy_2, x_projectile, x_projectile2, x, x2, health_f1, health_f2, is_hit, is_hit_2
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
        diff = x2 - x
        if diff<350:
            health_f2 -= 0.4
            diff = 0
            is_hit_2 = True  
    elif attack_3:
        senshi.attack_punch_1(x,y) 
        diff = x2 - x
        if diff<300:
            health_f2 -= 0.2
            diff = 0
            is_hit_2 = True 
    elif attack_4:
        senshi.attack_kick_2(x,y)
        diff = x2 - x
        if diff<350:
            health_f2 -= 0.3
            diff = 0
            is_hit_2 = True 
    elif is_hit:
        senshi.hit(x,y)
 
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
        diff = x2 - x
        if diff<350:
            health_f1 -= 0.4
            diff = 0
            is_hit = True  
    elif attack_3_2:
        senshi2.attack_punch_1(x2,y)
        diff = x2 - x
        if diff<300:
            health_f1 -= 0.2
            diff = 0
            is_hit = True 
    elif attack_4_2:
        senshi2.attack_kick_2(x2,y)
        diff = x2 - x
        if diff<350:
            health_f1 -= 0.3
            diff = 0
            is_hit = True 
    elif is_hit_2:
        senshi2.hit(x2,y) 
    else:
        senshi2.idle(x2,y)

    if attack_1_projectile:
        projectile_.move(x_projectile, y_projectile)
        x_projectile += 15
        diff = x2 - x_projectile
        if diff<50:
            health_f2 -= 0.25
            diff = 0
            is_hit_2 = True 

    if attack_1_projectile_2:            
        projectile_2.move(x_projectile2, y_projectile)
        x_projectile2 -= 15
        diff = x_projectile2 - x
        if diff<150:
            health_f1 -= 0.25
            diff = 0
            is_hit = True

    rugal_icon = pygame.image.load('rugal/rugal_9000-1.png')
    rugal_icon_2 = pygame.transform.flip(rugal_icon, True, False)

    win.blit(rugal_icon,(0,0))
    win. blit(rugal_icon_2,(1220,0))
    pygame.draw.rect(win, (255,0,0), (130,20,350,35))
    pygame.draw.rect(win, (255,0,0), (870,20,350,35))
    pygame.draw.rect(win, (0,255,0), (130,20,350-(5*(350-health_f1)),35))
    pygame.draw.rect(win, (0,255,0), (870,20,350-(5*(350-health_f2)),35))
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
            if event.key == pygame.K_v:
                crouch_2 = False
                anim2.crouch.elapsed = 0
            

    keys = pygame.key.get_pressed()

    if is_hit:
        anim.crouch.stop()
        anim.cutter.stop()
        attack_2 = False
        anim.punch_1.stop()
        attack_3 = False
        anim.kick_1.stop()
        attack_4 = False
        anim.repukken.stop()
        attack_1 = False
        x_change = 0
        right = False
        left = False
        anim.walkLeft.stop()
        anim.walkRight.stop()
        
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
            is_hit_2 = False
        if anim.cutter.isFinished():
            anim.cutter.elapsed = 0
            attack_2 = False
            busy = False
            is_hit_2 = False
        if anim.punch_1.isFinished():
            anim.punch_1.elapsed = 0
            attack_3 = False
            busy = False
            is_hit_2 = False
        if anim.kick_1.isFinished():
            anim.kick_1.elapsed = 0
            attack_4 = False
            busy = False
            is_hit_2 = False

    if not is_hit and not busy:
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

    if is_hit_2:
        anim2.crouch.stop()
        anim2.cutter.stop()
        attack_2_2 = False
        anim2.punch_1.stop()
        attack_3_2 = False
        anim2.kick_1.stop()
        attack_4_2 = False
        anim2.repukken.stop()
        attack_1_2 = False
        x2_change = 0
        right_2 = False
        left_2 = False
        anim2.walkLeft.stop()
        anim2.walkRight.stop()
        
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
            x_projectile2 = x2 - 185
            anim2.repukken_projectile.elapsed = 0
            busy_2 = False
            is_hit = False
        if anim2.cutter.isFinished():
            anim2.cutter.elapsed = 0
            attack_2_2 = False
            busy_2 = False
            is_hit = False
        if anim2.punch_1.isFinished():
            anim2.punch_1.elapsed = 0
            attack_3_2 = False
            busy_2 = False
            is_hit = False
        if anim2.kick_1.isFinished():
            anim2.kick_1.elapsed = 0
            attack_4_2 = False
            busy_2 = False
            is_hit = False
    if not is_hit_2 and not busy_2:
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

