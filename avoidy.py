import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

# Character movement arrays

walkdown = [pygame.image.load('tile000.png').convert(), pygame.image.load('tile001.png').convert(), pygame.image.load('tile002.png').convert(), pygame.image.load('tile003.png').convert()]
walkleft = [pygame.image.load('tile004.png'), pygame.image.load('tile005.png'), pygame.image.load('tile006.png'), pygame.image.load('tile007.png')]
walkright= [pygame.image.load('tile008.png'), pygame.image.load('tile009.png'), pygame.image.load('tile010.png'), pygame.image.load('tile011.png')]
walkup   = [pygame.image.load('tile012.png'), pygame.image.load('tile013.png'), pygame.image.load('tile014.png'), pygame.image.load('tile015.png')]
still    = pygame.image.load('tile000.png').convert()
bg       = pygame.image.load('green.jpg')

# Character x and y
x = 50
y = 50
width = 32
height = 32
vel = 5
left = False
right = False
up = False
down = False
walkcount = 0
clock = pygame.time.Clock()


def redrawGameWindow():
    global walkcount
    window.blit(bg, (0,0))
    
    if walkcount + 1 >= 17:
        walkcount = 0

    if left:
        window.blit(walkleft[walkcount//4], (x,y))
        walkcount += 1
    elif right:
        window.blit(walkright[walkcount//4], (x,y))
        walkcount += 1
    elif up:
        window.blit(walkup[walkcount//4], (x,y))
        walkcount += 1
    elif down:
        window.blit(walkdown[walkcount//4], (x, y))
        walkcount += 1
    else:
        window.blit(still, (x,y))
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        up = False
        down = False
        

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        left = False
        right = True
        up = False
        down = False

    if keys[pygame.K_UP] and y > vel:
        y -= vel
        left = False
        right = False
        up = True
        down = False

    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
        left = False
        right = False
        up = False
        down = True

    redrawGameWindow()

pygame.quit()

