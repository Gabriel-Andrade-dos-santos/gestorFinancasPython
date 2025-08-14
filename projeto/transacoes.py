from datetime import datetime, date
#Criar um arquivo onde será salvo as infomações
from salvarInfos import carregar_transacoes, salvar_transacoes

informacoes = carregar_transacoes()




def adicionar_transacoes():
    print("\n-----Adicionar transaões-----")
    tipo = input("Qual transação deseja registrar (ENTRADA/SAIDA)").strip().lower()
    if tipo not in ["entrada", "saida"]:
        print("Opção inválida, digite novamente. \n")
        return
    
    try:
        valor = float(input("Valor (EX:120.50): "))
        print()
    except ValueError:
        print("Valor inválido! Digite números. ")

    descricao = input("Descreva a transação: ")
    categoria = input("Categoria da transação: ")
    data_str = input("DATA (dd/mm/aaaa) ou deixe em branco para data atual: ").strip()

    if data_str:
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            data_formatada = data.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida ")
            return
    else:
        data = datetime.today().date()
        data_formatada = data.strftime("%d/%m/%Y")

    transacao = {
        "tipo" : tipo,
        "valor" : valor,
        "descrição" : descricao,
        "categoria" : categoria,
        "data" : data_formatada
    }

    informacoes.append(transacao)
    salvar_transacoes(informacoes)
    print("✅ Transação adicionada com sucesso!\n") 
    return



def listar_transacoes():
    if not informacoes:
        print("Ainda não há informações aqui. ")
        return
    
    for ordem, valor in enumerate(informacoes, 1):
        print(f"{ordem}) - {valor["data"]} - {valor["tipo"]} - {valor["valor"]} - {valor["descrição"]} - {valor["categoria"]}")



def exibir_resumo_mes():
    print("---RESUMO DO MÊS---")
    if not informacoes:
        print("Não há resumos. ")
        return
    
    transacao_filtrada = []
    mes = input("Mês mm: ").zfill(2)
    ano = input("De que ano aaaa: ")

    try:
        mesInt = int(mes)
        anoInt = int(ano)
    except ValueError:
        print("valor de mês e/ou ano inválido. ")
        return
    
    for info in informacoes:
        data = info["data"]
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                continue

        if data.month == mesInt and data.year == anoInt:
            transacao_filtrada.append(info)

    if not transacao_filtrada:
            print("Não há nenhum registro. ")
            return
        
    entrada = sum(item["valor"] for item in transacao_filtrada if item["tipo"] == "entrada")
    saida = sum(item["valor"] for item in transacao_filtrada if item["tipo"] == "saida")
    resumoMensal = entrada - saida

    print(f"\n---Saldo do mês {mesInt}/{anoInt}--- \n")
    print(f"Entradas: R${entrada:.2f} ")
    print(f"Saídas: R${saida:.2f} ")
    print(f"Saldo mensal: {resumoMensal:.2f}\n")

    if resumoMensal > 0:
        print(f"Você terminou o mês de {mesInt}/{anoInt} com valor positivo de R${resumoMensal:.2f}")
        
    elif resumoMensal == 0:
        print(f"Não há sobras nem dívidas no mês {mesInt}/{anoInt}. ")
            
    else:
        print(f"Você terminou o mês de {mesInt}/{anoInt} com uma dívida de R${resumoMensal:.2f}")



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