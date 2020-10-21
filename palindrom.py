def is_palindrom(x):
    x = str(abs(int(x)))
    a = []
    b = []
    for i in range(len(x)): 
        a.append(x[i])
    for i in range(len(x)-1,-1,-1):
        b.append(x[i])

    if a==b:
        return True
    else:
        return False


numar = input("Introdu numărul:  ")
while numar.lower() != "q":
    rezultat = is_palindrom(numar)
    if rezultat:
        print("Numărul introdus este un palindrom")
    else:
        print("Numărul introdus nu este un palindrom")

    print("-----------------------------------------------------\n")
    print("Apasă Q ca să inchizi programul")
    numar = input("Introdu numărul:  ")

print("\nSfârşit program")