entrada = int(input("Digite um numero inteiro: "))

dezena = int(entrada % 100)
digitodezena = int((entrada % 100) // 10)

print("O dígito das dezenas é",digitodezena)