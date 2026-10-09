import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense - Part 1")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

GREEN=(70,170,70)
BROWN=(150,100,60)
RED=(220,60,60)
WHITE=(255,255,255)
BLACK=(0,0,0)

path=[
    (0,350),
    (250,350),
    (250,150),
    (700,150),
    (700,500),
    (1200,500)
]

money=300
lives=20
wave=1

class Enemy:
    def __init__(self):
        self.x,self.y=path[0]
        self.point=1
        self.speed=2
        self.radius=15
        self.max_health=100
        self.health=100
        self.dead=False

    def update(self):
        global lives
        if self.point>=len(path):
            self.dead=True
            lives-=1
            return
        tx,ty=path[self.point]
        dx,dy=tx-self.x,ty-self.y
        dist=math.hypot(dx,dy)
        if dist<=self.speed:
            self.x,self.y=tx,ty
            self.point+=1
        else:
            self.x+=dx/dist*self.speed
            self.y+=dy/dist*self.speed

    def draw(self):
        pygame.draw.circle(screen,RED,(int(self.x),int(self.y)),self.radius)
        pygame.draw.rect(screen,(120,0,0),(self.x-15,self.y-28,30,5))
        pygame.draw.rect(screen,(0,255,0),(self.x-15,self.y-28,30*(self.health/self.max_health),5))

def draw_path():
    for i in range(len(path)-1):
        pygame.draw.line(screen,BROWN,path[i],path[i+1],70)

enemies=[]
spawn_timer=0
spawn_delay=90

running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    spawn_timer+=1
    if spawn_timer>=spawn_delay:
        spawn_timer=0
        enemies.append(Enemy())

    for e in enemies:
        e.update()
    enemies=[e for e in enemies if not e.dead]

    screen.fill(GREEN)
    draw_path()
    for e in enemies:
        e.draw()

    screen.blit(font.render(f"Money: ${money}",True,WHITE),(20,20))
    screen.blit(font.render(f"Lives: {lives}",True,WHITE),(20,50))
    screen.blit(font.render(f"Wave: {wave}",True,WHITE),(20,80))

    pygame.display.flip()

pygame.quit()

