#Kolmnurki liigitatakse külgede pikkuse järgi erikülgseteks, võrdhaarseteks ja võrdkülgseteks. 
#Kirjutada programm, mis küsib kasutajalt kolme külje pikkused ning väljastab vastusena 
#kolmnurga liigi. Lisaks tuleb kontrollida, kas etteantud küljepikkustega kolmnurk saab 
#üldse eksisteerida. Külje pikkused ei pea olema täisarvud. (ujukomaarv - float)

a = float(input('Sisesta kolmnurga esimese külje pikkus: '))
b = float(input('Sisesta kolmnurga teise külje pikkus: '))
c = float(input('Sisesta kolmnurga kolmanda külje pikkus: '))

#kontrolli, kas selliste küljepikkustega kolmnurk on võimalik
nums_sort  = sorted((a, b ,c))
#kontrolli võimalikkust

if nums_sort[0] > 0 and nums_sort[2] < nums_sort[0] + nums_sort[1]:  #eksisteerib
    num_dif_sides = len(set(nums_sort))
    if num_dif_sides == 1:
        answer = 'võrgkülgne'
    elif num_dif_sides == 2:
        answer = 'võrdhaarne'
    else:
        answer = 'erikülgne'
    print('Kolmnurk on {}.'.format(answer))
else:
    print('Sellist kolmnurka ei eksisteeri')
    