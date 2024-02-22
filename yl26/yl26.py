#https://www.reddit.com/r/dailyprogrammer/comments/8xzwl6/20180711_challenge_365_intermediate_sales/

#Lisatasu arvutamise ülesanne. Alusta algoritmi koostamisest. 
# Kommentaarides on kah lahendused, aga proovi ise lahendada. 
# Defineeri lisatasu arvutamise funktsioon. Sisendina defineeri dictionary.

# loe failist andmed
# töötle andmed kojule 
names_list = ["Frank", "Jane"]

sales_dictionary = {
    "Frank": ((120, 130), (243, 143)),
    "Jane" : ((145, 59), (265, 198)),
}

prod_rev_exp = sales_dictionary["Frank"][1]
commission = 0.062
#print(prod_rev_exp)

def calculate_commission(prod_rev_exp, commission): #
    
    revenue = prod_rev_exp[0]
    expenses = prod_rev_exp[1]
    if revenue > expenses:
        return (revenue - expenses) * commission
    else:
        return 0

def commission_dict (sales_dict):
    
    commission_dict = {}

    for i in sales_dictionary:
        commission = 0
        for j in range(len(sales_dictionary[i])):
            commission += (calculate_commission(sales_dictionary[i][j],))
            commission_dict[i] = commission
    
    return (commission_dict)

print(calculate_commission(prod_rev_exp, commission))
#print(commission_dict(sales_dictionary))