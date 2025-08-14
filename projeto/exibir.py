from transacoes import informacoes
from datetime import datetime

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