v1 = [4,8,16,32,64,128]
v2 = [2,0,4,8,0]
#Vamos efetuar a divisão entre o v1 e o v2
for i in range(len(v1)):
    try:
        div=v1[i]/v2[i]
        print("%d / %d = %d" %(v1[i],v2[i],div))

    except (ZeroDivisionError):
        print("Ops! Encontramos um erro: não é possível divisão por zero!")