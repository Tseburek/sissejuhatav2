#projektis peab olema pildid nimedega "background" ning "youwin"

import pygame
import time
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine")
screen.fill([204, 255, 204])

#lisame teksti
font = pygame.font.Font(pygame.font.match_font('arial'), 50)
font.set_underline(True)
text = font.render("Hello PyGame", True, [0,0,0])

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [320-text_width/2,240-text_height/2])

pygame.display.flip()

time.sleep (1.5)

#Lisame pildid
bg = pygame.image.load("background.jpg")
screen.blit(bg,[0,0])
pygame.display.flip()
youWin = pygame.image.load("youwin.png")
youWin = pygame.transform.scale(youWin, [300, 120])
screen.blit(youWin,[180,100])
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
