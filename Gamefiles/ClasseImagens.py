# -*- coding: utf-8 -*-
"""
Created on Fri May  6 07:34:13 2016

@author: Hugo
"""
from tkinter import PhotoImage


player_front = PhotoImage(file=".//Imagens//Sprites//player_front.png")
player_right = PhotoImage(file=".//Imagens//Sprites//player_right.png")
player_left =  PhotoImage(file=".//Imagens//Sprites//player_left.png")
player_back =  PhotoImage(file=".//Imagens//Sprites//player_back.png")

player = [player_front, player_right, player_left, player_back]
        
enemy1_front = PhotoImage(file=".//Imagens//Sprites//enemy1_front.png")
enemy1_right = PhotoImage(file=".//Imagens//Sprites//enemy1_right.png")
enemy1_left = PhotoImage(file=".//Imagens//Sprites//enemy1_left.png")
enemy1_back = PhotoImage(file=".//Imagens//Sprites//enemy1_back.png")

enemy1 = [enemy1_front, enemy1_right, enemy1_left, enemy1_back]  

boss1_front = PhotoImage(file=".//Imagens//Sprites//boss1_front.png")
boss1_right = PhotoImage(file=".//Imagens//Sprites//boss1_right.png")
boss1_left = PhotoImage(file=".//Imagens//Sprites//boss1_left.png")
boss1_back = PhotoImage(file=".//Imagens//Sprites//boss1_back.png")

boss1 = [boss1_front,boss1_right,boss1_left,boss1_back]

boss2_front = PhotoImage(file=".//Imagens//Sprites//boss2_front.png")
boss2_right = PhotoImage(file=".//Imagens//Sprites//boss2_right.png")
boss2_left = PhotoImage(file=".//Imagens//Sprites//boss2_left.png")
boss2_back = PhotoImage(file=".//Imagens//Sprites//boss2_back.png")

boss2 = [boss2_front,boss2_right,boss2_left,boss2_back]

enemy2_front = PhotoImage(file=".//Imagens//Sprites//enemy2_front.png")
enemy2_right = PhotoImage(file=".//Imagens//Sprites//enemy2_right.png")
enemy2_left = PhotoImage(file=".//Imagens//Sprites//enemy2_left.png")
enemy2_back = PhotoImage(file=".//Imagens//Sprites//enemy2_back.png")

enemy2 = [enemy2_front, enemy2_right, enemy2_left, enemy2_back] 

enemy=[enemy1, boss1, enemy2, boss2]

wood = PhotoImage(file=".//Imagens//Tiles//wood.png")
log = PhotoImage(file=".//Imagens//Tiles//log.png")
grass = PhotoImage(file=".//Imagens//Tiles//grass.png")
dirt = PhotoImage(file=".//Imagens//Tiles//dirt.png")
sand = PhotoImage(file=".//Imagens//Tiles//sand.png")
stone = PhotoImage(file=".//Imagens//Tiles//stone.png")
snow = PhotoImage(file=".//Imagens//Tiles//snow.png")
final = PhotoImage(file=".//Imagens//Tiles//Final.png")

Tiles = [wood, log, grass, grass, dirt, sand, stone, snow, final]

rangedwood = PhotoImage(file=".//Imagens//Tiles//woodranged.png")
rangedlog = PhotoImage(file=".//Imagens//Tiles//logranged.png")
rangedgrass = PhotoImage(file=".//Imagens//Tiles//grassranged.png")
rangeddirt = PhotoImage(file=".//Imagens//Tiles//dirtranged.png")
rangedsand = PhotoImage(file=".//Imagens//Tiles//sandranged.png")
rangedstone = PhotoImage(file=".//Imagens//Tiles//stoneranged.png")
rangedsnow = PhotoImage(file=".//Imagens//Tiles//snowranged.png")
rangedfinal = PhotoImage(file=".//Imagens//Tiles//Finalranged.png")

rangedTiles = [rangedwood, rangedlog, rangedgrass, rangedgrass, rangeddirt, rangedsand, rangedstone, rangedsnow, rangedfinal]

woodsubranged = PhotoImage(file=".//Imagens//Tiles//woodsubranged.png")
logsubranged = PhotoImage(file=".//Imagens//Tiles//logsubranged.png")
grasssubranged = PhotoImage(file=".//Imagens//Tiles//grasssubranged.png")
dirtsubranged = PhotoImage(file=".//Imagens//Tiles//dirtsubranged.png")
sandsubranged = PhotoImage(file=".//Imagens//Tiles//sandsubranged.png")
stonesubranged = PhotoImage(file=".//Imagens//Tiles//stonesubranged.png")
snowsubranged = PhotoImage(file=".//Imagens//Tiles//snowsubranged.png")
finalsubranged = PhotoImage(file=".//Imagens//Tiles//Finalsubranged.png")

subrangedTiles = [woodsubranged, logsubranged, grasssubranged, grasssubranged, dirtsubranged, sandsubranged, stonesubranged, snowsubranged, finalsubranged]

Pistol = PhotoImage(file=".//Imagens//Sprites//revolver.png")
Shotgun = PhotoImage(file=".//Imagens//Sprites//shotgun.png")
Sniper = PhotoImage(file=".//Imagens//Sprites//sniper.png")

guns = [Pistol,Shotgun,Sniper]

background = PhotoImage(file=".//Imagens//Sprites//background.png")
background1 = PhotoImage(file=".//Imagens//Sprites//background1.png")
background2 = PhotoImage(file=".//Imagens//Sprites//background2.png")
background3 = PhotoImage(file=".//Imagens//Sprites//background3.png")
lore = PhotoImage(file=".//Imagens//Sprites//lore.png")

backgrounds = [ background , background1, background2 , background3,lore]
#backgroundimage = PhotoImage(file=PhotoImage(file=".//Imagens//Tiles//Finalsubranged.png"))

MusicOn = PhotoImage(file=".//Imagens//Menu//Music_On.png")
MusicOff = PhotoImage(file=".//Imagens//Menu//Music_Off.png")