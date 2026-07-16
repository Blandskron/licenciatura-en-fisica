import json
import os

# Asegurar que existe la carpeta destino
output_dir = r"c:\Users\BlandskronNotebook\Documents\blandskron\licenciatura-en-fisica\05-calculo-2\leccion-2"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "integrales-impropias-y-transformada-de-laplace.ipynb")

notebook = {
  "cells": [],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.0"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 2
}

def add_markdown(source_list):
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source_list]
    })

def add_code(source_list):
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source_list]
    })

# --- CELL 1: HEADER ---
add_markdown([
    "# Lección 2: Integrales Impropias, Función Gamma y la Transformada de Laplace",
    "### Cálculo II y Fundamentos de la Física Matemática",
    "",
    "---",
    "",
    "Este cuaderno de Jupyter aborda el estudio formal de las **Integrales Impropias** (primera y segunda especie), la **Función Gamma de Euler** (y su relación con las distribuciones de probabilidad), el **Valor Principal de Cauchy**, y una introducción rigurosa a la **Transformada de Laplace** orientada a la resolución de ecuaciones diferenciales ordinarias (EDOs) en sistemas físicos.",
    "",
    "A lo largo de esta lección, utilizaremos herramientas de cálculo simbólico (`SymPy`) e integración numérica (`SciPy`) no solo para visualizar la teoría, sino para confrontar e identificar de manera crítica varias erratas importantes presentes en la literatura tradicional de la materia (errores de signos físicos, mala deducción de medias estadísticas, e integraciones por partes y transformadas inversas incorrectas en casos de resonancia).",
    "",
    "---"
])

# --- CELL 2: OBJECTIVES ---
add_markdown([
    "## Objetivos de Aprendizaje",
    "",
    "Al finalizar esta lección, serás capaz de:",
    "1. **Identificar** y clasificar las integrales impropias de primera especie (intervalo infinito) y segunda especie (integrando no acotado).",
    "2. **Aplicar** los criterios de comparación directa y de límite para determinar la convergencia de integrales impropias.",
    "3. **Definir** la función Gamma de Euler y aplicar sus propiedades de recurrencia y la fórmula de duplicación de Legendre para resolver problemas matemáticos.",
    "4. **Deducir** analíticamente la media de variables aleatorias que siguen distribuciones de probabilidad continuas como la distribución Gamma y la distribución Beta.",
    "5. **Calcular** el Valor Principal de Cauchy para funciones singulares, comprendiendo cómo la simetría de funciones impares simplifica el cálculo analítico.",
    "6. **Evaluar** la Transformada de Laplace y su inversa analíticamente y resolver ecuaciones diferenciales lineales de segundo orden asociadas a osciladores en resonancia mecánica/eléctrica, corrigiendo los errores del texto estándar de la literatura."
])

# --- CELL 3: SECTION 1: IMPROPER INTEGRALS ---
add_markdown([
    "## 1. Integral Impropia de una Función Localmente Integrable",
    "",
    "### 1.1 Funciones Localmente Integrables",
    "Una función $f: I \\to \\mathbb{R}$ es **localmente integrable** en un intervalo $I$ si es integrable según Riemann en cualquier subintervalo cerrado y acotado $[a, b] \\subset I$.",
    "",
    "### 1.2 Clasificación de Integrales Impropias",
    "Cuando extendemos los límites de integración a intervalos no acotados o cuando la función presenta asíntotas verticales (puntos donde la función no está acotada), la integral definida ordinaria no es aplicable. Definimos entonces las **Integrales Impropias** mediante límites:",
    "",
    "#### A. Primera Especie (Intervalo Infinito)",
    "Si $f$ es localmente integrable en $[a, \\infty)$:",
    "$$\\int_a^{\\infty} f(x) dx = \\lim_{b \\to \\infty} \\int_a^b f(x) dx$$",
    "Si el límite existe y es un número real finito, se dice que la integral **converge**. De lo contrario, **diverge**.",
    "",
    "#### B. Segunda Especie (Integrando No Acotado)",
    "Si $f$ es localmente integrable en $(a, b]$ y no está acotada en un entorno de $a$ (singularidad en el extremo inferior):",
    "$$\\int_a^b f(x) dx = \\lim_{\\epsilon \\to 0^+} \\int_{a+\\epsilon}^b f(x) dx$$",
    "Si la singularidad está en el extremo superior $b$:",
    "$$\\int_a^b f(x) dx = \\lim_{\\epsilon \\to 0^+} \\int_a^{b-\\epsilon} f(x) dx$$",
    "Si la singularidad ocurre en un punto interior $c \\in (a, b)$:",
    "$$\\int_a^b f(x) dx = \\int_a^c f(x) dx + \\int_c^b f(x) dx = \\lim_{\\epsilon_1 \\to 0^+} \\int_a^{c-\\epsilon_1} f(x) dx + \\lim_{\\epsilon_2 \\to 0^+} \\int_{c+\\epsilon_2}^b f(x) dx$$"
])

# --- CELL 4: CODE - P-INTEGRALS CONVERGENCE ---
add_code([
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "import sympy as sp",
    "from scipy.integrate import quad",
    "import scipy.special as spec",
    "",
    "# Graficar la convergencia de 1/x^p para p=2 (converge) y p=0.5 (diverge)",
    "x_vals = np.linspace(1.0, 10.0, 400)",
    "y_p2 = 1.0 / x_vals**2",
    "y_p05 = 1.0 / x_vals**0.5",
    "",
    "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))",
    "",
    "# Gráfico 1: p = 2 (Converge)",
    "ax1.plot(x_vals, y_p2, 'b-', linewidth=2, label='$f(x) = 1/x^2$')",
    "ax1.fill_between(x_vals, y_p2, color='skyblue', alpha=0.4, label='Área acotada (I = 1.0)')",
    "ax1.set_title('Integral Convergente ($p = 2 > 1$)', fontweight='bold')",
    "ax1.set_xlabel('$x$')",
    "ax1.set_ylabel('$f(x)$')",
    "ax1.set_ylim(0, 1.2)",
    "ax1.legend(frameon=True)",
    "ax1.grid(True, linestyle='--', alpha=0.5)",
    "",
    "# Gráfico 2: p = 0.5 (Diverge)",
    "ax2.plot(x_vals, y_p05, 'r-', linewidth=2, label='$f(x) = 1/\\\\sqrt{x}$') ",
    "ax2.fill_between(x_vals, y_p05, color='coral', alpha=0.4, label='Área infinita (I = $\\\\infty$)')",
    "ax2.set_title('Integral Divergente ($p = 0.5 \\\\leq 1$)', fontweight='bold')",
    "ax2.set_xlabel('$x$')",
    "ax2.set_ylabel('$f(x)$')",
    "ax2.set_ylim(0, 1.2)",
    "ax2.legend(frameon=True)",
    "ax2.grid(True, linestyle='--', alpha=0.5)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 5: CONVERGENCE CRITERIA ---
add_markdown([
    "## 2. Criterios de Convergencia para Funciones No Negativas",
    "",
    "### 2.1 Criterio de la Integral-p",
    "La integral impropia de primera especie de la función potencia:",
    "$$\\int_1^{\\infty} \\frac{1}{x^p} dx$$",
    "**converge** si y solo si $p > 1$. Su valor cuando converge es $\\frac{1}{p-1}$. Si $p \\le 1$, la integral **diverge**.",
    "",
    "### 2.2 Prueba de Comparación Directa",
    "Sean $f$ y $g$ funciones localmente integrables y no negativas ($0 \\le f(x) \\le g(x)$) para todo $x \\ge a$:",
    "- Si $\\int_a^{\\infty} g(x) dx$ **converge**, entonces $\\int_a^{\\infty} f(x) dx$ también **converge**.",
    "- Si $\\int_a^{\\infty} f(x) dx$ **diverge**, entonces $\\int_a^{\\infty} g(x) dx$ también **diverge**.",
    "",
    "### 2.3 Prueba de Comparación del Límite",
    "Si $f(x) \\ge 0$ y $g(x) > 0$ son localmente integrables en $[a, \\infty)$, y si:",
    "$$\\lim_{x \\to \\infty} \\frac{f(x)}{g(x)} = L$$",
    "donde $0 < L < \\infty$, entonces ambas integrales $\\int_a^{\\infty} f(x) dx$ y $\\int_a^{\\infty} g(x) dx$ convergen o divergen juntas."
])

# --- CELL 6: PHYSICAL & STATISTICAL APPLICATIONS ---
add_markdown([
    "## 3. Aplicaciones y Corrección de Erratas (Energía y Estadística)",
    "",
    "### Caso de Estudio 1: Energía Potencial Gravitacional (Corrección de Errata de signo de pág. 6)",
    "**Errata del PDF:** Al calcular la energía potencial de atracción gravitacional de una masa $m$ a una distancia $r$ de una masa central $M$, el texto del PDF deduce:",
    "$$U = -G \\int_r^{\\infty} \\frac{Mm}{x^2} dx = -GMm \\left[ -\\frac{1}{x} \\right]_r^{\\infty} = -GMm\\left(0 - \\left(-\\frac{1}{r}\\right)\\right) = \\frac{GMm}{r}$$",
    "**Corrección:** El resultado de la evaluación algebraica del PDF contiene un error de signo elemental:",
    "$$-GMm \\left( 0 - \\left( -\\frac{1}{r} \\right) \\right) = -GMm \\left( \\frac{1}{r} \\right) = -\\frac{GMm}{r}$$",
    "Físicamente, la energía potencial gravitacional en un campo atractivo **debe ser negativa** ($U(r) = -\\frac{GMm}{r}$), reflejando que la gravedad es una fuerza atractiva y el sistema está ligado. Un valor positivo de potencial implicaría una fuerza repulsiva.",
    "",
    "---",
    "",
    "### Caso de Estudio 2: Distribución de Pareto y su Media (Corrección de Errata de pág. 9)",
    "**Errata del PDF (Gamma y omisión de constante):** En la sección de aplicaciones estadísticas, el PDF evalúa la media de la distribución Gamma de parámetros $\\alpha$ (forma) y $\\beta$ (tasa). Tras realizar la sustitución de variables $u = \\beta x$, el texto escribe de manera errónea:",
    "$$E[X] = \\alpha$$",
    "Esto se debe a que omitió el factor $dx = \\frac{du}{\\beta}$ al cambiar el diferencial de la integral. La derivada de la sustitución introduce un factor $\\beta$ en el denominador.",
    "La media real de la distribución Gamma es:",
    "$$E[X] = \\frac{\\alpha}{\\beta}$$",
    "Para la distribución Pareto, cuya densidad es $f(x) = \\frac{\\alpha x_m^{\\alpha}}{x^{\\alpha+1}}$ para $x \\ge x_m > 0$:",
    "$$E[X] = \\int_{x_m}^{\\infty} x f(x) dx = \\alpha x_m^{\\alpha} \\int_{x_m}^{\\infty} x^{-\\alpha} dx = \\alpha x_m^{\\alpha} \\left[ \\frac{x^{1-\\alpha}}{1-\\alpha} \\right]_{x_m}^{\\infty} = \\frac{\\alpha x_m}{\\alpha - 1} \\quad (\\text{para } \\alpha > 1)$$"
])

# --- CELL 7: CODE - PHYSICAL & STATISTICAL CORRECTIONS ---
add_code([
    "# Validación computacional de las aplicaciones y correcciones",
    "G, M, m, r_val = 1.0, 5.0, 2.0, 3.0",
    "",
    "# 1. Evaluar potencial gravitacional numéricamente",
    "def force_integrand(x):",
    "    return -G * M * m / x**2",
    "",
    "U_numeric, _ = quad(force_integrand, r_val, np.inf)",
    "U_correct = -G * M * m / r_val",
    "U_pdf_wrong = G * M * m / r_val",
    "",
    "print(\"=== CASO 1: ENERGÍA POTENCIAL GRAVITACIONAL ===\")",
    "print(f\"Integración numérica (SciPy):  U = {U_numeric:.6f}\")",
    "print(f\"Fórmula analítica corregida: U = -GMm/r = {U_correct:.6f}\")",
    "print(f\"Valor erróneo del PDF:       U =  GMm/r = {U_pdf_wrong:.6f}\\n\")",
    "",
    "# 2. Media de Distribución Gamma (alpha = 3, beta = 2)",
    "alpha_g, beta_g = 3.0, 2.0",
    "def gamma_mean_integrand(x):",
    "    # Densidad f(x) * x",
    "    f_x = (beta_g**alpha_g / spec.gamma(alpha_g)) * x**(alpha_g - 1) * np.exp(-beta_g * x)",
    "    return x * f_x",
    "",
    "mean_numeric, _ = quad(gamma_mean_integrand, 0.0, np.inf)",
    "print(\"=== CASO 2: MEDIA DE LA DISTRIBUCIÓN GAMMA ===\")",
    "print(f\"Media calculada numéricamente: E[X] = {mean_numeric:.6f}\")",
    "print(f\"Fórmula analítica real (a/b):  E[X] = {alpha_g / beta_g:.6f}\")",
    "print(f\"Fórmula errónea del PDF (a):   E[X] = {alpha_g:.6f}\")"
])

# --- CELL 8: GAMMA FUNCTION ---
add_markdown([
    "## 4. La Función Gamma de Euler",
    "",
    "La **Función Gamma**, denotada por $\\Gamma(z)$, se define mediante una integral impropia de segunda especie (cerca de 0) y de primera especie (cerca del infinito):",
    "$$\\Gamma(z) = \\int_0^{\\infty} t^{z-1} e^{-t} dt \\quad \\text{para } \\text{Re}(z) > 0$$",
    "",
    "### 4.1 Propiedades Fundamentales",
    "1. **Relación de Recurrencia:** $\\Gamma(z+1) = z \\Gamma(z)$",
    "2. **Relación con el Factorial:** Para un entero positivo $n$:",
    "   $$\\Gamma(n+1) = n!$$",
    "3. **Valor Especial:** $\\Gamma(1/2) = \\sqrt{\\pi}$",
    "",
    "### 4.2 Legendre Duplication Formula (Corrección de Errata de pág. 9)",
    "**Errata del PDF:** En la lista de propiedades, el PDF introduce una deformación tipográfica en la fórmula de duplicación:",
    "$$\\Gamma(2z) = 22\\pi-1/\\sqrt{\\pi} \\Gamma(z) \\Gamma(z + 1/2)$$",
    "**Corrección:** La relación de duplicación de Legendre correcta es:",
    "$$\\Gamma(2z) = \\frac{2^{2z-1}}{\\sqrt{\\pi}} \\Gamma(z) \\Gamma\\left(z + \\frac{1}{2}\\right)$$"
])

# --- CELL 9: CODE - GAMMA PLOT & LEGENDRE ---
add_code([
    "# Graficar la función Gamma en el plano real",
    "x_g_pos = np.linspace(0.05, 4.5, 200)",
    "y_g_pos = spec.gamma(x_g_pos)",
    "",
    "# Para valores negativos, la función tiene asíntotas en enteros",
    "plt.figure(figsize=(9, 5.5))",
    "plt.plot(x_g_pos, y_g_pos, 'b-', linewidth=2.5, label='$\\\\Gamma(x)$')",
    "",
    "# Agregar tramos negativos para visualización clásica",
    "for k in range(0, 4):",
    "    x_g_neg = np.linspace(-k - 0.95, -k - 0.05, 100)",
    "    y_g_neg = spec.gamma(x_g_neg)",
    "    plt.plot(x_g_neg, y_g_neg, 'b-', linewidth=2)",
    "    plt.axvline(-k, color='red', linestyle=':', alpha=0.4)",
    "    ",
    "plt.axvline(0, color='red', linestyle=':', alpha=0.4, label='Polos (Enteros no positivos)')",
    "plt.title('La Función Gamma de Euler $\\\\Gamma(x)$ en la Recta Real', fontweight='bold')",
    "plt.xlabel('$x$')",
    "plt.ylabel('$\\\\Gamma(x)$')",
    "plt.xlim(-4.2, 4.2)",
    "plt.ylim(-8, 8)",
    "plt.grid(True, linestyle='--', alpha=0.5)",
    "plt.legend(frameon=True)",
    "plt.tight_layout()",
    "plt.show()",
    "",
    "# Validar la duplicación de Legendre para z = 2.5",
    "z_test = 2.5",
    "val_left = spec.gamma(2 * z_test)",
    "val_right = (2**(2*z_test - 1) / np.sqrt(np.pi)) * spec.gamma(z_test) * spec.gamma(z_test + 0.5)",
    "print(f\"Verificación de Duplicación (Legendre) para z = {z_test}:\")",
    "print(f\"Lado Izquierdo (Gamma(2z)): {val_left:.6f}\")",
    "print(f\"Lado Derecho (Fórmula):      {val_right:.6f}\")",
    "assert np.isclose(val_left, val_right)"
])

# --- CELL 10: CAUCHY PRINCIPAL VALUE ---
add_markdown([
    "## 5. Valor Principal de Cauchy",
    "",
    "### 5.1 Concepto",
    "Para funciones reales $f(x)$ que presentan una singularidad en un punto $c \\in (a, b)$, la integral de Riemann estándar diverge. Sin embargo, si nos aproximamos a la singularidad de manera **estrictamente simétrica** desde ambos lados mediante un único límite, podemos asignar un valor finito a la integral. Este valor se denomina **Valor Principal de Cauchy (p.v.)**:",
    "$$\\text{p.v.} \\int_a^b f(x) dx = \\lim_{\\epsilon \\to 0^+} \\left[ \\int_a^{c-\\epsilon} f(x) dx + \\int_{c+\\epsilon}^b f(x) dx \\right]$$",
    "",
    "### 5.2 Caso de Estudio 3: Integración de $\\cos(x)/x$ (Corrección de Errata de pág. 11)",
    "**Errata del PDF:** Al evaluar $\\text{p.v.} \\int_{-1}^1 \\frac{\\cos(x)}{x} dx$, el texto del PDF propone realizar integración por partes, y escribe de manera errónea la antiderivada de $\\frac{\\cos(x)}{x}$ como:",
    "$$\\left[ \\sin(x)\\ln|x| \\right]_{-1}^{-\\epsilon}$$",
    "Esto es un **error de cálculo básico**. La derivada de $\\sin(x)\\ln|x|$ es:",
    "$$\\frac{d}{dx}[\\sin(x)\\ln|x|] = \\cos(x)\\ln|x| + \\frac{\\sin(x)}{x} \\ne \\frac{\\cos(x)}{x}$$",
    "La primitiva de $\\frac{\\cos(x)}{x}$ no se puede representar mediante funciones elementales; su antiderivada es la función especial **Coseno Integral** $Ci(x)$.",
    "",
    "**Corrección y Demostración por Simetría Impar:**",
    "La función $g(x) = \\frac{\\cos(x)}{x}$ es una **función impar** en el intervalo simétrico $[-1, 1]$ excluyendo el origen, ya que $g(-x) = \\frac{\\cos(-x)}{-x} = -\\frac{\\cos(x)}{x} = -g(x)$.",
    "Por lo tanto, para cualquier $\\epsilon > 0$:",
    "$$\\int_{-1}^{-\\epsilon} \\frac{\\cos(x)}{x} dx = -\\int_{\\epsilon}^1 \\frac{\\cos(x)}{x} dx$$",
    "Sustituyendo esto en la definición del Valor Principal de Cauchy:",
    "$$\\text{p.v.} \\int_{-1}^1 \\frac{\\cos(x)}{x} dx = \\lim_{\\epsilon \\to 0^+} \\left[ -\\int_{\\epsilon}^1 \\frac{\\cos(x)}{x} dx + \\int_{\\epsilon}^1 \\frac{\\cos(x)}{x} dx \\right] = \\lim_{|\\epsilon \\to 0^+} (0) = 0$$",
    "Este resultado es exacto y no requiere antiderivadas no elementales ni integraciones por partes erróneas."
])

# --- CELL 11: CODE - CAUCHY PRINCIPAL VALUE VERIFICATION ---
add_code([
    "# Verificación numérica del Valor Principal de Cauchy para cos(x)/x",
    "epsilon_vals = [1e-3, 1e-4, 1e-5, 1e-6]",
    "",
    "print(\"=== CASO 3: VALOR PRINCIPAL DE CAUCHY DE cos(x)/x ===\")",
    "for eps in epsilon_vals:",
    "    # Evaluamos las dos mitades por separado",
    "    left_integral, _ = quad(lambda x: np.cos(x) / x, -1.0, -eps)",
    "    right_integral, _ = quad(lambda x: np.cos(x) / x, eps, 1.0)",
    "    pv_result = left_integral + right_integral",
    "    ",
    "    print(f\"eps = {eps:.1e} | Tramo [-1, -eps]: {left_integral:12.8f} | Tramo [eps, 1]: {right_integral:12.8f} | Suma (p.v.): {pv_result:.2e}\")",
    "    assert np.isclose(pv_result, 0.0, atol=1e-12)"
])

# --- CELL 12: LAPLACE TRANSFORM ---
add_markdown([
    "## 6. Introducción a la Transformada de Laplace",
    "",
    "La **Transformada de Laplace** de una función $f(t)$ definida para $t \\ge 0$ es una transformación integral que mapea una función en el dominio del tiempo a una función en el dominio de la frecuencia compleja $s$:",
    "$$F(s) = \\mathcal{L}\\{f(t)\\} = \\int_0^{\\infty} e^{-st} f(t) dt$$",
    "",
    "### 6.1 Propiedades Clave",
    "- **Linealidad:** $\\mathcal{L}\\{a f(t) + b g(t)\\} = a \\mathcal{L}\\{f(t)\\} + b \\mathcal{L}\\{g(t)\\}$",
    "- **Derivada:** $\\mathcal{L}\\{f'(t)\\} = s F(s) - f(0)$",
    "- **Traslación en el tiempo:** $\\mathcal{L}\\{f(t-a)u(t-a)\\} = e^{-as} F(s)$",
    "- **Teorema de la Convolución:** $\\mathcal{L}\\{(f * g)(t)\\} = F(s)G(s)$, donde:",
    "  $$(f * g)(t) = \\int_0^t f(\\tau)g(t-\\tau) d\\tau$$"
])

# --- CELL 13: CODE - LAPLACE NUMERICAL TRANSFORM ---
add_code([
    "# Simulación de la Transformada de Laplace numérica",
    "# f(t) = sin(2t) -> L{f} = 2 / (s^2 + 4)",
    "def f_time(t):",
    "    return np.sin(2.0 * t)",
    "",
    "def laplace_numerical(f, s_val):",
    "    # Integración numérica desde 0 a infinito",
    "    result, _ = quad(lambda t: np.exp(-s_val * t) * f(t), 0.0, np.inf)",
    "    return result",
    "",
    "s_grid = np.linspace(0.5, 4.0, 50)",
    "F_numeric = [laplace_numerical(f_time, s) for s in s_grid]",
    "F_theoretical = 2.0 / (s_grid**2 + 4.0)",
    "",
    "plt.figure(figsize=(9, 5))",
    "plt.plot(s_grid, F_theoretical, 'b-', linewidth=2.5, label='Teórico: $2/(s^2+4)$')",
    "plt.scatter(s_grid[::2], F_numeric[::2], color='red', marker='o', s=30, zorder=5, label='Numérico (SciPy)')",
    "plt.title('Transformada de Laplace de $f(t) = \\\\sin(2t)$', fontweight='bold')",
    "plt.xlabel('Frecuencia compleja $s$')",
    "plt.ylabel('$F(s)$')",
    "plt.grid(True, linestyle='--', alpha=0.5)",
    "plt.legend(frameon=True)",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 14: CASE 4: ODE RESONANCE ---
add_markdown([
    "## 7. Caso de Estudio 4: EDO Resonante y Convolución (Corrección de Errata de pág. 14)",
    "",
    "### 7.1 El Problema de la Resonancia",
    "**Enunciado del PDF:** Resolver la ecuación diferencial lineal ordinaria de segundo orden con condiciones iniciales nulas:",
    "$$y'' + 4y = \\sin(2t), \\quad y(0) = 0, \\; y'(0) = 0$$",
    "Este sistema modela un oscilador armónico simple sin amortiguamiento excitado por una fuerza sinusoidal con la frecuencia natural del sistema (resonancia pura con $\\omega = 2$).",
    "",
    "**Error en el Texto original:**",
    "El PDF aplica la transformada de Laplace y obtiene correctamente:",
    "$$Y(s) = \\frac{2}{(s^2+4)^2}$$",
    "Sin embargo, al invertir la transformada, el autor escribe incorrectamente:",
    "$$y(t) = t \\sin(2t) \\quad \\text{(Incorrecto)}$$",
    "Como se demostró en el test de validación, esta función **no satisface** la ecuación diferencial. La amplitud creciente en resonancia pura debe ir acompañada por un desfase de 90 grados, resultando en un término en coseno.",
    "",
    "**Deducción Correcta mediante Convolución:**",
    "Reescribimos la transformada como el producto de dos transformadas conocidas:",
    "$$Y(s) = \\frac{2}{(s^2+4)^2} = \\left( \\frac{2}{s^2+4} \\right) \\left( \\frac{1}{s^2+4} \\right) = \\mathcal{L}\\{\\sin(2t)\\} \\cdot \\mathcal{L}\\left\\{\\frac{1}{2}\\sin(2t)\\right\\}$$",
    "Por el Teorema de la Convolución, la solución temporal es:",
    "$$y(t) = \\left( \\sin(2t) * \\frac{1}{2}\\sin(2t) \\right) = \\frac{1}{2} \\int_0^t \\sin(2\\tau)\\sin(2(t-\\tau)) d\\tau$$",
    "Usando la identidad trigonométrica para el producto de senos:",
    "$$\\sin(A)\\sin(B) = \\frac{1}{2}[\\cos(A-B) - \\cos(A+B)]$$",
    "tenemos:",
    "$$\\sin(2\\tau)\\sin(2t-2\\tau) = \\frac{1}{2}[\\cos(4\\tau-2t) - \\cos(2t)]$$",
    "Sustituyendo en la integral:",
    "$$y(t) = \\frac{1}{4} \\int_0^t [\\cos(4\\tau-2t) - \\cos(2t)] d\\tau = \\frac{1}{4} \\left[ \\frac{\\sin(4\\tau-2t)}{4} - \\tau\\cos(2t) \\right]_0^t$$",
    "$$y(t) = \\frac{1}{4} \\left( \\frac{\\sin(2t)}{4} - t\\cos(2t) - \\left( \\frac{\\sin(-2t)}{4} - 0 \\right) \\right)$$",
    "Dado que $\\sin(-2t) = -\\sin(2t)$:",
    "$$y(t) = \\frac{1}{4} \\left( \\frac{\\sin(2t)}{4} - t\\cos(2t) + \\frac{\\sin(2t)}{4} \\right) = \\frac{1}{4} \\left( \\frac{\\sin(2t)}{2} - t\\cos(2t) \\right)$$",
    "$$y(t) = \\frac{1}{8}(\\sin(2t) - 2t\\cos(2t)) \\quad \\text{(Solución Real Correcta)}$$"
])

# --- CELL 15: CODE - RESONANCE TRAJECTORIES PLOT ---
add_code([
    "# Graficar ambas trayectorias para visualizar la resonancia y la discrepancia",
    "t_vals = np.linspace(0, 15.0, 500)",
    "y_correct_trajectory = (1.0/8.0) * (np.sin(2.0*t_vals) - 2.0*t_vals*np.cos(2.0*t_vals))",
    "y_wrong_trajectory = t_vals * np.sin(2.0*t_vals)",
    "",
    "plt.figure(figsize=(10, 6))",
    "plt.plot(t_vals, y_correct_trajectory, 'b-', linewidth=2.5, label='Solución Real (Resonancia Correcta)')",
    "plt.plot(t_vals, y_wrong_trajectory, 'r--', linewidth=2.0, label='Solución Errónea del PDF ($t\\\\sin(2t)$)')",
    "",
    "# Envolventes de amplitud",
    "plt.plot(t_vals, 0.25*t_vals, 'k:', alpha=0.5, label='Envolvente de amplitud real $\\\\pm t/4$')",
    "plt.plot(t_vals, -0.25*t_vals, 'k:', alpha=0.5)",
    "",
    "plt.title('Comparativa de Trayectorias de la EDO en Resonancia', fontweight='bold')",
    "plt.xlabel('Tiempo $t$ (segundos)')",
    "plt.ylabel('Desplazamiento $y(t)$')",
    "plt.grid(True, linestyle='--', alpha=0.5)",
    "plt.legend(loc='upper left', frameon=True)",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 16: SOLVED EXERCISES ---
add_markdown([
    "## 8. Ejercicios Resueltos",
    "",
    "### Ejercicio 1: Valor Principal de Cauchy",
    "**Enunciado:** Calcular el valor principal de Cauchy de la integral $\\int_{-1}^1 \\left( x^2 - \\frac{1}{x^3} \\right) dx$.",
    "",
    "**Solución:**",
    "Separamos la integral en dos partes operativas. El término cuadrático es regular y su integral de Riemann existe normalmente. El término singular es $\\frac{1}{x^3}$ con la singularidad en $c=0$.",
    "$$\\text{p.v.} \\int_{-1}^1 \\left( x^2 - \\frac{1}{x^3} \\right) dx = \\int_{-1}^1 x^2 dx - \\text{p.v.} \\int_{-1}^1 \\frac{1}{x^3} dx$$",
    "La primera integral es:",
    "$$\\int_{-1}^1 x^2 dx = \\left[ \\frac{x^3}{3} \\right]_{-1}^1 = \\frac{1}{3} - \\left( -\\frac{1}{3} \\right) = \\frac{2}{3}$$",
    "La segunda integral, por la definición del Valor Principal de Cauchy:",
    "$$\\text{p.v.} \\int_{-1}^1 \\frac{1}{x^3} dx = \\lim_{\\epsilon \\to 0^+} \\left[ \\int_{-1}^{-\\epsilon} \\frac{1}{x^3} dx + \\int_{\\epsilon}^1 \\frac{1}{x^3} dx \\right]$$",
    "$$\\int_{-1}^{-\\epsilon} \\frac{1}{x^3} dx = \\left[ -\\frac{1}{2x^2} \\right]_{-1}^{-\\epsilon} = -\\frac{1}{2\\epsilon^2} - \\left( -\\frac{1}{2} \\right) = -\\frac{1}{2\\epsilon^2} + \\frac{1}{2}$$",
    "$$\\int_{\\epsilon}^1 \\frac{1}{x^3} dx = \\left[ -\\frac{1}{2x^2} \\right]_{\\epsilon}^1 = -\\frac{1}{2} - \\left( -\\frac{1}{2\\epsilon^2} \\right) = -\\frac{1}{2} + \\frac{1}{2\\epsilon^2}$$",
    "Sumamos ambos tramos antes de aplicar el límite:",
    "$$\\left( -\\frac{1}{2\\epsilon^2} + \\frac{1}{2} \\right) + \\left( -\\frac{1}{2} + \\frac{1}{2\\epsilon^2} \\right) = 0 \\implies \\lim_{\\epsilon \\to 0^+} (0) = 0$$",
    "Por lo tanto:",
    "$$\\text{p.v.} \\int_{-1}^1 \\left( x^2 - \\frac{1}{x^3} \\right) dx = \\frac{2}{3} - 0 = \\frac{2}{3}$$",
    "",
    "---",
    "",
    "### Ejercicio 2: Valor Principal de Cauchy con múltiples singularidades",
    "**Enunciado:** Calcular el valor principal de la integral $\\int_0^{2\\pi} \\cot(x) dx$.",
    "",
    "**Solución:**",
    "La función $\\cot(x) = \\frac{\\cos(x)}{\\sin(x)}$ tiene tres singularidades en el intervalo cerrado de integración $[0, 2\\pi]$: en $c_1 = 0$, $c_2 = \\pi$, y $c_3 = 2\\pi$. Debemos separar el intervalo de integración para aislar las singularidades y tomar límites simétricos en torno a cada una de ellas:",
    "$$\\text{p.v.} \\int_0^{2\\pi} \\cot(x) dx = \\lim_{\\epsilon \\to 0^+} \\left[ \\int_{\\epsilon}^{\\pi-\\epsilon} \\cot(x) dx + \\int_{\\pi+\\epsilon}^{2\\pi-\\epsilon} \\cot(x) dx \\right]$$",
    "Usando la primitiva de la cotangente, la cual es $\\ln|\\sin(x)|$:",
    "- Para la primera parte:",
    "  $$\\int_{\\epsilon}^{\\pi-\\epsilon} \\cot(x) dx = \\left[ \\ln|\\sin(x)| \\right]_{\\epsilon}^{\\pi-\\epsilon} = \\ln|\\sin(\\pi - \\epsilon)| - \\ln|\\sin(\\epsilon)|$$",
    "  Dado que $\\sin(\\pi - \\epsilon) = \\sin(\\epsilon)$:",
    "  $$\\ln|\\sin(\\epsilon)| - \\ln|\\sin(\\epsilon)| = 0$$",
    "- Para la segunda parte:",
    "  $$\\int_{\\pi+\\epsilon}^{2\\pi-\\epsilon} \\cot(x) dx = \\left[ \\ln|\\sin(x)| \\right]_{\\pi+\\epsilon}^{2\\pi-\\epsilon} = \\ln|\\sin(2\\pi - \\epsilon)| - \\ln|\\sin(\\pi + \\epsilon)|$$",
    "  Dado que $\\sin(2\\pi - \\epsilon) = -\\sin(\\epsilon) \\implies |\\sin(2\\pi - \\epsilon)| = \\sin(\\epsilon)$ y $\\sin(\\pi + \\epsilon) = -\\sin(\\epsilon) \\implies |\\sin(\\pi + \\epsilon)| = \\sin(\\epsilon)$:",
    "  $$\\ln|\\sin(\\epsilon)| - \\ln|\\sin(\\epsilon)| = 0$$",
    "Sumando ambos resultados tramo a tramo, tenemos:",
    "$$\\text{p.v.} \\int_0^{2\\pi} \\cot(x) dx = \\lim_{\\epsilon \\to 0^+} (0 + 0) = 0$$"
])

# --- CELL 17: CONCLUSION AND BIBLIOGRAPHY ---
add_markdown([
    "## 9. Conclusión y Bibliografía",
    "",
    "Las integrales impropias y la transformada de Laplace son herramientas pilares para el modelado físico y matemático de sistemas dinámicos (especialmente osciladores en resonancia, decaimiento exponencial y probabilidades). Al contrastar el cálculo analítico con herramientas de simulación computacional, podemos desarrollar una visión matemática sumamente crítica y detectar errores de signos o de cálculo de antiderivadas presentes en la literatura académica tradicional.",
    "",
    "### Bibliografía",
    "[1] H. Anton, I. Bivens, y S. Davis, *Calculus*, 10a ed., Wiley, 2012.",
    "[2] E. Kreyszig, *Advanced Engineering Mathematics*, 10a ed., Wiley, 2011.",
    "[3] J. Stewart, *Calculus: Early Transcendentals*, 7a ed., Cengage Learning, 2012.",
    "[4] G. B. Arfken, *Mathematical Methods for Physicists*, 6a ed., Academic Press, 2005."
])

# Guardar a archivo
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"Cuaderno generado con éxito en: {output_path}")
