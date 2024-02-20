# Koosta dictionary vähemalt viie endale iseloomuliku tunnusega 
# (näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
my_dictionary = {
    "eesnimi": "Anne",
    "perenimi": "Ruusmann",
    "sünniaasta": 1986,
    "elukoht": "Kuressaare",
    "lemmik magustoit": "jäätis"
}

# Väljasta elukoht kahel erineval viisil (kasutades get() meetodit ja mitte kasutades seda).
print(my_dictionary.get("elukoht"))
print(my_dictionary["elukoht"])

# Muuda magustoidu väärtust.
my_dictionary["lemmik magustoit"] = "smuuti"

# Tee kordus üle dictionary ja väljasta kõik võtmed.
for i in my_dictionary:
    print(i)
    
# Tee kordus üle dictionary ja väljasta kõik väärtused (pööra tähelepanu sellele, et saab mitmel viisil, 
# proovi erinevaid võimalusi).
for i in my_dictionary:
    print(my_dictionary[i])
    
for i in my_dictionary:
    print(my_dictionary.get(i))

# Kontrolli, kas isikukood on dictionary's olemas.
print("isikukood" in my_dictionary)

# Leia dictionary suurus (elementide arv).
print(len(my_dictionary))

# Lisa element enda pikkuse jaoks.
my_dictionary["pikkus"] = 171

# Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
removed_value = my_dictionary.pop("sünniaasta")

# Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
# Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
# Tutvu kõigi dictionary meetoditega.
# Läbi ülesanne juhendi lõpus.
# https://www.w3schools.com/python/python_dictionaries.asp
