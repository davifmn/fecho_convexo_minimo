import random
import view
import JarvisMarch
import GrahamScan

n            = 100              # numero de pontos
pontos       = set()            # conjunto de pontos nao repetidos
left         = []               # pontos mais à esquerda
pontos_lista = list(pontos)


def posicionar_pontos(n):
    for _ in range(n):
        x = random.randint(5, 195)
        y = random.randint(5, 195)
        pontos.add((x, y))


def main(): 
    while len(pontos) < n:
        posicionar_pontos(n)

    # JarvisMarch
    left.append(JarvisMarch.StartJarvis(pontos)) 
    fecho_convexo = list(JarvisMarch.JarvisMarch(pontos, left[0]))
    view.plot_fecho_convexo_animado(pontos, fecho_convexo)

    #GrahamScan
    pontos_lista = list(pontos)
    fecho_convexo = GrahamScan.graham_scan(pontos_lista)
    view.plot_fecho_convexo_animado(pontos, fecho_convexo)


if __name__ == "__main__":
    main()