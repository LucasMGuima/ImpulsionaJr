def decompondoNumero(maxDigit: int) -> list:
    lstNums = list()
    # Retorna uma lista vazia se o maxDigit for menor ou igual a 5,
    # pos neste caso teriamos como maior numero possivel o 5555 que
    # geraria 5*4=20, sendo menor que 21
    if(maxDigit <= 5): return lstNums

    n_range = maxDigit + 1 #correção para usar range()

    for n1 in range(1,n_range):
        for n2 in range(n_range):
            for n3 in range(n_range):
                for n4 in range(n_range):
                    sum = n1 + n2 + n3 + n4
                    if(sum == 21):
                        #print(f"{n1}{n2}{n3}{n4} => {sum}")
                        num = int(f"{n1}{n2}{n3}{n4}")
                        lstNums.append(num)

    return lstNums