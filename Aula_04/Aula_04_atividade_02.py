def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente"))
    return nota
notaA = float(input("Digite a 1º nota:"))
notaA = verificar_nota(notaA)



NotaB = float(input("Digite a 2º nota: "))

NotaB = verificar_nota(NotaB)

media = (notaA + NotaB) / 2
print(media)