with open("mguide_backup.sql", encoding="utf-8") as f:
    lines = f.readlines()

with open("cleaned.txt", "w", encoding="utf-8") as out:
    for line in lines:
        if line.startswith("INSERT INTO"):
            out.write(line)