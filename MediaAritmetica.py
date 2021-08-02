nota1 = float(input("Digite a primeira nota: "))
if nota1 > 10:
    print("A nota deve ser menor que 10")
else:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 > 10:
        print("A nota digitada deve ser menor que 10")
    else:
        nota3 = float(input("Digite a terceira nota: "))
        if nota3 > 10:
            print("A nota digitada deve ser menor que 10")
        else:    
            nota4 = float(input("Digite a quarta nota: "))
            if nota4 > 10:
                print("A nota digitada deve ser menor que 10")
            else:
                totalnota = float(nota1) + float(nota2) + float(nota3) + float(nota4)
                média = float(totalnota / 4)
                print ("A média aritmética é:",média)