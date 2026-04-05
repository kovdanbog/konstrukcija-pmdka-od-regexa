from collections import deque

from visual_automata.fa.dfa import VisualDFA
from visual_automata.fa.nfa import VisualNFA
import patch


# U fajlu su definisane klase NKA i DKA, kao i neke potrebne metode
class Automat:

    def __init__(self,pocetno_stanje,zavrsna_stanja,prelazi):
        self.pocetno_stanje = pocetno_stanje
        self.zavrsna_stanja = zavrsna_stanja
        self.prelazi = prelazi

    # Metod kreira novo stanje
    @classmethod
    def novo_stanje(cls):
        stanje = cls.brojac_stanja
        cls.brojac_stanja += 1
        
        return stanje
    
    # Metod vraca azbuku automata
    def azbuka(self):
        rez = set()

        for prelazi in self.prelazi.values():
            for slovo in prelazi.keys():
                if slovo is not None:
                    rez.add(slovo)   

        return rez   
    
    # Metod vraca skup stanja automata
    def stanja(self):
        stanja = {self.pocetno_stanje} | set(self.prelazi.keys())

        for prelaz in self.prelazi.values():
            for vrednost in prelaz.values():
                if isinstance(vrednost, set):
                    stanja.update(vrednost)
                else:
                    stanja.add(vrednost)

        return stanja
    
    # Metod daje prikaz automata, uz pomoc biblioteke visual_automata i graphviz softvera 
    def prikaz(self):
        raise NotImplementedError
    
    # Metod vrsi renumeraciju stanja automata radi preglednosti
    def renumeracija(self):
        raise NotImplementedError

class NKA(Automat):
    brojac_stanja = 0


    def prikaz(self,rec=None):
        

        automat_digraf = VisualNFA(
                            states={str(stanje) for stanje in self.stanja()},
                            input_symbols={slovo for slovo in self.azbuka()},
                            transitions={str(stanje): {("" if slovo is None else slovo): set(map(str,skup_sledecih_stanja)) for slovo,skup_sledecih_stanja in prelaz.items()} for stanje,prelaz in self.prelazi.items()},
                            initial_state=str(self.pocetno_stanje),
                            final_states={str(stanje) for stanje in self.zavrsna_stanja}
                        )
        
        automat_digraf.show_diagram(input_str=rec,view=True)

        return
    

    def renumeracija(self):

        type(self).brojac_stanja = 0
        novi_prelazi = {}

        red = deque()
        red.append(self.pocetno_stanje)
        mapa = {}
        mapa[self.pocetno_stanje] = self.novo_stanje()

        sortirani_prelazi = {stanje: {slovo: tuple(sorted(skup)) for slovo,skup in prelazi.items()} for stanje,prelazi in sorted(self.prelazi.items())}

        while red:
            
            stanje = red.popleft()
            novo_stanje = mapa[stanje]
            novi_prelazi.setdefault(novo_stanje, {})

            for slovo, torka in sortirani_prelazi.get(stanje, {}).items():
                for sledece_stanje in torka:
                    
                    if sledece_stanje not in mapa:
                        mapa[sledece_stanje] = self.novo_stanje()
                        red.append(sledece_stanje)

                    novi_prelazi.setdefault(novo_stanje, {}).setdefault(slovo, set()).add(mapa[sledece_stanje])
    
        novo_pocetno_stanje = 0
        nova_zavrsna_stanja = {mapa[stanje] for stanje in self.zavrsna_stanja if stanje in mapa}


        return type(self)(novo_pocetno_stanje, nova_zavrsna_stanja, novi_prelazi)

class DKA(Automat):
    brojac_stanja = 0


    # Napomena: funkcija VisualDFA radi samo za PDKA
    def prikaz(self,rec=None):

        automat_digraf = VisualDFA(
                            states={str(stanje) for stanje in self.stanja()},
                            input_symbols={slovo for slovo in self.azbuka()},
                            transitions={str(stanje): {slovo: str(sledece_stanje) for slovo,sledece_stanje in prelaz.items()} for stanje,prelaz in self.prelazi.items()},
                            initial_state=str(self.pocetno_stanje),
                            final_states={str(stanje) for stanje in self.zavrsna_stanja}
                        )
        
        automat_digraf.show_diagram(input_str=rec,view=True)

        return          

    def renumeracija(self):
     
        type(self).brojac_stanja = 0
        novi_prelazi = {}

        red = deque()
        red.append(self.pocetno_stanje)
        mapa = {}
        mapa[self.pocetno_stanje] = self.novo_stanje()

        sortirani_prelazi = {stanje: {slovo: sledece_stanje for slovo,sledece_stanje in prelazi.items()} for stanje,prelazi in sorted(self.prelazi.items())}

        while red:
            
            stanje = red.popleft()
            novo_stanje = mapa[stanje]
            novi_prelazi.setdefault(novo_stanje, {})
            
            for slovo,sledece_stanje in sortirani_prelazi.get(stanje, {}).items():

                if sledece_stanje not in mapa:
                    mapa[sledece_stanje] = self.novo_stanje()
                    red.append(sledece_stanje)

                novi_prelazi.setdefault(novo_stanje, {})[slovo] = mapa[sledece_stanje]
    
        novo_pocetno_stanje = 0
        nova_zavrsna_stanja = {mapa[stanje] for stanje in self.zavrsna_stanja if stanje in mapa}


        return type(self)(novo_pocetno_stanje, nova_zavrsna_stanja, novi_prelazi)

