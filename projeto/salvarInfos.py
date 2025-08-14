import json
import os
from datetime import datetime, date

ARQUIVO = "transacoes.json"

def carregar_transacoes():
    try:
        if os.path.getsize(ARQUIVO) == 0:
            return []
        
        with open(ARQUIVO, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            for arquivos in dados:
                arquivos["data"] = datetime.strptime(arquivos["data"], "%d/%m/%Y").date()
            return dados
    except FileNotFoundError:
        return []
    
def salvar_transacoes(transacoes):
    with open(ARQUIVO, 'w', encoding='utf-8') as file:
        dados = []
        for itens in transacoes:
            itens_copy = itens.copy()

            if isinstance(itens_copy["data"], (datetime, date)):
                itens_copy["data"] = itens_copy["data"].isoformat()
            else:
                pass

            dados.append(itens_copy) 

        json.dump(dados, file,ensure_ascii=False, indent=4)