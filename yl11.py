# Kirjuta programm, mis küsib kasutajalt sisendina stringi.
# # Eemalda selle sisendi algusest ja lõpust tühikud.
# String peab vastama tingimustele, et selles on vähemalt seitse sümbolit ja et 
# sümbolite arv on paarituarvuline.
# Väljasta selle stringi kolm keskmist sümbolit.
# (stringi meetodid, list)

user_input = (input('Sisesta vähemalt 7 sümboli pikkune sõne, mille sümbolite arv on paaritu: ')).strip()
while not (len(user_input)%2) or (len(user_input) < 7):
    user_input = (input('Sisesta vähemalt 7 sümboli pikkune sõne, mille sümbolite arv on paaritu: ')).strip()

midpoint = len(user_input)//2
print(user_input[midpoint-1:midpoint+2])
