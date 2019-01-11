from pyautogui import press
from time import sleep
from PIL import ImageGrab
def detectObstacle():
    zone = ImageGrab.grab([400,460,450,490]) # a bit of space in front of the dino
    a=zone.getcolors() #get a value
    if a[0][0] != 1500: # if its not always white
        press("space") #press space
while True:
    sleep(1/30) # fps
    detectObstacle()