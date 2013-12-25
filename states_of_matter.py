

"""
Mohamamd Hassan Salim & Christopher Mazzullo
Personal Project
States of Matter
Last Edited:  12/25/2013

Useful sources:

http://www.pygame.org/docs/tut/chimp/ChimpLineByLine.html


Image sources:

http://www.we-impact.com/wp-content/uploads/2012/03/Four-Elements1.jpg

"""

import pygame,os,sys,math
from pygame.locals import *
import random

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#seperate this into a utility class
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


#seperate this into a utility class
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', wav
        raise SystemExit, message
    return sound

#seperate this into an object class
class Mouse(pygame.sprite.Sprite):
    """moves a hand on the screen, following the computer mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.clicking = 0
        self.image, self.rect = load_image('game_mouse.jpg', -1)
        
    def update(self):
        "move the hand based on the computer mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.clicking:
            self.rect.move_ip(5, 10)

    def click(self, target):
        "returns true if the hand collides with the target"
        if not self.clicking:
            self.clicking = 1
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unclick(self):
        self.clicking = 0


#seperate this into an object/menu class
class Button(pygame.sprite.Sprite):
    """Button class used for all menus.  Handles events"""
    def __init__(self, original_image_source, clicked_image_source, location_coordinates):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.original_image_source = original_image_source
        self.clicked_image_source = clicked_image_source
        self.location_coordinates = location_coordinates
        self.clicked = 0
        self.image, self.rect = load_image(original_image_source, -1)
        #screen = pygame.display.get_surface()
        #self.area = screen.get_rect()
        self.rect.midtop = location_coordinates

    def update(self):
        "update on click or unclick"
        if self.clicked:
            self.image, self.rect = load_image(self.clicked_image_source, -1)
            self.rect.midtop = self.location_coordinates
        else:
            self.image, self.rect = load_image(self.original_image_source, -1)
            self.rect.midtop = self.location_coordinates

    def set_clicked(self):
        self.clicked = 1

    def set_unclicked(self):
        self.clicked = 0

def main():

    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('States of Matter')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    
    #elements_background = load_image("4-elements-background.jpg")
    #background.blit(elements_background[0],(-450, -200))
    
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("States of Matter", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)


    screen.blit(background, (0, 0))
    pygame.display.flip()

    mouse = Mouse()
    start_button = Button("start_button_original.jpg", "start_button_clicked.jpg", (background.get_width()/2,background.get_height()/3))
    all_sprites = pygame.sprite.RenderPlain((mouse, start_button))
    clock = pygame.time.Clock()

    #game driver
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                if mouse.click(start_button):
                    start_button.set_clicked()
            elif event.type == MOUSEBUTTONUP:
                mouse.unclick()
                start_button.set_unclicked()

        all_sprites.update()

        #redraw everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
