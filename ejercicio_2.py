# Guia de Trabajo #1

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


def metodo_euler(edo, x0, y0, x_final, paso=0.01):
    x_vals, y_vals = [x0],[y0]
    if x_final < x0:
        paso = -paso
    x,y = x0,y0
    while (paso > 0 and x < x_final) or (paso < 0 and x > x_final):
        y = y + paso * edo.calcular(x, y)
        x = x + paso
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)

def campo_y_solucion(edo, x0, y0):

    x = np.arange(-5, 5, 0.5)
    y = np.arange(-5, 5, 0.5)

    X, Y = np.meshgrid(x, y)

    # Campo direccional
    M = edo.calcular(X, Y)

    U = 1 / np.sqrt(1 + M**2)
    V = M / np.sqrt(1 + M**2)

    plt.quiver(X, Y, U, V, alpha=0.5)

    # Solución hacia la derecha
    x_der, y_der = metodo_euler(edo, x0, y0, 4.5)

    # Solución hacia la izquierda
    x_izq, y_izq = metodo_euler(edo, x0, y0, -4.5)

    plt.plot(x_der, y_der, linewidth=2)
    plt.plot(x_izq, y_izq, linewidth=2)

    # Condición inicial
    plt.plot(x0, y0, 'ko')

    # Límites del gráfico
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(edo.expresion+" | "+edo.solucion)
    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)
    plt.grid()

    plt.show()


class EDO:

    def __init__(self,funcion,expresion=None,solucion=None):
        self.funcion = funcion
        self.expresion = expresion
        self.solucion = solucion

    def calcular(self, x, y):
        return self.funcion(x,y)

    def puntos_criticos(self):
        puntos = sp.solve(self.expresion, sp.Symbol('y'))
        puntos_reales = []
        for punto in puntos:
            if punto.is_real:
                puntos_reales.append(punto)
        return puntos_reales

    def diagrama_fase(self):
        puntos = self.puntos_criticos()
        print("Puntos críticos:", puntos)
        # Unir puntos críticos con -∞ y +∞
        puntos = [float(p) for p in puntos]
        puntos.sort()
        limites = [-10] + puntos + [10]

        print("---------------------")
        for i in range(len(limites) - 1):
            a = limites[i]
            b = limites[i + 1]
            punto = (a + b) / 2
            resultado = self.calcular(0, punto)

            if resultado > 0:
                print(f"{a} < y < {b}  ↑ creciente")
                print("---------------------")
            elif resultado < 0:
                print(f"{a} < y < {b}  ↓ decreciente")
                print("---------------------")
            else:
                print(f"{a} < y < {b}  = 0")
                print("---------------------")

        print("\nEstabilidad:")

        for punto in puntos:

            izquierda = self.calcular(0, punto - 0.1)
            derecha = self.calcular(0, punto + 0.1)

            if izquierda > 0 and derecha < 0:
                print(f"y = {punto}: estable")

            elif izquierda < 0 and derecha > 0:
                print(f"y = {punto}: inestable")

            else:
                print(f"y = {punto}: semiestable")

    def campo_direccional(self):

        # Crear puntos de x y y
        x = np.arange(-5, 5, 0.5)
        y = np.arange(-5, 5, 0.5)

        # Crear la cuadrícula
        X, Y = np.meshgrid(x, y)

        # Calcular la pendiente en cada punto
        M = self.calcular(X, Y)

        # Normalizar los vectores
        U = 1 / np.sqrt(1 + M ** 2)
        V = M / np.sqrt(1 + M ** 2)

        # Dibujar el campo
        plt.quiver(X, Y, U, V)

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Campo direccional")
        plt.grid()
        plt.show()

if __name__ == '__main__':
    # ------------------------------------------------------------------#
    # Punto 2
    #------------------------------------------------------------------#
    print("A)")
    y = sp.Symbol('y')
    p2_1 = EDO(lambda x,y: y*(3-y)*(y-2),y*(3-y)*(y-2))
    p2_1.diagrama_fase()
    print("----------------------------------------------------------")
    print("B)")
    p2_2 = EDO(lambda x, y: y ** 2 - y ** 3,y ** 2 - y ** 3)
    p2_2.diagrama_fase()
    print("----------------------------------------------------------")
    print("C)")
    p2_3 = EDO(lambda x, y: (y + 2) * (10 + 3*y - y**2),(y + 2) * (10 + 3*y - y**2))
    p2_3.diagrama_fase()
    print("----------------------------------------------------------")
    print("D)")
    p2_4 = EDO(lambda x, y: y ** 5 - 4*y ** 3 - 5*y**2,y ** 5 - 4*y ** 3 - 5*y**2)
    p2_4.diagrama_fase()
    print("----------------------------------------------------------")
    print("E)")
    p2_5 = EDO(lambda x, y: (1-y)*(y-2)**3,(1-y)*(y-2)**3)
    p2_5.diagrama_fase()
    print("----------------------------------------------------------")
