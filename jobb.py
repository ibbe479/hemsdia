class JobbDetaljer:
    def __init__(self, Ansvar, krav, Förmåner , Arbetstider, mail ):
        self.ansvar = Ansvar
        self.krav = krav
        self.förmåner = Förmåner
        self.arbetstider = Arbetstider
        self.mail = mail
# Skapa en klass för Jobb
class Jobb:
    def __init__(self, titel, beskrivning, lön, plats):
        self.titel = titel
        self.beskrivning = beskrivning
        self.lön = lön
        self.plats = plats

