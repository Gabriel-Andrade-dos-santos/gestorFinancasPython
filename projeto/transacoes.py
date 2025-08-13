from datetime import datetime, date
#Criar um arquivo onde será salvo as infomações
from salvarInfos import carregar_transacoes, salvar_transacoes

informacoes = carregar_transacoes()

def adicionar_transacoes():
    tipo = input("Qual transação deseja registrar (ENTRADA/SAIDA)").strip().lower()
    if tipo not in ["entrada", "saida"]:
        print("Opção inválida, digite novamente. \n")
        return
    
    try:
        valor = float(input("Valor (EX:120.50): "))
        print()
    except ValueError:
        print("Valor inválido! Digite números. ")

    descricao = input("Desvreva a transação: ")
    categoria = input("Categoria da transação: ")
    data_str = input("DATA (dd/mm/aaaa) ou deixe em branco para data atual: ")

    if data_str:
        try:
            data = datetime.strftime(data_str, "%d/%m/%Y").date()
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

    transacao.append(informacoes)
    salvar_transacoes(transacao)