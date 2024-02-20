# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

# UPC vöötkoodi kontrollsumma arvutamise ülesanne. 
# Alusta algoritmi koostamisest. Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri kontrollsumma arvutamise funktsioon. 
# (https://www.w3schools.com/python/python_functions.asp)

def upc_check_digits(code):
    
    # Code has to be with length 11, if less leading zeroes need to be added.
    leading_zeroes = 11 - len(code)
    updated_code = leading_zeroes * "0" + code
    
    sum_odd = 0
    for i in range(0, 11, 2):
        sum_odd += int(updated_code[i])

    result = sum_odd * 3
    
    sum_even = 0
    for i in range(1, 11, 2):
        sum_even += int(updated_code[i]) 
    
    result += sum_even
    
    m = result % 10
    
    if not m:
        return m
    else:
        return 10 - m
    
print(upc_check_digits("4210000526"))
print(upc_check_digits("3600029145"))
print(upc_check_digits("12345678910"))
print(upc_check_digits("1234567"))