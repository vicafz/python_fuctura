#ENTRADA
seuNome = str(input("Digite aqui o seu nome: "))
#SAÍDA
print("Bem-vindo(a) ao FucturaGame,",seuNome,'!')
print("Você está em uma caverna e o que você vê são 3 itens: ")
print("Uma espada, um arco, e um cajado. Qual deseja pegar?")

#ENTRADA
arma = str(input("Digite 1 para espada, 2 para arco e 3 para cajado: "))

#PROCESSAMENTO
if (arma == "1"):
    #SAÍDA
    print("Você se tornou um guerreiro! E apareceu um goblin na sua frente")
    print("O que deseja fazer? Digite 1 para atacar ou 2 para fugir.")
    #ENTRADA
    acao = str(input("Digite aqui a sua ação: "))
    #PROCESSAMENTO
    if (acao == "1"):
        #SAÍDA
        print("Você atacou o goblin mas ele tinha amigos e lhe matou.")
    #PROCESSAMENTO
    elif (acao == "2"):
        #SAÍDA
        print("Você não conseguiu fugir e infelizmente levou uma flechada.")
    #PROCESSAMENTO
    else:
        #SAÍDA
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão.")

#PROCESSAMENTO
elif (arma == "2"):
    #SAÍDA
    print("Você se tornou um arqueiro!")
    print("Apareceu uma cobra na sua frente o que você vai fazer?")
    #ENTRADA
    acao = str(input("Digite 1 para fugir ou 2 para atacar: "))
    #PROCESSAMENTO
    if (acao == "1"):
        #SAÍDA
        print("Você conseguiu fugir mas infelizmente...")
        print("Infelizmente caiu em um buraco e morreu.")
    #PROCESSAMENTO
    elif (acao == "2"):
        #SAÍDA
        print("Você conseguiu atacar... porém...")
        print("Percebeu que não tinha flechas e a cobra lhe picou.")
        print("E você morreu.")
    #PROCESSAMENTO
    else:
        #SAÍDA
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão.")

#PROCESSAMENTO
elif (arma == "3"):
    #SAÍDA
    print("Você agora é um mago! E com o poder investido pelo cajado, você acerta 2 goblins com uma cajadada só...")
    print("O que você deseja fazer logo em seguida?")
    #ENTRADA
    acao = str(input("Digite 1 para fugir e 2 para ir atrás de mais goblins: "))
    #PROCESSAMENTO
    if (acao == "1"):
        #SAÍDA
        print("excelente escolha! Você encontrou a saída e venceu o jogo!")
        print("Parabéns,", seuNome,"!!")
    #PROCESSAMENTO
    elif (acao == "2"):
        #SAÍDA
        print("Essa não foi uma das mais sábias ideias...")
        print("Um grupo de goblins lhe cercou,",seuNome,",","e agora infelizmente você nos deixou.")
    #PROCESSAMENTO    
    else:
        #SAÍDA
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão.")

#PROCESSAMENTO
else:
    #SAÍDA
    print("Má escolha, jovem", seuNome,", retorne e escolha uma opção válida.")