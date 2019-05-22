import pygame, math
import numpy as np
import sys

FPS = 20
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
import Objects.HeliClass as HC
import Objects.BulletClass as BC
# R G B
WHITE =     (255, 255, 255)
BLACK =     (0,   0,   0)
RED =       (255, 0,   0)
GREEN =     (0,   255, 0)
DARKGREEN = (0,   155, 0)
DARKGRAY =  (100,  100,  100)

pygame.init()
win = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption("Heli Fight")
music = pygame.mixer.music.load("Content/music.mp3")
bulletSound = pygame.mixer.Sound("Content/bullet.wav")
hitSound = pygame.mixer.Sound("Content/hit.wav")
heliBlack = pygame.image.load('Content/heliBlack.png')
heliBlack = pygame.transform.scale(heliBlack, (50, 50))
heliGreen = pygame.image.load('Content/heliGreen.png')
heliGreen = pygame.transform.scale(heliGreen, (50, 50))
heliRed = pygame.image.load('Content/heliRed.png')
heliRed = pygame.transform.scale(heliRed, (50, 50))

#bg = pygame.image.load('content/bg.jpg')

clock = pygame.time.Clock()

def redrawGameWindow():
    for y in range(5):
        for x in range(5):
            rect = pygame.Rect(x*(99+1), y*(99+1), 99, 99)
            pygame.draw.rect(win, DARKGRAY, rect)        
    #win.fill(DARKGRAY)
    text = font.render('Score: ' + str(heli1.score), 1, (0,0,0))
    win.blit(text, (100, 2))
    heli1.draw(win)
    heli2.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    image = font.render('x axis: {:0.3f}'.format(joysticks[0].get_axis(0)), 1, (0,200,0))
    win.blit(image,(2,2))
    image = font.render('y axis: {:0.3f}'.format(joysticks[0].get_axis(1)), 1, (0,200,0))
    win.blit(image,(2,17))
    image = font.render('axis2: {:0.3f}'.format(joysticks[0].get_axis(2)), 1, (0,200,0))
    win.blit(image,(2,32))
    image = font.render('axis3: {:0.3f}'.format(joysticks[0].get_axis(3)), 1, (0,200,0))
    win.blit(image,(2,47))
    for i in range(joysticks[0].get_numbuttons()):
        if(joysticks[0].get_button(i)):
            image = font.render('{}: push'.format(i), 1, (0,20,0))
            win.blit(image,(20,20))
    pygame.display.update()
    
def checkCollisions():
    for bullet in bullets:
        if abs(bullet.x - heli2.x)**2 + abs(bullet.y - heli2.y)**2 < HC.Heli.radius**2 and heli2.health > 0:
            hitSound.play()
            heli2.health -= 1
            heli1.score += 1
            bullets.pop(bullets.index(bullet))
        if bullet.x > 500 or bullet.x < 0 or bullet.y > 500 or bullet.y < 0:
            bullets.pop(bullets.index(bullet))

def executeInputs(keys):    
    pitch = -joysticks[0].get_axis(1)
    if pitch > -0.1 and pitch < 0.1:
        pitch = 0.0        
    roll = joysticks[0].get_axis(0)
    if roll > -0.1 and roll < 0.1:
        roll = 0.0
    yaw = -joysticks[0].get_axis(2)
    if yaw > -0.2 and yaw < 0.2:
        yaw = 0.0
    heli1.lonSpd += pitch
    heli1.latSpd += roll
    if heli1.lonSpd > heli1.maxVel: heli1.lonSpd = heli1.maxVel
    elif heli1.lonSpd < -heli1.maxVel: heli1.lonSpd = -heli1.maxVel
    if heli1.latSpd > heli1.maxVel: heli1.latSpd = heli1.maxVel
    elif heli1.latSpd < -heli1.maxVel: heli1.latSpd = -heli1.maxVel
    heli1.heading += yaw * 5    
    if joysticks[0].get_button(0) and len(bullets) < 3 and heli1.timer == 0:
        bulletSound.play()
        bullets.append(BC.Bullet(heli1.x, heli1.y, heli1.heading))
        heli1.timer = 10

#mainloop
pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping
font = pygame.font.SysFont('comicsans', 20, True)
heli1 = HC.Heli(190.0, 100.0, -90.0, heliRed)
heli2 = HC.Heli(350, 350, 135, heliGreen)
bullets = []
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joy in joysticks:
    joy.init()
run = True
while run:
    #start = pygame.time.get_ticks()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    executeInputs(keys)
    
    for bullet in bullets:
        bullet.update()
        
    heli1.update()
    checkCollisions()
    redrawGameWindow()


                
    #fps = 1000. / (pygame.time.get_ticks() - start)
    #print(fps)
pygame.quit()
