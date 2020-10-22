def print_meniu():
    print("1.Citire lista: ")
    print("2.Afisare cea mai lunga subsecventa de numere divizibile cu 10: ")
    print("3.Iesire program.")


def citire_lista():
    list = []
    n = int(input("Cititi numarul de elemente: "))
    for i in range(n):
        list.append(int(input()))
    return list

def subsecv(list):
    '''
    Determina cea mai lunga subsecventa de numere divizibile cu 10 dintr-o lista
    :param list: lista de numere intregi
    :return: lista cu cea mai lunga subsecventa de numere divizibile cu 10 dintr-o lista
    '''
    secv=[]
    secv_max=[]
    for x in list:
        if x%10 == 0:
            secv.append(x)
        else:
            secv.clear()
        if len(secv) > len(secv_max):
            secv_max = secv[:]
    return secv_max

def test_subsecv():
    assert subsecv([1,2,3,4]) == []
    assert subsecv([10,20,3,10,20,30,40,5]) == [10,20,30,40]
    assert subsecv([4,5,10,20,5]) == [10,20]

def toate_nr_div_cu_10(list):
    '''
    determina daca o lista este formata doar din nr. divizibile cu 10
    input: list - o lista de nr. intregi
    output: True, daca lista este formata doar din nr. divizibile cu 10, False in caz contrar
    '''
    for x in list:
        if x % 10 != 0:
            return False
    return True

def test_toate_nr_div_cu_10():
    assert toate_nr_div_cu_10([50,6,70]) == False
    assert toate_nr_div_cu_10([50,60,70]) == True

def subsecv2(list):
    '''
    Determina cea mai lunga subsecventa de numere divizibile cu 10 dintr-o lista
    :param list: lista de numere intregi
    :return: lista cu cea mai lunga subsecventa de numere divizibile cu 10 dintr-o lista
    '''
    secv_max = []
    for i in range(len(list)):
        for j in range(i,len(list)):
            if toate_nr_div_cu_10(list[i:j+1]) and len(list[i:j+1]) > len(secv_max):
                secv_max = list[i:j+1]
    return secv_max

def test_subsecv2():
    assert subsecv2([1,2,3,4]) == []
    assert subsecv2([10,20,3,10,20,30,40,5]) == [10,20,30,40]
    assert subsecv2([4,5,10,20,5]) == [10,20]

def main():

    test_subsecv()
    test_toate_nr_div_cu_10()
    test_subsecv2()
    list = []
    while True:
        print_meniu()
        option = int(input("Alegeti optiunea:"))
        if option == 1:
            list = citire_lista()
        elif option == 2:
            print(subsecv(list))
            print(subsecv2(list))
        elif option == 3:
            break
        else:
            print("optiune invalida ! Reincercati !")


main()