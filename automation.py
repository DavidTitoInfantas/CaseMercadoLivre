import pandas as pd
import os
import numpy as np

# Path para o diretório de trabalho
base_path = os.getcwd()

# leitura de arquivos Excel
data_dir = f'{base_path}/data/NAVEGANDO-db-challenge.xlsx'

# ler tudo o arquivo e salvar uma copia
xls = pd.ExcelFile(data_dir)
sheet_names = xls.sheet_names
print('Abas disponíveis no arquivo Excel:')
print(sheet_names)

# Salvar uma copia do arquivo lido
dfs = {}
for sheet in sheet_names:
    dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)
    print(f'Dados da aba "{sheet}" carregados com sucesso!')
#    display(dfs[sheet].head())  

# Salvar o arquivo lido em um arquivo excel igual
output_path = f'{base_path}/data_transformated/NAVEGANDO-db-challenge-copia.xlsx'

with pd.ExcelWriter(output_path) as writer:
    for sheet, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet, index=False)

print(f'Arquivo copiado com sucesso para {output_path}')
input("Pressione Enter para sair.")