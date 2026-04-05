from collections import deque

from automat import NKA


# Funkcija pravi ε-zatvorenje datog stanja
def epsilon_zatvorenje(stanje,prelazi):

    stek = [stanje]
    zatvorenje = {stanje}

    while stek:
        s = stek.pop()
        
        for novo_stanje in prelazi.get(s, {}).get(None,set()):
            if novo_stanje not in zatvorenje:
                zatvorenje.add(novo_stanje)
                stek.append(novo_stanje)

    return zatvorenje

# Funkcija oslobadja prosledjeni automat od ε-prelaza 
def oslobadjanje_od_epsilon_prelaza(automat):

    prelazi_automat = {stanje: {slovo: set(skup) for slovo,skup in prelazi.items()} for stanje,prelazi in automat.prelazi.items()}
    stanja = automat.stanja()
    zavrsna_stanja = set(automat.zavrsna_stanja)

    epsilon_zatvorenja = {stanje : epsilon_zatvorenje(stanje,prelazi_automat) for stanje in stanja}

    novi_prelazi = {}
    azbuka = automat.azbuka()

    red = deque()
    red.append(automat.pocetno_stanje)
    poseceni = set()

    while red:

        tekuce_stanje = red.pop()
        if tekuce_stanje in poseceni:
            continue

        poseceni.add(tekuce_stanje)
        
        for slovo in azbuka:
            for stanje in epsilon_zatvorenja[tekuce_stanje]:
                if slovo in prelazi_automat[stanje]:

                    skup_sledecih_stanja = prelazi_automat[stanje][slovo]
                    for sledece_stanje in skup_sledecih_stanja:
                        
                        novi_prelazi.setdefault(tekuce_stanje,{}).setdefault(slovo, set()).add(sledece_stanje)

                        for el in epsilon_zatvorenja[sledece_stanje]:
                            red.append(el)
                

    nova_zavrsna_stanja = set()

    for stanje in stanja:
        if any(p in zavrsna_stanja for p in epsilon_zatvorenja[stanje]):
            nova_zavrsna_stanja.add(stanje)


    return NKA(automat.pocetno_stanje, nova_zavrsna_stanja, novi_prelazi).renumeracija()