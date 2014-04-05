

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
import inputbox
import client
import traceback

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#seperate this into an object class
class Animation(pygame.sprite.Sprite):
    def __init__(self,path, number_of_frames, coordinates, infinite_loop):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        self.path = path
        self.number_of_frames = number_of_frames
        self.coordinates = coordinates
        self.infinite_loop = infinite_loop
        self.frames = util.get_frames(self.path, self.number_of_frames)
        self.current_frame = 0
        self.image, self.rect = self.frames[self.current_frame][0], self.frames[self.current_frame][1]
        #self.rect.midtop = self.coordinates
        self.rect = self.rect.move(self.coordinates)
        self.complete = False
        
    def update(self):
        #print("current frame is:  " + str(self.current_frame))
        if self.infinite_loop and self.current_frame + 1 == len(self.frames):
            self.current_frame = 0
        elif (not self.infinite_loop) and self.current_frame + 1 == len(self.frames):
            self.complete = True
            return
        self.current_frame = self.current_frame + 1
        self.image, self.rect = self.frames[self.current_frame][0], self.frames[self.current_frame][1]
        #self.rect.midtop = self.coordinates
        self.rect = self.rect.move(self.coordinates)

    def restart(self):
        self.current_frame = 0
        self.complete = False


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
            #self.flash = Animation('animation/Flashes/flash_c/flash_c_', 6, pos, False)


    def click(self, target):
        "returns true if the hand collides with the target"
        self.clicking = 1
        hitbox = self.rect.inflate(-5, -5)
        if hitbox.colliderect(target.rect):
            return True
    
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
        self.selected = 0

    def update(self):
        "update on click or unclick"
        if self.clicked or self.selected:
            self.image, self.rect = util.load_image(self.clicked_image_source, None)
            self.rect.midtop = self.location_coordinates
        else:
            self.image, self.rect = util.load_image(self.original_image_source, None)
            self.rect.midtop = self.location_coordinates

    def set_clicked(self):
        self.clicked = 1

    def set_unclicked(self):
        self.clicked = 0

    def set_selected(self):
        self.selected = 1

    def set_unselected(self):
        self.selected = 0

class MenuControl(object):
    def __init__(self):
        self.bools = {}
        self.make_all_false
        self.nextTurn

    def set_in_start_screen(self, boolean):
        self.make_all_false()
        self.bools["in_start_screen"] = boolean
        
    def set_in_main_menu(self, boolean):
        self.make_all_false()
        self.bools["in_main_menu"] = boolean
        
    def set_in_game(self, boolean):
        self.make_all_false()
        self.bools["in_game"] = boolean

    def set_in_enter_name(self, boolean):
        self.make_all_false()
        self.bools["in_enter_name"] = boolean

    def set_in_battle(self, boolean):
        self.make_all_false()
        self.bools["in_battle"] = boolean

    def nextTurn(self):
        self.play1MoveLocked = False;
        self.play2MoveLocked = False;

    def player1MoveLocked(self):
        self.play1MoveLocked = True;
        
    def player1MoveLocked(self):
        self.play2MoveLocked = True;

    def make_all_false(self):
        self.bools["in_start_screen"] = False
        self.bools["in_main_menu"] = False
        self.bools["in_game"] = False
        self.bools["in_enter_name"] = False
        self.bools["in_battle"] = False


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

    #for start screen
    mouse = Mouse()
    start_button = Button("start_button_original.jpg", "start_button_clicked.jpg", (background.get_width()/2, 12.5*background.get_height()/17))
    all_sprites = pygame.sprite.OrderedUpdates((start_button, mouse)) #order based on how they are added!
    clock = pygame.time.Clock()

    #for main menu
    battle_button = Button("battle_menu_button_original.jpg", "battle_menu_button_clicked.jpg", (background.get_width()/2,4.5*background.get_height()/17))
    options_button = Button("options_menu_button_original.jpg", "options_menu_button_clicked.jpg", (background.get_width()/2, 10.5*background.get_height()/17))
    #smoke = Animation('animation/smokes/smoke puff right/smoke_right_', 10, (-50,100))
    #flash = Animation('animation/Flashes/flash_c/flash_c_', 6, (600, 200))
    #cut = Animation('animation/cuts/cut_c/cut_c_', 5, (600, -25))
    gates_closed = Animation('animation/gates/gates_closed/gates_closed_', 13, (0, 0), False)
    gates_opened = Animation('animation/gates/gates_opened/gates_closed_', 13, (0, 0), False)

    player1_monster = Button("monsters/fire_dino2.png", "monsters/fire_dino2.png", (background.get_width()/5, 1*background.get_height()/17))
    player2_monster = Button("monsters/fire_dino2_flipped.png", "monsters/fire_dino2_flipped.png",  (4*background.get_width()/5, 1*background.get_height()/17))
    attack_button = Button("attack_button_original.jpg", "attack_button_clicked.jpg", (1.25*background.get_width()/5, 13*background.get_height()/17))
    switch_button = Button("switch_button_original.jpg", "switch_button_clicked.jpg", (3.75*background.get_width()/5, 13*background.get_height()/17))
    back_button = Button("back_button_original.jpg", "back_button_clicked.jpg", (.25*background.get_width()/5, 15*background.get_height()/17))
    move_locked = Button("move_locked_1.jpg", "move_locked_1.jpg", (2.5*background.get_width()/5, 8.75*background.get_height()/17))

    player1_attack_animation = Animation('animation/Flames/flamethrower_/flamethrower_', 10, (player1_monster.location_coordinates[0]+50,player1_monster.location_coordinates[1]-100), False)
    player2_attack_animation = Animation('animation/Flames/flamethrower_/flamethrower_', 10, (player1_monster.location_coordinates[0]+50,player1_monster.location_coordinates[1]-100), False)
    
    attack1_button = Button("attack_button_images/mud_bomb_original.jpg", "attack_button_images/mud_bomb_clicked.jpg", (1.5*background.get_width()/5, 11.5*background.get_height()/17))
    attack2_button = Button("attack_button_images/mud_bomb_original.jpg", "attack_button_images/mud_bomb_clicked.jpg", (3.5*background.get_width()/5, 11.5*background.get_height()/17))
    attack3_button = Button("attack_button_images/mud_bomb_original.jpg", "attack_button_images/mud_bomb_clicked.jpg", (1.5*background.get_width()/5, 14.5*background.get_height()/17))
    attack4_button = Button("attack_button_images/mud_bomb_original.jpg", "attack_button_images/mud_bomb_clicked.jpg", (3.5*background.get_width()/5, 14.5*background.get_height()/17))
    solid_button = Button("solid_state_button_unselected.jpg", "solid_state_button_selected.jpg", (4.6*background.get_width()/5, 10*background.get_height()/17))
    liquid_button = Button("liquid_state_button_unselected.jpg", "liquid_state_button_selected.jpg", (4.6*background.get_width()/5, 11.75*background.get_height()/17))
    gas_button = Button("gas_state_button_unselected.jpg", "gas_state_button_selected.jpg", (4.6*background.get_width()/5, 13.5*background.get_height()/17))
    plasma_button = Button("plasma_state_button_unselected.jpg", "plasma_state_button_selected.jpg", (4.6*background.get_width()/5, 15.25*background.get_height()/17))



    menu_control = MenuControl()
    menu_control.set_in_start_screen(True)
    login_name = ""
    login_control = False
    
    #game driver
    while 1:
        clock.tick(60)

        #button updates here
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                for but in all_sprites:
                    if isinstance(but, (Button)) and mouse.click(but):
                        but.set_clicked()
            elif event.type == MOUSEBUTTONUP:
                mouse.unclick()
                if menu_control.bools["in_start_screen"] and start_button.clicked:
                    #enter main manu
                    start_button.set_unclicked()
                    all_sprites.empty()
                    #update again for login section
                    all_sprites.update()
                    screen.blit(background, (0, 0))
                    all_sprites.draw(screen)
                    pygame.display.flip() 
                    menu_control.set_in_enter_name(True)
                    login_name = inputbox.ask(screen, "Login:  ")
                    print ("login name is:  " + login_name)
                elif menu_control.bools["in_start_screen"]:
                    start_button.set_unclicked()

                if (menu_control.bools["in_enter_name"]) and (login_name != ""):
                    all_sprites.add(gates_closed)
                    menu_control.set_in_main_menu(True)
                    start_button.set_unclicked()
                    all_sprites.empty()
                    all_sprites.add(battle_button, options_button, mouse)
                    all_sprites.add(gates_closed)
                    try:
                        print "Attempting to create client....."
                        client.createClient(login_name)
                    except Exception:
                        traceback.print_exc() 
                        pass
                    
                if menu_control.bools["in_main_menu"] and battle_button.clicked:
                    #battle music!
                    pygame.mixer.music.load("music/Fated Encounter.mp3")
                    pygame.mixer.music.play(-1)

                    #update background
                    background = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
                    background = background.convert()
                    screen.blit(background, (0, 0))
                    pygame.display.flip()
    
                    all_sprites.empty()
                    all_sprites.add(player1_monster, player2_monster, attack_button, switch_button, mouse)
                    all_sprites.add(gates_closed)
                    gates_closed.restart()
                    gates_opened.restart()
                    battle_button.set_unclicked()
                    menu_control.set_in_battle(True)
                if menu_control.bools["in_main_menu"] and options_button.clicked:
                    all_sprites.add(gates_closed)
                    gates_closed.restart()
                    gates_opened.restart()
                    options_button.set_unclicked()

                if menu_control.bools["in_battle"] and attack_button.clicked:
                    attack_button.set_unclicked()
                    all_sprites.remove(attack_button, switch_button, mouse)
                    #update attack buttons from monster
                    #only add states that the monster can be
                    solid_button.set_clicked()
                    liquid_button.set_unclicked()
                    gas_button.set_unclicked()
                    plasma_button.set_unclicked()
                    all_sprites.add(attack1_button, attack2_button, attack3_button, attack4_button, solid_button, liquid_button, gas_button, plasma_button, back_button, mouse)
                if menu_control.bools["in_battle"] and switch_button.clicked:
                    switch_button.set_unclicked()
                    all_sprites.remove(attack_button, switch_button, mouse)
                    all_sprites.add(back_button, mouse)
                if menu_control.bools["in_battle"] and back_button.clicked:
                    back_button.set_unclicked()
                    all_sprites.remove(attack1_button, attack2_button, attack3_button, attack4_button, solid_button, liquid_button, gas_button, plasma_button,  back_button, mouse)
                    all_sprites.add(attack_button, switch_button, mouse)


                    
                if menu_control.bools["in_battle"] and (attack1_button.clicked or attack2_button.clicked or attack3_button.clicked or attack4_button.clicked):
                    if attack1_button.clicked:
                        player1_attack_animation = Animation('animation/Flames/flamethrower_/flamethrower_', 10, (player1_monster.location_coordinates[0]+50,player1_monster.location_coordinates[1]-100), False)
                        attack1_button.set_unclicked()
                    if attack2_button.clicked:
                        attack2_button.set_unclicked()
                    if attack3_button.clicked:
                        attack3_button.set_unclicked()
                    if attack4_button.clicked:
                        attack4_button.set_unclicked()
                    all_sprites.remove(attack_button, switch_button, back_button, attack1_button, attack2_button, attack3_button, attack4_button, solid_button, liquid_button, gas_button, plasma_button,  back_button, mouse)
                    #all_sprites.add(player1_attack_animation, mouse)
                    all_sprites.add(move_locked, mouse)
                    #TODO:  Create packet to send to server on this player's moves.
                if menu_control.bools["in_battle"] and solid_button.clicked:
                    solid_button.set_selected()
                    liquid_button.set_unselected()
                    gas_button.set_unselected()
                    plasma_button.set_unselected()
                    solid_button.set_unclicked()
                    liquid_button.set_unclicked()
                    gas_button.set_unclicked()
                    plasma_button.set_unclicked()
                if menu_control.bools["in_battle"] and liquid_button.clicked:
                    solid_button.set_unselected()
                    liquid_button.set_selected()
                    gas_button.set_unselected()
                    plasma_button.set_unselected()
                    solid_button.set_unclicked()
                    liquid_button.set_unclicked()
                    gas_button.set_unclicked()
                    plasma_button.set_unclicked()
                if menu_control.bools["in_battle"] and gas_button.clicked:
                    solid_button.set_unselected()
                    liquid_button.set_unselected()
                    gas_button.set_selected()
                    plasma_button.set_unselected()
                    solid_button.set_unclicked()
                    liquid_button.set_unclicked()
                    gas_button.set_unclicked()
                    plasma_button.set_unclicked()
                if menu_control.bools["in_battle"] and plasma_button.clicked:
                    solid_button.set_unselected()
                    liquid_button.set_unselected()
                    gas_button.set_unselected()
                    plasma_button.set_selected()
                    solid_button.set_unclicked()
                    liquid_button.set_unclicked()
                    gas_button.set_unclicked()
                    plasma_button.set_unclicked()
                    
        #do animation updates here.  
        if gates_closed.complete:
            all_sprites.remove(gates_closed)
            all_sprites.add(gates_opened)
        if gates_opened.complete:
            all_sprites.remove(gates_opened)
        if menu_control.bools["in_battle"] and player1_attack_animation.complete:
            all_sprites.remove(player1_attack_animation)
        if menu_control.bools["in_battle"] and player2_attack_animation.complete:
            all_sprites.remove(player2_attack_animation)




        #TODO:

        #packet = get packet from server
        #packet types:
        #   calculated moves packet
        #   oppenent quit packet (no response)
        #   oppenent ready packet (optional...may not be needed)
    
        #if menu_control.bools["in_battle"] and (recieves "calculated moves packet" from server):
        #   if this player made move:
        #       play animations based on sent stats (move animations, hp changes, or switched monsters)
        #       if this player lost all monsters and oppenent lost all monsters:
        #           tie game!
        #       elif this player lost all monsters:
        #           oppenent wins!
        #       elif opponent lost all monsters:
        #           you win!
        #   elif this player has not made a move:
        #       ignore until player makes move
        #       maybe set timer? future idea

        #
        #if oppenent quits ("oppenent quit packet" from other server via no response from other client):
        #   you win!

        all_sprites.update()

        #redraw everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

if __name__ == '__main__': main()
