#Kirjuta programm, mis leiab kahest kasutaja poolt sisestatud arvust miinimumi 
#(ära kasuta min funktsiooni). (muutuja - variable, tingimus - condition, 
# if-lause - if statement)

num1 = input('Sisesta üks arv: ')
num1_f = float(num1)
num2 = (input('Sisesta teine arv: '))
num2_f = float(num2)
if num1_f > num2_f:
    print(num2)
elif num1_f < num2_f:
    print(num1)
else:
    print('Arvud on omavahel võrdsed.')
    