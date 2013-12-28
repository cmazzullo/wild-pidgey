

"""
Mohamamd Hassan Salim & Christopher Mazzullo
Personal Project
States of Matter
Last Edited:  12/25/2013


"""

import pygame,os,sys,math
from pygame.locals import *
import random
import util


if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#seperate this into an object class
class Animation(pygame.sprite.Sprite):
    def __init__(self,path, number_of_frames, coordinates):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.path = path
        self.number_of_frames = number_of_frames
        self.coordinates = coordinates
        self.frames = util.get_frames(self.path, self.number_of_frames)
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
        self.image, self.rect = util.load_image('cursor.png',-1)
        
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
        self.image, self.rect = util.load_image(original_image_source, None)
        self.rect.midtop = location_coordinates

    def update(self):
        "update on click or unclick"
        if self.clicked:
            self.image, self.rect = util.load_image(self.clicked_image_source, None)
            self.rect.midtop = self.location_coordinates
        else:
            self.image, self.rect = util.load_image(self.original_image_source, None)
            self.rect.midtop = self.location_coordinates

    def set_clicked(self):
        self.clicked = 1

    def set_unclicked(self):
        self.clicked = 0


class MenuControl(object):
    def __init__(self):
        self.bools = {}
        self.bools["in_start_screen"] = False
        self.bools["in_main_menu"] = False
        self.bools["in_game"] = False

    def set_in_start_screen(self, boolean):
        self.make_all_false()
        self.bools["in_start_screen"] = boolean
        
    def set_in_main_menu(self, boolean):
        self.make_all_false()
        self.bools["in_main_menu"] = boolean
        
    def set_in_game(self, boolean):
        self.make_all_false()
        self.bools["in_game"] = boolean

    def make_all_false(self):
        for b in self.bools:
            b = False


def main():

    #initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('States of Matter')
    pygame.mouse.set_visible(0)

    #music!!!
    pygame.mixer.music.load("music/Glorious Morning 2.mp3")
    pygame.mixer.music.play(-1, 53.0)

    background = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    background = background.convert()
    background.fill((250, 250, 250))
    
    elements_background = util.load_image("4-elements-background.jpg")
    
    
    if pygame.font:
        font = pygame.font.Font(None, 180)
        font.set_italic(True)
        text = font.render("States of Matter", 1, (20, 125, 120))
        textpos = text.get_rect(centerx=elements_background[0].get_width()/2, centery=elements_background[0].get_height()/4)
        elements_background[0].blit(text, textpos)


    background.blit(elements_background[0],(-450, -200))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    flamethrower = Animation('animation/Flames/flamethrower_/flamethrower_', 29, (-50,0))
    bolt_tsela = Animation('animation/voltage_0/bolt_tesla/bolt_tesla_', 10, (600, 200))
    mouse = Mouse()
    start_button = Button("start_button_original.jpg", "start_button_clicked.jpg", (background.get_width()/2, 12.5*background.get_height()/17))
    #all_sprites = pygame.sprite.RenderPlain((flamethrower, bolt_tsela, mouse, start_button))   #arbitary order
    all_sprites = pygame.sprite.OrderedUpdates((flamethrower, bolt_tsela, start_button, mouse)) #order based on how they are added!
    clock = pygame.time.Clock()

    battle_button = Button("battle_menu_button_original.jpg", "battle_menu_button_clicked.jpg", (background.get_width()/2,4.5*background.get_height()/17))
    options_button = Button("options_menu_button_original.jpg", "options_menu_button_clicked.jpg", (background.get_width()/2, 10.5*background.get_height()/17))

    buttons = [start_button]

    menu_control = MenuControl()
    menu_control.set_in_start_screen(True)
    
    #game driver
    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for but in buttons:
                    if mouse.click(but):
                        but.set_clicked()
            elif event.type == MOUSEBUTTONUP:
                if menu_control.bools["in_start_screen"] and start_button.clicked:
                    #enter main manu
                    menu_control.set_in_main_menu(True)
                    mouse.unclick()
                    start_button.set_unclicked()
                    all_sprites.empty()
                    buttons = [battle_button, options_button]
                    all_sprites = pygame.sprite.OrderedUpdates((battle_button, options_button, mouse))
                elif menu_control.bools["in_start_screen"]:
                    mouse.unclick()
                    start_button.set_unclicked()
                if menu_control.bools["in_main_menu"] and battle_button.clicked:
                    mouse.unclick()
                    battle_button.set_unclicked()
                if menu_control.bools["in_main_menu"] and options_button.clicked:
                    mouse.unclick()
                    options_button.set_unclicked()

        all_sprites.update()

        #redraw everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
