from collections import deque

from automat import DKA


# Funkcija vrsi determinizaciju NKA konstrukcijom podskupova
def determinizacija(automat):

    for stanje,prelazi in automat.prelazi.items():
        for slovo,skup_sledecih_stanja in prelazi.items():
            if slovo is None:
                raise ValueError("Greska, unet automat nije oslobodjen od ε-prelaza.")

    frozenset_pocetno_stanje = frozenset({automat.pocetno_stanje})

    red = deque()
    red.append(frozenset_pocetno_stanje)

    podskupovi = set()
    podskupovi.add(frozenset_pocetno_stanje)

    mapa_stanja = {}
    mapa_stanja[frozenset_pocetno_stanje] = DKA.novo_stanje()

    azbuka = automat.azbuka()
    novi_prelazi = {}


    while red:

        skup_stanja = red.popleft()
    
        for slovo in azbuka:
            podskup_prelaza_po_slovu = set()

            for stanje in skup_stanja:  
                for sledece_stanje in automat.prelazi.get(stanje,{}).get(slovo,set()):                        
                    podskup_prelaza_po_slovu.add(sledece_stanje)
            
            frozenset_podskup = frozenset(podskup_prelaza_po_slovu)
          
            if frozenset_podskup:
                
                if frozenset_podskup not in podskupovi:
                    red.append(frozenset_podskup)    
                    podskupovi.add(frozenset_podskup)
                    mapa_stanja.setdefault(frozenset_podskup,DKA.novo_stanje())
            
                novi_prelazi.setdefault(mapa_stanja[skup_stanja],{})[slovo] = mapa_stanja[frozenset_podskup]

    nova_zavrsna_stanja = {stanje for podskup,stanje in mapa_stanja.items() if any(p in automat.zavrsna_stanja for p in podskup)}
    
    
    return DKA(mapa_stanja[frozenset_pocetno_stanje],nova_zavrsna_stanja,novi_prelazi).renumeracija()