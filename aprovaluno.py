print("AprovAluno versão professor.")

nome = input("Nome do aluno:")
nota = int(input("1ª nota: "))
nota2 = int(input("2ª nota: "))

media = (nota + nota2) / 2

if media >= 60:
    print(f"seu aluno {nome} é aprovado com uma média de {media}.")
else:
    print(f"seu aluno {nome} é reprovado com uma média de {media}.")
