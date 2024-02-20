#Kirjuta programm, mis küsib kasutajalt täisarvu n vahemikus 1-9. 
#Arvuta n + nn + nnn väärtus ja väljasta see. (Näiteks kui kasutaja sisestab 2, 
#siis on vaja väljastada tulemus 2 + 	22 + 222 = 246). Ära kasuta korrutamistehet. 
#Ülesanne on lahendatav ainult liitmise operaatorit kasuades.

int1 = (input('Sisesta täisarv vahemikus 1-9: '))
int2 = int1 + int1
int3 = int2 + int1
answer = int(int1) + int(int2) + int(int3)

print(int1, '+', int2, '+', int3, '=', answer) 

