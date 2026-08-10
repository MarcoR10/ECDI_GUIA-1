import numpy as np
import matplotlib.pyplot as plt

# 1. Definir las ecuaciones diferenciales
def f_a(x, y): return -y - np.sin(x)
def f_b(x, y): return x + y
def f_c(x, y): return -x**2 + np.sin(y)
def f_d(x, y): return (6*x - 3*x*y) / (x**2 + 1)
def f_e(x, y): return x * np.exp(y)
def f_f(x, y): return x - y


def metodo_euler(f, x0, y0, x_final, paso=0.05):
    x_vals, y_vals = [x0], [y0]

    if x_final < x0: paso = -paso 
    
    x, y = x0, y0

    while (paso > 0 and x < x_final) or (paso < 0 and x > x_final):
        y = y + paso * f(x, y)
        x = x + paso
        x_vals.append(x)
        y_vals.append(y)
    return np.array(x_vals), np.array(y_vals)

# Lista de problemas (funcion, x_inicial, y_inicial, titulo)
problemas = [
    (f_a, 0, 1, "a) y' = -y - sin(x) | y(0)=1"),
    (f_b, -2, 2, "b) y' = x + y | y(-2)=2"),
    (f_c, 0, 0, "c) y' = -x^2 + sin(y) | y(0)=0"),
    (f_d, 0, 1, "d) y' = (6x - 3xy)/(x^2 + 1) | y(0)=1"),
    (f_e, 0, -2, "e) y' = x*e^y | y(0)=-2"),
    (f_f, 1, 1, "f) y' = x - y | y(1)=1")
]

fig, axes = plt.subplots(2, 3, figsize=(16, 10))
axes = axes.flatten()

# Variables para la malla direccional
h_malla = 0.5
m = np.arange(-10, 11)
n = np.arange(-10, 11)
X, Y = np.meshgrid(m*h_malla, n*h_malla)

for i, (func, x0, y0, titulo) in enumerate(problemas):
    ax = axes[i]
    
    # --- CAMPO DIRECCIONAL 
    pendiente = func(X, Y)
    norm = np.sqrt(1 + pendiente**2)
    U = 1 / norm                          
    V = pendiente / norm                  
    ax.quiver(X, Y, U, V, angles='xy', color='navy', alpha=0.5)

    # Traza de la curva hacia la derecha (hasta x=5) y hacia la izquierda (hasta x=-5)
    x_der, y_der = metodo_euler(func, x0, y0, 5)
    x_izq, y_izq = metodo_euler(func, x0, y0, -5)
    
    ax.plot(x_der, y_der, color='red', linewidth=2)
    ax.plot(x_izq, y_izq, color='red', linewidth=2)
    
    # Detalles visuales
    ax.plot(x0, y0, 'ko', markersize=5) # Punto inicial
    ax.set_title(titulo)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
