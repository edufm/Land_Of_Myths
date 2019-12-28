# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:34:13 2016

@author: Hugo
"""
from tkinter import *

class Imagem:
    def __init__(self,ImagemFront,ImagemRight,ImagemLeft,ImagemBack):
        self.Imagem = Imagem
        self.ImagemDir= ImagemDir
        self.ImagemEsq = ImagemEsq
        self.ImagemCost = ImagemCost
        
enemy1_front = PhotoImage(file=".//Imagens//Sprites//enemy1_front.png")
enemy1_right = PhotoImage(file=".//Imagens//Sprites//enemy1_right.png")
enemy1_left = PhotoImage(file=".//Imagens//Sprites//enemy1_left.png")
enemy1_back = PhotoImage(file=".//Imagens//Sprites//enemy1_back.png")

enemy1 = (enemy1_front,enemy1_right,enemy1_left,enemy1_back)   

enemy2_front = PhotoImage(file=".//Imagens//Sprites//enemy2_front.png")
enemy2_right = PhotoImage(file=".//Imagens//Sprites//enemy2_right.png")
enemy2_left = PhotoImage(file=".//Imagens//Sprites//enemy2_left.png")
enemy2_back = PhotoImage(file=".//Imagens//Sprites//enemy2_back.png")

enemy2 = (enemy2_front,enemy2_right,enemy2_left,enemy2_back)   

