import ClasseMapa
import ClasseTrack

def Timer(pl,Turn):
    
    try:
        if Turn == ClasseTrack.Tracker.Turn - 1 or Turn == ClasseTrack.Tracker.Turn:
            ClasseMapa.Mapa.Roda_jogo(ClasseTrack.Tracker.Map, pl)
    except:
        ClasseTrack.Tracker.Timername.cancel()