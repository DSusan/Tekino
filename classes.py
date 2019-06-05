import pygame
import pyganim
import anim
import anim2
from pygame_functions import *
from time import sleep

pygame.init()


size = width ,height = 1350,700
win = pygame.display.set_mode(size)
health_f1 = 350
health_f2 = 350
health_before = 350
health_before2 = 350
GameOver = False

pygame.display.set_caption("Tekino")
clock = pygame.time.Clock()
run = True

size = width ,height = 1350,700
left, right, attack_1, attack_1_projectile, attack_2, attack_3, attack_4, crouch, is_hit, busy = False, False, False, False, False, False, False, False, False, False
left_2, right_2, attack_1_2, attack_1_projectile_2, attack_2_2, attack_3_2, attack_4_2, crouch_2, is_hit_2, busy_2 = False, False, False, False, False, False, False, False, False, False
playerPosX = 500
playerPosY = 240
playerPosX2 = 1000
char_radius = 125
stagePosX = 0 
startscrollingPosX = size[0]/2

x_projectile = playerPosX + 185
x_projectile2 = playerPosX2 - 185 
y_projectile = 395
x_change = 0
x2_change = 0
t_elapsed = 0

font = pygame.font.Font('freesansbold.ttf', 90) 
text = font.render('PLAYER 1 WINS', True, (255,0,0,))
text2 = font.render('PLAYER 2 WINS', True, (255,0,0,))
textRect = text.get_rect()
textRect.center = (size[0] // 2, size[1] // 2)


largeText = pygame.font.Font('freesansbold.ttf',120)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

rugal_pos = pygame.image.load("rugal_pos.png")
rugal_pos = pygame.transform.scale(rugal_pos,(600,458))

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


    # def idle(self):
    #     rel_z= self.z % anim.bckg[0]
    #     anim.stage_idle.blit(win,(rel_z - anim.bckg[0] ,0))
    #     # 1800-1350 = 450
    #     if (rel_z < size[0]+450):
    #         anim.stage_idle.blit(win,(rel_z-450,0))
    #     self.z-=1

class fighter:
    def __init__(self):
        anim.crouch.loop = False
        anim.repukken.loop = False
        anim.cutter.loop = False
        anim.punch_1.loop = False
        anim.kick_1.loop = False
        anim.hit.loop = False
        
    def walkLeft(self,x_pos,y_pos):
        anim.walkLeft.play()
        anim.walkLeft.blit(win,(x_pos,y_pos))
    def walkRight(self,x_pos,y_pos):
        anim.walkRight.play()
        anim.walkRight.blit(win,(x_pos,y_pos))
    def idle(self,x_pos,y_pos):
        anim.idle.play()
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
    def hit(self, x_pos, y_pos):
        anim.hit.play()
        anim.hit.blit(win,(x_pos,y_pos))

class fighter2:
    def __init__(self):
        anim2.crouch.flip(True,False)
        anim2.crouch.loop = False
        anim2.idle.flip(True,False)
        anim2.repukken.flip(True,False)
        anim2.repukken.loop = False
        anim2.cutter.flip(True,False)
        anim2.cutter.loop = False
        anim2.punch_1.flip(True,False)
        anim2.punch_1.loop = False
        anim2.kick_1.flip(True,False)
        anim2.kick_1.loop = False
        anim2.hit.flip(True,False)
        anim2.hit.loop = False
        
    def walkLeft(self,x_pos,y_pos):
        anim2.walkLeft.play()
        anim2.walkLeft.blit(win,(x_pos,y_pos))
    def walkRight(self,x_pos,y_pos):
        anim2.walkRight.play()
        anim2.walkRight.blit(win,(x_pos,y_pos))
    def idle(self,x_pos,y_pos):
        anim2.idle.play()
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
    def hit(self, x_pos, y_pos):
        anim2.hit.play()
        anim2.hit.blit(win,(x_pos,y_pos))

def colorize(image, newColor):
    """
    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
    original).
    :param image: Surface to create a colorized copy of
    :param newColor: RGB color to use (original alpha values are preserved)
    :return: New colorized Surface instance
    """
    image = image.copy()

    # zero out RGB values
    image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    # add in new RGB values
    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    return image
        