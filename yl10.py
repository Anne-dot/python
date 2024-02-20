#Kirjuta programm, mis küsib kasutajalt nime, tervitab teda nimepidi, küsib kasutajalt elukoha, 
#kui elukoht on Saaremaa, siis väljastab mingi kommentaari, küsib kasutajalt vanuse, kui vanus 
#on väiksem kui 18, siis ütleb, et kasutaja on liiga noor, et autot juhtida, kui vanus on 18, 
#siis õnnitleb täisealiseks saamise puhul, kui kasutaja on vanem kui 18, siis ütleb, et 
#kasutaja võib autot juhtida. (sõne - string)
name = input('Palun sisesta oma nimi: ')
print('Tere,', name + '!')
location = input('Palun kirjuta, kus sa elad: ')
if 'saaremaa' in location.lower():
    print('Miks kogunevad saarlased äikese ilmaga Saaremaa põhjarannikule? Sest nad arvavad, et hiidlased teevad nendest pilti.')
age = float(input('Sisesta oma vanus: '))
if age < 18:
    print('Sa oled kahjuks liiga noor, et autot juhtida.')
elif age == 18:
    print('Palju õnne täisealiseks saamise puhul!')
else:
    print('Võid autot juhtida küll! Kui oled kaine.')
    