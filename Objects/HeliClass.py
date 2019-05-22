import pygame, math
from .ObjectTemplate import ObjectTemp
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
class Heli(ObjectTemp):
    radius = 25.0
    numHelis = 0
    maxVel = 5
    turnRate = 5.0
    acc = 1.0
    def __init__(self, x, y, heading, img):
        self.x = x
        self.y = y
        self.lonSpd = 1.0
        self.latSpd = 0.0
        self.heading = heading
        self.score = 0
        self.timer = 0
        self.health = 5 
        self.orj_img = img
        self.orj_img = pygame.transform.scale(self.orj_img, (50, 50))        
        self.img = self.orj_img # This will reference our rotated image.
        Heli.numHelis += 1

    def update(self):
        self.x += self.lonSpd * math.cos(math.radians(self.heading)) + self.latSpd * math.cos(math.radians(self.heading-90))
        if self.x < 10 or self.x > WINDOWWIDTH-10: 
            self.lonSpd = 0
            self.latSpd = 0
        self.y -= self.lonSpd * math.sin(math.radians(self.heading)) + self.latSpd * math.sin(math.radians(self.heading-90))
        if self.y < 10 or self.y > WINDOWHEIGHT-10:
            self.lonSpd = 0
            self.latSpd = 0
        self.lonSpd = self.lonSpd * 0.98
        self.latSpd = self.latSpd * 0.96
        if self.timer > 0: self.timer -= 1
    def draw(self, win):
        if self.health > 0:
            self.img = pygame.transform.rotate(self.orj_img, self.heading-90.0)
            win.blit(self.img, self.img.get_rect(center=(self.x,self.y)))
            pygame.draw.rect(win, (255,0,0), (self.x-self.radius, self.y - self.radius, 50, 3))
            pygame.draw.rect(win, (0,128,0), (self.x-self.radius, self.y - self.radius, 50 - (10 * (5 - self.health)), 3))
