import pandas as pd
from bancos_api_app.models import Instituicao

def importar_dados_excel(nome_arquivo):
    dados_excel = pd.read_excel(nome_arquivo)
    
    for index, linha in dados_excel.iterrows():
        # Criar uma instância do modelo Django com base nos dados da linha da planilha
        instancia_modelo = Instituicao(
            codigo_compensacao=linha['Código de compensação'],
            nome=linha['Nome Instituição']
        )
        # Salvar a instância do modelo no banco de dados
        instancia_modelo.save()

# Chame a função de importação com o nome do arquivo Excel
importar_dados_excel('bancos.xls')