import pygame
import sys

pygame.init()

black = 0,0,0
green = 0,255,0
red = 255,0,0
blue = 0,0,255

button_width = 300
button_height = 80     

screen = pygame.display.set_mode((500, 800))
size = width, height = 500, 800 

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    # screen.blit(textSurf, textRect)
    if msg == "Play":
        image = pygame.image.load("play.png")
        image = pygame.transform.scale(image, (w, h))
        screen.blit(image, (x,y))
    elif msg == "Shop":
        image = pygame.image.load("shop.png")
        image = pygame.transform.scale(image, (w, h))
        screen.blit(image, (x,y))
    elif msg == "Quit":
        image = pygame.image.load("quit.png")
        image = pygame.transform.scale(image, (w, h))
        screen.blit(image, (x,y))
    elif msg == "Menu":
        image = pygame.image.load("menu.png")
        image = pygame.transform.scale(image, (w, h))
        screen.blit(image, (x,y))

def play():
    print("Play")
def shop():
    print("Shop")
def quit():
    pygame.quit()
    sys.exit()

