import pyganim
import pygame


stage_idle = pyganim.PygAnimation(
   [('imagenes/stage_0.gif', 200),
    ('imagenes/stage_1.gif', 200),
    ('imagenes/stage_2.gif', 200),
    ('imagenes/stage_3.gif', 200),
    ('imagenes/stage_4.gif', 200),
    ('imagenes/stage_5.gif', 200),
    ('imagenes/stage_6.gif', 200),
    ('imagenes/stage_7.gif', 200)])
#1060
repukken = pyganim.PygAnimation(
   [('rugal_scaled/rugal_1000-0.png', 125),
    ('rugal_scaled/rugal_1000-1.png', 100),
    ('rugal_scaled/rugal_1000-2.png', 100),
    ('rugal_scaled/rugal_1000-3.png', 100),
    ('rugal_scaled/rugal_1000-4.png', 100),
    ('rugal_scaled/rugal_1000-5.png', 90),
    ('rugal_scaled/rugal_1000-6.png', 80),
    ('rugal_scaled/rugal_1000-7.png', 70),
    ('rugal_scaled/rugal_1000-8.png', 65),
    ('rugal_scaled/rugal_1000-9.png', 60),
    ('rugal_scaled/rugal_1000-10.png', 70),
    ('rugal_scaled/rugal_1000-11.png', 100)])
#1490    
cutter = pyganim.PygAnimation(
   [('rugal_scaled/rugal_1250-0.png', 50),
    ('rugal_scaled/rugal_1250-1.png', 50),
    ('rugal_scaled/rugal_1250-2.png', 50),
    ('rugal_scaled/rugal_1250-3.png', 50),
    ('rugal_scaled/rugal_1250-4.png', 50),
    ('rugal_scaled/rugal_1250-5.png', 100),
    ('rugal_scaled/rugal_1250-6.png', 70),
    ('rugal_scaled/rugal_1250-7.png', 100),
    ('rugal_scaled/rugal_1250-8.png', 50),
    ('rugal_scaled/rugal_1250-9.png', 50),
    ('rugal_scaled/rugal_1250-10.png', 50),
    ('rugal_scaled/rugal_1250-11.png', 50),
    ('rugal_scaled/rugal_1250-12.png', 50),
    ('rugal_scaled/rugal_1250-13.png', 50),
    ('rugal_scaled/rugal_1250-14.png', 80),
    ('rugal_scaled/rugal_1250-15.png', 100),
    ('rugal_scaled/rugal_1250-17.png', 40),
    ('rugal_scaled/rugal_1250-18.png', 35),
    ('rugal_scaled/rugal_1250-19.png', 50),
    ('rugal_scaled/rugal_1250-20.png', 50),
    ('rugal_scaled/rugal_1250-21.png', 50),
    ('rugal_scaled/rugal_1250-22.png', 50),
    ('rugal_scaled/rugal_1250-23.png', 50),
    ('rugal_scaled/rugal_1250-24.png', 35),
    ('rugal_scaled/rugal_1250-25.png', 35),
    ('rugal_scaled/rugal_1250-26.png', 35),
    ('rugal_scaled/rugal_1250-27.png', 35),
    ('rugal_scaled/rugal_1250-28.png', 70),
    ('rugal_scaled/rugal_1250-29.png', 70),
    ('rugal_scaled/rugal_1250-30.png', 120),
    ('rugal_scaled/rugal_1250-31.png', 150)])

repukken_projectile = pyganim.PygAnimation(
   [('rugal/rugal_4140-0.png', 80),
    ('rugal/rugal_4140-1.png', 70),
    ('rugal/rugal_4140-2.png', 70),
    ('rugal/rugal_4140-3.png', 70),
    ('rugal/rugal_4140-0.png', 70),
    ('rugal/rugal_4140-1.png', 80),
    ('rugal/rugal_4140-2.png', 80),
    ('rugal/rugal_4140-3.png', 80),
    ('rugal/rugal_4140-0.png', 80),
    ('rugal/rugal_4140-1.png', 80),
    ('rugal/rugal_4140-6.png', 80),
    ('rugal/rugal_4140-7.png', 70),
    ('rugal/rugal_4140-8.png', 70),
    ('rugal/rugal_4140-9.png', 70),
    ('rugal/rugal_4140-10.png', 70),
    ('rugal/rugal_4140-11.png', 70)])

walkLeft = pyganim.PygAnimation(
   [('rugal/rugal_20-0.png', 200),
    ('rugal/rugal_20-1.png', 200),
    ('rugal/rugal_20-2.png', 200),
    ('rugal/rugal_20-3.png', 200),
    ('rugal/rugal_20-4.png', 200),
    ('rugal/rugal_20-5.png', 200),
    ('rugal/rugal_20-6.png', 200),
    ('rugal/rugal_20-7.png', 200)])

idle = pyganim.PygAnimation(
   [('rugal/rugal_0-0.png', 200),
    ('rugal/rugal_0-1.png', 200),
    ('rugal/rugal_0-2.png', 200),
    ('rugal/rugal_0-3.png', 200),
    ('rugal/rugal_0-4.png', 200),
    ('rugal/rugal_0-5.png', 200)])

walkRight = walkLeft
idle.scale((250,400))
walkLeft.scale((250,400))
repukken_projectile.scale((150,250))
stage_idle.scale((1350,700))
