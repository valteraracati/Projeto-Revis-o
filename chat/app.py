""" Chat - Módulo tal que faz isso.

O módulo main faz isso e aquilo. Ele, de vez em quando, quase nunca, mais com frequência, parece que não é.

Área do quadrado = lado x lado

"""

def calcula_area_quadrado():
    lado_do_quadrado: float = 0.0

    lado_do_quadrado = float(input('Informe o lado do quadrado: '))

    print(f"Área do quadrado: {lado_do_quadrado**2}")


calcula_area_quadrado()