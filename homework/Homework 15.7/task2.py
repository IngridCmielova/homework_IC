def analyze_file(input_file, output_file):
    # Definujeme samohlásky, souhlásky a číslice
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"

    # Inicializujeme počítadla
    char_count = 0
    line_count = 0
    vowel_count = 0
    consonant_count = 0
    digit_count = 0

    # Otevřeme vstupní soubor pro čtení
    with open(input_file, 'r') as file:
        # Procházíme každou řádku ve vstupním souboru
        for line in file:
            line_count += 1  # Zvýšíme počet řádků
            char_count += len(line)  # Přidáme počet znaků v aktuální řádce

            # Procházíme každý znak v řádce
            for char in line:
                if char in vowels:
                    vowel_count += 1  # Zvýšíme počet samohlásek
                elif char in consonants:
                    consonant_count += 1  # Zvýšíme počet souhlásek
                elif char in digits:
                    digit_count += 1  # Zvýšíme počet číslic

    # Otevřeme výstupní soubor pro zápis
    with open(output_file, 'w') as file:
        # Zapíšeme statistiky do výstupního souboru
        file.write(f"Chars: {char_count}\n")
        file.write(f"Lines: {line_count}\n")
        file.write(f"Vowels: {vowel_count}\n")
        file.write(f"Consonant: {consonant_count}\n")
        file.write(f"Digits: {digit_count}\n")

# Definujeme názvy souborů
input_file = 'file1.txt'
output_file = 'statistics.txt'

# Zavoláme funkci pro analýzu souboru
analyze_file(input_file, output_file)
