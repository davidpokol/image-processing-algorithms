import math
import cmath

def dft2(matrix):
    N = len(matrix)
    M = len(matrix[0])
    
    F = [[0j for _ in range(M)] for _ in range(N)]
    
    for u in range(N):
        for v in range(M):
            s = 0j
            for x in range(N):
                for y in range(M):
                    angle = -2 * math.pi * ((u * x) / N + (v * y) / M)
                    s += matrix[x][y] * cmath.exp(1j * angle)
            F[u][v] = s
    return F


def idft2(F):
    N = len(F)
    M = len(F[0])
    
    f = [[0j for _ in range(M)] for _ in range(N)]
    
    for x in range(N):
        for y in range(M):
            s = 0j
            for u in range(N):
                for v in range(M):
                    angle = 2 * math.pi * ((u * x) / N + (v * y) / M)
                    s += F[u][v] * cmath.exp(1j * angle)
            f[x][y] = s / (N * M)
    
    return f


# ===== Teszt =====

f = [
    [1, 2],
    [3, 4]
]

F = dft2(f)
f_back = idft2(F)

# csak valós rész + kerekítés
f_back_real = [[round(f_back[i][j].real) for j in range(len(f[0]))] for i in range(len(f))]

print("Eredeti:")
print(f)

print("\nVisszaállított:")
print(f_back_real)