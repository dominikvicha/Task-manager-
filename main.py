"""
Projekt: Task manager

author: Vícha Dominik 
emial: dominik.vicha@gmail.com 
discord: Dominik V 

"""



def hlavni_menu():

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

        else:
            print("Neplatná volba. Zadejte číslo 1 až 4.")

    else:
        print("Vstup musí být číselný.")

hlavni_menu()





#def pridat_ukol():






#def zobraz_ukoly():






#def odstranit_ukol():




#def main():