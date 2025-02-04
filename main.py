import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 500
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

#definition des variables du jeu
ground_scroll = 0
scroll_speed = 4

#je veux générer mon background
bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')



class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'img/bird{num}.png')
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]


bird_group = pygame.sprite.Group()

flappy = Bird(180, int(screen_height / 2))

bird_group.add(flappy)



run = True

while run:


    clock.tick(fps)
    #dessiner le background
    screen.blit(bg, (0,-65))

    bird_group.draw(screen)

    if abs(ground_scroll) > 35:
        ground_scroll = 0

    #dessiner et scroll le ground_background
    screen.blit(ground_img , (ground_scroll, 650))
    ground_scroll -= scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.QUIT