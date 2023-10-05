#Koosta tõeväärtustabel kahele avaldisele
#A AND (B OR C)
#(A  B) OR NOT(C AND A)

a,b,c = 1,0,1

print(bool(a) and (bool(b) or bool(c)))
print(bool(a) and bool(b)) or not (bool(c) and bool(a))