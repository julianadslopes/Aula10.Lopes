import pandas as pd

try:
    df_base_de_dados = pd.read_csv("ClassicDisco.csv", sep= ',', encoding='utf-8')

    print(df_base_de_dados)

except Exception as e:
    print (f"Erro {e}")



# IMPRIMINDO AS 5 PRIMEIRAS LINHAS
print (df_base_de_dados.head())

# IMPRIMINDO AS 10 PRIMEIRAS LINHAS
print (df_base_de_dados.head(10))

# IMPRIMINDO AS 5 ÚLTIMAS LINHAS
print (df_base_de_dados.tail())

# IMPRIMINDO INFORMAÇÕES DA BASE DE DADOS
print (df_base_de_dados.info())

# IMPRIMINDO RESUMO DOS DADOS
print (df_base_de_dados.describe())
