from automat import DKA
from upotpunjavanje import potpun


# Funkcija vrsi Murov algoritam minimizacije PDKA
def minimizacija_Mur(automat):

    if(not potpun(automat)):
        raise ValueError("Greska, automat nije potpun.")
    

    prelazi = {stanje: {slovo: sledece_stanje for slovo,sledece_stanje in prelazi.items()} for stanje,prelazi in automat.prelazi.items()}
    stanja = automat.stanja()
    zavrsna_stanja = set(automat.zavrsna_stanja)

    azbuka = automat.azbuka()
    particija = []

    if zavrsna_stanja:
        particija.append(set(zavrsna_stanja))
    
    if stanja - zavrsna_stanja:
        particija.append(stanja - zavrsna_stanja)

    
    while True:
        nova_particija = []

        for skup in particija:
            mapa_nove_particije = {}

            for stanje in skup:
                indeksi = []

                for slovo in azbuka:
                    sledece_stanje = prelazi[stanje][slovo]

                    indeks = None

                    for indeks_pripada, skup_pripada in enumerate(particija):

                        if sledece_stanje in skup_pripada:
                            indeks = indeks_pripada
                            break

                    indeksi.append(indeks)

                mapa_nove_particije.setdefault(tuple(indeksi), set()).add(stanje)

            nova_particija.extend(mapa_nove_particije.values())

        if nova_particija == particija:
            break

        particija = nova_particija


    mapa = {}

    for skup in particija:

        novo_stanje = DKA.novo_stanje()
        
        for stanje in skup:
            mapa[stanje] = novo_stanje

    novi_prelazi = {}

    for skup in particija:
        
        predstavnik = next(iter(skup))
        stanje = mapa[predstavnik]

        for slovo in azbuka:
            novi_prelazi.setdefault(stanje, {})[slovo] = mapa[prelazi[predstavnik][slovo]]

    novo_pocetno_stanje = mapa[automat.pocetno_stanje]
    nova_zavrsna_stanja = {mapa[stanje] for stanje in zavrsna_stanja}


    return DKA(novo_pocetno_stanje, nova_zavrsna_stanja, novi_prelazi).renumeracija()