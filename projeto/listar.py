from transacoes import informacoes

def listar_transacoes():
    if not informacoes:
        print("Ainda não há informações aqui. ")
        return
    
    for ordem, valor in enumerate(informacoes, 1):
        print(f"{ordem}) - {valor["data"]} - {valor["tipo"]} - {valor["valor"]} - {valor["descrição"]} - {valor["categoria"]}")