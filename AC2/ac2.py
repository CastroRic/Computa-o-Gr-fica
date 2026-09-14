import numpy as np
import matplotlib.pyplot as plt

def mostra_ponto(p1, p2, titulo):
    plt.figure()
    plt.scatter(p1[0, 0], p1[0, 1], label="Original")
    plt.scatter(p2[0, 0], p2[0, 1], label="Transformado")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.axis("equal")
    plt.legend()
    plt.title(titulo)
    plt.show()

def mostra_figura(a, b, titulo):
    a = np.vstack([a, a[0]])
    b = np.vstack([b, b[0]])

    plt.figure()
    plt.plot(a[:, 0], a[:, 1], "o-", label="Original")
    plt.plot(b[:, 0], b[:, 1], "o--", label="Transformado")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.axis("equal")
    plt.legend()
    plt.title(titulo)
    plt.show()

# 1 - Translação

p = np.array([[2, 3]])
p2 = p + [4, -2]

print("Exercicio 1")
print("P original:", p[0])
print("P transformado:", p2[0])

mostra_ponto(p, p2, "Exercicio 1 - Translacao")

# 2 - Escala uniforme

tri = np.array([
    [1, 1],
    [3, 1],
    [2, 4]
])

tri2 = tri * 2

print("\nExercicio 2")
print("Triangulo original:")
print(tri)
print("Triangulo transformado:")
print(tri2)

mostra_figura(tri, tri2, "Exercicio 2 - Escala Uniforme")

# 3 - Escala nao uniforme

tri2 = tri * [2, 0.5]

print("\nExercicio 3")
print("Triangulo original:")
print(tri)
print("Triangulo transformado:")
print(tri2)
mostra_figura(tri, tri2, "Exercicio 3 - Escala Nao Uniforme")

# 4 - Rotação

p = np.array([[1, 0]])
ang = np.radians(90)
mat = np.array([
    [np.cos(ang), -np.sin(ang)],
    [np.sin(ang), np.cos(ang)]
])

p2 = p @ mat.T

print("\nExercicio 4")
print("P original:", p[0])
print("P transformado:", p2[0])

mostra_ponto(p, p2, "Exercicio 4 - Rotacao")

# 5 - Rotação do quadrado

quad = np.array([
    [1, 1],
    [1, 4],
    [4, 4],
    [4, 1]
])

ang = np.radians(-45)
mat = np.array([
    [np.cos(ang), -np.sin(ang)],
    [np.sin(ang), np.cos(ang)]
])

quad2 = quad @ mat.T

print("\nExercicio 5")
print("Quadrado transformado:")
print(quad2)
mostra_figura(quad, quad2, "Exercicio 5 - Rotacao de 45 graus")

# 6 - Reflexão no eixo Y

p = np.array([[2, 5]])
mat = np.array([
    [-1, 0],
    [0, 1]
])

p2 = p @ mat.T

print("\nExercicio 6")
print("P original:", p[0])
print("P transformado:", p2[0])
mostra_ponto(p, p2, "Exercicio 6 - Reflexao no eixo Y")

# 7 - Reflexão no eixo X

tri = np.array([
    [2, 3],
    [4, 3],
    [3, 5]
])
mat = np.array([
    [1, 0],
    [0, -1]
])

tri2 = tri @ mat.T

print("\nExercicio 7")
print("Triangulo transformado:")
print(tri2)
mostra_figura(tri, tri2, "Exercicio 7 - Reflexao no eixo X")

# 8 - Cisalhamento horizontal

p = np.array([[2, 3]])
k = 2
mat = np.array([
    [1, k],
    [0, 1]
])

p2 = p @ mat.T

print("\nExercicio 8")
print("P original:", p[0])
print("P transformado:", p2[0])
mostra_ponto(p, p2, "Exercicio 8 - Cisalhamento Horizontal")

# 9 - Composição

p = np.array([[3, 2]])

# translacao
p1 = p + [1, -1]

# rotacao
ang = np.radians(90)

mat = np.array([
    [np.cos(ang), -np.sin(ang)],
    [np.sin(ang), np.cos(ang)]
])

p2 = p1 @ mat.T

# escala
p3 = p2 * 2

print("\nExercicio 9")
print("Inicial:", p[0])
print("Depois da translacao:", p1[0])
print("Depois da rotacao:", p2[0])
print("Resultado final:", p3[0])

plt.figure()

plt.scatter(p[0, 0], p[0, 1], label="Inicial")
plt.scatter(p1[0, 0], p1[0, 1], label="Translacao")
plt.scatter(p2[0, 0], p2[0, 1], label="Rotacao")
plt.scatter(p3[0, 0], p3[0, 1], label="Escala")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.axis("equal")
plt.legend()
plt.title("Exercicio 9 - Composicao")
plt.show()


# 10 - Transformações no retângulo

ret = np.array([
    [1, 1],
    [5, 1],
    [5, 3],
    [1, 3]
])

# translacao
r1 = ret + [-2, 3]

# escala
r2 = r1 * [1.5, 0.5]

# reflexao no eixo Y
mat = np.array([
    [-1, 0],
    [0, 1]
])

r3 = r2 @ mat.T

print("\nExercicio 10")
print("Retangulo original:")
print(ret)

print("Depois da translacao:")
print(r1)

print("Depois da escala:")
print(r2)

print("Resultado final:")
print(r3)

plt.figure()

ret = np.vstack([ret, ret[0]])
r1 = np.vstack([r1, r1[0]])
r2 = np.vstack([r2, r2[0]])
r3 = np.vstack([r3, r3[0]])

plt.plot(ret[:, 0], ret[:, 1], "o-", label="Original")
plt.plot(r1[:, 0], r1[:, 1], "o--", label="Translacao")
plt.plot(r2[:, 0], r2[:, 1], "o-.", label="Escala")
plt.plot(r3[:, 0], r3[:, 1], "o:", label="Reflexao")

plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.axis("equal")
plt.legend()
plt.title("Exercicio 10 - Combinacao de Transformacoes")
plt.show()
