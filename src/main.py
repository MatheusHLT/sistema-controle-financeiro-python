def adicionar_transacao(tipo):
    descricao = input("Descrição: ")

    while True:
        valorTexto = input("Valor: R$ ")

        try:
            valor = float(valorTexto.replace(",", "."))

            if valor <= 0:
                print("O valor deve ser maior que zero. Tente novamente.")
                continue

            break

        except ValueError:
            print("Valor inválido! Digite um número adequado.")

    categoria = input("Categoria: ")

    print("\nTransação cadastrada!")
    print(f"Tipo: {tipo.capitalize()}")
    print(f"Descrição: {descricao}")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Categoria: {categoria}")

while True:
    print("\n" + "="*40)
    print("SISTEMA DE CONTROLE FINANCEIRO".center(40))
    print("="*40 + "\n")

    print("1 - Adicionar receita")
    print("2 - Adicionar despesa" + "\n")

    print("3 - Listar transações")
    print("4 - Buscar transação")
    print("5 - Editar transação")
    print("6 - Remover transação" + "\n")

    print("7 - Exibir saldo")
    print("8 - Exibir resumo financeiro" + "\n")

    print("0 - Sair" + "\n")

    try:
        opt = int(input("Escolha uma opção: "))
    except ValueError:
        print("\nErro: Digite apenas números inteiros!\n")
        continue
        
    match opt:
        case 0:
            print("Encerrando o programa...")
            break
        case 1:
            adicionar_transacao("receita")
        case 2:
            adicionar_transacao("despesa")
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case _:
            print("\nOpção inválida.\n")