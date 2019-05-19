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
music = pygame.mixer.music.load("content/music.mp3")
bulletSound = pygame.mixer.Sound("content/bullet.wav")
hitSound = pygame.mixer.Sound("content/hit.wav")
heliBlack = pygame.image.load('content/heliBlack.png')
heliBlack = pygame.transform.scale(heliBlack, (50, 50))
heliGreen = pygame.image.load('content/heliGreen.png')
heliGreen = pygame.transform.scale(heliGreen, (50, 50))
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
    def __init__(self, x, y, heading, img):
        self.x = x
        self.y = y
        self.vel = 5.0
        self.heading = heading
        self.score = 0
        self.timer = 0
        self.health = 5 
        self.orj_img = img
        self.orj_img = pygame.transform.scale(self.orj_img, (50, 50))        
        self.img = self.orj_img # This will reference our rotated image.
        Heli.numHelis += 1

    def update(self):
        self.x += self.vel * math.cos(math.radians(self.heading))
        self.y -= self.vel * math.sin(math.radians(self.heading))
        if self.timer > 0: self.timer -= 1
    def draw(self, win):
        if self.health > 0:
            self.img = pygame.transform.rotate(self.orj_img, self.heading-90.0)
            win.blit(self.img, self.img.get_rect(center=(self.x,self.y)))
            pygame.draw.rect(win, (255,0,0), (self.x-self.radius, self.y - self.radius, 50, 5))
            pygame.draw.rect(win, (0,128,0), (self.x-self.radius, self.y - self.radius, 50 - (5 * (10 - self.health)), 5))
        
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
        if bullet.x > 500 or bullet.x < 0 or bullet.y > 500 or bullet.y < 0:
            bullets.pop(bullets.index(bullet))
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
    heli2.draw(win)
    for bullet in bullets:
        bullet.draw(win)    
    pygame.display.update()
    
def checkCollisions():
    for bullet in bullets:
        if abs(bullet.x - heli2.x)**2 + abs(bullet.y - heli2.y)**2 < Heli.radius**2 and heli2.health > 0:
            hitSound.play()
            heli2.health -= 1
            heli1.score += 1
            bullets.pop(bullets.index(bullet))

def executeInputs(keys):
    if keys[pygame.K_LEFT]:
        heli1.heading += Heli.turnRate
    elif keys[pygame.K_RIGHT] and heli1.x < WINDOWWIDTH - heli1.radius- heli1.vel:
        heli1.heading -= Heli.turnRate
    if keys[pygame.K_UP] and  heli1.vel < Heli.maxVel:
        heli1.vel += Heli.acc
    elif keys[pygame.K_DOWN] and  heli1.vel > -Heli.maxVel:
        heli1.vel -= Heli.acc
    if keys[pygame.K_SPACE] and len(bullets) < 3 and heli1.timer == 0:
        bulletSound.play()
        bullets.append(Bullet(heli1.x, heli1.y, heli1.heading))
        heli1.timer = 10        

#mainloop
pygame.mixer.music.play(-1) # -1 will ensure the song keeps looping
font = pygame.font.SysFont('comicsans', 30, True)
heli1 = Heli(50.0, 0.0, -90.0, heliBlack)
heli2 = Heli(350, 350, 135, heliGreen)
bullets = []
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
