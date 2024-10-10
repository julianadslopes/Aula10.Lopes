import os



# dicionário de alunos com 4 notas

alunos = {}

for i in range (1):
    os.system ("cls")
    nome = input ("Digite nome do aluno: ")
    nota1 = float (input("Digite a primeira nota: "))
    nota2 = float (input("Digite a segunda nota: "))
    nota3 = float (input("Digite a terceira nota: "))

    media = (nota1+nota2+nota3)/3

    alunos [nome] = {
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": (media)
    }


print (alunos)

for aluno, dados in alunos.items():
    print(f"Nome: {aluno}, Média: {dados['media']:.2f}")