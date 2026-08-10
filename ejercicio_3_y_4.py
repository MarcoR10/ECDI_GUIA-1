"""
GUÍA DE TRABAJO 1 - ECUACIONES DIFERENCIALES
Escuela Colombiana de Ingeniería Julio Garavito

Desarrollo de los puntos 3 y 4
Tema: Ecuaciones diferenciales autónomas y diagramas de fase.

El programa:
1. Construye los diagramas de fase de los modelos de población.
2. Identifica los puntos de equilibrio.
3. Determina el comportamiento de las soluciones.
4. Responde los incisos de los puntos 3 y 4.
5. Visualiza el comportamiento del modelo modificado del punto 4(f).

Librerías utilizadas:
- NumPy
- Matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ================================================================
# FUNCIONES AUXILIARES
# ================================================================

def diagrama_fase(f, puntos_criticos, limites, titulo):
    """
    Construye un diagrama de fase vertical para una ecuación autónoma:

        dP/dt = f(P)

    Los puntos críticos se muestran sobre la recta de fase
    y las flechas indican si la población aumenta o disminuye.
    """

    minimo, maximo = limites
    puntos = sorted(puntos_criticos)

    fig, ax = plt.subplots(figsize=(7, 8))

    # ------------------------------------------------------------
    # Recta principal del diagrama de fase
    # ------------------------------------------------------------

    ax.plot(
        [0, 0],
        [minimo, maximo],
        color="black",
        linewidth=2.2,
        zorder=1
    )

    # ------------------------------------------------------------
    # Determinación de los intervalos
    # ------------------------------------------------------------

    extremos = [minimo] + puntos + [maximo]

    for i in range(len(extremos) - 1):

        a = extremos[i]
        b = extremos[i + 1]

        # Punto de prueba dentro del intervalo
        prueba = (a + b) / 2

        # Signo de la derivada
        signo = np.sign(f(prueba))

        # Centro del intervalo
        centro = (a + b) / 2

        # Longitud de la flecha
        longitud = min((b - a) * 0.32, 0.45)

        # Pequeño desplazamiento horizontal para
        # que la flecha no quede oculta por la recta
        x_flecha = 0.02

        # --------------------------------------------------------
        # Flecha hacia arriba
        # --------------------------------------------------------

        if signo > 0:

            ax.annotate(
                "",
                xy=(x_flecha, centro + longitud),
                xytext=(x_flecha, centro - longitud),
                arrowprops=dict(
                    arrowstyle="-|>",
                    linewidth=2.5,
                    color="black",
                    mutation_scale=18
                ),
                zorder=4
            )

            texto = "P aumenta"

        # --------------------------------------------------------
        # Flecha hacia abajo
        # --------------------------------------------------------

        elif signo < 0:

            ax.annotate(
                "",
                xy=(x_flecha, centro - longitud),
                xytext=(x_flecha, centro + longitud),
                arrowprops=dict(
                    arrowstyle="-|>",
                    linewidth=2.5,
                    color="black",
                    mutation_scale=18
                ),
                zorder=4
            )

            texto = "P disminuye"

        else:

            texto = "P constante"

        # --------------------------------------------------------
        # Texto explicativo del intervalo
        # --------------------------------------------------------

        ax.text(
            0.18,
            centro,
            texto,
            va="center",
            fontsize=10.5
        )

    # ------------------------------------------------------------
    # Puntos de equilibrio
    # ------------------------------------------------------------

    for punto in puntos:

        ax.scatter(
            0,
            punto,
            s=100,
            zorder=5
        )

        ax.text(
            0.18,
            punto,
            f"P = {punto:g}",
            va="center",
            fontsize=11,
            fontweight="bold"
        )

    # ------------------------------------------------------------
    # Formato del gráfico
    # ------------------------------------------------------------

    ax.set_xlim(-0.45, 1.55)
    ax.set_ylim(minimo, maximo)

    ax.set_xticks([])

    ax.set_ylabel("P", fontsize=12)

    ax.set_title(
        titulo,
        fontsize=14,
        fontweight="bold",
        pad=15
    )

    ax.grid(
        axis="y",
        alpha=0.20
    )

    plt.tight_layout()
    plt.show()


def mostrar_conclusion(titulo, texto):
    """
    Muestra una conclusión organizada en la terminal.
    """

    print("\n" + "=" * 72)
    print(titulo)
    print("=" * 72)
    print(texto)


# =================================================================
# PUNTO 3
# =================================================================

print("\n" + "#" * 72)
print("PUNTO 3 - MODELO DE POBLACIÓN")
print("#" * 72)

# P está expresada en miles de ejemplares.
#
# Ecuación:
# P' = P(P - 1)(2 - P)

def f3(P):
    return P * (P - 1) * (2 - P)


# -----------------------------------------------------------------
# 3(a) DIAGRAMA DE FASE
# -----------------------------------------------------------------

puntos_criticos_3 = [0, 1, 2]

diagrama_fase(
    f=f3,
    puntos_criticos=puntos_criticos_3,
    limites=(-0.5, 2.7),
    titulo=r"Punto 3(a) - Diagrama de fase: $P' = P(P-1)(2-P)$"
)


mostrar_conclusion(
    "Punto 3(a) - Análisis del diagrama de fase",
    (
        "Los puntos críticos se obtienen haciendo P' = 0:\n\n"
        "P(P - 1)(2 - P) = 0\n\n"
        "Por tanto:\n"
        "P = 0, P = 1 y P = 2.\n\n"
        "El análisis del signo de P' permite determinar el comportamiento:\n\n"
        "• Si P < 0, P' > 0 y P aumenta.\n"
        "• Si 0 < P < 1, P' < 0 y P disminuye.\n"
        "• Si 1 < P < 2, P' > 0 y P aumenta.\n"
        "• Si P > 2, P' < 0 y P disminuye.\n\n"
        "Los equilibrios P = 0 y P = 2 son estables,\n"
        "mientras que P = 1 es inestable."
    )
)


# -----------------------------------------------------------------
# 3(b) POBLACIÓN INICIAL DE 3000 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 3(b) - P(0) = 3",
    (
        "Como P está medida en miles, 3000 ejemplares corresponden a:\n"
        "P(0) = 3.\n\n"
        "Como P > 2, se cumple P' < 0, por lo que la población disminuye.\n"
        "La solución se acerca al equilibrio estable P = 2.\n\n"
        "Conclusión:\n"
        "Después de mucho tiempo, la población tiende a P = 2,\n"
        "es decir, aproximadamente 2000 ejemplares."
    )
)


# -----------------------------------------------------------------
# 3(c) POBLACIÓN INICIAL DE 1500 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 3(c) - P(0) = 1.5",
    (
        "1500 ejemplares corresponden a:\n"
        "P(0) = 1.5.\n\n"
        "Como 1 < P < 2, se cumple P' > 0,\n"
        "por lo que la población aumenta.\n"
        "La solución se acerca al equilibrio estable P = 2.\n\n"
        "Conclusión:\n"
        "La población aumenta y, después de mucho tiempo,\n"
        "tiende a 2000 ejemplares."
    )
)


# -----------------------------------------------------------------
# 3(d) POBLACIÓN INICIAL DE 500 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 3(d) - P(0) = 0.5",
    (
        "500 ejemplares corresponden a:\n"
        "P(0) = 0.5.\n\n"
        "Como 0 < P < 1, se cumple P' < 0,\n"
        "por lo que la población disminuye.\n"
        "La solución se acerca al equilibrio P = 0.\n\n"
        "Conclusión:\n"
        "La población disminuye y tiende a 0 ejemplares."
    )
)


# -----------------------------------------------------------------
# 3(e) ¿900 EJEMPLARES PUEDEN CRECER HASTA 1100?
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 3(e) - P(0) = 0.9",
    (
        "900 ejemplares corresponden a P(0) = 0.9.\n"
        "1100 ejemplares corresponden a P = 1.1.\n\n"
        "Como 0 < P < 1 implica P' < 0,\n"
        "una población que comienza en P = 0.9 disminuye\n"
        "en lugar de crecer.\n\n"
        "Además, P = 1 es un equilibrio inestable.\n"
        "Una solución que comienza por debajo de 1 no puede\n"
        "atravesarlo hacia P > 1 bajo este modelo.\n\n"
        "Conclusión:\n"
        "No. Una población inicial de 900 ejemplares\n"
        "no puede crecer hasta 1100 ejemplares."
    )
)


# =================================================================
# PUNTO 4
# =================================================================

print("\n" + "#" * 72)
print("PUNTO 4 - MODELO LOGÍSTICO")
print("#" * 72)

# P está expresada en miles de ejemplares.
#
# Ecuación:
# P' = 3P - 2P²

def f4(P):
    return 3 * P - 2 * P**2


# -----------------------------------------------------------------
# 4(a) DIAGRAMA DE FASE
# -----------------------------------------------------------------

puntos_criticos_4 = [0, 1.5]

diagrama_fase(
    f=f4,
    puntos_criticos=puntos_criticos_4,
    limites=(-0.5, 2.7),
    titulo=r"Punto 4(a) - Diagrama de fase: $P' = 3P-2P^2$"
)


mostrar_conclusion(
    "Punto 4(a) - Análisis del diagrama de fase",
    (
        "Los puntos críticos se obtienen haciendo P' = 0:\n\n"
        "3P - 2P² = 0\n"
        "P(3 - 2P) = 0\n\n"
        "Por tanto:\n"
        "P = 0 y P = 1.5.\n\n"
        "Para 0 < P < 1.5 se cumple P' > 0,\n"
        "por lo que la población aumenta.\n\n"
        "Para P > 1.5 se cumple P' < 0,\n"
        "por lo que la población disminuye.\n\n"
        "Por tanto, P = 1.5 es un equilibrio estable.\n"
        "El equilibrio P = 0 es inestable para poblaciones positivas."
    )
)


# -----------------------------------------------------------------
# 4(b) POBLACIÓN INICIAL DE 2000 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 4(b) - P(0) = 2",
    (
        "2000 ejemplares corresponden a:\n"
        "P(0) = 2.\n\n"
        "Como P > 1.5, se cumple P' < 0,\n"
        "por lo que la población disminuye.\n\n"
        "La solución se aproxima al equilibrio estable P = 1.5.\n\n"
        "Conclusión:\n"
        "Después de mucho tiempo, la población tiende a\n"
        "P = 1.5, es decir, aproximadamente 1500 ejemplares."
    )
)


# -----------------------------------------------------------------
# 4(c) POBLACIÓN INICIAL DE 100 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 4(c) - P(0) = 0.1",
    (
        "100 ejemplares corresponden a:\n"
        "P(0) = 0.1.\n\n"
        "Como 0 < P < 1.5, se cumple P' > 0,\n"
        "por lo que la población aumenta.\n\n"
        "La solución se aproxima al equilibrio estable P = 1.5.\n\n"
        "Conclusión:\n"
        "La población aumenta y tiende a 1500 ejemplares."
    )
)


# -----------------------------------------------------------------
# 4(d) POBLACIÓN INICIAL DE 1500 EJEMPLARES
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 4(d) - P(0) = 1.5",
    (
        "1500 ejemplares corresponden exactamente a:\n"
        "P(0) = 1.5.\n\n"
        "Este valor es un punto de equilibrio, por lo que:\n"
        "P' = 0.\n\n"
        "Conclusión:\n"
        "La población permanece constante en 1500 ejemplares."
    )
)


# -----------------------------------------------------------------
# 4(e) TASA DE NACIMIENTOS Y MUERTES POR TRIMESTRE
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 4(e) - Modelo anual con nacimientos y muertes",
    (
        "La población P está expresada en miles de ejemplares\n"
        "y el tiempo t está expresado en años.\n\n"
        "Tasa de nacimientos:\n"
        "150 ejemplares por trimestre.\n\n"
        "Tasa de muertes:\n"
        "s ejemplares por trimestre.\n\n"
        "Como un año tiene 4 trimestres, el cambio anual es:\n\n"
        "4(150 - s) = 600 - 4s ejemplares/año.\n\n"
        "Como P está expresada en miles de ejemplares,\n"
        "se divide entre 1000:\n\n"
        "dP/dt = (600 - 4s)/1000\n"
        "      = 0.6 - 0.004s.\n\n"
        "Por tanto, la ecuación diferencial anual es:\n\n"
        "dP/dt = 0.6 - 0.004s."
    )
)


# -----------------------------------------------------------------
# 4(f) ANÁLISIS DEL COMPORTAMIENTO SEGÚN s
# -----------------------------------------------------------------

mostrar_conclusion(
    "Punto 4(f) - Comportamiento según la tasa de muertes",
    (
        "El comportamiento depende de la comparación entre s y 150.\n\n"

        "Si s < 150:\n"
        "dP/dt > 0, por lo que la población aumenta.\n\n"

        "Si s = 150:\n"
        "dP/dt = 0, por lo que la población permanece constante.\n\n"

        "Si s > 150:\n"
        "dP/dt < 0, por lo que la población disminuye.\n\n"

        "La solución general es:\n"
        "P(t) = P(0) + (0.6 - 0.004s)t.\n\n"

        "En el caso s > 150, el modelo predice que la población\n"
        "puede llegar a P = 0 en un tiempo finito.\n"
        "Desde el punto de vista biológico, una población no puede\n"
        "tomar valores negativos."
    )
)


# =================================================================
# VISUALIZACIÓN DEL PUNTO 4(f)
# =================================================================

# Para comparar los tres escenarios se toma como ejemplo:
# P(0) = 1, es decir, 1000 ejemplares.

P0 = 1.0

# Tiempo en años
t = np.linspace(0, 8, 400)

# Tasas de muerte solicitadas
tasas_muerte = [100, 150, 200]

fig, ax = plt.subplots(figsize=(10, 6))


for s in tasas_muerte:

    # Pendiente anual del modelo
    pendiente = 0.6 - 0.004 * s

    # Solución del modelo
    P = P0 + pendiente * t

    # ------------------------------------------------------------
    # La población no puede ser negativa.
    # ------------------------------------------------------------

    P = np.maximum(P, 0)

    ax.plot(
        t,
        P,
        linewidth=2.5,
        label=f"s = {s} muertes/trimestre"
    )


# Línea de población cero
ax.axhline(
    0,
    color="black",
    linewidth=1.2
)


# ---------------------------------------------------------------
# Marcar el punto de extinción para s = 200
# ---------------------------------------------------------------

s_extincion = 200
pendiente_extincion = 0.6 - 0.004 * s_extincion

if pendiente_extincion < 0:

    tiempo_extincion = -P0 / pendiente_extincion

    if 0 <= tiempo_extincion <= 8:

        ax.scatter(
            tiempo_extincion,
            0,
            s=80,
            zorder=5
        )

        ax.annotate(
            f"P = 0\n(t ≈ {tiempo_extincion:.1f} años)",
            xy=(tiempo_extincion, 0),
            xytext=(tiempo_extincion + 0.35, 0.25),
            arrowprops=dict(
                arrowstyle="->",
                linewidth=1.5
            ),
            fontsize=10
        )


# ---------------------------------------------------------------
# Etiquetas y formato
# ---------------------------------------------------------------

ax.set_xlabel(
    "Tiempo, t (años)",
    fontsize=12
)

ax.set_ylabel(
    "Población, P (miles de ejemplares)",
    fontsize=12
)

ax.set_title(
    "Punto 4(f) - Comportamiento según la tasa de muertes\n"
    "Ejemplo con P(0) = 1000 ejemplares",
    fontsize=14,
    fontweight="bold"
)

ax.grid(
    alpha=0.25
)

ax.legend(
    fontsize=10
)

ax.set_xlim(0, 8)
ax.set_ylim(bottom=0)

plt.tight_layout()
plt.show()


# =================================================================
# RESUMEN FINAL
# =================================================================

print("\n" + "#" * 72)
print("FIN DEL DESARROLLO DE LOS PUNTOS 3 Y 4")
print("#" * 72)

print(
    "\nEl programa ejecutó correctamente el análisis cualitativo "
    "de los modelos de población."
)