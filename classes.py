import pyganim
import pygame
import anim
import anim2
size = width ,height = 1350,700
win = pygame.display.set_mode((1350,700))

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