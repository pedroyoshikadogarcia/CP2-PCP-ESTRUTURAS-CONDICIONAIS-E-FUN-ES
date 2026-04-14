def ordenar_lados(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    if b < c:
        b, c = c, b
    return a, b, c

def classificar_triangulo(a, b, c):
    if a >= b + c:
        print("nao forma triangulo")
    else:
        if (a**2) == (b**2 + c**2):
            print("triangulo retangulo")
        elif (a**2) > (b**2 + c**2):
            print("triangulo obtusangulo")
        else:
            print("triangulo acutangulo")

        if a == b == c:
            print("triangulo equilatero")
        elif a == b or b == c or a == c:
            print("triangulo isosceles")

lado1 = float(input("Digite o lado A: "))
lado2 = float(input("Digite o lado B: "))
lado3 = float(input("Digite o lado c: "))

A, B, C = ordenar_lados(lado1, lado2, lado3)
classificar_triangulo(A, B, C)