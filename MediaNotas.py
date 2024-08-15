#criar um programa para cálculo de média de notas
def lernotas():
    n=float(input("Digite uma nota para o aluno(a): "))
    return n

def resultado (n1,n2):
    media=(n1+n2)/2
    print ("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media >=6:
        print ("Você foi aprovado")
    else:
        print ("Você foi reprovado")


a = lernotas()
b = lernotas()
resultado (a , b)