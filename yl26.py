#https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.

revenue_expenses = {
    "Revenue" : {
        "users" : ("Frank", "Jane"),
        "tea" : (120, 145),
        "coffee": (243, 265),
        },
    "Expenses" : {
        "users" : ("Frank", "Jane"),
        "tea" : (130, 59),
        "coffee": (143, 198),
        },
    }

revenue, expenses = "Revenue", "Expenses"
users = revenue_expenses[revenue]["users"]
len_users = len(users)

list_level2_keys = ()
print_list = ()
profit = []

# fill profit with ceroes
for i in range(len_users):
    profit.append(0)

# get keys for inner dictionaries
for i in revenue_expenses["Revenue"]:
    list_level2_keys += (i,)

#print(users)
#print(list_level2_keys)

for i in list_level2_keys:
    if i != "users":
#        print(i)
#        print(revenue_expenses[revenue][i])
#        print(revenue_expenses[expenses][i])
        for j in range(len_users):
            profit_for_product = int(revenue_expenses[revenue][i][j]) - int(revenue_expenses[expenses][i][j])
            if (profit_for_product > 0):
                profit[j] += profit_for_product * 0.062
#            profit = str(int(revenue_expenses[revenue][i][j] - int(revenue_expenses[expenses][i][j])))
#            print(users[j] + " profit for ..." + ": " + profit)

# Convert profit list of int -> list of str
for i in range(len_users):
    profit[i] = str(profit[i])

print("\t\t" + "\t".join(users))    
print("Commissions\t" + "\t".join(profit))    

    
def monthly_commissions(monthly_data):
    return 

# Description

# You're a regional manager for an office beverage sales company, and right now you're in charge of paying 
# your sales team they're monthly commissions.

# Sales people get paid using the following formula for the total commission: commission is 6.2% of profit, 
# with no commission for any product to total less than zero.

# Input Description

# You'll be given two matrices showing the sales figure per salesperson for each product they sold, and the 
# expenses by product per salesperson. Example: 

'''Revenue 

        Frank   Jane
Tea       120    145
Coffee    243    265

Expenses

        Frank   Jane
Tea       130     59
Coffee    143    198
'''

# Output Description

#Your program should calculate the commission for each salesperson for the month. Example: 

"""
                Frank   Jane
Commission       6.20   9.49
"""

# Challenge Input

ch_input = """ Revenue

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
print("\n")
list_lines = ch_input.split("\n")
dict_revenue = {}
counter = 1
for line in list_lines:
    counter += 1
#    print(counter)
    if len(line.strip().split()) == 1:
        print(line.strip())
        counter = -1
#        print(counter)
    
    elif counter == 1:
        print(line)

# ! kasuta readline ja siis tingimusi