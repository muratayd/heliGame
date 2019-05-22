import pygame, math
from .ObjectTemplate import ObjectTemp
bulletImg = pygame.image.load('Content/bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (25, 25))
class Bullet(ObjectTemp):
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
