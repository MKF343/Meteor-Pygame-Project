
import pygame,sys
import random
import time
pygame.init()
#screen initialization
screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()
pygame.display.set_caption('Meteor Evader')
#initialization for sounds
pygame.mixer.init()
spawn = pygame.mixer.Sound("spawn.mp3")
crash = pygame.mixer.Sound("crash.mp3")
#Font
font = pygame.font.Font(None, 36)
#time variables
starttime = 0
timesurvived = 0
longesttime = 0
#meteor variables
meteors = []
lastspawn = 0
meteorspawnrate = 5000
#rect for player
player = pygame.Rect(screenwidth//2 - 40//2,screenheight//2 - 40//2,40,40)
#method for meteors
def spawnmeteor():
    spawn.play()
    side = random.choice(['top', 'bottom', 'left', 'right'])

    if side == 'top':
        x = random.randint(0, screenwidth)
        y = 0
        dx = random.uniform(-2, 2)
        dy = random.uniform(1, 4)
    elif side == 'bottom':
        x = random.randint(0, screenwidth)
        y = screenheight
        dx = random.uniform(-2, 2)
        dy = random.uniform(-1, -4)
    elif side == 'left':
        x = 0
        y = random.randint(0, screenheight)
        dx = random.uniform(1, 4)
        dy = random.uniform(-2, 2)
    elif side == 'right':
        x = screenwidth
        y = random.randint(0, screenheight)
        dx = random.uniform(-1, -4)
        dy = random.uniform(-2, 2)

    size = random.randint(20, 60)
    meteor = pygame.Rect(x, y, size, size)
    return meteor, dx, dy
#method for resetting the game (Global variables)
def resetgame():
    global meteors, starttime, timesurvived, meteorspawnrate
    meteors.clear()
    player.x, player.y = screenwidth//2 - 40//2,screenheight//2 - 40//2
    starttime = pygame.time.get_ticks()
    timesurvived = 0
    meteorspawnrate = 5000

#reset to start
resetgame()
while True:
    keys = pygame.key.get_pressed()
    clock.tick(60)

    #drawing the player and filling the screen
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), player)

    #movement and boundaries
    if keys[pygame.K_w]:
        player.y -= 5
    if keys[pygame.K_s]:
        player.y +=5
    if keys[pygame.K_a]:
        player.x -=5
    if keys[pygame.K_d]:
        player.x +=5
    if keys[pygame.K_r]:
        player.x = screenwidth//2 - 40//2
        player.y = screenheight//2 - 40//2
    if player.x < 0:
        player.x = 0
    if player.y < 0:
        player.y = 0
    if player.x > 800 - 40:
        player.x = 800 - 40
    if player.y > 800 - 40:
        player.y = 800-40
    #timer and spawning meteors
    currenttime = pygame.time.get_ticks()
    timesurvived = (currenttime-starttime) // 1000
    if currenttime - lastspawn > meteorspawnrate:
        meteors.append(spawnmeteor())
        lastspawn = currenttime

    #difficulty spike or reduction
    if timesurvived > 0 and timesurvived % 10 == 0:
        meteorspawnrate = max(1000, meteorspawnrate-100)
    #spawning meteors with for loop because of list
    for meteor, dx, dy in meteors:
        pygame.draw.rect(screen, (255,0,0), meteor)

    for meteordata in meteors[:]:
        meteor, dx, dy = meteordata
        meteor.x += dx
        meteor.y += dy

        #Removes meteors in boundaries
        if meteor.right < 0 or meteor.left > screenwidth or meteor.bottom < 0 or meteor.top > screenheight:
            meteors.remove(meteordata)

        #Collision Check
        if player.colliderect(meteor):
            crash.play()
            if timesurvived > longesttime:
                longesttime = timesurvived
            time.sleep(1)  #short pause for break
            resetgame()

    timesurvived = font.render(f'Time: {timesurvived}s', False, (255,255,255))
    Recordtime = font.render(f'Longest Time: {longesttime}s', False, (255, 255, 255))
    screen.blit(timesurvived, (0,0))
    screen.blit(Recordtime, (0,40))
    #update screen
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()