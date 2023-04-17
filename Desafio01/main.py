import func

while(True):
    print("---DECOMPONDO NUMERO---")
    print("1 -> Achar número")
    print("0 -> Sair")
    op = int(input("Opção escolhida: "))
    if(op == 0): break
    elif(op == 1):
        print('===================')
        maxDigit = int(input("Entre com o valor maximo para o digito: "))
        print('=================== \nOs números gerados foram: ')
        nums = func.decompondoNumero(maxDigit)
        for num in nums:
            print(f"-> {num}")
        print("====================\n")
