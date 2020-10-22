def print_menu():
    print("\n")
    print("1.Introdu lista")
    print("2.Cel mai lung palindrom")
    print("3.Cel mai scurt string care incepe cu o cifra")
    print("4.Toate string-urile formate din acelaşi caracter")
    print("5.Indexi numere prime")


def citire_lista():
    lista = []
    a = int(input("Cate elemente vrei sa adaugi: "))
    for i in range(a):
        n = str(input(":"))
        lista.append(n)

    return lista


def palindrom_lung(lista):
    a = []
    b = []
    c = ""
    for i in lista:
        for j in range(len(i)):
            a.append(i[j])
        for j in range(len(i)-1,-1,-1):
            b.append(i[j])
        if a == b :
            if len(i) > len(c):
                c = i
    return c


def test_palindrom_lung():
    assert palindrom_lung(["ana","aaaa"]) == "aaaa"


def string_cu_int(lista):
    c = 0
    for i in lista:
        if i[0].isdigit():
            if c:
                if len(i) < len(c):
                    c = i
            else:
                c = i
    return c


def test_string_cu_int():
    assert string_cu_int(["1abc","a","0bc"]) == "0bc"

"""
def string_cu_acelasi_char(lista):
    j=0
    c = []
    for i in lista:

        while j<len(i):
            if j+1 < len(i):
                if i[j] != i[j+1]:
                    
        j+=1
    return c


def test_string_cu_acelasi_char():
    assert string_cu_acelasi_char(["ana","aaaa"]) == "aaaa"
"""

def main():
    test_palindrom_lung()
    test_string_cu_int()
   # test_string_cu_acelasi_char()
    lista = []
    while True:
        print_menu()
        option = int(input(":"))
        if option == 1:
            lista = citire_lista()
        elif option == 2:
            print(palindrom_lung(lista))
        elif option == 3 :
            string_cu_int(lista)
        #elif option == 4 :

        #elif option == 5 :

        else:
            print("Introdu o optiune valida!")

main()