import json
import os

# Asegurar que existe la carpeta destino
output_dir = r"c:\Users\BlandskronNotebook\Documents\blandskron\licenciatura-en-fisica\05-calculo-2\introduccion"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "conceptos-esenciales.ipynb")

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
    "# Introducción al Módulo 5: Conceptos Esenciales y Prerrequisitos de Cálculo II",
    "### Preparación Matemática y Computacional en Python",
    "",
    "---",
    "",
    "¡Bienvenido al **Módulo 5: Cálculo II**! Este módulo es uno de los pilares de la física matemática y el análisis numérico avanzado. Abarca temas como integrales múltiples, análisis vectorial (teoremas de Green, Stokes y Gauss), optimización multivariable con restricciones (multiplicadores de Lagrange) y ecuaciones diferenciales ordinarias (EDOs) y parciales (EDPs).",
    "",
    "Para aprovechar al máximo este módulo y poder ejecutar las simulaciones computacionales sin inconvenientes, es necesario contar con una base matemática sólida y conocer el funcionamiento de las librerías científicas clásicas de Python. Esta lección de **Introducción** actúa como un puente didáctico. En ella repasaremos:",
    "1. **Teoremas y técnicas de integración clásicas** del Cálculo I (una variable).",
    "2. **Conceptos de álgebra lineal y vectorial** en 2D y 3D (productos punto y cruz, matrices y determinantes).",
    "3. **Uso de Python científico:** manipulación simbólica con `SymPy`, discretización y mallas con `NumPy`, y visualizaciones 2D/3D con `Matplotlib`.",
    "",
    "---"
])

# --- CELL 2: OBJECTIVES ---
add_markdown([
    "## Objetivos de Aprendizaje",
    "",
    "Al finalizar esta lección de introducción, serás capaz de:",
    "1. **Aplicar** técnicas de integración clásicas de una variable (sustitución, partes) de manera manual y verificar los resultados simbólicamente en Python.",
    "2. **Operar** con vectores en $\\mathbb{R}^3$, calculando normas, productos escalares (punto) y vectoriales (cruz), interpretando sus propiedades geométricas.",
    "3. **Calcular** determinantes de matrices de segundo y tercer orden, comprendiendo su rol en las transformaciones lineales y Jacobianas.",
    "4. **Utilizar** `SymPy` para calcular límites, derivadas e integrales de forma analítica en celdas de Jupyter.",
    "5. **Construir** mallas bidimensionales discretas (`np.meshgrid`) en `NumPy` para evaluar campos y funciones sobre regiones espaciales.",
    "6. **Visualizar** curvas paramétricas y superficies tridimensionales utilizando `Matplotlib` de forma limpia y profesional."
])

# --- CELL 3: CALCULUS I REVIEW ---
add_markdown([
    "## 1. Repaso de Cálculo I: Derivadas y Técnicas de Integración",
    "",
    "En Cálculo II, las funciones dependerán de múltiples variables independientes. Sin embargo, las reglas para derivar e integrar respecto a cada una de ellas siguen siendo las mismas del Cálculo I (derivación parcial).",
    "",
    "### 1.1 Regla de la Cadena",
    "Si $y = f(u)$ y $u = g(x)$, entonces la derivada de la composición de funciones es:",
    "$$\\frac{dy}{dx} = f'(g(x)) \\cdot g'(x)$$",
    "",
    "### 1.2 Métodos Fundamentales de Integración",
    "1. **Integración por Sustitución (Cambio de Variable):** Basado en la regla de la cadena. Si $u = g(x)$, entonces $du = g'(x) dx$:",
    "   $$\\int f(g(x)) g'(x) dx = \\int f(u) du$$",
    "2. **Integración por Partes:** Basado en la regla del producto. Sean $u$ y $v$ funciones de $x$:",
    "   $$\\int u \\, dv = u v - \\int v \\, du$$",
    "3. **Fracciones Parciales:** Técnica para descomponer funciones racionales complejas (cociente de polinomios) en sumas de términos más simples de integrar (usada en la transformada inversa de Laplace en la Lección 2).",
    "",
    "### 1.3 Teorema Fundamental del Cálculo",
    "Si $f$ es continua en $[a, b]$ y $F$ es una antiderivada de $f$ ($F'(x) = f(x)$):",
    "$$\\int_a^b f(x) dx = F(b) - F(a)$$"
])

# --- CELL 4: CODE - SYMPY SYMBOLIC ---
add_code([
    "import sympy as sp",
    "",
    "print(\"=== REPASO SIMBÓLICO CON SYMPY ===\")",
    "# Definir la variable simbólica x",
    "x = sp.Symbol('x')",
    "",
    "# 1. Derivada de una función compuesta usando la regla de la cadena",
    "# f(x) = sin(x^2)",
    "f = sp.sin(x**2)",
    "df_dx = sp.diff(f, x)",
    "print(f\"Derivada de sin(x^2): \\n  df/dx = {df_dx}\\n\")",
    "",
    "# 2. Integración por partes de g(x) = x * exp(x)",
    "g = x * sp.exp(x)",
    "int_g = sp.integrate(g, x)",
    "print(f\"Integral indefinida de x * e^x (por partes): \\n  integral = {int_g}\\n\")",
    "",
    "# 3. Integral definida de h(x) = 1 / (x^2 + 1) en el intervalo [0, 1]",
    "h = 1 / (x**2 + 1)",
    "int_h_def = sp.integrate(h, (x, 0, 1))",
    "print(f\"Integral definida de 1/(x^2 + 1) de 0 a 1: \\n  resultado = {int_h_def}  (o sea, pi/4)\")"
])

# --- CELL 5: VECTOR & MATRIX ALGEBRA ---
add_markdown([
    "## 2. Álgebra Vectorial y Matricial",
    "",
    "El cálculo multivariable utiliza vectores para describir posiciones, velocidades, aceleraciones y fuerzas en el espacio tridimensional $\\mathbb{R}^3$.",
    "",
    "### 2.1 Vectores, Norma y Productos",
    "Sea $\\mathbf{u} = \\langle u_1, u_2, u_3 \\rangle$ y $\\mathbf{v} = \\langle v_1, v_2, v_3 \\rangle$ dos vectores en $\\mathbb{R}^3$:",
    "- **Norma (Magnitud o longitud):**",
    "  $$\\|\\mathbf{u}\\| = \\sqrt{u_1^2 + u_2^2 + u_3^2}$$",
    "- **Producto Punto (Escalar):** Devuelve un número real. Mide la proyección y ortogonalidad:",
    "  $$\\mathbf{u} \\cdot \\mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$$",
    "  Si $\\mathbf{u} \\cdot \\mathbf{v} = 0$, los vectores son **ortogonales** (perpendiculares).",
    "- **Producto Cruz (Vectorial):** Devuelve un vector perpendicular a ambos vectores. Su magnitud es el área del paralelogramo formado por ellos:",
    "  $$\\mathbf{u} \\times \\mathbf{v} = \\det \\begin{pmatrix} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ u_1 & u_2 & u_3 \\\\ v_1 & v_2 & v_3 \\end{pmatrix} = \\langle u_2 v_3 - u_3 v_2, \\, u_3 v_1 - u_1 v_3, \\, u_1 v_2 - u_2 v_1 \\rangle$$",
    "",
    "### 2.2 Matrices y Determinantes",
    "Una matriz es un arreglo bidimensional de números. Para el cálculo multivariable, los determinantes de las matrices de derivadas (Jacobianos) e segundas derivadas (Hessianos) son esenciales para cambios de coordenadas y análisis de estabilidad.",
    "- **Determinante de segundo orden (2x2):**",
    "  $$\\det \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix} = ad - bc$$"
])

# --- CELL 6: CODE - NUMPY VECTORS & MATRICES ---
add_code([
    "import numpy as np",
    "",
    "print(\"=== CÁLCULOS VECTORIALES CON NUMPY ===\")",
    "# Definir vectores u y v en R^3",
    "u = np.array([3.0, -1.0, 2.0])",
    "v = np.array([1.0, 4.0, -2.0])",
    "",
    "# 1. Calcular normas",
    "norm_u = np.linalg.norm(u)",
    "print(f\"Norma de u: {norm_u:.4f}\")",
    "",
    "# 2. Producto Punto",
    "dot_product = np.dot(u, v)",
    "print(f\"Producto Punto u . v: {dot_product:.4f}\")",
    "",
    "# 3. Producto Cruz",
    "cross_product = np.cross(u, v)",
    "print(f\"Producto Cruz u x v: {cross_product}\\n\")",
    "",
    "print(\"=== MATRICES Y DETERMINANTES ===\")",
    "# Definir una matriz de transformación A 2x2",
    "A = np.array([[2.0, 3.0],",
    "              [1.0, 5.0]])",
    "",
    "# Calcular determinante de A",
    "det_A = np.linalg.det(A)",
    "print(f\"Matriz A: \\n{A}\")",
    "print(f\"Determinante de A: {det_A:.4f}  (Esperado: 2*5 - 3*1 = 7)\")"
])

# --- CELL 7: MESHGRID AND PLOTTING ---
add_markdown([
    "## 3. Herramientas Computacionales de Visualización (NumPy & Matplotlib)",
    "",
    "En Cálculo II, trabajaremos frecuentemente con funciones de dos variables $z = f(x, y)$ que representan superficies tridimensionales en el espacio.",
    "",
    "### 3.1 Discretización Espacial con `np.meshgrid`",
    "Para evaluar computacionalmente una función $f(x, y)$ sobre una región rectangular $[a, b] \\times [c, d]$, no basta con crear listas simples de $x$ e $y$. Debemos generar una **rejilla bidimensional** que combine cada coordenada $x$ con cada coordenada $y$.",
    "La función `np.meshgrid` toma dos vectores unidimensionales y devuelve dos matrices bidimensionales $X$ e $Y$ que contienen las coordenadas de todos los nodos de la rejilla. Esto permite evaluar $Z = f(X, Y)$ de forma vectorizada.",
    "",
    "### 3.2 Visualización 3D",
    "Utilizando el módulo `Axes3D` de `Matplotlib`, podemos graficar:",
    "- **Curvas en el espacio (Paramétricas):** Trayectorias unidimensionales descritas por $\\mathbf{r}(t) = \\langle x(t), y(t), z(t) \\rangle$. Se dibujan con `ax.plot()`.",
    "- **Superficies:** Pliegues bidimensionales descritos por $z = f(x, y)$. Se dibujan con `ax.plot_surface()`."
])

# --- CELL 8: CODE - MESHGRID AND 3D PLOTS ---
add_code([
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "from mpl_toolkits.mplot3d import Axes3D",
    "",
    "# 1. Crear una rejilla espacial bidimensional",
    "x_vals = np.linspace(-2.0, 2.0, 50)",
    "y_vals = np.linspace(-2.0, 2.0, 50)",
    "X, Y = np.meshgrid(x_vals, y_vals)",
    "",
    "# Definir una superficie: paraboloide hiperbólico (silla de montar)",
    "# f(x, y) = x^2 - y^2",
    "Z = X**2 - Y**2",
    "",
    "# 2. Graficación de la superficie en 3D",
    "fig = plt.figure(figsize=(14, 6))",
    "",
    "ax1 = fig.add_subplot(1, 2, 1, projection='3d')",
    "surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', alpha=0.9)",
    "fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)",
    "ax1.set_title('Superficie 3D: Silla de Montar ($z = x^2 - y^2$)', fontweight='bold')",
    "ax1.set_xlabel('$x$')",
    "ax1.set_ylabel('$y$')",
    "ax1.set_zlabel('$z$')",
    "ax1.grid(True, ls='--', alpha=0.5)",
    "",
    "# 3. Graficar una curva paramétrica (Hélice tridimensional)",
    "# r(t) = <cos(t), sin(t), t>",
    "t_vals = np.linspace(0, 4 * np.pi, 200)",
    "x_curve = np.cos(t_vals)",
    "y_curve = np.sin(t_vals)",
    "z_curve = t_vals",
    "",
    "ax2 = fig.add_subplot(1, 2, 2, projection='3d')",
    "ax2.plot(x_curve, y_curve, z_curve, 'b-', linewidth=3, label='Hélice tridimensional')",
    "ax2.set_title('Curva Paramétrica 3D: Hélice', fontweight='bold')",
    "ax2.set_xlabel('$x$')",
    "ax2.set_ylabel('$y$')",
    "ax2.set_zlabel('$z$')",
    "ax2.legend(frameon=True)",
    "ax2.grid(True, ls='--', alpha=0.5)",
    "",
    "plt.tight_layout()",
    "plt.show()"
])

# --- CELL 9: DIAGNOSTIC CHALLENGE ---
add_markdown([
    "## 4. Reto de Diagnóstico y Autoevaluación",
    "",
    "Para comprobar que estás listo para iniciar el Módulo 5, resuelve el siguiente reto práctico:",
    "",
    "### El Desafío:",
    "Considera la función de dos variables $f(x, y) = x^2 y + 2 x y^3$.",
    "1. Calcula analíticamente las derivadas parciales de primer orden respecto a $x$ y respecto a $y$:",
    "   $$\\frac{\\partial f}{\\partial x} = \\frac{\\partial}{\\partial x}[x^2 y + 2 x y^3], \\quad \\frac{\\partial f}{\\partial y} = \\frac{\\partial}{\\partial y}[x^2 y + 2 x y^3]$$",
    "   *(Recuerda: al derivar respecto a $x$, trata a $y$ como una constante, y viceversa).*",
    "2. Escribe un script en Python usando `SymPy` para verificar simbólicamente tus resultados.",
    "3. Grafica la superficie $f(x, y)$ en el rango $[-2, 2] \\times [-2, 2]$ usando `meshgrid` y `plot_surface`."
])

# --- CELL 10: CODE - CHALLENGE SOLUTION ---
add_code([
    "import sympy as sp",
    "import numpy as np",
    "import matplotlib.pyplot as plt",
    "from mpl_toolkits.mplot3d import Axes3D",
    "",
    "# 1. Cálculo simbólico de derivadas parciales con SymPy",
    "x_sym, y_sym = sp.symbols('x y')",
    "f_sym = x_sym**2 * y_sym + 2 * x_sym * y_sym**3",
    "",
    "df_dx_sym = sp.diff(f_sym, x_sym)",
    "df_dy_sym = sp.diff(f_sym, y_sym)",
    "",
    "print(\"=== SOLUCIÓN DEL RETO SÍMBOLO ===\")",
    "print(f\"Función f(x, y): {f_sym}\")",
    "print(f\"Derivada parcial df/dx: {df_dx_sym}  (Esperado: 2*x*y + 2*y^3)\")",
    "print(f\"Derivada parcial df/dy: {df_dy_sym}  (Esperado: x^2 + 6*x*y^2)\\n\")",
    "",
    "# 2. Graficar la superficie resultante",
    "x_grid = np.linspace(-2.0, 2.0, 50)",
    "y_grid = np.linspace(-2.0, 2.0, 50)",
    "X_g, Y_g = np.meshgrid(x_grid, y_grid)",
    "Z_g = X_g**2 * Y_g + 2 * X_g * Y_g**3",
    "",
    "fig = plt.figure(figsize=(8, 6))",
    "ax = fig.add_subplot(1, 1, 1, projection='3d')",
    "surf = ax.plot_surface(X_g, Y_g, Z_g, cmap='viridis', edgecolor='none', alpha=0.9)",
    "fig.colorbar(surf, shrink=0.5, aspect=10)",
    "ax.set_title('Superficie del Reto: $f(x,y) = x^2 y + 2 x y^3$', fontweight='bold')",
    "ax.set_xlabel('$x$')",
    "ax.set_ylabel('$y$')",
    "ax.set_zlabel('$f(x,y)$')",
    "ax.grid(True, ls='--', alpha=0.5)",
    "plt.show()"
])

# --- CELL 11: REFERENCES ---
add_markdown([
    "## 5. Referencias y Próximos Pasos",
    "",
    "¡Felicidades! Si has ejecutado con éxito las celdas anteriores y comprendes el comportamiento de las derivadas, los vectores y los determinantes, estás completamente preparado para adentrarte en el Módulo 5.",
    "",
    "A lo largo del curso, consultaremos y contrastaremos de forma crítica los conceptos con los siguientes textos clásicos:",
    "",
    "### Bibliografía de Referencia",
    "[1] J. Stewart, *Calculus: Early Transcendentals*, 7a ed., Cengage Learning, 2012.",
    "[2] H. Anton, I. Bivens, y S. Davis, *Calculus*, 10a ed., Wiley, 2012.",
    "[3] E. Kreyszig, *Advanced Engineering Mathematics*, 10a ed., Wiley, 2011.",
    "[4] G. B. Arfken, *Mathematical Methods for Physicists*, 6a ed., Academic Press, 2005."
])

# Guardar a archivo
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2, ensure_ascii=False)

print(f"Cuaderno de Introducción generado con éxito en: {output_path}")
