# Anna muutuja väärtuseks list kolmest oma lemmik puuviljast ja väljasta see
# Väljasta listi esimene väärtus
# Lisa listi lõppu uus puuvili
# Väljasta listi viimane väärtus
# Muuda ühe elemendi väärtust ja väljasta kogu list
# Kontrolli kas väärtus (näiteks õun) eksisteerib listis
# Väljasta listi pikkus
# Eemalda listist element ja väljasta kogu list
# Muuda listi järjekord vastupidiseks
# Sorteeri list ja väljasta
# (jada, list, listi element, listi meetodid)


fruits = ['apple', 'pear', 'plum'] #tegin listi
print(fruits) #väljastasin listi
print(fruits[0]) #1. element
fruits.append('orange') #lisasin lõppu ühe puuvilja
print(fruits[-1]) #väljastasin selle 
fruits[1] = 'coconut' #asendasin teise elemendi
print(fruits) #printisin listi
print('apple' in fruits) #kontroll, kas 'apple' on - True
print('pear' in fruits) #kontroll, kas 'pear on - False
print(len(fruits)) #nimekirja pikkus
fruits = fruits[1:] #eemaldasin 1. elemendi
print(fruits) #väljastasin nimekirja
fruits = fruits[::-1] #pöörasin ümber
print(fruits)
fruits = sorted(fruits)
print(fruits)