#ENTRADA
nota1 = float(input("Digite aqui a primeira nota: "))
nota2 = float(input("Digite aqui a segunda nota: "))
nota3 = float(input("Digite aqui a terceira nota: "))
#PROCESSAMENTO
media = (nota1 + nota2 + nota3)/3
#SAÍDA
print("A média do aluno é:",media)
#PROCESSAMENTO
if media >=7:
    #SAÍDA
    print("O aluno está aprovado!")
else:
    #SAÍDA
    print("O aluno está reprovado!")
