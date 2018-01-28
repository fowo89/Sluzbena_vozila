# -*- coding: utf-8 -*-

class Vozilo:
    def __init__(self, znamka, model, st_prev_km, zadnji_servis):
        self.znamka = znamka
        self.model = model
        self.st_prev_km = st_prev_km
        self.zadnji_servis = zadnji_servis


def seznam_vozil(vozila):
    if vozila == []:
        print "V seznamu še ni nobenega vozila. Prosimo, izberite možnost 4 in na seznam dodajte novo vozilo."
    else:
        for i, vozilo in enumerate(vozila):
            print str(i+1) + ".", vozilo.znamka, vozilo.model
            print "Število prevoženih kilometrov: " + str(vozilo.st_prev_km) + "km"
            print "Zadnji servis: " + str(vozilo.zadnji_servis)
            print ""

def ustvari_novo_vozilo(znamka, model, st_prev_km, zadnji_servis, vozila):
    novo_vozilo = Vozilo(znamka, model, st_prev_km, zadnji_servis)

    vozila.append(novo_vozilo)

def vnos_novega_vozila(vozila):
    znamka = raw_input("Vnesite znamko vozila: ")
    model = raw_input("Vnesite model vozila: ")
    st_prev_km = float(raw_input("Vnesite število prevoženih kilometrov: "))
    zadnji_servis = raw_input("Vnesite datum zadnjega servisa (DD.MM.LL): ")

    rezultat = ustvari_novo_vozilo(znamka, model, st_prev_km, zadnji_servis, vozila) #zakaj to? da funkcija ima nek rezultat?

def izbira_vozila(vozila):
    print "Vozila na razpolago:"
    print ""
    seznam_vozil(vozila)
    print ""
    izbira = raw_input("Izberite številko pred vozilom, za katerega bi radi posodobili podatke/katerega bi radi odstranili iz seznama: ")
    return vozila[int(izbira) - 1]

def dodajanje_km(vozila):
    izbrano_vozilo = izbira_vozila(vozila)

    print "Izbrano vozilo: %s %s s trenutnim stanjem kilometrov: %s km." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.st_prev_km)
    print ""
    novo_stanje_km = str(raw_input("Vnesite novo stanje prevoženih kilometrov: "))
    print ""
    izbrano_vozilo.st_prev_km = novo_stanje_km
    print "Stanje kilometrov za izbrano vozilo %s %s je bilo posodobljeno. Novo stanje je %s km." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.st_prev_km)

def spr_datuma_servisa(vozila):
    izbrano_vozilo = izbira_vozila(vozila)

    print "Izbrano vozilo: %s %s s trenutnim datumom zadnjega servisa: %s." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.zadnji_servis)
    print ""
    nov_datum = str(raw_input("Vnesite nov datum zadnjega servisa (DD.MM.LL): "))
    print ""
    izbrano_vozilo.zadnji_servis = nov_datum
    print "Datum zadnjega servisa za izbrano vozilo %s %s je bil posodobljen. Novo datum je %s." % (izbrano_vozilo.znamka, izbrano_vozilo.model, izbrano_vozilo.zadnji_servis)

def izbris_vozila(vozila):
    izbrano_vozilo = izbira_vozila(vozila)
    vozila.remove(izbrano_vozilo)
    print "Vozilo %s %s je bilo odstranjeno iz seznama." % (izbrano_vozilo.znamka, izbrano_vozilo.model)

def izpis_seznama(vozila):
    seznam_file = open("Seznam sluzbenih vozil.txt", "w+")

    seznam_file.write("Seznam službenih vozil:\n")
    seznam_file.write("\n")

    for i, vozilo in enumerate(vozila):
        seznam_file.write(str(i + 1) + "." + "" + vozilo.znamka + vozilo.model + "\n")
        seznam_file.write("Prevoženi kilometri: " + str(vozilo.st_prev_km) + "\n")
        seznam_file.write("Datum zadnjega servisa: " + vozilo.zadnji_servis + "\n")
        seznam_file.write("\n")

    seznam_file.close()



def main():

    print "Pozdravljeni v programu Vozilko, s katerim boste lahko upravljali s službenimi vozili!"

    vozila = []

    while True:
        print "Na voljo imate sledeče možnosti: "
        print ""
        print "1) Ogled seznama službenih vozil."
        print "2) Urejanje števila prevoženih kilometrov."
        print "3) Urejanje datuma zadnjega servisa."
        print "4) Dodajanje novega vozila na seznam."
        print "5) Izbris vozila s seznama."
        print "6) Izpis seznama vozil v txt datoteko."
        print "7) Izhod iz programa."
        print ""

        izbor = int(raw_input("Prosimo, izberite številko pred izbrano možnostjo (1, 2, 3, 4, 5, 6): "))

        print ""

        if izbor == 1:
            print "V voznem parku imamo trenutno sledeča vozila:"
            seznam_vozil(vozila)
        elif izbor == 2:
            print "Urejati želite število prevoženih kilometrov."
            dodajanje_km(vozila)
        elif izbor == 3:
            print "Urejati želite datum zadnjega servisa."
            spr_datuma_servisa(vozila)
        elif izbor == 4:
            print "Na seznam želite dodati novo vozilo."
            vnos_novega_vozila(vozila)
        elif izbor == 5:
            print "S seznama želite izbrisati vozilo."
            izbris_vozila(vozila)
        elif izbor == 6:
            print "Program vam bo seznam vozil izpisal v txt datoteko."
            izpis_seznama(vozila)
        elif izbor == 7:
            print "Hvala za uporabo programa!"
            break
        else:
            "Izbor je neveljaven. Prosimo ponovite izbor."

        print ""
        print "Prosimo, ponovno izberite željen ukaz."
        print ""











if __name__ == '__main__':
        main()

