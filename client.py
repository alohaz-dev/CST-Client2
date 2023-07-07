import pygame
from network import Network

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Client')

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys [pygame.K_UP]:
            self.y -= self.vel

        if keys [pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + ',' + str(tup[1])

def redrawScreen(screen, player, player2):
    screen.fill((0, 255, 255))
    player.draw(screen)
    player2.draw(screen)
    pygame.display.update()

def main():
    run = True
    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (255, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 255, 0))
    p2.update()
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]

        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawScreen(screen, p, p2)

main()