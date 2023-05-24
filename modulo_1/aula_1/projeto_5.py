seuNome = str(input("Digite aqui o seu nome: "))
print("Bem-vindo(a) ao FucturaGame,",seuNome,'!')
print("Você está em uma caverna e o que você vê são 3 itens: ")
print("Uma espada, um arco, e um cajado. Qual deseja pegar?")

arma = str(input("Digite 1 para espada, 2 para arco e 3 para cajado: "))

if (arma == "1"):
    print("Você se tornou um guerreiro! E apareceu um goblin na sua frente")
    print("O que deseja fazer? Digite 1 para atacar ou 2 para fugir.")
    acao = str(input("Digite aqui a sua ação: "))
    if (acao == "1"):
        print("Você atacou o goblin mas ele tinha amigos e lhe matou.")
    elif (acao == "2"):
        print("Você não conseguiu fugir e infelizmente levou uma flechada.")
    else:
        print("Você não escolheu a acao correta, os deuses não lhe ajudarão.")

elif (arma == "2"):
    print("Você se tornou um arqueiro!")
    print("Apareceu uma cobra na sua frente o que você vai fazer?")
    acao = str(input("Digite 1 para fugir ou 2 para atacar: "))
    if (acao == "1"):
        print("Você conseguiu fugir mas infelizmente...")
        print("Infelizmente caiu em um buraco e morreu.")
    elif (acao == "2"):
        print("Você conseguiu atacar... porém...")
        print("Percebeu que não tinha flechas e a cobra lhe picou.")
        print("E você morreu.")
    else:
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão.")

elif (arma == "3"):
    print("Você agora é um mago! E com o poder investido pelo cajado, você acerta 2 goblins com uma cajadada só...")
    print("O que você deseja fazer logo em seguida?")
    acao = str(input("Digite 1 para fugir e 2 para ir atrás de mais goblins: "))
    if (acao == "1"):
        print("excelente escolha! Você encontrou a saída e venceu o jogo!")
        print("Parabéns,", seuNome,"!!")
    elif (acao == "2"):
        print("Essa não foi uma das mais sábias ideias...")
        print("Um grupo de goblins lhe cercou,",seuNome,",","e agora infelizmente você nos deixou.")
    else:
        print("Você não escolheu a ação correta, os deuses não lhe ajudarão.")

else:
    print("Má escolha, jovem", seuNome,", retorne e escolha uma opção válida.")