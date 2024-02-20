# Väljasta korduslause abil 8 korrutis arvudega 0..12 ja vorminda väljund nii:
#   8 x 0 = 0
#   8 x 1 = 8
#   8 x 2 = 16

# Täienda programmi nii, et kasutajalt küsitakse arv x, mille kohta korrutustabel väljastatakse

def multiply_by_8():
    number = 8
    answer = 0

    for i in range(13):
        answer = number * i
        print(str(number) + " x " + str(i) + " = " + str(answer))
        
#multiply_by_8()

def multiply():
    condition = False
    
    while not condition:
        user_answer = input("Palun sisesta üks arv: ")
        condition = user_answer.isnumeric()
        
    
    number = int(user_answer)
    answer = 0

    for i in range(13):
        answer = number * i
        print(str(number) + " x " + str(i) + " = " + str(answer))

multiply()