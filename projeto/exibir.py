from transacoes import informacoes
from datetime import datetime

def exibir_resumo_mes():
    print("---RESUMO DO MÊS---")
    if not informacoes:
        print("Não há resumos mensais. ")
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

def exibir_resumo_ano():
    print("---RESUMO DO ANO---")
    if not informacoes:
        print("Não há resumos anuais. ")
        return
    transacao_filtrada = []
    ano = input("Digite o ano de visualização dos resumos: ")

    try:
        anoInt = int(ano)
    except ValueError:
        print("Ano digitado inválido! \n")
        return
    
    for info in informacoes:
        data = info["data"]
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                return
        if data.year == anoInt:
            transacao_filtrada.append(info)
    
    if not transacao_filtrada:
            print("Não há nenhum registro. ")
            return
    
    entrada = sum(item["valor"] for item in transacao_filtrada if item["tipo"] == "entrada")
    saida = sum(item["valor"] for item in transacao_filtrada if item["tipo"] == "saida")
    resumoAnual = entrada - saida

    print(f"Saldo do ano {anoInt}. ")
    print(f"Entradas -> {entrada:.2f}")
    print(f"Saídas -> {saida:.2f}")
    print(f"Resumo anual -> {resumoAnual:.2f}")

    if resumoAnual > 0:
        print(f"Você terminou o ano de {anoInt} com valor positivo de R${resumoAnual:.2f}")
        
    elif resumoAnual == 0:
        print(f"Não há sobras nem dívidas no ano de {anoInt}. ")
            
    else:
        print(f"Você terminou o ano de {anoInt} com uma dívida de R${resumoAnual:.2f}")

def exibir_resumos():
    print("Digite qual resumo deseja visualizar. ")
    escolha = input("Digite MÊS ou ANO: ").lower()

    if escolha == "mês":
        exibir_resumo_mes()

    elif escolha == "ano":
        exibir_resumo_ano()

    else:
        print("Informação inválida! Digite MÊS ou ANO")
        print("para selecionar uma visualização. ")
        print()
        return