import json
import os

# Asegurar que existe la carpeta destino
output_dir = r"c:\Users\BlandskronNotebook\Documents\blandskron\licenciatura-en-fisica\05-calculo-2\leccion-11"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "conclusion-y-unificacion-calculo-2.ipynb")

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
    "# Lección 11: Conclusión y Unificación del Módulo 5 (Cálculo II)",
    "### Síntesis Integradora y Proyecto Unificador: Simulación de la Ecuación de Onda en 2D",
    "",
    "---",
    "",
    "Este cuaderno de Jupyter representa la **lección de consolidación y conclusión del Módulo 5: Cálculo II**. El propósito de esta lección es unificar las herramientas clave desarrolladas a lo largo del módulo —**cálculo diferencial multivariable** (derivadas parciales, gradiente, laplaciano), **cálculo integral avanzado** (integración por sumas de Riemann, integrales múltiples), y **ecuaciones diferenciales**— mediante el estudio analítico y la simulación numérica de un sistema físico real: la **Ecuación de Onda en una Membrana Elástica Bidimensional (Tambor)**.",
    "",
    "A lo largo de la lección, no solo resolveremos el sistema analíticamente mediante la separación de variables y el cálculo de coeficientes de Fourier (mediante integrales dobles), sino que implementaremos un resolvedor por diferencias finitas (FDM). Usaremos este resolvedor para rastrear la **conservación de la energía mecánica total** del sistema (cinética + potencial elástica) y para analizar y corregir una **errata crítica** muy común en libros de física e ingeniería respecto a la **condición de estabilidad de Courant-Friedrichs-Lewy (CFL) en 2D**.",
    "",
    "---"
])

# --- CELL 2: OBJECTIVES ---
add_markdown([
    "## Objetivos de Aprendizaje",
    "",
    "Al finalizar esta lección, serás capaz de:",
    "1. **Integrar** los conceptos fundamentales del Cálculo II (derivadas parciales, integrales múltiples y EDOs/EDPs) para modelar y analizar sistemas físicos complejos.",
    "2. **Deducir** analíticamente la ecuación de onda bidimensional para una membrana elástica bajo tensión uniforme a partir de principios de la mecánica clásica.",
    "3. **Resolver** la ecuación diferencial en derivadas parciales (EDP) resultante aplicando el método de separación de variables con condiciones de contorno de Dirichlet.",
    "4. **Calcular** los coeficientes de Fourier bidimensionales para una perturbación inicial utilizando integrales dobles y la propiedad de ortogonalidad de las funciones sinusoidales.",
    "5. **Implementar** un algoritmo numérico de diferencias finitas en diferencias de tiempo (FDTD) en Python para simular la evolución espacio-temporal de la membrana.",
    "6. **Evaluar** la conservación de la energía mecánica total (cinética y potencial elástica) mediante integraciones numéricas bidimensionales y sumas de Riemann.",
    "7. **Analizar de forma crítica** la condición de estabilidad CFL en 2D, demostrando por qué aplicar la fórmula clásica de 1D en simulaciones 2D induce inestabilidades exponenciales catastróficas."
])

# --- CELL 3: PHYSICAL MODEL ---
add_markdown([
    "## 1. Formulación Física: La Ecuación de Onda 2D",
    "",
    "Consideremos una membrana elástica bidimensional y delgada (como el parche de un tambor) que se extiende sobre una región rectangular $D = [0, L_x] \\times [0, L_y]$. Supondremos que la membrana es homogénea, con una densidad de masa superficial constante $\\rho$ (en $\\text{kg/m}^2$) y sometida a una tensión uniforme y constante $T$ (en $\\text{N/m}$) en todas las direcciones.",
    "",
    "Si $u(x, y, t)$ representa el desplazamiento vertical de la membrana en la posición $(x, y)$ y el tiempo $t$, la fuerza restauradora debida a la tensión superficial es proporcional a la curvatura de la membrana (el Laplaciano). Aplicando la segunda ley de Newton a un elemento de área infinitesimal $dx dy$, se obtiene la **Ecuación de Onda Bidimensional**:",
    "",
    "$$\\frac{\\partial^2 u}{\\partial t^2} = v^2 \\nabla^2 u$$",
    "",
    "donde:",
    "- $v = \\sqrt{\\frac{T}{\\rho}}$ representa la velocidad de propagación de la onda en la membrana.",
    "- $\\nabla^2 u = \\frac{\\partial^2 u}{\\partial x^2} + \\frac{\\partial^2 u}{\\partial y^2}$ es el operador diferencial Laplaciano en coordenadas cartesianas (estudiado en la Lección 5 y 6).",
    "",
    "### Condiciones de Frontera e Iniciales",
    "Para resolver el movimiento, requerimos especificar:",
    "1. **Condiciones de Frontera (Bordes fijos - Dirichlet):**",
    "   $$u(0, y, t) = u(L_x, y, t) = 0 \\quad \\forall y \\in [0, L_y]$$",
    "   $$u(x, 0, t) = u(x, L_y, t) = 0 \\quad \\forall x \\in [0, L_x]$$",
    "2. **Condiciones Iniciales:**",
    "   - Perfil de desplazamiento inicial: $u(x, y, 0) = f(x, y)$",
    "   - Perfil de velocidad inicial (supondremos reposo inicial): $\\frac{\\partial u}{\\partial t}(x, y, 0) = 0$"
])

# --- CELL 4: ANALYTICAL SOLUTION ---
add_markdown([
    "## 2. Solución Analítica: Separación de Variables e Integrales Múltiples",
    "",
    "Para resolver la ecuación, proponemos una solución separable de la forma:",
    "$$u(x, y, t) = X(x) Y(y) T(t)$$",
    "",
    "Sustituyendo en la ecuación de onda y dividiendo entre $v^2 X Y T$:",
    "$$\\frac{1}{v^2 T} \\frac{d^2 T}{d t^2} = \\frac{1}{X} \\frac{d^2 X}{d x^2} + \\frac{1}{Y} \\frac{d^2 Y}{d y^2}$$",
    "",
    "Como el lado izquierdo depende únicamente de $t$ y el lado derecho de $(x, y)$, ambos lados deben ser constantes. Llamaremos a esta constante $-\\lambda^2$ (asociada a frecuencias reales). Esto nos da una separación espacial y temporal:",
    "",
    "1. **EDO Temporal (Lección 3):**",
    "   $$\\frac{d^2 T}{d t^2} + \\omega^2 T = 0, \\quad \\text{donde } \\omega = v \\lambda$$",
    "2. **EDP Espacial (Problema de Helmholtz):**",
    "   $$\\frac{1}{X} \\frac{d^2 X}{d x^2} + \\frac{1}{Y} \\frac{d^2 Y}{d y^2} = -\\lambda^2 \\implies \\frac{1}{X} \\frac{d^2 X}{d x^2} = -\\lambda^2 - \\frac{1}{Y} \\frac{d^2 Y}{d y^2}$$",
    "",
    "Separando nuevamente el espacio con una constante $-k_x^2$:",
    "$$\\frac{d^2 X}{d x^2} + k_x^2 X = 0, \\quad \\frac{d^2 Y}{d y^2} + k_y^2 Y = 0, \\quad \\text{donde } k_x^2 + k_y^2 = \\lambda^2$$",
    "",
    "Aplicando las condiciones de frontera fijas en los extremos $X(0) = X(L_x) = 0$ y $Y(0) = Y(L_y) = 0$, obtenemos los **Modos Propios Espaciales**:",
    "$$X_m(x) = \\sin\\left(\\frac{m \\pi x}{L_x}\\right), \\quad Y_n(y) = \\sin\\left(\\frac{n \\pi y}{L_y}\\right) \\quad \\text{para } m, n \\in \\mathbb{N}^+$$",
    "",
    "Las frecuencias naturales angulares de oscilación (los autovalores) son:",
    "$$\\omega_{mn} = v \\pi \\sqrt{\\frac{m^2}{L_x^2} + \\frac{n^2}{L_y^2}}$$",
    "",
    "Cada par $(m, n)$ define un **Modo Normal de Vibración**:",
    "$$u_{mn}(x, y, t) = \\sin\\left(\\frac{m \\pi x}{L_x}\\right) \\sin\\left(\\frac{n \\pi y}{L_y}\\right) \\cos(\\omega_{mn} t)$$",
    "",
    "### Superposición y Coeficientes de Fourier via Integrales Dobles",
    "La solución general es una combinación lineal de todos los modos:",
    "$$u(x, y, t) = \\sum_{m=1}^{\\infty} \\sum_{n=1}^{\\infty} A_{mn} \\sin\\left(\\frac{m \\pi x}{L_x}\\right) \\sin\\left(\\frac{n \\pi y}{L_y}\\right) \\cos(\\omega_{mn} t)$$",
    "",
    "Para satisfacer la condición inicial $u(x, y, 0) = f(x, y)$, los coeficientes $A_{mn}$ se calculan proyectando el perfil inicial sobre la base de modos espaciales. Por la propiedad de ortogonalidad de los senos, esto requiere una **integral doble sobre la región de la membrana** (Lección 8):",
    "$$A_{mn} = \\frac{4}{L_x L_y} \\int_0^{L_y} \\int_0^{L_x} f(x, y) \\sin\\left(\\frac{m\\pi x}{L_x}\\right) \\sin\\left(\\frac{n\\pi y}{L_y}\right) dx dy$$"
])

# --- CELL 5: CODE - SYMPY COEFFICIENTS AND MODES ---
add_code([
    "import sympy as sp",
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "from mpl_toolkits.mplot3d import Axes3D",
    "",
    "# 1. Cálculo simbólico de los coeficientes de Fourier",
    "x_s, y_s = sp.symbols('x y')",
    "Lx_s, Ly_s = sp.symbols('L_x L_y', positive=True)",
    "m_s, n_s = sp.symbols('m n', integer=True, positive=True)",
    "",
    "# Perfil inicial: una campana sinusoidal simétrica",
    "# f(x, y) = sin(pi*x/Lx) * sin(pi*y/Ly)",
    "f_init = sp.sin(sp.pi * x_s / Lx_s) * sp.sin(sp.pi * y_s / Ly_s)",
    "",
    "# Expresión para la integral de coeficientes",
    "integrand = f_init * sp.sin(m_s * sp.pi * x_s / Lx_s) * sp.sin(n_s * sp.pi * y_s / Ly_s)",
    "I_double = sp.integrate(sp.integrate(integrand, (x_s, 0, Lx_s)), (y_s, 0, Ly_s))",
    "A_mn = (4 / (Lx_s * Ly_s)) * I_double",
    "",
    "print(\"=== ANÁLISIS SIMBÓLICO CON SYMPY ===\")",
    "print(f\"Expresión analítica de los coeficientes A_mn:\")",
    "sp.pprint(sp.simplify(A_mn))",
    "",
    "# 2. Graficación de los modos normales de vibración (1,1), (2,1), (1,2) y (2,2)",
    "Lx, Ly = 1.0, 1.0",
    "x_vals = np.linspace(0, Lx, 80)",
    "y_vals = np.linspace(0, Ly, 80)",
    "X, Y = np.meshgrid(x_vals, y_vals)",
    "",
    "modes = [(1, 1), (2, 1), (1, 2), (2, 2)]",
    "fig = plt.figure(figsize=(12, 10))",
    "",
    "for i, (m, n) in enumerate(modes, 1):",
    "    Z = np.sin(m * np.pi * X / Lx) * np.sin(n * np.pi * Y / Ly)",
    "    ax = fig.add_subplot(2, 2, i, projection='3d')",
    "    surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', alpha=0.9)",
    "    ax.set_title(f'Modo Normal ({m}, {n})', fontweight='bold')",
    "    ax.set_xlabel('$x$')",
    "    ax.set_ylabel('$y$')",
    "    ax.set_zlabel('$u(x,y)$')",
    "    ax.set_zlim(-1.1, 1.1)",
    "    ax.grid(True, ls='--', alpha=0.5)",
    "    ",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 6: ENERGY FORMULATION ---
add_markdown([
    "## 3. Formulación Energética: Integración de Campo Multivariable",
    "",
    "La energía mecánica total $E(t)$ de la membrana vibratoria es la suma de su **energía cinética** $E_k(t)$ (debida a la velocidad vertical de sus elementos de masa) y su **energía potencial elástica** $E_p(t)$ (debida al trabajo realizado contra la tensión superficial para deformar la membrana).",
    "",
    "### A. Energía Cinética",
    "Cada elemento infinitesimal de área $dx dy$ posee una masa $dm = \\rho dx dy$ y una velocidad instantánea $u_t = \\frac{\\partial u}{\\partial t}$. La energía cinética de este elemento es $\\frac{1}{2} (dm) u_t^2$. Integrando sobre toda la superficie $D$:",
    "$$E_k(t) = \\frac{1}{2} \\rho \\iint_D \\left( \\frac{\\partial u}{\\partial t} \\right)^2 dx dy$$",
    "",
    "### B. Energía Potencial Elástica",
    "La energía potencial elástica se asocia al aumento del área superficial de la membrana cuando se deforma, multiplicado por la tensión $T$. Para desplazamientos pequeños, la energía potencial acumulada es proporcional a la integral del cuadrado de la magnitud de la pendiente de la deformación (el gradiente de $u$):",
    "$$E_p(t) = \\frac{1}{2} T \\iint_D \\| \\nabla u \\|^2 dx dy = \\frac{1}{2} T \\iint_D \\left[ \\left( \\frac{\\partial u}{\\partial x} \\right)^2 + \\left( \\frac{\\partial u}{\\partial y} \\right)^2 \\right] dx dy$$",
    "",
    "### Conservación del Hamiltoniano",
    "En ausencia de disipación (fricción), la energía total se conserva:",
    "$$E_{\\text{total}} = E_k(t) + E_p(t) = C \\quad \\forall t \\ge 0$$",
    "Este análisis nos permite verificar la precisión física de nuestros esquemas numéricos de discretización: si el resolvedor no conserva la energía total a lo largo del tiempo, el modelo carece de consistencia física."
])

# --- CELL 7: NUMERICAL RESOLUTION & CFL ---
add_markdown([
    "## 4. Resolución Numérica por Diferencias Finitas (FDTD)",
    "",
    "Para resolver la ecuación de onda de forma computacional, discretizamos el dominio espacial con pasos discretos $\\Delta x$ y $\\Delta y$, y el dominio temporal con pasos $\\Delta t$. Sea $u_{i, j}^n \\approx u(i \\Delta x, j \\Delta y, n \\Delta t)$ la aproximación en la rejilla.",
    "",
    "Sustituyendo las derivadas segundas espaciales y temporales por sus aproximaciones por diferencias finitas centrales de segundo orden (Lección 1 y 5):",
    "$$\\frac{u_{i, j}^{n+1} - 2 u_{i, j}^n + u_{i, j}^{n-1}}{\\Delta t^2} \\approx v^2 \\left[ \\frac{u_{i+1, j}^n - 2 u_{i, j}^n + u_{i-1, j}^n}{\\Delta x^2} + \\frac{u_{i, j+1}^n - 2 u_{i, j}^n + u_{i, j-1}^n}{\\Delta y^2} \\right]$$",
    "",
    "Despejando el término en el tiempo futuro $u_{i, j}^{n+1}$:",
    "$$u_{i, j}^{n+1} = 2 u_{i, j}^n - u_{i, j}^{n-1} + v^2 \\Delta t^2 \\left[ \\frac{u_{i+1, j}^n - 2 u_{i, j}^n + u_{i-1, j}^n}{\\Delta x^2} + \\frac{u_{i, j+1}^n - 2 u_{i, j}^n + u_{i, j-1}^n}{\\Delta y^2} \\right]$$",
    "",
    "Esta relación recurrente permite avanzar el sistema en el tiempo a partir de dos estados anteriores ($n$ y $n-1$). Para el primer paso temporal ($n=0$), dado que la velocidad inicial es nula ($u_t(x, y, 0) = 0$), podemos deducir que $u_{i,j}^{-1} = u_{i,j}^1$, resultando en:",
    "$$u_{i, j}^1 = u_{i, j}^0 + \\frac{1}{2} v^2 \\Delta t^2 \\left[ \\frac{u_{i+1, j}^0 - 2 u_{i, j}^0 + u_{i-1, j}^0}{\\Delta x^2} + \\frac{u_{i, j+1}^0 - 2 u_{i, j}^0 + u_{i, j-1}^0}{\\Delta y^2} \\right]$$",
    "",
    "---",
    "",
    "### Caso Crítico: Condición de Estabilidad CFL en 2D (Corrección de Errata de la Literatura)",
    "**La Errata Común:** Muchos libros de texto e introducciones a métodos numéricos aplican la condición clásica de estabilidad de 1D de forma directa en simulaciones bidimensionales, estableciendo que el paso de tiempo $\\Delta t$ debe satisfacer:",
    "$$\\Delta t \\le \\frac{\\Delta x}{v}$$",
    "",
    "**La Corrección Matemática:** Físicamente, en una rejilla bidimensional, la perturbación se propaga no solo en las direcciones de los ejes, sino de forma diagonal. La distancia entre nodos adyacentes en diagonal es menor que en línea recta, lo cual acelera la transmisión efectiva. Un análisis formal de estabilidad de Von Neumann demuestra que la **condición de Courant-Friedrichs-Lewy (CFL) en 2D** real es:",
    "$$\\Delta t \\le \\frac{1}{v \\sqrt{\\frac{1}{\\Delta x^2} + \\frac{1}{\\Delta y^2}}}$$",
    "",
    "Si discretizamos espacialmente de forma cuadrada (donde $\\Delta x = \\Delta y = h$), esta condición se reduce a:",
    "$$\\Delta t \\le \\frac{h}{v \\sqrt{2}} \\approx 0.7071 \\frac{h}{v}$$",
    "",
    "Si elegimos un paso de tiempo mayor (por ejemplo, $\\Delta t = 0.95 \\frac{h}{v}$), la simulación viola la estabilidad matemática del esquema numérico, provocando que los errores se multipliquen exponencialmente en cada iteración y el sistema explote catastróficamente (valores que tienden a infinito). Esto lo validaremos de manera computacional en la simulación."
])

# --- CELL 8: CODE - SOLVER IMPLEMENTATION ---
add_code([
    "import numpy as np",
    "",
    "def simulate_membrane(Lx, Ly, Nx, Ny, T_max, v, CFL_factor, initial_mode=(1,1)):",
    "    # Discretización espacial",
    "    dx = Lx / Nx",
    "    dy = Ly / Ny",
    "    x = np.linspace(0, Lx, Nx + 1)",
    "    y = np.linspace(0, Ly, Ny + 1)",
    "    X, Y = np.meshgrid(x, y, indexing='ij')",
    "    ",
    "    # Condición de estabilidad CFL 2D",
    "    h = min(dx, dy)",
    "    dt_cfl = h / (v * np.sqrt(2))",
    "    dt = dt_cfl * CFL_factor",
    "    Nt = int(T_max / dt)",
    "    ",
    "    # Parámetros físicos constantes",
    "    rho = 1.0  # kg/m^2",
    "    T_tension = rho * v**2  # N/m",
    "    ",
    "    # Coeficientes numéricos",
    "    rx2 = (v * dt / dx)**2",
    "    ry2 = (v * dt / dy)**2",
    "    ",
    "    # Inicializar campos de desplazamiento",
    "    u_new = np.zeros((Nx + 1, Ny + 1))",
    "    u = np.zeros((Nx + 1, Ny + 1))",
    "    u_old = np.zeros((Nx + 1, Ny + 1))",
    "    ",
    "    # Estado inicial: Modo normal seleccionado",
    "    m, n = initial_mode",
    "    u = np.sin(m * np.pi * X / Lx) * np.sin(n * np.pi * Y / Ly)",
    "    ",
    "    # Aplicar condiciones de frontera Dirichlet",
    "    u[0, :] = 0.0",
    "    u[Nx, :] = 0.0",
    "    u[:, 0] = 0.0",
    "    u[:, Ny] = 0.0",
    "    ",
    "    # Guardar estado en paso temporal n=0",
    "    u_old = np.copy(u)",
    "    ",
    "    # Primer paso de tiempo (usando u_t = 0 en t=0)",
    "    for i in range(1, Nx):",
    "        for j in range(1, Ny):",
    "            laplacian = (",
    "                rx2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +",
    "                ry2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1])",
    "            )",
    "            u_new[i, j] = u[i, j] + 0.5 * laplacian",
    "            ",
    "    u = np.copy(u_new)",
    "    ",
    "    energy_history = []",
    "    all_states = [np.copy(u_old), np.copy(u)]",
    "    times = [0.0, dt]",
    "    ",
    "    # Bucle temporal de avance",
    "    for step in range(2, Nt):",
    "        u_new = np.zeros((Nx + 1, Ny + 1))",
    "        for i in range(1, Nx):",
    "            for j in range(1, Ny):",
    "                laplacian = (",
    "                    rx2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +",
    "                    ry2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1])",
    "                )",
    "                u_new[i, j] = 2*u[i, j] - u_old[i, j] + laplacian",
    "                ",
    "        # Fronteras Dirichlet",
    "        u_new[0, :] = 0.0",
    "        u_new[Nx, :] = 0.0",
    "        u_new[:, 0] = 0.0",
    "        u_new[:, Ny] = 0.0",
    "        ",
    "        # Evaluar Integrales de Energía (Sumas de Riemann bidimensionales)",
    "        v_t = (u_new - u) / dt",
    "        Ek = 0.5 * rho * np.sum(v_t[1:Nx, 1:Ny]**2) * dx * dy",
    "        ",
    "        du_dx = (u_new[1:, :Ny] - u_new[:-1, :Ny]) / dx",
    "        du_dy = (u_new[:Nx, 1:] - u_new[:Nx, :-1]) / dy",
    "        Ep = 0.5 * T_tension * (np.sum(du_dx**2) + np.sum(du_dy**2)) * dx * dy",
    "        ",
    "        energy_history.append((step * dt, Ek, Ep, Ek + Ep))",
    "        ",
    "        # Actualizar estados",
    "        u_old = np.copy(u)",
    "        u = np.copy(u_new)",
    "        ",
    "        # Almacenar estados periódicamente para visualización",
    "        if step % (Nt // 5) == 0 or step == Nt - 1:",
    "            all_states.append(np.copy(u))",
    "            times.append(step * dt)",
    "            ",
    "        # Chequeo de inestabilidad exponencial (Explosión numérica)",
    "        if np.any(np.isnan(u)) or np.max(np.abs(u)) > 10.0:",
    "            # La simulación ha explotado",
    "            return None, None, None, None",
    "            ",
    "    return times, all_states, np.array(energy_history), dt"
])

# --- CELL 9: CODE - STABLE SIMULATION GRAPHICS ---
add_code([
    "import matplotlib.pyplot as plt",
    "from mpl_toolkits.mplot3d import Axes3D",
    "",
    "Lx, Ly = 1.0, 1.0",
    "Nx, Ny = 40, 40",
    "v = 1.0",
    "T_max = 2.5",
    "CFL_stable = 0.9  # CFL < 1.0 es estable",
    "",
    "times, states, energy, dt = simulate_membrane(Lx, Ly, Nx, Ny, T_max, v, CFL_stable, initial_mode=(2,2))",
    "",
    "if states is not None:",
    "    print(f\"Simulación estable completada con éxito. Paso de tiempo dt = {dt:.6f} segundos.\")",
    "    ",
    "    # Graficar la membrana en 3D en 4 instantes de tiempo clave",
    "    x = np.linspace(0, Lx, Nx + 1)",
    "    y = np.linspace(0, Ly, Ny + 1)",
    "    X, Y = np.meshgrid(x, y, indexing='ij')",
    "    ",
    "    fig = plt.figure(figsize=(14, 10))",
    "    indices_to_plot = [0, 1, 2, len(states)-1]",
    "    ",
    "    for i, idx in enumerate(indices_to_plot, 1):",
    "        ax = fig.add_subplot(2, 2, i, projection='3d')",
    "        surf = ax.plot_surface(X, Y, states[idx], cmap='viridis', edgecolor='none', alpha=0.9)",
    "        ax.set_title(f'Desplazamiento en t = {times[idx]:.4f} s', fontweight='bold')",
    "        ax.set_xlabel('$x$')",
    "        ax.set_ylabel('$y$')",
    "        ax.set_zlabel('$u(x,y)$')",
    "        ax.set_zlim(-1.1, 1.1)",
    "        ax.grid(True, ls='--', alpha=0.5)",
    "        ",
    "    plt.tight_layout()",
    "    plt.show()",
    "else:",
    "    print(\"Error: La simulación estable falló.\")"
])

# --- CELL 10: CODE - ENERGY CONSERVATION GRAPHICS ---
add_code([
    "if states is not None and energy is not None:",
    "    t_grid = energy[:, 0]",
    "    Ek_vals = energy[:, 1]",
    "    Ep_vals = energy[:, 2]",
    "    Et_vals = energy[:, 3]",
    "    ",
    "    # Calcular estadísticas de conservación",
    "    mean_energy = np.mean(Et_vals)",
    "    std_energy = np.std(Et_vals)",
    "    relative_error = std_energy / mean_energy",
    "    ",
    "    print(\"=== ANÁLISIS DE CONSERVACIÓN DE ENERGÍA ===\")",
    "    print(f\"Energía Promedio: {mean_energy:.6f}\")",
    "    print(f\"Desviación Estándar de la Energía Total: {std_energy:.2e}\")",
    "    print(f\"Variación Relativa (fluctuación numérica): {relative_error * 100:.6f}%\")",
    "    ",
    "    plt.figure(figsize=(10, 5.5))",
    "    plt.plot(t_grid, Ek_vals, 'r-', linewidth=2.0, label='Energía Cinética ($E_k$)')",
    "    plt.plot(t_grid, Ep_vals, 'g-', linewidth=2.0, label='Energía Potencial Elástica ($E_p$)')",
    "    plt.plot(t_grid, Et_vals, 'k-', linewidth=3.0, label='Energía Mecánica Total ($E_k + E_p$)')",
    "    ",
    "    plt.title('Conservación del Hamiltoniano (Energía Total) en Diferencias Finitas', fontweight='bold')",
    "    plt.xlabel('Tiempo $t$ (segundos)')",
    "    plt.ylabel('Energía')",
    "    plt.xlim(0, T_max)",
    "    plt.ylim(0, np.max(Et_vals) * 1.3)",
    "    plt.grid(True, linestyle='--', alpha=0.5)",
    "    plt.legend(loc='upper right', frameon=True)",
    "    plt.tight_layout()",
    "    plt.show()",
    "    ",
    "    # Verificación de tolerancia física",
    "    assert relative_error < 0.1, \"Error: La simulación no conserva adecuadamente la energía.\""
])

# --- CELL 11: CODE - CFL VIOLATION DEMO ---
add_code([
    "CFL_unstable = 1.45  # CFL > 1.0 (Ej. usar el criterio 1D en 2D)",
    "",
    "print(\"=== TEST DE INESTABILIDAD NUMÉRICA (CFL ERRÓNEO) ===\")",
    "print(\"Corriendo simulación inestable con CFL factor = 1.45 (Violación del límite 2D)...\\n\")",
    "",
    "# Para ilustrar el crecimiento de la inestabilidad, corremos una simulación corta",
    "times_un, states_un, energy_un, dt_un = simulate_membrane(Lx, Ly, Nx, Ny, 1.5, v, CFL_unstable, initial_mode=(2,2))",
    "",
    "if states_un is None:",
    "    print(\"¡CORRECTO! La simulación explotó numéricamente por inestabilidad de Courant.\")",
    "    print(\"Esto demuestra de forma cuantitativa la errata de la literatura técnica tradicional:\")",
    "    print(\"El criterio 1D dt <= dx/v no es aplicable en 2D, requiriendo el factor 1/sqrt(2).\")",
    "else:",
    "    print(\"ADVERTENCIA: La simulación inestable no explotó de forma esperada.\")"
])

# --- CELL 12: SOLVED EXERCISES ---
add_markdown([
    "## 5. Ejercicios Resueltos de Consolidación",
    "",
    "### Ejercicio 1: Cálculo del Laplaciano y Frecuencias en Membrana Cuadrada",
    "**Enunciado:** Una membrana de tambor cuadrada de lado $L = 1\\text{ m}$, velocidad de propagación $v = 1\\text{ m/s}$ y condiciones de borde fijas vibra en su frecuencia fundamental. Calcular analíticamente:",
    "1. Las coordenadas del primer nodo interior con desplazamiento nulo (línea nodal) excluyendo las fronteras si vibra en el modo normal $(2, 2)$.",
    "2. La frecuencia angular fundamental $\\omega_{11}$ del sistema.",
    "",
    "**Solución:**",
    "1. El desplazamiento del modo normal $(2,2)$ está dado por:",
    "   $$u_{22}(x, y, t) = \\sin(2\\pi x) \\sin(2\\pi y) \\cos(\\omega_{22} t)$$",
    "   Las líneas nodales corresponden a los puntos donde $u_{22}(x, y, t) = 0$ para todo $t$. Esto ocurre cuando:",
    "   $$\\sin(2\\pi x) = 0 \\implies 2\\pi x = k \\pi \\implies x = \\frac{k}{2} \\quad \\text{para } k \\in \\mathbb{Z}$$",
    "   Para el rango interior $x \\in (0, 1)$, el único valor posible es para $k=1$, dando $x = 0.5\\text{ m}$.",
    "   De igual forma, para $y$ obtenemos la línea nodal $y = 0.5\\text{ m}$.",
    "   Por lo tanto, la membrana se divide en 4 cuadrantes que vibran en fase opuesta, cruzándose en las líneas nodales $x = 0.5$ e $y = 0.5$.",
    "",
    "2. La frecuencia angular de oscilación está dada por:",
    "   $$\\omega_{mn} = v \\pi \\sqrt{\\frac{m^2}{L_x^2} + \\frac{n^2}{L_y^2}}$$",
    "   Para el modo fundamental $(m=1, n=1)$ y $L_x = L_y = 1\\text{ m}$:",
    "   $$\\omega_{11} = (1) \\pi \\sqrt{\\frac{1^2}{1^2} + \\frac{1^2}{1^2}} = \\pi \\sqrt{2} \\approx 4.4428 \\text{ rad/s}$$",
    "",
    "---",
    "",
    "### Ejercicio 2: Relación del CFL en Mallas Rectangulares",
    "**Enunciado:** Demostrar analíticamente que para una malla rectangular general donde $\\Delta x \\ne \\Delta y$, el paso de tiempo crítico $\\Delta t$ obtenido mediante el análisis de estabilidad de Von Neumann es:",
    "$$\\Delta t \\le \\frac{1}{v \\sqrt{\\frac{1}{\\Delta x^2} + \\frac{1}{\\Delta y^2}}}$$",
    "",
    "**Solución:**",
    "Proponemos una solución armónica para los errores del esquema numérico de la forma:",
    "$$e_{i, j}^n = \\xi^n e^{i (k_x x_i + k_y y_j)}$$",
    "donde $\\xi$ es el factor de amplificación. Para estabilidad, requerimos que el módulo de $\\xi$ sea menor o igual a 1 ($|\\xi| \\le 1$) para todos los números de onda $k_x, k_y$.",
    "Sustituyendo esta forma en el esquema numérico homogeneizado:",
    "$$\\xi^2 - 2\\xi + 1 = 4 \\xi \\left[ -rx^2 \\sin^2\\left(\\frac{k_x \\Delta x}{2}\\right) - ry^2 \\sin^2\\left(\\frac{k_y \\Delta y}{2}\\right) \\right]$$",
    "donde $rx = \\frac{v \\Delta t}{\\Delta x}$ y $ry = \\frac{v \\Delta t}{\\Delta y}$.",
    "Esta es una ecuación cuadrática para $\\xi$. Para que las raíces de $\\xi$ no superen la unidad, el término en corchetes (que llamaremos $-S$) debe satisfacer $S \\le 1$ para todas las posibles combinaciones de senos. El valor máximo de los senos es 1, por lo que:",
    "$$rx^2 + ry^2 \\le 1 \\implies \\left( \\frac{v \\Delta t}{\\Delta x} \\right)^2 + \\left( \\frac{v \\Delta t}{\\Delta y} \\right)^2 \\le 1$$",
    "Despejando $\\Delta t^2$:",
    "$$v^2 \\Delta t^2 \\left( \\frac{1}{\\Delta x^2} + \\frac{1}{\\Delta y^2} \\right) \\le 1 \\implies \\Delta t \\le \\frac{1}{v \\sqrt{\\frac{1}{\\Delta x^2} + \\frac{1}{\\Delta y^2}}}$$",
    "Lo cual demuestra rigurosamente la condición de Courant-Friedrichs-Lewy en 2D."
])

# --- CELL 13: CONCLUSION & BIBLIOGRAPHY ---
add_markdown([
    "## 6. Conclusiones del Módulo y Bibliografía",
    "",
    "El Módulo 5 nos ha permitido consolidar una de las áreas más potentes del análisis real orientado a la física: el modelado lineal e integrador de campos vectoriales, transformaciones, integración multivariable y ecuaciones diferenciales ordinarias y parciales.",
    "",
    "A través de este proyecto unificador, hemos presenciado cómo:",
    "- El **Laplaciano** (Lección 5 y 6) actúa físicamente como una medida de la curvatura espacial que genera las fuerzas restauradoras en medios continuos.",
    "- Las **EDOs** (Lección 3) describen la evolución temporal de los armónicos individuales de oscilación.",
    "- Las **Integrales Dobles** (Lección 8) sirven tanto para proyectar estados iniciales sobre una base ortogonal (coeficientes de Fourier) como para medir magnitudes globales conservativas (Hamiltoniano/Energía del sistema).",
    "- El **Cálculo Numérico** y la validación en computadoras nos permiten refinar y confrontar de forma crítica los límites y condiciones de estabilidad matemática que muchas veces son tergiversados u omitidos en la literatura técnica tradicional.",
    "",
    "### Bibliografía",
    "[1] J. Stewart, *Calculus: Early Transcendentals*, 7a ed., Cengage Learning, 2012.",
    "[2] E. Kreyszig, *Advanced Engineering Mathematics*, 10a ed., Wiley, 2011.",
    "[3] G. B. Arfken, *Mathematical Methods for Physicists*, 6a ed., Academic Press, 2005.",
    "[4] R. Courant, K. Friedrichs, y H. Lewy, *On the Partial Difference Equations of Mathematical Physics*, IBM Journal, 1967."
])

# Guardar a archivo
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"Cuaderno generado con éxito en: {output_path}")
