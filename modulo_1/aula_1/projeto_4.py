#ENTRADA
salario = float(input("Digite aqui o seu salário: "))
emprestimo = float(input("Digite o valor do seu empréstimo: "))

#PROCESSAMENTO
if(emprestimo <= salario * 0.5):
    #SAÍDA
   print("Seu empréstimo foi aprovado! ")

#PROCESSAMENTO
elif(emprestimo <= salario * 0.75):
    #SAÍDA
    print ("Seu empréstimo está em análise!")

#PROCESSAMENTO
else:
    #SAÍDA
    print("Seu empréstimo foi negado!")