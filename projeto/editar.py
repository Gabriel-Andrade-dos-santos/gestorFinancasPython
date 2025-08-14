from transacoes import informacoes
from datetime import datetime
from listar import listar_transacoes
from salvarInfos import salvar_transacoes

def editar_transacoes():
    print("---EDITOR DE TRANSAÇÕES---")
    if not informacoes:
        print("Não há informações para edição")
        return
    listar_transacoes()

    try:
        indice = int(input("Digite o índice que deseja editar: "))
        print()

        if 1 <= indice <= len(informacoes):
            info = informacoes[indice -1]
            print(f"Editando: {info["descrição"]} - R${info["valor"]:.2f}")

            novo_tipo = input(f"Digite o novo tipo: (ENTER - Para manter -> {info["tipo"]} <- )")
            if novo_tipo:
                info["tipo"] = novo_tipo

            novo_valor = input(f"Novo valor: (ENTER - Para manter -> {info['valor']} <- )  ")
            if novo_valor:
                info["valor"] = float(novo_valor)

            nova_descricao = input(f"Digite a nova descrição: (ENTER- Para manter -> {info["descrição"]} <- )")
            if nova_descricao:
                info["descrição"] = nova_descricao

            nova_categoria = input(f"Digite a nova categoria: (ENTER - Para manter -> {info["categoria"]} <- )")
            if nova_categoria:
                info["categoria"] = nova_categoria

            nova_data = input(f"Digite a nova data (dd/mm/aaaa): ENTER - Para manter -> {info["data"]} <- ")
            if nova_data:
                try:
                    info["data"] = datetime.strptime(nova_data, "%d/%m/%Y").date()
                except ValueError:
                    print("⚠️ Data inválida. Mantendo a original.")
                    #return
                    
                salvar_transacoes(informacoes)
                print("✅ Transação atualizada com sucesso!")
            else:
                 print("Índice inválido.")
    except ValueError:
        print("Digite um índice válido! ")
        #return