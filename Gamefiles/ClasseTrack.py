class Track():
    def __init__(self, Turn, Enemies, Boss, Weaponselected, Music, Musicenabled, Map, pl, Timername,Pistol_up, Shotgun_up, Sniper_up):
        self.Turn = Turn 
        self.Enemies = Enemies
        self.Boss = Boss
        self.Weaponselected = Weaponselected
        self.Music = Music
        self.Musicenabled = Musicenabled
        self.Map = Map
        self.pl = pl
        self.Timername = Timername
        self.Pistol_up = Pistol_up
        self.Shotgun_up = Shotgun_up
        self.Sniper_up = Sniper_up
        
Tracker = Track(0, 0, 0, 0, 0, True, 0, 0, 0, 0, 0, 0)
