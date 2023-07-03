from os.path import join
import numpy as np
from PIL import ImageGrab
from move_char import *
import keyboard
import pickle as cp
import time


"""
up -> 38 -> 0x26
down -> 40 -> 0x28
left -> 37 -> 0x25
right -> 39 -> 0x27
X (A in emu) -> 88 -> 0x58 
"""
if __name__ == "__main__":
    data = {'url':[], 'key':[]}
    i = 0

    while(True):
                
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'q' or event.name == 'Q':
                break
            img = ImageGrab.grab(bbox=(0,40,800,640))
            img.save(join('Screens', f'{i}.jpg'))
            data['url'].append(join('Screens', f'{i}.jpg'))
            data['key'].append(event.name)
            i+=1
        time.sleep(0.5)
    with open(f'data{i-1}.pkl', 'wb+') as fw:
        cp.dump(data, fw)