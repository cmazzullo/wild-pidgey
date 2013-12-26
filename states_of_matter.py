

"""
Mohamamd Hassan Salim & Christopher Mazzullo
Personal Project
States of Matter
Last Edited:  12/25/2013


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

    #image = pygame.Surface((image.get_rect().width,image.get_rect().height) , pygame.SRCALPHA, 32)
    #image = image.set_colorkey(TRANSPARENT)
    if image.get_alpha():
        image = image.convert_alpha()
    else:
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


#seperate into an animation utility class
def get_frames(path,number_of_frames):
    """
    creates animation frames
    """

    if not pygame.display.get_init ():
        raise Exception ("pygame.display.get_init() returned False.")

    pygame.mixer.init(frequency=44100, size=16, channels=2)

    frames = []
    for i in range(1,number_of_frames):
        frames.append(load_image(path+str(i)+".png"))
        #print("appending frame number " + str(i))
    return frames


class Animation(pygame.sprite.Sprite):
    def __init__(self,path, number_of_frames, coordinates):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.path = path
        self.number_of_frames = number_of_frames
        self.coordinates = coordinates
        self.frames = get_frames(self.path, self.number_of_frames)
        self.current_frame = 0
        self.image, self.rect = self.frames[self.current_frame][0], self.frames[self.current_frame][1]
        #self.rect.midtop = self.coordinates
        self.rect = self.rect.move(self.coordinates)
        
    def update(self):
        #print("current frame is:  " + str(self.current_frame))
        if self.current_frame + 1 == len(self.frames):
            self.current_frame = 0
        else:
            self.current_frame = self.current_frame + 1
        self.image, self.rect = self.frames[self.current_frame][0], self.frames[self.current_frame][1]
        #self.rect.midtop = self.coordinates
        self.rect = self.rect.move(self.coordinates)


#seperate this into an object class
class Mouse(pygame.sprite.Sprite):
    """moves a hand on the screen, following the computer mouse"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.clicking = 0
        #self.image, self.rect = load_image('game_mouse.jpg', -1)
        self.image, self.rect = load_image('cursor.png',-1)
        #self.whiff_sound = load_sound('high_tone_sword.wav')
        
    def update(self):
        "move the hand based on the computer mouse position"
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.clicking:
            pygame.mixer.Sound("data/high_tone_sword.wav").play()
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

    #initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('States of Matter')
    pygame.mouse.set_visible(0)

    #music!!!
    pygame.mixer.music.load("music/Glorious Morning 2.mp3")
    pygame.mixer.music.play(-1)

    background = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    background = background.convert()
    background.fill((250, 250, 250))
    
    elements_background = load_image("4-elements-background.jpg")
    
    
    if pygame.font:
        font = pygame.font.Font(None, 180)
        font.set_italic(True)
        text = font.render("States of Matter", 1, (20, 125, 120))
        textpos = text.get_rect(centerx=elements_background[0].get_width()/2, centery=elements_background[0].get_height()/4)
        elements_background[0].blit(text, textpos)


    background.blit(elements_background[0],(-450, -200))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    
    start_button = Button("start_button_original.jpg", "start_button_clicked.jpg", (background.get_width()/2, 12.5*background.get_height()/17))
    flamethrower = Animation('animation/Flames/flamethrower_/flamethrower_', 29, (-50,0))
    bolt_tsela = Animation('animation/voltage_0/bolt_tesla/bolt_tesla_', 10, (600, 200))
    mouse = Mouse()
    all_sprites = pygame.sprite.RenderPlain((start_button, flamethrower, bolt_tsela, mouse))
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
                    #all_sprites.remove(start_button)
                    #all_sprites = pygame.sprite.RenderPlain((mouse, clicked_start_button))
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
