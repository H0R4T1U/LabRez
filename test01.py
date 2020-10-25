def print_menu():
    print("\n"
          "1.Introdu Lista \n"
          "2. Nr cu cei mai putini divizori. \n"
          "3. Palindrom prim\n" 
          "4. Suma divizorilor numar prim"
          "5. Opreste programul"
          )


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# EX 1
def citire_lista():
    lista = []
    while True:
        numar=int(input("Scrieti un numar sau 00 pentru a va opri : "))
        if numar == 00:
            break
        lista.append(numar)
    return lista

# EX 2
def putini_divizori(lista):
    c = 9999
    for i in lista:
        if is_prime(i):
            if c>i:
                c = i
    if c == 9999:
        c = min(lista)

    return c


def test_putini_divizori():
    assert  putini_divizori([4,6,8,10]) == 4
    assert  putini_divizori([7,9,6,10]) == 7
    assert putini_divizori([1078,848,3600,1092]) == 848
    assert putini_divizori([7,23,13]) == 7

# EX 3
def ii_palindrom_prim(x):
    x = str(abs(int(x)))
    a = []
    b = []
    for i in range(len(x)):
        if is_prime(int(x[i])):
            a.append(x[i])
        else:
            break
    for i in range(len(x) - 1, -1, -1):
        if is_prime(int(x[i])):
            b.append(x[i])
        else:
            break

    if a == b:
        return True
    else:
        return False





def toti_palindromi_primi(lista):
    c = []
    for i in lista:
        if ii_palindrom_prim(i):
            c.append(i)
    return c


def test_toti_palindromi_primi():
    assert toti_palindromi_primi([1213, 56323, 7293, ]) == []
    assert toti_palindromi_primi([2222,5555,7293,]) == [2222,5555]

# EX 4
def get_all_divs(x):
    c = []
    for i in range(1,x):
        if x % i ==0:
            c.append(i)
    return c


def suma_divizori_prim(lista):
    c = []
    for i in lista:
        lista_divizori = get_all_divs(i)
        suma = 0
        for j in lista_divizori:
            suma +=j
        if is_prime(suma):
            c.append(i)
    return c

def test_suma_divizori_prim():
    assert suma_divizori_prim([4]) == [4]
    assert suma_divizori_prim([2]) == [2]
    assert suma_divizori_prim([4,2,64,125]) == [4,2,125]


def main():
    test_putini_divizori()
    test_toti_palindromi_primi()
    test_suma_divizori_prim()
    lista = []
    while True:
        print_menu()
        option = int(input(":"))
        if option == 1:
            lista = citire_lista()

        if option == 2:
            mic = putini_divizori(lista)
            print("Nr cu cei mai putini divizori este:"+str(mic))

        if option == 3:
            rezultat = toti_palindromi_primi(lista)
            print("Palindroamele alcatuite numai din nr prime sunt:",*rezultat)

        if option == 4:
            rezultat = suma_divizori_prim(lista)
            print("Numerele a caror suma de divizori este un nr prim sunt:", *rezultat)

        if option == 5:
            break


main()