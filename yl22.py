#Kivi-paber-käärid mäng. 
#Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.
#Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

def game_choices():
    a = 'kivi'
    b = 'paber'
    c = 'käärid'
    choices = [a,b,c]

    from random import choice
    computer = choice(choices)
    user_input = input('Mängime kivi, paber, käärid. Mis sa valid?: ')
    while user_input.lower() not in choices:
        user_input = input('Ma ei saanud sinu valikust aru, palun kirjuta uuesti: ')

    print('Mina valisin', computer + '. Sina valisid', user_input + '.')
    return(computer, user_input)

def game_result(c,u)
    if c == u:
        print('Jäime viiki :)')

def game_new():
    new_game = input('Kas tahad veel mängida? y/n: ')
    return new_game == 'y'

# a < b and a > c
# b < c
# a == a, b == b, 

