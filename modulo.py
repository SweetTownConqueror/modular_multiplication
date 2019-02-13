# coding=utf-8
import sys, pygame, math
from pygame.locals import *
import time
import sys

# constants
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)

BGCOLOR = WHITE

WINDOWWIDTH = 640 # width of the program's window, in pixels
WINDOWHEIGHT = 480 # height in pixels
WIN_CENTERX = int(WINDOWWIDTH / 2)
WIN_CENTERY = int(WINDOWHEIGHT / 2)

FPS = 1
speed = 0.2
#####
if len(sys.argv) != 5:
    print "Erreur dans le nombre d'arguments passés au script. La commande s'exécute de la façon suivante: "
    print sys.argv[0]+" [modulo] [repetitions] [table_de_multiplication] [vitesse]. Ex : "
    print sys.argv[0]+" 100 1000 5 0.2"
    print "la commande suivante a été lancée : "
    print sys.argv[0]+" 100 1000 5 0.2"
    modulo=100
    repetitions=1000
    mult_table=5
    speed=0.2
else:
    modulo=int(sys.argv[1])
    repetitions=int(sys.argv[2])
    mult_table=int(sys.argv[3])
    speed = float(sys.argv[4])
unit_rad_angle=(2*math.pi)/modulo
list_coord = []
DIAM = 100
#on parcourt le cercle du modulo
tmp=0
for i in range(modulo):
    #on met les coordonnees correspondant a chaque point de langle qui touche le cercle dans une array
    x = WIN_CENTERX + math.cos(tmp) * DIAM
    y = WIN_CENTERY + math.sin(tmp) * DIAM
    list_coord.append((x, y))
    tmp = tmp + unit_rad_angle



# standard pygame setup code
pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Multiplications Modulaires')


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    angle = math.atan2(x1 - x2, y1 - y2) # get the angle in radians
    angle = angle * (180 / math.pi) # convert to degrees
    angle = (angle + 90) % 360 # adjust for a right-facing sprite
    return angle


counter = 0

i=0
# boucle pcp
while True:
    # event handling loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    # fill the screen to draw from a blank state
    DISPLAYSURF.fill(BGCOLOR)

    # cercle rouge
    pygame.draw.circle(DISPLAYSURF, RED, (WIN_CENTERX, WIN_CENTERY), 100, 4)

    FPSCLOCK.tick(FPS)
    for i in range(repetitions):
        #il faut tracer la droite du point list_coord[i] si i< len(list_coord)
        #list_coord[i%len(list_coord)] si i > len(list_coord[i])
        #au point de coordonnees list_coord[i* mult_table] si i* mult_table < len(list_coord)
        #au point de coordonnees  list_coord[(i* mult_table)%len(list_coord)] si i* mult_table > len(list_coord[i])
        coord_begin = [0,0]
        coord_end = [0,0]
        if i < len(list_coord):
            coord_begin = list_coord[i]
        else:
            coord_begin = list_coord[i%len(list_coord)]
        if i* mult_table < len(list_coord):
            coord_end = list_coord[i* mult_table]
        else:
            coord_end = list_coord[(i* mult_table)%len(list_coord)]
        tmp=[]
        tmp.append((coord_begin,coord_end))
        pygame.draw.line(DISPLAYSURF, BLACK, coord_begin, coord_end  )
        pygame.display.update()
        time.sleep(speed)