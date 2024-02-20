#Leia muutuja abil etteantud tekstis olevate täishäälikute (a, e, i, o, u, õ, ä, ö, ü) arv. 

def vowel_counter(text):
    
    counter = 0
    
    for character in text:
        if character.lower() in "aeiouõäöü":
            counter += 1
    
    print(counter)
    
text1 = "" # -> 0
text2 = "klm" # -> 0
text3 = "abcde" # -> 2
text4 = "AE" # -> 2
text5 = "See on väikeste ja SUURTE tähtedega tekst" # -> 16

vowel_counter(text5)