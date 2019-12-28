from numpy import random as ran

import ClasseImagens
from ClasseGun import Gun
import ClasseTrack
from ClassSound import *

class Enemys():
    def __init__(self, ID, health, damage, pos):
        self.ID = ID
        self.health = health
        self.damage = damage
        self.pos = pos

    def cria_inimigos(waves, Map):
        level = 0
        if waves > 12:
            level = 2
        Map.LEnemys = []
        if waves%4 != 0:
            N = waves // 4
            for i in range((waves%4)*3):
                b = True
                while b:
                    a = ran.randint(1,5)
                    if a == 1:
                        x = ran.randint(0,14)
                        if Map.matriz[x][26] == 0:
                            b = False
                            E = Enemys(0+level, 1+N, 1, [x, 26])
                            Map.matriz[x][26] = 2
                            Map.b[x][26].config(image = ClasseImagens.enemy1[0])
                            Map.b[x][26].image = ClasseImagens.enemy1[0]
                            Map.LEnemys.append(E)
                    elif a == 2:
                        x = ran.randint(0,14)
                        if Map.matriz[x][0] == 0:
                            b = False
                            E = Enemys(0+level, 1+N, 1, [x, 0])
                            Map.matriz[x][0] = 2
                            Map.b[x][0].config(image = ClasseImagens.enemy1[0])
                            Map.b[x][0].image = ClasseImagens.enemy1[0]
                            Map.LEnemys.append(E)
                    elif a == 3:
                        x = ran.randint(0,26)
                        if Map.matriz[14][x] == 0:
                            b = False
                            E = Enemys(0+level, 1+N, 1, [14, x])
                            Map.matriz[14][x] = 2
                            Map.b[14][x].config(image = ClasseImagens.enemy1[0])
                            Map.b[14][x].image = ClasseImagens.enemy1[0]
                            Map.LEnemys.append(E)
                    elif a == 4:
                        x = ran.randint(0,26)
                        if Map.matriz[0][x] == 0:
                            b = False
                            E = Enemys(0+level, 1+N, 1, [0, x])
                            Map.matriz[0][x] = 2
                            Map.b[0][x].config(image = ClasseImagens.enemy1[0])
                            Map.b[0][x].image = ClasseImagens.enemy1[0]
                            Map.LEnemys.append(E)
                
        if waves%4 == 0:
            N = ClasseTrack.Tracker.Boss
            E = Enemys(1+level, 7 + N-1*3, 5, [14, 13])
            Map.matriz[14][13] = 3
            Map.b[14][13].config(image = ClasseImagens.boss1[0])
            Map.b[14][13].image = ClasseImagens.boss1[0]
            Map.LEnemys.append(E)
                    
    def Take_Damage(loc, pl, Map):
        if pl.weapon.ID == 100:
            Gun.Take_Damage_P(loc,pl,Map)
            
        elif pl.weapon.ID == 101:
            Gun.Shotgun_Shot(pl, loc, Map)
            
        elif pl.weapon.ID == 102:
            if pl.inv[2] > 0: 
                pl.inv[2] -= 1
                Gun.Sniper_X(loc,Map,pl,7, 1, 0)
            
    
    def left(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]            
        self.pos[1] -= 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][2])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][2]
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        
    def right(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[1] += 1
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        Map.b[self.pos[0]][self.pos[1]].config(image= ClasseImagens.enemy[self.ID][1])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][1]
            
    def up(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0            
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[0] -= 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][0])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][0]
        Map.matriz[self.pos[0]][self.pos[1]] = 2        
        
    def down(self, Map):
        Map.matriz[self.pos[0]][self.pos[1]] = 0
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
        self.pos[0] += 1
        Map.b[self.pos[0]][self.pos[1]].config(image=ClasseImagens.enemy[self.ID][3])
        Map.b[self.pos[0]][self.pos[1]].image = ClasseImagens.enemy[self.ID][3]
        Map.matriz[self.pos[0]][self.pos[1]] = 2
        
        
    def jogada(self, pl, Map):
        distanciax = pl.pos[1] - self.pos[1]
        distanciay = pl.pos[0] - self.pos[0]
        
        down = self.pos[0] + 1 < 15
        up = self.pos[0] -1 >= 0
        left = self.pos[1] - 1 >= 0
        right = self.pos[1] + 1 <= 26
        
        left_clear = False
        right_clear = False
        up_clear = False
        down_clear= False
        
        if left:
            left_clear = Map.matriz[self.pos[0]][self.pos[1]-1] == 0
            
        if right:
            right_clear = Map.matriz[self.pos[0]][self.pos[1]+1] == 0
            
        if up:
            up_clear = Map.matriz[self.pos[0]-1][self.pos[1]] == 0
            
        if down:
            down_clear = Map.matriz[self.pos[0]+1][self.pos[1]] == 0
            
            

        if (abs(distanciax) == 0 and abs(distanciay) == 1) or (abs(distanciax) == 1 and abs(distanciay) == 0):
           self.atack(pl)
        
        elif right_clear and distanciax > 0 and abs(distanciax) > abs(distanciay):
            self.right(Map)
            
        elif left_clear and distanciax < 0 and abs(distanciax) > abs(distanciay):
            self.left(Map)
            
        elif down_clear and distanciay > 0 and abs(distanciay) > abs(distanciax):
            self.down(Map)
            
        elif up_clear and distanciay < 0 and abs(distanciay) > abs(distanciax):
            self.up(Map)

        elif abs(distanciay) == abs(distanciax):
            Op = ran.randint(1,3)
            if up_clear and left_clear and distanciay < 0 and distanciax < 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.up(Map)
                    
            if down_clear and left_clear and distanciay > 0 and distanciax < 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.down(Map)
                    
            if right_clear and up_clear and distanciay < 0 and distanciax > 0:
                if Op == 1:
                    self.right(Map)
                if Op == 2:
                    self.up(Map)

            if right_clear and down_clear and distanciay > 0 and distanciax > 0:
                if Op == 1:
                    self.right(Map)
                if Op == 2:
                    self.down(Map)
            
        elif (distanciay != 0) and (distanciax != 0):
            if up_clear and distanciay < 0:
                self.up(Map)
                
            elif down_clear and distanciay > 0:
                self.down(Map)
                
            elif left_clear and distanciax < 0:
                self.left(Map)
            
            elif right_clear and distanciax > 0:
                self.right(Map)
                
        else:
            Op = ran.randint(1,3)
            if left_clear and right_clear and distanciay < 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.right(Map)
                
            elif left_clear and right_clear and distanciay > 0:
                if Op == 1:
                    self.left(Map)
                if Op == 2:
                    self.right(Map)
                
            elif up_clear and down_clear and distanciax < 0:
                if Op == 1:
                    self.up(Map)
                if Op == 2:
                    self.down(Map)
            
            elif up_clear and down_clear and distanciax > 0:
                if Op == 1:
                    self.up(Map)
                if Op == 2:
                    self.down(Map)
        
    
    def atack(self, pl):
        pl.health -= self.damage