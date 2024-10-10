import os

os.system ("cls")

dicionario = {
    "nome":"João",
    "telefone": "92574-8964",
    "idade": 25,
    "cpf": "012.254.365-79"
}

dicionario1= {
    "nome": "Maria"
}

# ACESSAR OS VALORES DO DICIONÁRIO  (alt+shift+seta duplica seleção)
# print (dicionario["nome"])
# print (dicionario["telefone"])
# print (dicionario["idade"])

# ALTERAR OS VALORES DO DICIONÁRIO
dicionario["nome"] = "Paula"
print (dicionario)

# CRIANDO NOVAS CHAVES E VALORES PARA O DICIONÁRIO
dicionario1 ["email"] = "maria@gmail.com"
dicionario1 ["idade"] = 25
#print (dicionario1)

# REMOVER CHAVES DO DICIONÁRIO - USANDO del
del dicionario1["email"]
print (dicionario1)

# REMOVER CHAVES DO DICIONÁRIO - USANDO pop (retorna o valor da chave apagada)
print (dicionario.pop("idade", "não encontrado"))

# DICIONARIO DE DICIONÁRIOS 
pessoas = {}

for i in range (1):
    os.system ("cls")
    nome = input ("Digite o nome: ")
    email = input ("Digite o email: ")
    idade = input ("Digite a idade: ")
    cpf = input ("Digite o CPF: ")

    pessoas [nome] = {
        "email": email,
        "idade": idade,
        "CPF": cpf
    }

print (pessoas[nome]["email"])