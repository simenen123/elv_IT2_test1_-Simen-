
class Varer:
    def __init__(self, pris, mva, navn):
        self.pris = pris
        self.mva = mva
        self.navn = navn
    
class grønnvarer(Varer):
    def __init__(self, pris, mva, navn, mdg_pos):
        super().__init__(pris, mva, navn)
        self.mdg_pos = mdg_pos
    
    def regn_ut_verdi_grønnvarer(self):
        return self.pris + self.pris * (1 + self.mva)

class kjøttvarer(Varer):
    def __init__(self, pris, mva, navn, mental_kostnader):
        super().__init__(pris, mva, navn)
        self.mental_kostnader = mental_kostnader
    
    def regn_ut_verdi_kjøttvarer(self):
        return self.pris + self.pris * (1 + self.mva) + self.mental_kostnader

eple = grønnvarer(100, 0.25, "eple", 30)
banan = grønnvarer(200, 0.25, "banan", 40)
granateple = grønnvarer(300, 0.25, "granateple", 50)

kjøttboller = kjøttvarer(100, 0.25, "kjøttboller", 200)
biff =  kjøttvarer(200, 0.25, "biff", 300)
pølse = kjøttvarer(300, 0.25, "pølse", 400)


kjøtt_produkter = ["kjøttboller",  "biff", "pølse"]

grønn_produkter = ["eple", "banan", "granateple"]

handlevogn = []

total_sum = 0

def start_handel():
    mengde_varer = int(input("Hvor mange varer vil du ha i handlevognen? "))
    print("hvilke varer vil du ha?", kjøtt_produkter, grønn_produkter, "skriv navent på produktet")
    for i in range(0, mengde_varer):
        vare = str(input(""))
        if vare == "elpe":
            handlevogn.append(eple)
        elif vare == "banan":
            handlevogn.append(banan)
        elif  vare == "granateple":
            handlevogn.append(granateple)
        elif  vare == "kjøttboller":
            handlevogn.append(kjøttboller)
        elif vare == "biff":
            handlevogn.append(biff)
        elif vare ==  "pølse":
            handlevogn.append(pølse)
    

start_handel()
for vare in handlevogn:
    if vare.navn in kjøtt_produkter:
        pris = vare.regn_ut_verdi_kjøttvarer()
        total_sum = total_sum + pris

print("total_sum er", int(total_sum))
