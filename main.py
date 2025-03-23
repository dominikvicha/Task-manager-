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
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}, {ukol['název']}")

def odstranit_ukol():

    if not ukoly:
        print("Žádné úkoly k odstranění.")
        return
    
    while True:
        print("\nSeznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}, {ukol['název']}")

        volba = input("Zadejte číslo úkolu k odstranění nebo (N) pro návrat do hlavního menu:").strip()

        if volba.lower() == "n":
            print("Vracím se do hlavního menu.")
            return
        
        if not volba.isdigit:
            print("Zadejte platné číslo úkolu.")
            continue

        if volba != int:
            print("Neplatný vstup. Zadejte číselný vstup.")
            continue

        cislo_ukolu = int(volba)

        if 1 <= cislo_ukolu <= len(ukoly):
            odstraneny_ukol = ukoly.pop(cislo_ukolu - 1)
            print(f"Úkol '{odstraneny_ukol['název']}' byl úspěšně odstraněn.")
            return
        else:
            print("Zadné číslo neexstiuje. Zkuste to znovu.")

def main():

    while True: 
        volba = hlavni_menu()

        if volba == 1:
            pridat_ukol()
        elif volba == 2:
            zobraz_ukoly()
        elif volba == 3:
            odstranit_ukol()
        elif volba == 4:
            print("Ukončuji program.")
            break

if __name__ == "__main__":
    main()
