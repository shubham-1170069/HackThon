# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:48:25 2018

@author: Tony
"""

# -*-   coding: utf-8 -*-
""" 
Crea ted on Sat Sep  1 16:16:58 2018

@auth or: Tony
"""
 
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from  numpy import *
class  Cordinates():
    replaybtn=(342,421)
    dinosaur=(170,425)
      
def restartGame():
    pyautogui.click(Cordinates.replaybtn)
    #pyautogui.keyDown('down')
     
def pressSpace():
    #pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    #time.sleep(0.01)
    #  print("jum p")
    pyautogui.keyUp('space')
    #pyautogui.keyDown('down')
      
def imageGrab():
    box=(Cordinates.dinosaur[0]+70,Cordinates.dinosaur[1]+5, #x1Inc
         Cordinates.dinosaur[0]+x2Inc,Cordinates.dinosaur[1]+y2Inc)
    image =ImageGrab.grab(box) 
    grayImage =ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    #print(a.sum())
    return(a.sum())  
    
    

startTime=time.time()
endTime=time.time()
x1Inc=70 
x2Inc=100 
y2Inc=31
restartGame()
while True:
    if (endTime-startTime%3950==0):
        #      x1Inc+=(round(5.5+0.1*(endTime-startTime)/100))
        x2Inc+=(round(6+0.2*(endTime-startTime)/100))
    if(imageGrab()>1027):  
         pressSpace()  
         #time.sleep(0.1)
    endTime=time.time() 
exit(0)  
#(170   ,442)
