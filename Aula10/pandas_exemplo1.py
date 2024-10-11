import pandas as pd
import os

os.system ("cls")

dados = {
    "Cargos": ["assistente", "auxiliar", "gerente"],
    "Salarios": [2500,1800,750]
}

dados_bi = pd.DataFrame(dados)
print (dados_bi)

print (30*"-")

# dados_cargos = pd.Series(dados["Cargos"])
# print (dados_cargos)

# print (30*"-")

# dados_salarios = pd.Series(dados["Salario"])
# print (dados_salarios)

# print (30*"-")

# # Índices e Valores
# print (dados_cargos.index)

# print (30*"-")

# # Printar os valores
# print(dados_cargos.values)

# print (30*"-")

# Imprime a linha do índice
df_linha = dados_bi.iloc[1]["Cargos"]
print (df_linha)

