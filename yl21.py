#Arvu arvamise mäng. Arvuti mõtleb välja arvu nullist sajani. 
# Lase kasutajal pakkuda, mis arvu arvuti välja mõtles. 
# Vale pakkumise korral annab arvuti vihje, kas pakkumine on õigest arvust suurem või väiksem. 
# Pakkuda saab seni, kuni kasutaja on õige arvu pakkunud. (juhuarv - random)


import random

def user_guess(start_num, end_num):
    # Ask for user to guess the number - input
    # check if the input is valid - numeric, correct range, int
    
    guess = input("Arva, mis arvu peale ma mõtlen? Arv on vahemikus " + str(start_num) + " - " +str(end_num) + ": ")
    valid_type = guess.isnumeric() and int(guess) <= end_num and int(guess) >= start_num
    
    while not valid_type:
        guess = input("Sisesta arv vahemikus " + str(start_num) + " - " +str(end_num) + ": ")
        valid_type = guess.isnumeric() and int(guess) <= end_num and int(guess) >= start_num
    
    return int(guess)

def hint(start_num, end_num, random_number, guessed_number):
    # check if guess is lower or greater and give a hint
    
    while not guessed_number == random_number:

        if guessed_number < random_number:
            print("Minu arv on suurem. Paku uuesti: ")
        else:
            print("Minu arv on väiksem. Paku uuesti: ")
        
        guessed_number = user_guess(start_num, end_num)


# GAME

def guessing_game(start = 0, end = 100):
    
    # Generate a random number within the bounds
    random_number = random.randrange(start, end + 1)
    print(random_number)
    
    # Ask user for user input and validate the answer
    guessed_number = user_guess(start, end)
    
    # Check if guess is correct. Give hints until the user guesses correctly
    guess_correct = (random_number == guessed_number)
    
    if not guess_correct:
        hint(start, end, random_number, guessed_number)
        
    print("Palju õnne! Arvasid ära! Minu arv on " + str(random_number))
    
    
guessing_game()

