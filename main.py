"""
Projekt: Task manager

author: Vícha Dominik 
emial: dominik.vicha@gmail.com 
discord: Dominik V 

"""

ukoly = []

def hlavni_menu():

    while True: 
        zadani = """
        Vítejte v programu Task manager. 
        Task manager - hlavní menu: 
        1. Přidat nový úkol. ¨
        2. Zobraz všechny úkoly. 
        3. Odstraň úkol. 
        4. Konec programu.
        Vyberte možnost (1-4).
        """

        spravny_vstup = range(1,5)
        volba_uzivatele = input(zadani)

        if volba_uzivatele.isdigit():
            volba_uzivatele = int(volba_uzivatele)

            if volba_uzivatele in spravny_vstup:
                print("Vybrali jste možnost:", volba_uzivatele)
                return volba_uzivatele
            else:
                print("Neplatná volba. Zadejte číslo 1 až 4.")

        else:
            print("Vstup musí být číselný.")


def pridat_ukol():

    while True: 
        pridej_novy_ukol = input("Přidej nový úkol: ").strip()

        if not pridej_novy_ukol:
            print("Vstup nesmí být prázdný.")
            continue

        ukoly.append({"název": pridej_novy_ukol})
        print(f"Úkol '{pridej_novy_ukol}' byl úspěšně přidán.")
        break


def zobraz_ukoly():

    if not ukoly:
        print("Nebyly přidány žádné úkoly.")
    else:
        print("\nSeznam úkolů:")
        for i in enumerate(ukoly, 1):
            print("f{i}, {ukol['název']}")



#def odstranit_ukol():




def main():

    while True: 
        volba = hlavni_menu()

        if volba == 1:
            pridat_ukol()
        
        elif volba == 2:
            zobraz_ukoly()

        elif volba == 3:
            print("loading 3")

        elif volba == 4:
            print("Konec programu.")
            break

if __name__ == "__main__":
    main()
