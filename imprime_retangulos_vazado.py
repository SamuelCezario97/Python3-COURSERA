largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))


while largura > 0:
    if altura == 1:
        print("#" * largura,end="\n")
        largura = 0
    else:
        if altura == 2:
                print("#" * largura,end="\n")
                print("#" * largura,end="\n")
                largura = 0
        else:
            if altura == 3:
                altura = 2
                print(largura * "#")
                while altura > 0:
                    print("#"," " * (largura - 4),"#",end="\n")
                    altura = altura - 2
                print(largura * "#")
                largura = 0
            else:
                if altura > 3:
                    print(largura * "#")
                    altura = altura - 2
                    while altura > 0:
                        print("#"," " * (largura - 4),"#",end="\n")
                        altura = altura - 1
                    print(largura * "#")
                    largura = 0
