notaA=float (input("Informe a primeira nota: "))
notaB=float (input("Informe a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if mediafinal >= 6.0:
    print ("A média é: %1f - Aprovado " %mediafinal)
else:
    print("A média é: %.1f - Reprovado " %mediafinal)