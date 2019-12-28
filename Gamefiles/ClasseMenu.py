# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:50:21 2016

@author: Hugo
"""
from tkinter import *

window = Tk()
window.title("Land of Myths")
window.configure(bg="black")
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(),window.winfo_screenheight()))

from ClasseMapa import Mapa
from ClasseImagens import *
from ClassSound import *

class Menu():
    def __init__(self, lista):
        self.lista = lista
        
        
    def Construir_menu():
            
            sound.menu_music()
            
            background = Label(window)           
            imagem = PhotoImage(file=".//Imagens//Sprites//background1.png")
            background.config(image = imagem )
            background.image = imagem
            background.grid(row=0,column = 0)
                                  
            menu = Menu([])
    
            Play = Button(window)
            Play.config(text="Play",font=("impact",20),bg = "white")
            Play.config(height = 2 , width = 15)
            Play.configure(command = lambda : Menu.clear_start(menu))
            Play.place(x=575, y= 270)
            
            Rank = Button(window)
            Rank.configure(text="Rank",font=("impact",20),bg = "white", command = lambda : FireBase.Construir_Rank_Menu())
            Rank.config(height = 2 , width = 15)
            Rank.place(x = 575 , y = 370)
            
            Lore = Button(window)
            Lore.config(text="Lore",font=("impact",20),bg = "white")
            Lore.config(height = 2 , width = 15)
            Lore.config(command = lambda: Menu.show_lore(menu))
            Lore.place(x=575, y= 470)
            
            
            Exit = Button(window)
            Exit.config(text="Exit",font=("impact",20),bg = "white")
            Exit.config(height = 2 , width = 15)
            Exit.config(command =lambda: Mapa.Exit(window))
            Exit.place(x=575, y= 570)
            
            Music = Button(window)
            Music.config(image = MusicOn)
            Music.image = MusicOn
            Music.config(height = 48 , width = 48)
            Music.configure(command = lambda : menu.Enable_music())
            Music.place(x=1270, y= 650)
            
            menu.lista.append(Play)
            menu.lista.append(Rank)
            menu.lista.append(background)
            menu.lista.append(Exit)
            menu.lista.append(Music)
        
            window.mainloop()
            
    def Construir_menu1(lorethings):
            
            for i in lorethings:
                i.destroy()
            
            background = Label(window)           
            imagem = PhotoImage(file=".//Imagens//Sprites//background1.png")
            background.config(image = imagem )
            background.image = imagem
            background.grid(row=0,column = 0)
                                  
            menu = Menu([])
    
            Play = Button(window)
            Play.config(text="Play",font=("impact",20),bg = "white")
            Play.config(height = 2 , width = 15)
            Play.configure(command = lambda : Menu.clear_start(menu))
            Play.place(x=575, y= 270)
                        
            Lore = Button(window)
            Lore.config(text="Lore",font=("impact",20),bg = "white")
            Lore.config(height = 2 , width = 15)
            Lore.config(command = lambda: Menu.show_lore(menu))
            Lore.place(x=575, y= 470)
            
            Exit = Button(window)
            Exit.config(text="Exit",font=("impact",20),bg = "white")
            Exit.config(height = 2 , width = 15)
            Exit.config(command =lambda: Mapa.Exit(window))
            Exit.place(x=575, y= 570)
            
            Music = Button(window)
            Music.config(image = MusicOn)
            Music.image = MusicOn
            Music.config(height = 48 , width = 48)
            Music.configure(command = lambda : menu.Enable_music())
            Music.place(x=1270, y= 650)
            
            menu.lista.append(Play)
            menu.lista.append(Rank)
            menu.lista.append(background)
            menu.lista.append(Exit)
            menu.lista.append(Music)
            
    def Enable_music(self):
        if ClasseTrack.Tracker.Musicenabled:
            ClasseTrack.Tracker.Musicenabled = False
            self.lista[-1].config(image= MusicOff)
            self.lista[-1].image = MusicOff
            sound.Stop_All()
            
        else:
            ClasseTrack.Tracker.Musicenabled = True
            self.lista[-1].config(image=MusicOn)
            self.lista[-1].image = MusicOn
            sound.menu_music()
    
    def clear_start(menu):
        for i in menu.lista:
            i.destroy()

        ws.PlaySound(None,ws.SND_PURGE)
        Mapa.Start_Game(0, 0, window)
    
    def show_lore(menu):
        lorethings = []
        for i in menu.lista:
            i.destroy()
        lorelabel = Label(window)
        lorethings.append(lorelabel)
        lorelabel.config(image = lore)
        lorelabel.image = lore
        lorelabel.grid(row=0,column=0)
        backtomenu = Button(window)
        lorethings.append(backtomenu)
        backtomenu.config(text="Go Back To Menu",font=("impact",15),bg = "white")
        backtomenu.config(command = lambda : Menu.Construir_menu1(lorethings))
        backtomenu.place(x = 1000 ,y = 580)
    
         
            
        
