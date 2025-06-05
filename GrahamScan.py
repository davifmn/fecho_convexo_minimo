from JarvisMarch import StartJarvis
from matematica import produto_vetorial, distancia
from functools import cmp_to_key

def sort_graham_scan(pontos, left_most):
    pontos_sem_left = [p for p in pontos if p != left_most]
    
    def compare(p1, p2):
        cross = produto_vetorial(left_most, p1, p2)
        if cross > 0:
            return -1  
        elif cross < 0:
            return 1  
        else:
            d1 = distancia(left_most, p1)
            d2 = distancia(left_most, p2)
            if d2 > d1:
                return 1
            elif d2 < d1:
                return -1
    
    return sorted(pontos_sem_left, key=cmp_to_key(compare))

def graham_scan(pontos):
    n = len(pontos)
    pontos = list(pontos)
    if n <= 2:
        return pontos
    
    left_most = StartJarvis(pontos)
    pontos_ordenados = sort_graham_scan(pontos, left_most)
    
    if not pontos_ordenados:
        return [left_most]
    
    fecho = [left_most, pontos_ordenados[0]]

    for p in pontos_ordenados[1:]:
        
        while len(fecho) > 1:
            topo = fecho[-1]
            anterior = fecho[-2]
            cross = produto_vetorial(anterior, topo, p)
            
            if cross > 0:  
                break
            elif cross < 0:  # Curva à direita - remove ponto
                fecho.pop()
            else:  # Pontos colineares  -> Mantém apenas o ponto mais distante
                if distancia(anterior, p) > distancia(anterior, topo):
                    fecho.pop()
                else:
                    break
                    
            # Segurança para não esvaziar o fecho
            if len(fecho) < 2:
                break
        
        fecho.append(p)
    
    return fecho