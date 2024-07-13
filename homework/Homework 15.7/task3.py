def remove_last_line_and_save(input_file, output_file):
    # Otevřeme vstupní soubor pro čtení
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Uložíme poslední řádek
    last_line = lines[-1]

    # Odstraníme poslední řádek
    lines = lines[:-1]

    # Přepíšeme původní soubor bez posledního řádku
    with open(input_file, 'w') as file:
        file.writelines(lines)

    # Uložíme odstraněný řádek do nového souboru
    with open(output_file, 'w') as file:
        file.write(last_line)


# Definujeme názvy souborů
input_file = 'File2.txt'
output_file = 'File3.txt'

# Zavoláme funkci pro odstranění posledního řádku a jeho uložení do nového souboru
remove_last_line_and_save(input_file, output_file)