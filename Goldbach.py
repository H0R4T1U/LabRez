# Conjectura lui Goldbach spune ca pentru orice numar mai mare ca 5 poate fi scris ca suma de nr prime,
# totusi problema aici te pune sa folosesti o alta formula creată de Euler care spune ca
# orice numar intreg par mai mare ca 3 poate fi scris ca suma de doua nr prime.
def is_prime(nr):
    for i in range(2,nr):
        if nr % i == 0 :
            return False
    return True


def cel_mai_mare_prim(nr):
    if nr %2 ==0 and nr > 2:
        for i in range(nr,1,-1):
            if is_prime(i):
                a= i
                b= nr-i

                if b!=1 and is_prime(b):
                    print("Numărul {} poate fi scris ca si suma a {} si {}, doua numere prime.".format(numar, a, b))
    else:
        print("Numarul trebuie sa fie par si mai mare decat 2!")


print("Apasă Q ca să inchizi programul")
numar = input("Introdu numărul : ")

while numar.lower() != "q":
    cel_mai_mare_prim(int(numar))
    print("-----------------------------------------------------\n")
    print("Apasă Q ca să inchizi programul")
    numar = input("Introdu numărul : ")


print("\nSfârşit program")