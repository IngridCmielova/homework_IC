def find_longest_line_length(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    longest_line = max(lines, key=len)

    longest_line_length = len(longest_line)

    return longest_line_length

file_name = 'File2.txt'

longest_line_length = find_longest_line_length(file_name)
print(f'Délka nejdelšího řádku je: {longest_line_length}')