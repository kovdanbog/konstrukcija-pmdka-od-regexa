from automat import NKA

# Funkcija konstruise automat ciji jezak odgovara {ε}
def epsilon():
    pocetno_stanje = NKA.novo_stanje()
    zavrsno_stanje = NKA.novo_stanje()

    prelazi = {pocetno_stanje: {None: {zavrsno_stanje}}}

    return NKA(pocetno_stanje, {zavrsno_stanje}, prelazi)

# Funkcija konstruise automat ciji jezik odgovara {s} za bilo koji karakter s (definisani zasad samo [a-zA-Z0-9] kao karakteri)
def slovo(s):
    pocetno_stanje = NKA.novo_stanje()
    zavrsno_stanje = NKA.novo_stanje()

    prelazi = {pocetno_stanje: {s: {zavrsno_stanje}}}

    return NKA(pocetno_stanje, {zavrsno_stanje}, prelazi)

# Funkcija spaja prelaze dva automata
def spoji_prelaze(prvi_automat_prelazi, drugi_automat_prelazi):
    rez = {stanje: {slovo: set(skup) for slovo,skup in prelazi.items()} for stanje,prelazi in prvi_automat_prelazi.items()}

    for stanje,prelazi in drugi_automat_prelazi.items():
        for slovo,skup in prelazi.items():
            rez.setdefault(stanje,{}).setdefault(slovo,set()).update(skup)

    return rez    

# Funkcija vrsi konkatenaciju dva regularna izraza data automatima
def konkatenacija(prvi_automat, drugi_automat):
    prvi_automat_prelazi_kopija = {stanje: {slovo: set(skup) for slovo,skup in prelazi.items()} for stanje,prelazi in prvi_automat.prelazi.items()}
    drugi_automat_prelazi_kopija = {stanje: {slovo: set(skup) for slovo,skup in prelazi.items()} for stanje,prelazi in drugi_automat.prelazi.items()}

    zavrsno_stanje_prvi = next(iter(prvi_automat.zavrsna_stanja))

    for slovo,skup_sledecih_stanja in drugi_automat.prelazi.get(drugi_automat.pocetno_stanje, {}).items():
        drugi_automat_prelazi_kopija.setdefault(zavrsno_stanje_prvi, {}).setdefault(slovo, set()).update(skup_sledecih_stanja)
        
    for stanje,prelazi in drugi_automat.prelazi.items():
        for slovo,skup_sledecih_stanja in prelazi.items():
            for sledece_stanje in skup_sledecih_stanja:
                if sledece_stanje == drugi_automat.pocetno_stanje:
                    drugi_automat_prelazi_kopija[stanje][slovo].add(zavrsno_stanje_prvi)
                    drugi_automat_prelazi_kopija[stanje][slovo].remove(drugi_automat.pocetno_stanje)
                    break
           
    del drugi_automat_prelazi_kopija[drugi_automat.pocetno_stanje]
    
    prelazi = spoji_prelaze(prvi_automat_prelazi_kopija, drugi_automat_prelazi_kopija)

    return NKA(prvi_automat.pocetno_stanje, drugi_automat.zavrsna_stanja, prelazi)

# Funkcija vrsi uniju dva regularna izraza data automatima
def unija(prvi_automat, drugi_automat):
    pocetno_stanje = NKA.novo_stanje()
    zavrsno_stanje = NKA.novo_stanje()

    prelazi = spoji_prelaze(prvi_automat.prelazi, drugi_automat.prelazi)
    prelazi.setdefault(pocetno_stanje, {}).setdefault(None, set()).update({prvi_automat.pocetno_stanje, drugi_automat.pocetno_stanje})

    for zavrsno_prvi in prvi_automat.zavrsna_stanja:
        prelazi.setdefault(zavrsno_prvi, {}).setdefault(None, set()).add(zavrsno_stanje)

    for zavrsno_drugi in drugi_automat.zavrsna_stanja:
        prelazi.setdefault(zavrsno_drugi, {}).setdefault(None, set()).add(zavrsno_stanje)

    return NKA(pocetno_stanje, {zavrsno_stanje}, prelazi)

# Funkcija vrsi Klinijevo zatvorenje regularnog izraza datog automatom
def klinijevo_zatvorenje(automat):
    pocetno_stanje = NKA.novo_stanje()
    zavrsno_stanje = NKA.novo_stanje()

    prelazi = {stanje: {slovo: set(skup) for slovo,skup in prelazi.items()} for stanje,prelazi in automat.prelazi.items()}

    prelazi.setdefault(pocetno_stanje, {}).setdefault(None, set()).update({automat.pocetno_stanje, zavrsno_stanje})

    for zavrsno in automat.zavrsna_stanja:
        prelazi.setdefault(zavrsno, {}).setdefault(None, set()).update({automat.pocetno_stanje, zavrsno_stanje})

    return NKA(pocetno_stanje, {zavrsno_stanje}, prelazi)

# Funkcija vrsi Tompsonovu konstrukciju NKA, kao argument prihvata AST u vidu torke
def napravi_nka_Tompson_pomocna(ast):

    operacija = ast[0]

    if operacija == "char":
        if ast[1] is None:
            return epsilon()
        
        return slovo(ast[1])

    elif operacija == "concat":

        levi = napravi_nka_Tompson_pomocna(ast[1])
        desni = napravi_nka_Tompson_pomocna(ast[2])

        return konkatenacija(levi, desni)
    
    elif operacija == "union":

        levi = napravi_nka_Tompson_pomocna(ast[1])
        desni = napravi_nka_Tompson_pomocna(ast[2])

        return unija(levi, desni)
    
    elif operacija == "star":

        automat = napravi_nka_Tompson_pomocna(ast[1])

        return klinijevo_zatvorenje(automat)
    
    elif operacija == "plus":

        # Za r regularni izraz r+ = rr*, te nam nije neophodna zasebna funkcija
        automat = napravi_nka_Tompson_pomocna(ast[1])
        kopija_automat = napravi_nka_Tompson_pomocna(ast[1])
        klinijevo = klinijevo_zatvorenje(kopija_automat)

        automat = konkatenacija(automat,klinijevo)

        return automat
    
    elif operacija == "optional":
        
        # Za r regularni izraz r? = r | ε, te nam nije neophodna zasebna funkcija
        automat = napravi_nka_Tompson_pomocna(ast[1])

        return unija(automat,epsilon())
    
    else:
        raise ValueError(f"Nepoznata operacija: {operacija}")
    
# Funkcija renumerise automat konstruisan pomocnom funkcijom
def napravi_nka_Tompson(ast):
    return napravi_nka_Tompson_pomocna(ast).renumeracija()



