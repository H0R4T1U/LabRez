def print_meniu():
    print("1.Citire lista:")
    print("2.Afisare numere prime:")
    print("3.Iesire program.")


def citire_lista():
    list = []
    n = int(input("Cititi numarul de elemente: "))
    for i in range(n):
        list.append(int(input()))
    return list


def prim(p):
    """
    Determina daca un nr este prim.
    input -p- un numar intreg
    :return: True daca numarul este prim, False in caz contrar.
    """
    if p < 2:
        return False

    else:
        for i in range(2, p // 2 + 1):
            if p % i == 0:
                return False
    return True


def test_prim():
    assert prim(5) == True
    assert prim(4) == False
    assert prim(-3) == False


def get_numere_prime(list):
    """
    Determina numerele prime dintr-o lista.
    input - list - o lista de numere
    :return: - lista_numere_prime - o lsita cu nr prime
    """
    lista_numere_prime = []
    for element in list:
        if prim(element):
            lista_numere_prime.append(element)
    return lista_numere_prime


def test_get_numere_prime():
    assert get_numere_prime([3, 4, 5]) == [3, 5]
    assert get_numere_prime([-3, 4, 5]) == [5]
    assert get_numere_prime([-3, 4, 6]) == []


def main():
    list = []
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            list = citire_lista()
        elif option == 2:
            rezultat = get_numere_prime(list)
            print(rezultat)
        elif option == 3:
            break
        else:
            print("optiune invalida ! Reincercati !")


test_prim()

test_get_numere_prime()

main()