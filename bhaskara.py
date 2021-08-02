import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    raiz1 = ( -b + math.sqrt(delta)) / (2 * a)
    print("A raiz desta equação é", raiz1)
else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        raiz1 = ( -b + math.sqrt(delta)) / (2 * a)
        raiz2 = ( -b - math.sqrt(delta)) / (2 * a)
        ordem = [raiz1,raiz2]
        print("As raízes da equação são", sorted(ordem))    
        
    