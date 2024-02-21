#https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.

input_dict = {
    "Revenue" : {
        "users" : ["Frank", "Jane"],
        "tea" : [120, 145],
        "coffee": [243, 265],
        },
    "Expenses" : {
        "users" : ["Frank", "Jane"],
        "tea" : [130, 59],
        "coffee": [143, 198],
        },
    }

for i in input_dict:
    print(input_dict[i])

# Description

# You're a regional manager for an office beverage sales company, and right now you're in charge of paying 
# your sales team they're monthly commissions.

# Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, 
# with no commission for any product to total less than zero.

# Input Description

# You'll be given two matrices showing the sales figure per salesperson for each product they sold, and the 
# expenses by product per salesperson. Example: 

"""Revenue 

        Frank   Jane
Tea       120    145
Coffee    243    265

Expenses

        Frank   Jane
Tea       130     59
Coffee    143    198"""

# Output Description

#Your program should calculate the commission for each salesperson for the month. Example: 

"""
                Frank   Jane
Commission       6.20   9.49
"""

# Challenge Input

# Revenue
"""
            Johnver Vanston Danbree Vansey  Mundyke
Tea             190     140    1926     14      143
Coffee          325      19     293   1491      162
Water           682      14     852     56      659
Milk            829     140     609    120       87

Expenses

            Johnver Vanston Danbree Vansey  Mundyke
Tea             120      65     890     54      430
Coffee          300      10      23    802      235
Water            50     299    1290     12      145
Milk             67     254      89    129       76
"""

#Challenge Output
"""
            Johnver Vanston Danbree Vansey  Mundyke
Commission       92       5     113     45       32
"""
