# Kirjuta programm, mis küsib kasutajalt failinime kujul “failinimi.ext” (
#ext - extension - faili laiend) ja prindib välja laiendi (“ext”). (str.split)

filename = ''
while '.' not in filename:
    filename = input('Sisesta failinimi kujul “failinimi.ext” (ext - extension - faili laiend): ')
extension = filename.split('.')
print(extension)