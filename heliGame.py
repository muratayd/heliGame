import pygame
FPS = 20
WINDOWWIDTH = 1200
WINDOWHEIGHT = 800

# R G B
WHITE =     (255, 255, 255)
BLACK =     (0,   0,   0)
RED =       (255, 0,   0)
GREEN =     (0,   255, 0)
DARKGREEN = (0,   155, 0)
DARKGRAY =  (40,  40,  40)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

pygame.init()
win = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

pygame.display.set_caption("Heli Fight")

heliBlack = pygame.image.load('content/heliBlack.png')
heliBlack = pygame.transform.scale(heliBlack, (50, 50))
heliRed = pygame.image.load('content/heliRed.png')
heliRed = pygame.transform.scale(heliRed, (50, 50))
bg = pygame.image.load('content/bg.jpg')

clock = pygame.time.Clock()

class heli(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def draw(self, win):
        win.blit(heliRed, (self.x, self.y))

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + "10", 1, (0,0,0))
    win.blit(text, (390, 10))
    heli1.draw(win)
    #for bullet in bullets:
     #   bullet.draw(win)
    
    pygame.display.update()

#mainloop
font = pygame.font.SysFont('comicsans', 30, True)
heli1 = heli(200, 410, 64,64)
heli2 = heli(200, 410, 64,64)
bullets = []
run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and heli1.x > heli1.vel:
        heli1.x -= heli1.vel
    elif keys[pygame.K_RIGHT] and heli1.x < 500 - heli1.width - heli1.vel:
        heli1.x += heli1.vel       
            
    redrawGameWindow()

pygame.quit()