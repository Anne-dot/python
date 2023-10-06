#Kirjutada programm, mis kontrollib, kas antud positiivne täisarv on liig- või lihtaasta 
#number.
#Aasta on liigaasta kui ta jagub neljasajaga või jagub neljaga ja ei jagu sajaga.

def leap_year(num):

    if not num%400 or (not num%4 and num%100):
        print('Aasta on liigaasta')
    else:
        print('Aasta on lihtaasta')

year = 405
leap_year(year)