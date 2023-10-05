# Kirjuta programm, mis leiab kolmest kasutaja poolt sisestatud arvust maksimumi 
# (ära kasuta max funktsiooni). (loogikatehted - logic operators)

num1 = float(input('Sisesta üks arv: '))
num2 = float(input('Sisesta veel üks arv: '))
num3 = float(input('Sisesta kolmas ka: '))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

#Siin on eeldatud, et kõik arvud on erinevad, st pole ühesuguseid arve.