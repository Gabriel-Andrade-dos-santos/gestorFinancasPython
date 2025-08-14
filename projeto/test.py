from transacoes import *

def exibir_menu():
    print("\n---Gestor de finanças---\n")
    print("1 - Adicionar transações. ")
    print("2 - Listar transações. ")
    print("3 - Exibir resumos. ")
    print("4 - Editar transação do sistema.")
    print("5 - Excluir transação do sistema.")
    print("6 - Sair. ")

def main():
    while True:
        exibir_menu()
        escolha = input("\nDigite a opção desejada: ")
        print()
        try:    
            if escolha == '1':
                adicionar_transacoes()
            if escolha == '2':
                listar_transacoes()
            if escolha == '3':
                exibir_resumo_mes()
            if escolha == '4':
                editar_transacoes()
            if escolha == '5':
                ...
            if escolha == '6':
                print("Saiu do sistema. ")
                break
            else:
                print("Digite um dos valores acima. ")
                continue
        except ValueError:
            continue

if __name__ == "__test__":
    main()
