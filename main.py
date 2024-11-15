from math import *
from  decimal import Decimal

def checar_casas_decimais(n):
    str_num = str(n)
    
    if '.' not in str_num:
        return False
        
    casa_decimal = str_num.split('.')[1]
    
    return len(casa_decimal) > 3

def menu():
  while True:
    opcao = int(input("Digite a quantidade de polarizadores(2 ou 3, 0 para sair): "))
    

    if opcao == 2:
      menu2()
      print()
    elif opcao == 3:
      menu3()
      print()
    elif opcao == 0:
        print("Saindo...")
        break

def menu2():
    print()
    while True:
        print("1 - Itensidade original")
        print("2 - Itensidade ao passar pelo primeiro polarizador")
        print("3 - Itensidade ao passar pelo segundo polarizador")
        print("0 - Voltar\n")
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
            print("Voltando...")
            break

def menu3():
    print()
    while True:
        print("1 - Itensidade original")
        print("2 - Itensidade ao passar pelo primeiro polarizador")
        print("3 - Itensidade ao passar pelo segundo polarizador")
        print("4 - Itensidade ao passar pelo terceiro polarizador")
        print("0 - Voltar\n")
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
        elif opcao == 4:
            i3_3()
            print()
        elif opcao == 0:
            print("Voltando...")
            break

def i0_2():
    print()
    print("Entre com a intensidade inicial (W/cm²): ")
    i0 = float(input())    
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta =  radians(float(input()))

    i1 = i0/2
    i2 = i1*( cos(theta)**2)

    print(f'Intensidade ao passar pelo primeiro polarizador: {Decimal(i1):.3} W/cm²' 
          if checar_casas_decimais(i1) else f'Intensidade ao passar pelo primeiro polarizador: {i1} W/cm²')
    print(f'Intensidade ao passar pelo segundo polarizador: {Decimal(i2):.3} W/cm²' 
          if checar_casas_decimais(i2) else f'Intensidade ao passar pelo segundo polarizador: {i2} W/cm²')

def i1_2():
    print()
    print("Entre com a intensidade ao passar pelo primeiro polarizador (W/cm²): ")
    i1 = float(input())
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta = radians(float(input()))

    i0 = i1*2
    i2 = i1*( cos(theta)**2)

    print(f'Intensidade original: {Decimal(i0):.3} W/cm²' 
          if checar_casas_decimais(i0) else f'Intensidade original: {i0} W/cm²')
    print(f'Intensidade ao passar pelo segundo polarizador: {Decimal(i2):.3} W/cm²' 
          if checar_casas_decimais(i2) else f'Intensidade ao passar pelo segundo polarizador: {i2} W/cm²')

def i2_2():
    print()
    print("Entre com a intensidade ao passar pelo segundo polarizador (W/cm²): ")
    i2 = float(input())
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta =  radians(float(input()))

    i1 = i2/(cos(theta)**2)
    i0 = i1*2

    print(f'Intensidade original: {Decimal(i0):.3} W/cm²' 
          if checar_casas_decimais(i0) else f'Intensidade original: {i0} W/cm²')
    print(f'Intensidade ao passar pelo primeiro polarizador: {Decimal(i1):.3} W/cm²' 
          if checar_casas_decimais(i1) else f'Intensidade ao passar pelo primeiro polarizador: {i1} W/cm²')

def i0_3():
    print()
    print("Entre com a intensidade inicial (W/cm²): ")
    i0 = float(input())    
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta2 =  radians(float(input()))
    print("Entre com o ângulo do terceiro polarizador (em graus): ")
    theta3 =  radians(float(input()))

    i1 = i0/2
    i2 = i1*( cos(theta2)**2)
    i3 = i2*( cos(theta3 - theta2)**2)

    print(f'Intensidade ao passar pelo primeiro polarizador: {Decimal(i1):.3} W/cm²' 
          if checar_casas_decimais(i1) else f'Intensidade ao passar pelo primeiro polarizador: {i1} W/cm²')
    print(f'Intensidade ao passar pelo segundo polarizador: {Decimal(i2):.3} W/cm²' 
          if checar_casas_decimais(i2) else f'Intensidade ao passar pelo segundo polarizador: {i2} W/cm²')
    print(f'Intensidade ao passar pelo terceiro polarizador: {Decimal(i3):.3} W/cm²' 
          if checar_casas_decimais(i3) else f'Intensidade ao passar pelo terceiro polarizador: {i3} W/cm²')

def i1_3():
    print()
    print("Entre com a intensidade ao passar pelo primeiro polarizador (W/cm²): ")
    i1 = float(input())  
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta2 =  radians(float(input()))
    print("Entre com o ângulo do terceiro polarizador (em graus): ")
    theta3 =  radians(float(input()))

    i0 = i1*2
    i2 = i1*( cos(theta2)**2) 
    i3 = i2*( cos(theta3 - theta2)**2)

    print(f'Intensidade original: {Decimal(i0):.3} W/cm²' 
          if checar_casas_decimais(i0) else f'Intensidade original: {i0} W/cm²')
    print(f'Intensidade ao passar pelo segundo polarizador: {Decimal(i2):.3} W/cm²' 
          if checar_casas_decimais(i2) else f'Intensidade ao passar pelo segundo polarizador: {i2} W/cm²')
    print(f'Intensidade ao passar pelo terceiro polarizador: {Decimal(i3):.3} W/cm²' 
          if checar_casas_decimais(i3) else f'Intensidade ao passar pelo terceiro polarizador: {i3} W/cm²')

def i2_3():
    print()
    print("Entre com a intensidade ao passar pelo segundo polarizador (W/cm²): ")
    i2 = float(input())  
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta2 =  radians(float(input()))
    print("Entre com o ângulo do terceiro polarizador (em graus): ")
    theta3 =  radians(float(input()))

    i1 = i2/( cos(theta2)**2)
    i0 = i1*2
    i3 = i2*( cos(theta3 - theta2)**2)

    print(f'Intensidade original: {Decimal(i0):.3} W/cm²' 
          if checar_casas_decimais(i0) else f'Intensidade original: {i0} W/cm²')
    print(f'Intensidade ao passar pelo primeiro polarizador: {Decimal(i1):.3} W/cm²' 
          if checar_casas_decimais(i1) else f'Intensidade ao passar pelo primeiro polarizador: {i1} W/cm²')
    print(f'Intensidade ao passar pelo terceiro polarizador: {Decimal(i3):.3} W/cm²' 
          if checar_casas_decimais(i3) else f'Intensidade ao passar pelo terceiro polarizador: {i3} W/cm²')
    
def i3_3():
    print()
    print("Entre com a intensidade ao passar pelo terceiro polarizador (W/cm²): ")
    i3 = float(input())  
    print("Entre com o ângulo do segundo polarizador (em graus): ")
    theta2 =  radians(float(input()))
    print("Entre com o ângulo do terceiro polarizador (em graus): ")
    theta3 =  radians(float(input()))

    i2 = i3/( cos(theta3 - theta2)**2)
    i1 = i2/( cos(theta2)**2)
    i0 = i1*2

    print(f'Intensidade original: {Decimal(i0):.3} W/cm²' 
          if checar_casas_decimais(i0) else f'Intensidade original: {i0} W/cm²')
    print(f'Intensidade ao passar pelo primeiro polarizador: {Decimal(i1):.3} W/cm²' 
          if checar_casas_decimais(i1) else f'Intensidade ao passar pelo primeiro polarizador: {i1} W/cm²')
    print(f'Intensidade ao passar pelo segundo polarizador: {Decimal(i2):.3} W/cm²' 
          if checar_casas_decimais(i2) else f'Intensidade ao passar pelo segundo polarizador: {i3} W/cm²')



print("Polarizadores de luz")

print("Autores:")
print("Kayna de Deus Ferreira da Silva")
print("Mario Eugenio Silva")
print()
print("------------------------------------------------------------------------------------")
print()
print("Quando uma luz nao polarizada passa por certos materiais (como filtros polarizadores) \n"
      "as oscilações podem ser limitadas a uma única direção, \n"
      "resultando em luz polarizada - similar a uma corda que pode vibrar em várias direções sendo forçada a \n"
      "vibrar em apenas uma direção específica, este processo acaba por afetar sua intensidade.")
print("O programa realiza os calculos das intensidades da luz em qualquer parte do circuito entre dois ou tres polarizadores")
print()
print("------------------------------------------------------------------------------------")
print()
menu()
