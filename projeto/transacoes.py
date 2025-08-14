from datetime import datetime, date
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