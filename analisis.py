def Error(valorV,valorA):
    Ea = abs(valorV-valorA) 
    Er =  Ea/abs(valorV)
    ErP=  Er*100 

    print("Error absoluto ",Ea)
    print("Error relativo ", Er)
    print("Erro Porcentual ", ErP,"%")
print("Introduce el Valor verdadero")
ValorV = int(input())
print("Introduce el Valor aproximado")
ValorA = int(input())
Error(ValorV,ValorA)