from parser.RegexParser import parse_regex
from pprint import pprint

from Tompson import napravi_nka_Tompson
from oslobadjanje_od_epsilon_prelaza import oslobadjanje_od_epsilon_prelaza
from Gluskov import napravi_nka_Gluskov
from determinizacija import determinizacija
from upotpunjavanje import upotpunjavanje
from Mur import minimizacija_Mur
from Hopkroft import minimizacija_Hopkroft

from time import perf_counter_ns

# Funkcija sluzi za odvijanje koraka u konstrukciji automata, vraca novonastali automat i daje njegov prikaz uz pomoc biblioteke visual_automata i graphviz softvera 
# ako se unese opcioni boolean argument True, osim automata vraca se i izmereno vreme trajanja koraka u milisekundama sa tacnoscu 3 decimale
def prikaz_automata(korak,funkcija_koraka,automat,meri_vreme=False):

        if meri_vreme:
            pocetak = perf_counter_ns()

        automat_sledeci_korak = funkcija_koraka(automat)

        if meri_vreme:
            kraj = perf_counter_ns()
            vreme = kraj - pocetak

        pprint((automat_sledeci_korak.pocetno_stanje,automat_sledeci_korak.prelazi, automat_sledeci_korak.zavrsna_stanja, korak))
        automat_sledeci_korak.prikaz()

        if meri_vreme:
            return automat_sledeci_korak,vreme
        
        else:
            return automat_sledeci_korak

# Funkcija proverava da li dat program prihvata unetu rec sve dok se ne unese q, 
# takodje izbacuje vizuelni prikaz prihvatanja/odbijanja reci uz pomoc biblioteke visual_automata i graphviz softvera        
def provera_reci(automat):

     while True:

        rec = input("Unesite rec za proveru: ")

        if rec == "q":
            return

        stanje = automat.pocetno_stanje
        azbuka = automat.azbuka()
        izvan_abuke = False
        ne_postoji_prelaz = False

        for slovo in rec:
            if slovo in azbuka:
                if slovo in automat.prelazi.get(stanje, {}):
                    stanje = automat.prelazi[stanje][slovo]
                else:
                    ne_postoji_prelaz = True
                    break
            else:
                izvan_abuke = True
                break

        if stanje in automat.zavrsna_stanja and not izvan_abuke and not ne_postoji_prelaz:
            pprint(f"Rec {rec} je prihvacena! :)")
            automat.prikaz(rec)
            
        else:
            pprint(f"Rec {rec} nije prihvacena :(")

# Funkcija vrsi konstrukciju PMDKA od datog regularnog izraza u obliku AST, 
# uz dodatna dva parametra: nacin konstrukcije i algoritam minimalizacije
def tok_konstrukcije(ast,konstrukcija,minimizacija):

    pprint("Konstruisanje PMDKA - potpunog minimalnog deterministickog konacnog automata")

    if konstrukcija == "T":

        pprint("Tompsonova konstrukcija: ")
        automat_Tompson, vreme_Tompson = prikaz_automata("Tompson",napravi_nka_Tompson,ast,True)
        input("Pritisnite Enter za nastavak izvrsavanja programa")

        pprint("Oslobadjanje od epsilon prelaza: ")
        automat, vreme_epsilon = prikaz_automata("epsilon",oslobadjanje_od_epsilon_prelaza,automat_Tompson,True)

        vreme = vreme_Tompson + vreme_epsilon
        pprint(f"Vreme Tompsonove konstrukcije uz oslobadjanje od epsilon prelaza je: {vreme/1000000:.3f} ms")
        input("Pritisnite Enter za nastavak izvrsavanja programa")

    elif konstrukcija == "G":

        pprint("Gluskovljeva konstrukcija: ")
        automat, vreme_Gluskov = prikaz_automata("Gluskov",napravi_nka_Gluskov,ast,True)
        pprint(f"Vreme Gluskovljeve konstrukcije je: {vreme_Gluskov/1000000:.3f} ms")
        input("Pritisnite Enter za nastavak izvrsavanja programa")

    pprint("Determinizacija - Konstrukcijom podskupova: ")
    automat_determinizovan = determinizacija(automat)
    pprint((automat_determinizovan.pocetno_stanje,automat_determinizovan.prelazi, automat_determinizovan.zavrsna_stanja, "deterministicki"))
    input("Pritisnite Enter za nastavak izvrsavanja programa")

    pprint("Upotpunjavanje: ")
    automat_potpun = prikaz_automata("potpun",upotpunjavanje,automat_determinizovan)
    input("Pritisnite Enter za nastavak izvrsavanja programa")

    if minimizacija == "M":

        pprint("Murov algoritam: ")
        automat_pmdka, vreme_Mur = prikaz_automata("Mur",minimizacija_Mur,automat_potpun,True)
        pprint(f"Vreme minimizacije Murovim algoritmom je: {vreme_Mur/1000000:.3f} ms")

    elif minimizacija == "H":
        
        pprint("Hopkroftov algoritam: ")
        automat_pmdka, vreme_Hopkroft = prikaz_automata("Hopkroft",minimizacija_Hopkroft,automat_potpun,True)
        pprint(f"Vreme minimizacije Hopkroftovim algoritmom je: {vreme_Hopkroft/1000000:.3f} ms")


    provera_reci(automat_pmdka)

"""
# Zadati primer regularnog izraza
regex_primer = r"(a|b)*abb"

# Parsiranje primera regularnog izraza
try:
    parsirani_regex_primer = parse_regex(regex_primer)
    pprint(parsirani_regex_primer)

except Exception as e:
    pprint(f"Greska pri parsiranju regexa. Proverite ispravnost regularnog izraza. {e}")

# Izvrsavanje konstrukcije PMDKA za zadataki parsirani regularni izraz u obliku AST 
tok_konstrukcije(parsirani_regex_primer, "T", "M")
"""

# Petlja koja za uneti regularni izraz konstruise PMDKA izabranom metodom i algoritmom minimizacije, sve dok se ne unese q
# Napomena: mogu se parsirati samo regularni izrazi sa karakterima [a-zA-Z0-9] i operacijama *,|,+,? i konkatenacija, 
# sa dobro uparenim zagradama i () koji predstavlja simbol ε

if __name__ == "__main__":
    
    while True:

        regex = input("Unesite regularni izraz: ")

        if regex == "q":
            break

        try:
            parsirani_regex = parse_regex(regex)
            pprint(parsirani_regex)

        except Exception as e:
            pprint(f"Greska pri parsiranju regexa. Proverite ispravnost regularnog izraza: {e}")
            continue


        while True:
            konstrukcija = input("Unesite nacin konstruckije (T ili G) : ")

            if konstrukcija != "T" and konstrukcija != "G":
                pprint("Niste uneli dobar nacin konstrukcije!")
                continue
            break   

        while True:
            minimizacija = input("Unesite algoritam minimizacije (M ili H) : ")

            if minimizacija != "M" and minimizacija != "H":
                pprint("Niste uneli dobar algoritam minimizacije!")
                continue
            break

        tok_konstrukcije(parsirani_regex, konstrukcija, minimizacija)