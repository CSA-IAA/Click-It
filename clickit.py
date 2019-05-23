'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Click It!
Version 1.0
'''

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Click It!') #title


#set up the colors
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)

image_file = "superman.png"
image = pygame.image.load(image_file).convert()
start_rect = image.get_rect()
image_rect = start_rect
l=[0,100]
image_rect = start_rect.move(l)
autob = pygame.image.load('autobot.png')
decept = pygame.image.load('decepticon.png')
#chet = pygame.image.load('Cheetah3.png')
outfile = open('gamecords.txt','w')  # placed here incase click user clicks 'load' before 'save' cuz then file wouldn't exist

while True: # the main game loop
    DISPLAYSURF.fill(BLACK) #continusly makes background white
    event = pygame.event.poll()
    keyinput = pygame.key.get_pressed()

    soundObj = pygame.mixer.Sound('SHUTDOWN.wav') #imports the music on standby

    quitgame = pygame.Rect(30, 30, 100, 55)
    loadgame = pygame.Rect(200, 30, 100, 55)
    savegame = pygame.Rect(360, 30, 100, 55)

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
        soundObj.stop()
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1: #makes so only can click right button on mouse
            mouse_pos = list(event.pos)
            if(mouse_pos[1]>=100):
                if (mouse_pos[0] >= 395 and mouse_pos[1] >= 420):
                    mouse_pos[0] = 395
                    mouse_pos[1] = 420
                    image_rect = start_rect.move(mouse_pos)
                    soundObj.play()
                elif (mouse_pos[0] >= 395):
                    mouse_pos[0] = 395
                    image_rect = start_rect.move(mouse_pos)
                    soundObj.play()
                elif (mouse_pos[1] >= 420):
                    mouse_pos[1] = 420
                    image_rect = start_rect.move(mouse_pos)
                    soundObj.play()
                image_rect = start_rect.move(mouse_pos)
                soundObj.play()
            if quitgame.collidepoint(event.pos):
                pygame.quit()
                sys.exit()
                soundObj.stop()
            elif loadgame.collidepoint(event.pos):
                DISPLAYSURF.blit(autob, (190, 20))
                infile = open('gamecords.txt', 'r')
                for x in infile:
                    y=x.split(',')
                    a=int(y[0])
                    b=int(y[1])
                    mouse_pos1=[a,b]
                    if (mouse_pos1[0] >= 395 and mouse_pos[1] >= 420):
                        mouse_pos1[0] = 395
                        mouse_pos1[1] = 420
                        image_rect = start_rect.move(mouse_pos1)
                    elif (mouse_pos1[0] >= 395):
                        mouse_pos1[0] = 395
                        image_rect = start_rect.move(mouse_pos1)
                    elif (mouse_pos1[1] >= 420):
                        mouse_pos1[1] = 420
                        image_rect = start_rect.move(mouse_pos1)
                    image_rect = start_rect.move(mouse_pos1)
                infile.close()
            elif savegame.collidepoint(event.pos):
                DISPLAYSURF.blit(decept, (355, 50))
                outfile = open('gamecords.txt', 'w')
                gameimg=str(image_rect)
                gameimg=gameimg.strip('<rect(')
                gameimg =gameimg.strip(')>')
                gameimg =gameimg.split(',')
                outfile.write(gameimg[0]+', '+gameimg[1])
                outfile.close()

    pygame.draw.rect(DISPLAYSURF, GREEN, (quitgame))
    basicfont = pygame.font.SysFont(None, 26)  # 48 is font size, no font type
    text = basicfont.render('Quit', True, BLUE, GREEN)  # first set of parenthesis is the font color, second set is the background of the words
    DISPLAYSURF.blit(text, (59, 50))  # Where on the destination surface to render said font
    pygame.draw.rect(DISPLAYSURF, GREEN, (loadgame))
    basicfont = pygame.font.SysFont(None, 26)  # 48 is font size, no font type
    text = basicfont.render('Load', True, BLUE, GREEN)  # first set of parenthesis is the font color, second set is the background of the words
    DISPLAYSURF.blit(text, (230, 50))  # Where on the destination surface to render said font
    pygame.draw.rect(DISPLAYSURF, GREEN, (savegame))
    basicfont = pygame.font.SysFont(None, 26)  # 48 is font size, no font type
    text = basicfont.render('Save', True, BLUE, GREEN)  # first set of parenthesis is the font color, second set is the background of the words
    DISPLAYSURF.blit(text, (390, 50))  # Where on the destination surface to render said font
    DISPLAYSURF.blit(image, image_rect)
    pygame.display.update()
    fpsClock.tick(FPS)
