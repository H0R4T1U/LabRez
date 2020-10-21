import datetime  # modul care ofera functii pentru a lucra cu date


def timp_trait(data):
    date_obj = datetime.datetime.strptime(data, "%d/%m/%Y")  #functie din librăria datetime care converteşte un şir de caractere într-o dată(obiect datetime)
    acum = datetime.datetime.now()
    traiti = acum - date_obj
    return traiti

print("Apasă Q ca să inchizi programul")
date = input("Introdu data naşterii: ")

while date.lower() != "q":
    zile = timp_trait(date).days
    if zile >= 0:
        print('Ai trait {} zile!'.format(zile))
    else:
        print("Încă nu te-ai născut.")
    print("-----------------------------------------------------\n")
    print("Apasă Q ca să inchizi programul")
    date = input("Introdu data naşterii: ")


print("\nSfârşit program")