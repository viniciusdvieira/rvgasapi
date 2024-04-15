import pandas as pd

import os
import sys
import django


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bancos_api_project.settings")
django.setup()

from bancos_api_app.models import Instituicao

def importar_dados_excel(nome_arquivo):
    dados_excel = pd.read_excel(nome_arquivo)
    
    for index, linha in dados_excel.iterrows():

        instancia_modelo = Instituicao(
            codigo_compensacao=linha['Código de compensação'],
            nome=linha['Nome Instituição']
        )
   
        instancia_modelo.save()


importar_dados_excel('bancos.xls')