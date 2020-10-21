# Functie care verifică dacă un număr este prim
def is_prime(n):
    for i in range(n-1, 1, -1):
        if n % i == 0:
            return False
    return True


def cel_mai_mare_prim(n):
    for i in range(n-1,1,-1):
        if is_prime(i):
            return i

print("Apasă Q ca să inchizi programul")
alegere = input("Alege un nr: ")

while alegere.lower() != "q":
    alegere = int(alegere)  # int(string) converteste un sir de caractere in numere

    if alegere > 1:
        rezultat = cel_mai_mare_prim(alegere)
        print("Cel mai mare nr prim mai mic ca si {} este {}".format(alegere,rezultat))
    else:
        print("Numarul trebuie sa fie mai mare ca 1")
    print("-----------------------------------------------------\n")  # Doar pentru aspect
    print("introdu Q ca să inchizi programul")
    alegere = input("Alege un nr: ")

print("\nSfârşit program")
