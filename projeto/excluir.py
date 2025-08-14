from transacoes import informacoes
from listar import listar_transacoes
from salvarInfos import salvar_transacoes

def excluir_transacoes():
    print("---EXCLUIR ITENS---")
    if not informacoes:
        print("Não há nada para excluir. ")
        return
    listar_transacoes()
    try:
        indice = int(input("Digite o índice que deseja excluir: "))
        print()

        if 1 <= indice <= len(informacoes):
            info = informacoes[indice -1]
        print(f"O item do índice {indice} com os itens: {info["tipo"]} - {info["valor"]} - {info["descrição"]} - {info["categoria"]} - {info["data"]}")
        print("Será excluído permanentemente")
        escolha = input("Tem certeza ? (S/N)").lower()
        if escolha == 's':
            removida = informacoes.pop(indice - 1)
            salvar_transacoes(informacoes)
            print(f"✅ Transação removida: {removida['descrição']} - R$ {removida['valor']:.2f}")
        elif escolha == 'n':
            print("Exclusão cancelada. ")
            return
        else:
            print("Caractére inválodo! ")
            
    except ValueError:
        print("Entrada inválida.")
        return