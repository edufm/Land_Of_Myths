import random

import ClasseImagens
import ClasseTrack

class Gun():
    def __init__(self, ID, Ammo, Range, Damage,Type):
        self.ID = ID 
        self.Ammo = Ammo
        self.Range = Range
        self.Damage = Damage

    def Check_Range(self ,loc, pl):
        distanciax = pl.pos[1] - loc[1]
        if distanciax < 0:
            distanciax = loc[1] - pl.pos[1]
        distanciay = pl.pos[0] - loc[0]
        if distanciay < 0:
            distanciay = loc[0] - pl.pos[0]
            
        Distance = distanciax +  distanciay

        if Distance < self.Range:
            return 1
        else:
            return 0

    def Pick_Weapon(ID, pl):
        Ammo = pl.inv[ID]
        Ammo += WeaponList[ID].Ammo
        if Ammo >= WeaponList[ID].Ammo * 3:
            pl.inv[ID] = WeaponList[ID].Ammo * 3
        else:
            pl.inv[ID] += WeaponList[ID].Ammo
    
    def Weapon_Swap(ID,pl):
        Weapon = ID - 100
        pl.Weapon = WeaponList[Weapon]        
            
    def Shotgun_Shot(pl, loc, Map):
    
        if loc[1] == (pl.pos[1] - 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Left([loc[0], pl.pos[1] - 1], Map, pl)
        if loc[1] == (pl.pos[1] + 1) and loc[0] == pl.pos[0]:
            Gun.Shotgun_Right([loc[0], pl.pos[1] + 1], Map, pl)
        if loc[0] == (pl.pos[0] - 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Up([pl.pos[0] - 1, loc[1]], Map, pl)
        if loc[0] == (pl.pos[0] + 1) and loc[1] == pl.pos[1]:
            Gun.Shotgun_Down([pl.pos[0] + 1, loc[1]], Map, pl)
            
#______________________________Upgrades____________________________
    def Up_Pistol(pl, button):
        if pl.inv[0] == 33 and ClasseTrack.Tracker.Pistol_up != ClasseTrack.Tracker.Map.Waves:
            button.config(state = 'disabled')
            pl.inv[0] = 0
            Pistol.Damage += 1
            ClasseTrack.Tracker.Pistol_up = ClasseTrack.Tracker.Map.Waves
            
    def Up_Shotgun(pl, button):
        if pl.inv[1] == 12 and ClasseTrack.Tracker.Shotgun_up != ClasseTrack.Tracker.Map.Waves:
            button.config(state = 'disabled')
            pl.inv[1] = 0
            Shotgun.Damage += 1
            ClasseTrack.Tracker.Shotgun_up = ClasseTrack.Tracker.Map.Waves
    
    def Up_Sniper(pl, button):
        if pl.inv[2] == 9 and ClasseTrack.Tracker.Sniper_up != ClasseTrack.Tracker.Map.Waves:
            button.config(state = 'disabled')
            pl.inv[2] = 0
            Sniper.Damage += 1
            ClasseTrack.Tracker.Sniper_up = ClasseTrack.Tracker.Map.Waves
                    
        
#___________________________________________Shotgun____________________________
    
    def Shotgun_Left(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:  
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 5 + Shotgun.Damage)
                
                loc[1] -= 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
                
            else:
                loc[1] -= 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 4 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
                
            
    def Shotgun_Right(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:  
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 5 + Shotgun.Damage)
                
                loc[1] += 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
            else:
                loc[1] += 1
                loc[0] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 4 + Shotgun.Damage)
                loc[0] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
            
    def Shotgun_Down(loc,Map,pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:          
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 5 + Shotgun.Damage)
                
                loc[0] += 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
            else:
                loc[0] += 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 4 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
            
    def Shotgun_Up(loc, Map, pl):
        Ammo = Gun.Ammo_Count(pl)
        if Ammo == 1:        
            x = loc[0]
            y = loc[1]
            if Map.matriz[x][y] < 100 and Map.matriz[x][y] != 0:
                Gun.Take_Damage_SG(loc, pl, Map, 5 + Shotgun.Damage)
                
                loc[0] -= 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 1 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 2 + Shotgun.Damage)
            else:
                loc[0] -= 1
                loc[1] -= 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 4 + Shotgun.Damage)
                loc[1] += 1
                Gun.Take_Damage_SG(loc, pl, Map, 3 + Shotgun.Damage)
            
    

    #_______________________________Sniper___________________________
    
    def Sniper_X(loc,Map,pl,Damage,First,count):

        Ammo = 0
        count += 1
        if count == 1:  
            RangeTest =Gun.Check_Range(Sniper, loc, pl) 
            Damage += Sniper.Damage
        else: 
            RangeTest = 1
            
        if RangeTest == 1:
            x = pl.pos[0]
            y = pl.pos[1]
            if loc[0] == x and loc[1] > y: # right
                if loc[1] < 27:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[1] += 1
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        loc[1] += 1
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
            if loc[0] == x and loc[1] < y: # left
                if loc[1] >= 0:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[1] -= 1
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        loc[1] -= 1
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
            if loc[0] < x and loc[1] == y: # up
                if loc[0] >= 0:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:
                        loc[0] -= 1
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        loc[0] -= 1
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
            if loc[0] > x and loc[1] == y: # down
                if loc[0] <= 14:
                    if Map.matriz[loc[0]][loc[1]] == 0 or Map.matriz[loc[0]][loc[1]] > 100:                    
                        loc[0] += 1
                        Gun.Sniper_X(loc,Map,pl,Damage,0,count)
                    else:
                        Gun.Take_Damage_SN(loc, pl, Map,Damage,count,Ammo)
                        Damage -= 1
                        loc[0] += 1
                        Gun.Sniper_X(loc,Map,pl,Damage, 0, count)
                        
        #_______________________GErador armas_____________________
        

    def Gerar_Guns(Map):
        a = 0
        b = 0
        c = 0
        for i in range(15):
            for j in range(27):
                if Map.matriz[i][j] == 100:           
                    a += 1
                if Map.matriz[i][j] == 101:
                    b += 1
                if Map.matriz[i][j] == 101:
                    c += 1
                
        x = random.randint(1,101)
        
        if a < 4:
            if x <= 10:
                Gun.Gerar_Pistol(Map)
        x = random.randint(1,101)
        if b <= 3:
            if x <= 3:
                Gun.Gerar_Shotgun(Map)
        x = random.randint(1,101)
        if c < 2:
            if x <= 2:
                Gun.Gerar_Sniper(Map)
        
    def Gerar_Pistol(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 100
            Map.b[x][y].config(image = ClasseImagens.guns[0])
            Map.b[x][y].image = ClasseImagens.guns[0]
        else:
            Gun.Gerar_Pistol(Map)
        
    def Gerar_Shotgun(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 101
            Map.b[x][y].config(image = ClasseImagens.guns[1])
            Map.b[x][y].image = ClasseImagens.guns[1]
        else:
            Gun.Gerar_Shotgun(Map)

    def Gerar_Sniper(Map):
        x = random.randint(0,14)
        y = random.randint(0,26)
        if Map.matriz[x][y] == 0:
            Map.matriz[x][y] = 102
            Map.b[x][y].config(image = ClasseImagens.guns[2])
            Map.b[x][y].image = ClasseImagens.guns[2]
        else:
            Gun.Gerar_Sniper(Map)
            
            #______________________Dano_______________________________________
        
    
    def Take_Damage_P(loc, pl, Map):
        RangeTest =Gun.Check_Range(Pistol, loc, pl)
        
        if RangeTest == 1:
            Ammo = Gun.Ammo_Count(pl)
            for i in Map.LEnemys:     
                if Ammo == 1:
                    if i.pos == loc:
                        i.health -= pl.weapon.Damage
                        if i.health <= 0:
                            Map.LEnemys.remove(i)    
                            Map.matriz[i.pos[0]][i.pos[1]] = 0
                            Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                            Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]

    def Take_Damage_SG(loc, pl, Map, Damage): #Função exclusiva do shotgun       
            for i in Map.LEnemys:
                if i.pos == loc:
                    i.health -= Damage
                    if i.health <= 0:
                        Map.LEnemys.remove(i)    
                        Map.matriz[i.pos[0]][i.pos[1]] = 0
                        Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
    
    def Take_Damage_SN(loc, pl, Map, Damage,count,Ammo):
            for i in Map.LEnemys:
                if i.pos == loc:
                    i.health -= Damage
                    if i.health <= 0:
                        Damage -= i.health
                        Map.LEnemys.remove(i)    
                        Map.matriz[i.pos[0]][i.pos[1]] = 0
                        Map.b[i.pos[0]][i.pos[1]].config(image= ClasseImagens.Tiles[ClasseTrack.Tracker.Boss])
                        Map.b[i.pos[0]][i.pos[1]].image = ClasseImagens.Tiles[ClasseTrack.Tracker.Boss]
  
                    
            #________________________________Ammo__________________________________________
                    
    def Ammo_Count(pl):
        Ammo = pl.weapon.ID - 100
        if pl.inv[Ammo] > 0:    
            pl.inv[Ammo] -= 1
            return 1
        else:
            return 0
            
            #__________________________Trap and torret_____________________________________
#    def Torret_Shot(pl,Map)

        
Pistol = Gun(100,11,7, 1,"Shoot")

Shotgun = Gun(101,4,3, 0,"Burst")

Sniper = Gun(102,3,2, 0,"LongWatch")

WeaponList = [Pistol,Shotgun,Sniper]