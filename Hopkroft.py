from collections import deque

from automat import DKA
from upotpunjavanje import potpun

# Funkcija vrsi Hopkroftov algoritam minimizacije PDKA 
def minimizacija_Hopkroft(automat):

    if(not potpun(automat)):
        raise ValueError("Greska, automat nije potpun.")


    prelazi = {stanje: {slovo: sledece_stanje for slovo,sledece_stanje in prelazi.items()} for stanje,prelazi in automat.prelazi.items()}
    stanja = automat.stanja()
    zavrsna_stanja = set(automat.zavrsna_stanja)
    azbuka = automat.azbuka()


    prelazi_obrnuto = {slovo: {} for slovo in azbuka}

    for stanje, prelaz in prelazi.items():
        for slovo, sledece_stanje in prelaz.items():
            prelazi_obrnuto.setdefault(slovo, {}).setdefault(sledece_stanje, set()).add(stanje)

    
    particija = set()

    if zavrsna_stanja:
        particija.add(frozenset(zavrsna_stanja))
    
    if stanja - zavrsna_stanja:
        particija.add(frozenset(stanja - zavrsna_stanja))

    nova_particija_red = deque(particija)
    nova_particija_skup = set(particija)

    while nova_particija_red:

        A = nova_particija_red.popleft()

        if A not in nova_particija_skup:
            continue

        nova_particija_skup.remove(A)

        for slovo in azbuka:
            stanja_prelaz_do_A = set()

            for stanje in A:
                stanja_prelaz_do_A |= prelazi_obrnuto[slovo].get(stanje, set())

            particija_lista = list(particija)

            for skup in particija_lista:

                presek = skup & stanja_prelaz_do_A
                razlika = skup - stanja_prelaz_do_A

                if presek and razlika:
                    particija.remove(skup)
                    particija.add(presek)
                    particija.add(razlika)

                    if skup in nova_particija_skup:
                        nova_particija_skup.remove(skup)
                        nova_particija_skup.add(presek)
                        nova_particija_skup.add(razlika)

                        nova_particija_red.append(presek)
                        nova_particija_red.append(razlika)

                    elif len(presek) <= len(razlika):
                        nova_particija_red.append(presek)
                        nova_particija_skup.add(presek)

                    else:
                        nova_particija_red.append(razlika)    
                        nova_particija_skup.add(razlika)
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