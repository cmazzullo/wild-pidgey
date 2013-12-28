

"""
Mohamamd Hassan Salim & Christopher Mazzullo
Personal Project
States of Matter
Last Edited:  12/27/2013


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
    for i in range(1, number_of_frames + 1):
        frames.append(load_image(path+str(i)+".png"))
        #print("appending frame number " + str(i))
    return frames

