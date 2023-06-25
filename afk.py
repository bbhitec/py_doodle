##!/usr/bin/env python
'''
    @author [mst]
    @brief   simple mouse moves using pyautogui

    @version 2023.02
'''

import pyautogui as pag
import random
import time


################## DRIVER
def main():
    print ("[mst] afk app")
    while True:
        x = random.randint(600,700)
        y = random.randint(200,600)
        pag.moveTo(x,y,0.5)
        time.sleep(2)


if __name__ == ("__main__"):
    main()
