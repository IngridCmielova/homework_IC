def count_word_in_file(file_name, target_word):
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    word_count = content.lower().count(target_word.lower())

    return word_count

file_name = 'File1.txt'
target_word = 'řádek'

word_count = count_word_in_file(file_name, target_word)
print(f'Slovo "{target_word}" se v souboru objevuje {word_count} krát.')