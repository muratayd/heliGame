import pygame, math
FPS = 20
WINDOWWIDTH = 500
WINDOWHEIGHT = 500

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

heliBlack = pygame.image.load('content/heliBlack.png')
heliBlack = pygame.transform.scale(heliBlack, (50, 50))
heliRed = pygame.image.load('content/heliRed.png')
heliRed = pygame.transform.scale(heliRed, (50, 50))
bulletImg = pygame.image.load('content/bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (5, 20))
#bg = pygame.image.load('content/bg.jpg')

clock = pygame.time.Clock()

class Heli(object):
    radius = 25.0
    numHelis = 0
    maxVel = 10.0
    turnRate = 5.0
    acc = 1.0
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.vel = 5.0
        self.heading = heading
        self.score = 0
        self.timer = 0
        self.orj_img = pygame.image.load('content/heliBlack.png')
        self.orj_img = pygame.transform.scale(self.orj_img, (50, 50))        
        self.img = self.orj_img # This will reference our rotated image.
        Heli.numHelis += 1

    def update(self):
        self.x += self.vel * math.cos(math.radians(self.heading))
        self.y -= self.vel * math.sin(math.radians(self.heading))
        if self.timer > 0: self.timer -= 1
    def draw(self, win):
        self.img = pygame.transform.rotate(self.orj_img, self.heading-90.0)
        win.blit(self.img, self.img.get_rect(center=(self.x,self.y)))
        
class Bullet(object):
    radius = 5.0
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.vel = 15.0
        self.heading = heading
    def update(self):
        #print('{} {}'.format(self.x, self.y))
        self.x += self.vel * math.cos(math.radians(self.heading))
        self.y -= self.vel * math.sin(math.radians(self.heading))
    def draw(self,win):
        self.img = pygame.transform.rotate(bulletImg, self.heading-90.0)
        win.blit(self.img, self.img.get_rect(center=(self.x,self.y)))

def redrawGameWindow():

    for y in range(10):
        for x in range(10):
            rect = pygame.Rect(x*(49+1), y*(49+1), 49, 49)
            pygame.draw.rect(win, DARKGRAY, rect)
        
    #win.fill(DARKGRAY)
    text = font.render('Score: ' + str(heli1.score), 1, (0,0,0))
    win.blit(text, (100, 10))
    heli1.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
heli1 = Heli(50.0, 0.0, -90.0)
#heli2 = Heli(50, 50)
bullets = []
run = True
while run:
    #start = pygame.time.get_ticks()
    clock.tick(FPS)    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x > 500 or bullet.x < 0 or bullet.y > 500 or bullet.y < 0:
            bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        heli1.heading += Heli.turnRate
    elif keys[pygame.K_RIGHT] and heli1.x < WINDOWWIDTH - heli1.radius- heli1.vel:
        heli1.heading -= Heli.turnRate
    if keys[pygame.K_UP] and  heli1.vel < Heli.maxVel:
        heli1.vel += Heli.acc
    elif keys[pygame.K_DOWN] and  heli1.vel > -Heli.maxVel:
        heli1.vel -= Heli.acc
    if keys[pygame.K_SPACE] and len(bullets) < 3 and heli1.timer == 0:
        bullets.append(Bullet(heli1.x, heli1.y, heli1.heading))
        heli1.timer = 10
    for bullet in bullets:
        bullet.update()
    heli1.update()
    redrawGameWindow()

    #fps = 1000. / (pygame.time.get_ticks() - start)
    #print(fps)
pygame.quit()
