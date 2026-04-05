from automat import NKA


# E(r) = L(r) ∩ {ε} za regularni izraz r
def E(ast):

    if ast == set():
        return False
    
    elif ast[0] == "char":
        if ast[1] == None:
            return True
        else:
            return False

# P(r) - skup slova kojima pocinju reci iz L(r) za dat regularni izraz r
def P(ast):

    if ast == set():
        return set()
    
    elif ast[0] == "char":
        if ast[1] == None:
            return set()
        else:
            return {ast[1]}

# K(r) - skup slova kojima se zavrsavaju reci iz L(r) za dat regularni izraz r
def K(ast):

    if ast == set():
        return set()
    
    elif ast[0] == "char":
        if ast[1] == None:
            return set()
        else:
            return {ast[1]}

# S(r) - skup svih parova slova koje sadrze reci iz L(r) za dat regularni izraz r
def S(ast):

    if ast == set():
        return set()
    
    elif ast[0] == "char":
        if ast[1] == None:
            return set()
        else:
            return set()

# Prethodne funkcije su definisane samo za atome (karakteri ili ε), 
# dok se ostatak induktivne definicije nalazi u funkciji napravi_nka_Gluskov_pomocna

# Pomocna funkcija - sadrzi ostatak induktivnih definicija prethodnih funkcija
def napravi_nka_Gluskov_pomocna(ast):

    operacija = ast[0]

    if operacija == "char":

        return E(ast), P(ast), K(ast), S(ast)

    elif operacija == "concat":

        E_levi,P_levi,K_levi,S_levi = napravi_nka_Gluskov_pomocna(ast[1])
        E_desni,P_desni,K_desni,S_desni = napravi_nka_Gluskov_pomocna(ast[2])

        E_automat = E_levi and E_desni
        P_automat = P_levi

        if E_levi:
            P_automat |= P_desni
          
        K_automat = K_desni  

        if E_desni:
            K_automat |= K_levi

        S_automat = S_levi | {(a,b) for a in K_levi for b in P_desni} | S_desni


        return E_automat,P_automat,K_automat,S_automat
    
    elif operacija == "union":

        E_levi,P_levi,K_levi,S_levi = napravi_nka_Gluskov_pomocna(ast[1])
        E_desni,P_desni,K_desni,S_desni = napravi_nka_Gluskov_pomocna(ast[2])

        E_automat = E_levi or E_desni
        P_automat = P_levi | P_desni
          
        K_automat = K_levi | K_desni

        S_automat = S_levi | S_desni


        return E_automat,P_automat,K_automat,S_automat
    
    elif operacija == "star":

        E_automat,P_automat,K_automat,S_automat = napravi_nka_Gluskov_pomocna(ast[1])

        E_automat = True
        S_automat |= {(a,b) for a in K_automat for b in P_automat}


        return E_automat,P_automat,K_automat,S_automat
    
    elif operacija == "plus":
        stablo = ('concat', ast[1], ('star', ast[1]))


        return napravi_nka_Gluskov_pomocna(stablo)
    
    elif operacija == "optional":
        
        E_automat,P_automat,K_automat,S_automat = napravi_nka_Gluskov_pomocna(ast[1])

        E_automat = True

        return E_automat,P_automat,K_automat,S_automat
    
    else:
        raise ValueError(f"Nepoznata operacija: {operacija}")
    
# Funkcija prima AST i vraca AST u kojem su sva pojavljivanja karaktera zamenjena njhivoim pozicijama u pocetnom AST-u, 
# zajedno sa odgovorajacuom mapom CHAR -> POZICIJA i brojem pozicija karaktera
def pozicije(ast):

    brojac = 1
    mapa = {}

    def walk(ast):
    
        operacija = ast[0]

        if operacija == "char":
            if ast[1] is None:
                return ast
            
            nonlocal brojac
            pos = brojac
            mapa[pos] = ast[1]
            brojac += 1

            return ('char', pos)

        elif operacija == "concat":

            return ('concat', walk(ast[1]), walk(ast[2]))
    
        elif operacija == "union":

            return ('union', walk(ast[1]), walk(ast[2]))
    
        elif operacija == "star":

            return ('star', walk(ast[1]))
    
        elif operacija == "plus":

            return ('plus', walk(ast[1]))
        
        elif operacija == "optional":
      
            return ('optional', walk(ast[1]))
        
        else:
            raise ValueError(f"Nepoznata operacija: {operacija}")

    return walk(ast),mapa,brojac

# Funkcija vrsi Gluskovljevu konstrukciju NKA
def napravi_nka_Gluskov(ast):

    ast_pozicije,mapa,broj_stanja = pozicije(ast)

    E_automat,P_automat,K_automat,S_automat = napravi_nka_Gluskov_pomocna(ast_pozicije)

    NKA.brojac_stanja = 0
    pocetno_stanje = NKA.novo_stanje()

    zavrsna_stanja = set(K_automat)
    if E_automat:
        zavrsna_stanja.add(pocetno_stanje)

    stanja = set()
    stanja.add(pocetno_stanje)

    for _ in range(broj_stanja - 1):
        stanja.add(NKA.novo_stanje())

    prelazi = {}
    prelazi.setdefault(pocetno_stanje, {})

    for sledece_stanje in P_automat:
        prelazi[pocetno_stanje].setdefault(mapa[sledece_stanje],set()).add(sledece_stanje)

    for stanje in stanja:
        prelazi.setdefault(stanje, {})

        for prvo_stanje,sledece_stanje in S_automat:
            if stanje == prvo_stanje:
                prelazi[stanje].setdefault(mapa[sledece_stanje],set()).add(sledece_stanje)

    return NKA(pocetno_stanje,zavrsna_stanja,prelazi).renumeracija()     