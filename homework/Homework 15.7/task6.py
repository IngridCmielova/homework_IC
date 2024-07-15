# Otevření a čtení obsahu souboru file4.txt
with open("file4.txt", "r", encoding="utf-8") as file:
    content = file.read()

updated_content = content.replace("žízeň", "hlad")

with open("file4_updated.txt", "w", encoding="utf-8") as file:
    file.write(updated_content)

print("Slovo 'žízeň' bylo nahrazeno slovem 'hlad' ve všech případech v souboru file4.txt.")