def compare_files(file1, file2):
    try:
        # Otevřeme první soubor pro čtení
        f1 = open(file1, 'r')
        # Otevřeme druhý soubor pro čtení
        f2 = open(file2, 'r')

        # Přečteme všechny řádky z prvního souboru
        lines1 = f1.readlines()
        # Přečteme všechny řádky z druhého souboru
        lines2 = f2.readlines()

        # Zavřeme oba soubory, protože je již nepotřebujeme
        f1.close()
        f2.close()

        # Zjistíme, kolik řádků má každý soubor
        len1 = len(lines1)
        len2 = len(lines2)

        # Projdeme všechny řádky (až do maxima řádků mezi dvěma soubory)
        for i in range(max(len1, len2)):
            # Pokud je řádek v prvním souboru, vezmeme ho, jinak použijeme prázdný řádek
            if i < len1:
                line1 = lines1[i].strip()
            else:
                line1 = ""

            # Pokud je řádek v druhém souboru, vezmeme ho, jinak použijeme prázdný řádek
            if i < len2:
                line2 = lines2[i].strip()
            else:
                line2 = ""

            # Porovnáme řádky a pokud se neshodují, vypíšeme je
            if line1 != line2:
                print("Neshoda na řádku", i + 1)
                print("file1.txt:", line1)
                print("file2.txt:", line2)

    except FileNotFoundError as e:
        # Pokud soubor nebyl nalezen, vypíšeme chybovou zprávu
        print("Chyba:", e)
    except Exception as e:
        # Pokud došlo k jiné chybě, vypíšeme chybovou zprávu
        print("Došlo k chybě:", e)


# Názvy souborů, které chceme porovnat
file1 = 'file1.txt'
file2 = 'file2.txt'

# Zavoláme funkci pro porovnání souborů
compare_files(file1, file2)