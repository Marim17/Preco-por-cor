from termcolor import cprint

j = True
i = True

while j:
    while i:
        print("Cores disponíveis para acessar preços: Verde, Azul, Amarelo, Vermelho")
        cd = input("Escolha uma das cores: ")
        cd = cd.lower().strip()

        if cd == "verde":
            cprint("R$9,99", 'green')
            i = False
        elif cd == "azul":
            cprint("R$19,99", 'blue')
            i = False
        elif cd == "amarelo":
            cprint("R$29,99", 'yellow')
            i = False
        elif cd == "vermelho":
            cprint("R$39,99", 'red')
            i = False
        else:
            print("Você não digitou uma das cores disponíveis")
            i = True
    consulta = input("Deseja fazer outra consulta? ")
    consulta.lower()
    if consulta == "sim":
        j = True
        i = True
    else:
        j = False
