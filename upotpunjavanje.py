from automat import DKA

# Funkcija proverava da li je prosledjen automat potpun
def potpun(automat):

    azbuka = automat.azbuka()
    stanja = automat.stanja()

    for stanje in stanja:
        if set(automat.prelazi.get(stanje, {}).keys()) != azbuka:
            return False

    return True    

# Funkcija za upotpunjavanje prosledjenog automata
def upotpunjavanje(automat):

    if potpun(automat):
        return DKA(automat.pocetno_stanje,automat.zavrsna_stanja,automat.prelazi).renumeracija()
    
    stanje_greske = DKA.novo_stanje()
    azbuka = automat.azbuka()
    stanja = list(automat.prelazi.keys())
    prelazi = {stanje : dict(prelazi) for stanje,prelazi in automat.prelazi.items()}

    for slovo in azbuka:
        prelazi.setdefault(stanje_greske,{})[slovo] = stanje_greske

    for stanje in stanja:
        for slovo in azbuka:
            if slovo not in prelazi.get(stanje, {}):
                prelazi.setdefault(stanje,{})[slovo] = stanje_greske


    return DKA(automat.pocetno_stanje,automat.zavrsna_stanja,prelazi).renumeracija()