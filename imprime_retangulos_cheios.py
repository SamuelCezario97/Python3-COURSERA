largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while largura > 0:
    while altura > 0:
        print(largura * "#", end="\n")
        altura = altura - 1
    largura = 0