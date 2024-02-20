# yl13
# Küsi kasutajalt lemmikloom. Väljasta selle muutuja esimene täht.
# Koosta list, mis koosneb kolmest loomast.
# Lisa selle listi lõppu kasutaja sisestatud lemmikloom.
# Väljasta see lemmikloomade list.
# Väljasta listi viimase elemendi viimane täht.
# (sõne kui list, mitmemõõtmeline list - multi dimensional)

pet = input('Sisesta oma lemmik loom: ')
print(pet[0])
pets = ['jänes', 'koer', 'kass']
pets.append(pet)
print(pets)
print(pets[-1][-1])
