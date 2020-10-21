def get_all_numbers(x):  #Ia un numar si face rost de toate numerele din acesta si le adauga intr-o lista, dupa modelul: 233 -> 2,23,233
    x = str(x)
    a = []
    b = ""
    for i in range(len(x)):
        b+=str((int(x[i])%10))
        a.append(b)
    return a


def is_prime(nr): # Verifica daca un numar este prim
    for i in range(2,nr):
        if nr % i == 0 :
            return False
    return True


def is_superprime(list): #verifica daca un numar este superprim verificand daca fiecare numar din lista este prim
    for i in range(len(list)):
        nr = int(list[i])
        if not is_prime(nr):
            return False
    return True

numar = input("Introdu numărul:  ")
while numar.lower() != "q":
    numere = get_all_numbers(numar)

    if is_superprime(numere):
        print("Numărul introdus este un numar super prim")
    else:
        print("Numărul introdus nu este un numar super prim")

    print("-----------------------------------------------------\n")
    print("Apasă Q ca să inchizi programul")
    numar = input("Introdu numărul:  ")

print("\nSfârşit program")