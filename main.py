import math
from  decimal import Decimal

def menu():
  while True:
    opcao = int(input("Digite a quantidade de polarizadores(2 ou 3): "))

    if opcao == 2:
      menu2()
      print()
    elif opcao == 3:
      menu3()
      print()
    elif opcao == 0:
        print("Saindo")
        break

def menu2():
    while True:
        print("1 - Itensidade original")
        print("2 - Itensidade ao passar pelo primeiro polarizador")
        print("3 - Itensidade ao passar pelo segundo polarizador")
        print("0- Sair\n")
        opcao = int(input("Digite a itensidade disponivel: "))

        if opcao == 1:
            i0_2()
            print()
        elif opcao == 2:
            i1_2()
            print()
        elif opcao == 3:
            i2_2()
            print()
        elif opcao == 0:
            print("Saindo...")
            break

def menu3():
    while True:
        print("1 - Itensidade original")
        print("2 - Itensidade ao passar pelo primeiro polarizador")
        print("3 - Itensidade ao passar pelo segundo polarizador")
        print("4 - Itensidade ao passar pelo terceiro polarizador")
        print("0- Sair\n")
        opcao = int(input("Digite a opcao desejada: "))

        if opcao == 1:
            i0_3()
            print()
        elif opcao == 2:
            i1_3()
            print()
        elif opcao == 3:
            i2_3()
            print()
        elif opcao == 3:
            i3_3()
            print()
        elif opcao == 0:
            print("Saindo...")
            break

def i0_2():
    print("i1 e i2")

def i1_2():
    print("i0 e i2")

def i2_2():
    print("i0 e i1")

def i0_3():
    print("i1, i2, i3")

def i1_3():
    print("i0, i2, i3")

def i2_3():
    print("i0, i1, i3")
    
def i3_3():
    print("i0, i1, i2")

menu()
