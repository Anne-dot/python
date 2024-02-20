#Kivi-paber-käärid mäng. 
# Arvuti mõtleb välja ühe variandi - kivi, paber või käärid. 
# Arvuti küsib kasutaja valikut. Programm ütleb, kes võitis.

import random

def single_game():
    
    choose_from_here = ["kivi", "paber", "käärid"]

    computer_choice = random.choice(choose_from_here)

    user_choice = input("Kivi, paber või käärid? ").lower()
    print(user_choice)

    while user_choice not in (choose_from_here):
        user_choice = input("See polnud valikute hulgas. Paku uuesti. ").lower()
        
    # Who wins - VIIGI PUHUL LÄHEB computer-wins lappesse
    
    message1 = "Mul oli " + computer_choice + " ja sul oli " + user_choice + "."
    
    if computer_choice == user_choice:
        message2 = "Jäime viiki."
    elif computer_choice == choose_from_here[0] and user_choice == choose_from_here[1] or computer_choice == choose_from_here[1] and user_choice == choose_from_here[2] or computer_choice == choose_from_here[2] and user_choice == choose_from_here[0]:
        message2 = "Palju õnne! Sina võitsid!"
    else:
        message2 = "Mina võitsin. Nanananaaa"
        
    print(message1 + "\n" + message2)       
    
# Täienda programmi nii, et mängitakse seni, kuni kasutaja ei taha enam mängida.

def multigame():
    
    continue_playing = True
    
    while continue_playing:
        single_game()
        user_answer = input("Kas sa soovid uuesti mängida? y/n ").lower()
        if user_answer != "y":
            continue_playing = False
    
    print("Sinuga oli tore mängida :) Head aega!")

#single_game()    
multigame()