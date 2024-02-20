#Kirjuta programm, mis ütleb, kas kasutaja poolt etteantud täisarv on paarisarv või mitte. 
#(paarisarvu mõiste - odd/even)


num = int(input('Sisesta üks arv: '))
if num % 2:
    answer = 'paaritu.'
else:
    answer = 'paaris.'
print('Sisestatud arv on', answer)

# Siinse ülesande raames on 0 paarisarvude hulka loetud.