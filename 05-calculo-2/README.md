# Módulo 5: Cálculo II

Este módulo abarca el estudio formal del Cálculo Integral Avanzado, Sucesiones y Series de Funciones, Ecuaciones Diferenciales Ordinarias, y el Cálculo Multivariable (diferencial e integral), esenciales para la formulación matemática de la física teórica y experimental. Cada lección combina un desarrollo matemático riguroso con modelado computacional y simulaciones interactivas en Python (Jupyter Colab).

---

## Índice del Módulo

### [Introducción al Módulo 5: Conceptos Esenciales y Prerrequisitos de Cálculo II](./introduccion/conceptos-esenciales.ipynb)
- **Conceptos**: Repaso de límites, derivadas (regla de la cadena), teoremas fundamentales del cálculo y técnicas clásicas de integración (por partes, sustitución) de una variable. Álgebra lineal básica para cálculo multivariable: vectores en 2D/3D (norma, producto punto y cruz), matrices, multiplicación de matrices y determinantes. Introducción al entorno de programación científica en Python con `SymPy` (cálculo simbólico), `NumPy` (cálculo numérico y mallas discretas/`meshgrid`) y `Matplotlib` (visualizaciones bidimensionales y tridimensionales de curvas y superficies).
- **Código**: Verificación simbólica de derivadas e integrales complejas con `SymPy`, cálculo de productos vectoriales y determinantes matriciales con `NumPy`, discretización y generación de mallas bidimensionales con `np.meshgrid`, graficación en 3D de una superficie en forma de silla de montar y una hélice paramétrica en 3D, y resolución interactiva de un reto de derivación parcial y visualización 3D.
- **Estado**: **Desarrollado**

### [Lección 1: La Integral de Riemann y sus Extensiones](./leccion-1/integral-de-riemann.ipynb)
- **Conceptos**: Definición formal de la integral de Riemann mediante sumas de Riemann con particiones y normas. Propiedades fundamentales de linealidad, aditividad, acotamiento y monotonía. Teoremas fundamentales (Teorema del Valor Medio y Teorema Fundamental del Cálculo/Regla de Barrow). Criterio de integrabilidad y relación con la continuidad. Métodos de aproximación numérica (Trapecio, Simpson) y análisis de convergencia. Aplicaciones geométricas (áreas, volúmenes de revolución, longitud de arco) y físicas (trabajo mecánico, potencial electrostático, densidad de probabilidad cuántica). Extensiones de la integral (Riemann-Stieltjes y Lebesgue).
- **Código**: Visualización interactiva de sumas de Riemann (izquierda, derecha y punto medio), verificación computacional de aditividad y valor absoluto, implementación didáctica y comparación de convergencia log-log de la regla del trapecio y de Simpson, visualización de aproximaciones poligonales de longitud de arco, corrección de erratas de integración del texto (potencial eléctrico y caja cuántica), y gráfico conceptual del contraste Riemann vs. Lebesgue.
- **Estado**: **Desarrollado**

### [Lección 2: Integrales Impropias, Función Gamma y Transformada de Laplace](./leccion-2/integrales-impropias-y-transformada-de-laplace.ipynb)
- **Conceptos**: Definición de función localmente integrable y concepto de integral impropia de primera y segunda especie. Criterios de convergencia (comparación directa y por límite con la integral de p). La función Gamma de Euler: definición, propiedades de recurrencia, relación de Legendre para duplicación y su vínculo con el factorial. Distribución Gamma y Beta con obtención analítica de sus medias. Valor principal de Cauchy (definición y cálculo en presencia de singularidades). Introducción a la Transformada de Laplace: propiedades de linealidad, derivación, traslación y convolución. Teoremas del valor inicial y final. Aplicación de Laplace para resolver EDOs lineales con oscilaciones en resonancia.
- **Código**: Visualización de la convergencia/divergencia de funciones potencia ($1/x^p$), graficación de la función Gamma $\Gamma(x)$ en el plano real, simulación numérica de la transformada de Laplace de funciones elementales, resolución simbólica de la EDO resonante con SymPy, y gráfico comparativo de la trayectoria de resonancia real frente a la errónea reportada en el texto.
- **Estado**: **Desarrollado**

### [Lección 3: Ecuaciones Diferenciales Ordinarias de Primer Orden](./leccion-3/ecuaciones-diferenciales-de-primer-orden.ipynb)
- **Conceptos**: Clasificación de EDOs. Ecuaciones de variables separables, homogéneas, lineales de primer orden y exactas (factor integrante). Ecuaciones de Bernoulli y Riccati.
- **Código**: Trazado de campos de direcciones, método de Euler y Runge-Kutta para aproximar soluciones de primer orden.
- **Estado**: **Desarrollado**

### [Lección 4: Introducción al Cálculo con Varias Variables](./leccion-4/introduccion-al-calculo-de-varias-variables.ipynb)
- **Conceptos**: Espacios en $\mathbb{R}^n$, producto escalar, distancias y sucesiones en $\mathbb{R}^n$, topología básica (conjuntos abiertos, bolas abiertas), campos escalares y vectoriales, límites multivariables y límites direccionales, continuidad, y geometría de curvas en $\mathbb{R}^2$ y $\mathbb{R}^3$ (longitud de arco, curvatura, torsión, plano osculador).
- **Código**: Visualización interactiva 3D de superficies y curvas en el espacio (hélice y curvas de intersección), graficación 3D de campos escalares y vectoriales (campo eléctrico y magnético), cálculo de límites direccionales y análisis geométrico de curvas (tangente, normal, binormal).
- **Estado**: **Desarrollado**

### [Lección 5: Derivación de Campos Escalares y Optimización](./leccion-5/derivacion-de-campos-escalares-y-optimizacion.ipynb)
- **Conceptos**: Derivadas direccionales y parciales. Diferencial total. Regla de la cadena multivariable. Derivadas de orden superior (Teorema de Clairaut). Fórmula de Taylor en dos y tres variables. Matriz Hessiana y clasificación de puntos críticos (máximos, mínimos y puntos de silla).
- **Código**: Visualización en 3D de derivadas parciales como pendientes de rectas tangentes, cálculo de cambios de presión por diferencial total en gases ideales, comprobación del Teorema de Clairaut con SymPy, aproximación por Taylor en 3D (exponencial real vs. paraboloide de aproximación) y clasificación interactiva de los 9 puntos críticos de la superficie $x^4-4x^2+y^4-4y^2$.
- **Estado**: **Desarrollado**

### [Lección 6: Derivación de Campos Vectoriales](./leccion-6/derivacion-de-campos-vectoriales.ipynb)
- **Conceptos**: Transformaciones y campos vectoriales en $\mathbb{R}^n$. Matriz Jacobiana (definición y cálculo paso a paso). Diferenciabilidad de campos vectoriales. Regla de la cadena vectorial. Teorema de la Función Inversa y de la Función Implícita para sistemas. Optimización con restricciones mediante Multiplicadores de Lagrange. Operadores diferenciales (gradiente, divergencia y rotacional). Álgebra tensorial elemental: delta de Kronecker $\delta_{ij}$, tensor de Levi-Civita $\epsilon_{ijk}$ e identidades vectoriales clásicas.
- **Código**: Transformación e interactividad en 3D de coordenadas cartesianas a esféricas y cilíndricas (cálculo de sus Jacobianas), verificación numérica del teorema de la función inversa y de la diferenciabilidad de transformaciones vectoriales, minimización condicionada por multiplicadores de Lagrange con visualización 3D, y validación simbólica de identidades rotacionales complejas con SymPy.
- **Estado**: **Desarrollado**

### [Lección 7: Integrales de Línea en Campos Escalares y Vectoriales](./leccion-7/integrales-de-linea.ipynb)
- **Conceptos**: Definición e importancia de las integrales de línea. Integrales de línea de campos escalares a lo largo de curvas en $\mathbb{R}^2$ y $\mathbb{R}^3$. Integrales de línea de campos vectoriales (circulación y flujo). Trabajo realizado por una fuerza. Integrales de línea independientes del camino y campos de fuerza conservativos (existencia de función potencial). Interpretación física de integrales dependientes (fuerzas de fricción no conservativas) e independientes del camino (potenciales gravitatorios y electrostáticos).
- **Código**: Graficación 3D interactiva de curvas paramétricas junto a campos escalares y vectoriales, implementaciones numéricas de aproximaciones de integrales de línea en trayectorias curvas, resolvedor simbólico de funciones potenciales en campos conservativos, y visualización del trabajo mecánico realizado a lo largo de caminos dependientes e independientes del camino en campos de fuerza gravitatorios y de fricción.
- **Estado**: **Desarrollado**

### [Lección 8: Integrales Múltiples y Teorema de Green](./leccion-8/integrales-multiples.ipynb)
- **Conceptos**: Definición e interpretación geométrica (volumen) de la integral doble. Integrales dobles sobre regiones rectangulares. Teorema de Fubini e integración simple reiterada. Integrales dobles sobre regiones generales (tipo I y tipo II). Cambio de variables en integrales dobles: coordenadas polares. El Teorema de Green: formulación matemática, relación entre integrales de línea sobre curvas cerradas e integrales dobles de rotacionales. Aplicaciones físicas (centro de masa, flujo, cálculo de áreas y momentos de inercia).
- **Código**: Cálculo numérico de integrales dobles iteradas mediante sumas de Riemann bidimensionales sobre rectángulos y regiones generales, graficación en 3D de volúmenes bajo superficies, simulación de cambios de variable a coordenadas polares con su respectivo Jacobiano de área ($r dr d\theta$), y validación computacional del Teorema de Green comparando la integral de línea en sentido antihorario contra la integral doble del rotacional en regiones poligonales y elípticas.
- **Estado**: **Desarrollado**

### [Lección 9: Integrales de Superficie, Volumen y Teoremas de Stokes y Gauss](./leccion-9/integrales-superficie-volumen.ipynb)
- **Conceptos**: Parametrización y descripción geométrica de superficies en $\mathbb{R}^3$ (implícitas y explícitas). Área de una superficie parametrizada (fórmula del producto cruz de derivadas parciales). Integración sobre superficies de campos escalares y de campos vectoriales (flujo a través de superficies abiertas y cerradas). El Teorema de Stokes como generalización tridimensional del Teorema de Green. El Teorema de Gauss (Teorema de la Divergencia): flujo saliente e integral de volumen de la divergencia. Aplicaciones físicas en electrostática, hidrodinámica y termodinámica.
- **Código**: Visualización 3D interactiva de superficies parametrizadas complejas (esferas, paraboloides y sólidos deformados), cálculo computacional del área de superficies complejas, aproximación numérica del flujo de campos vectoriales, y validación simbólica y numérica de los teoremas de Stokes y Gauss (calculando y comparando las integrales de contorno/volumen frente a las integrales de superficie asociadas).
- **Estado**: **Desarrollado**

### [Lección 10: Transformaciones de Coordenadas](./leccion-10/transformaciones-coordenadas.ipynb)
- **Conceptos**: Rotaciones en el plano (2D) y su representación matricial. Generadores del grupo de rotaciones SO(2) mediante la matriz generadora infinitesimal y exponenciación de matrices. Rotaciones en 3D: matrices de rotación alrededor de los ejes principales, águlos de Euler, y la fórmula de rotación de Rodrigues para rotaciones sobre ejes arbitrarios. Álgebra multilineal: definición de tensores de rango 2 (tensor de tensiones, tensor de inercia, tensor electromagnético en relatividad especial). Elementos curvilíneos diferenciales en coordenadas cilíndricas y esféricas (elemento de línea $ds$, factor de escala, Jacobiano de volumen).
- **Código**: Simulación de rotaciones de figuras poligonales en 2D (triángulos y cuadrados), visualización animada del comportamiento exponencial en la serie de Taylor de matrices de rotación SO(2), cálculo interactivo en 3D de rotaciones sobre ejes arbitrarios con la fórmula de Rodrigues, visualización en mapas de calor de tensores de rango 2 (distribución de tensiones y tensor de inercia), y cálculo de Jacobianas y conversión simbólica a coordenadas cilíndricas y esféricas con `SymPy`.
- **Estado**: **Desarrollado**

### [Lección 11: Conclusión y Unificación del Módulo 5](./leccion-11/conclusion-y-unificacion-calculo-2.ipynb)
- **Conceptos**: Síntesis integradora de cálculo diferencial avanzado, ecuaciones diferenciales ordinarias y cálculo multivariable. Proyecto unificador aplicado a la física teórica: modelado de la vibración de una membrana elástica 2D (parche de tambor rectangular) mediante la ecuación de onda bidimensional. Solución analítica mediante separación de variables y cálculo de coeficientes de Fourier por integrales dobles de proyección. Formulación energética del sistema: cálculo de energía cinética y potencial elástica por sumas de Riemann bidimensionales. Condición de estabilidad Courant-Friedrichs-Lewy (CFL) en 2D.
- **Código**: Cálculo simbólico de los coeficientes de Fourier de la vibración con `SymPy`, resolvedor didáctico por diferencias finitas (FDTD) de la ecuación de onda en 2D, graficación 3D en subplots del desplazamiento de la membrana en instantes clave, análisis y gráfico de la conservación de la energía mecánica total (Hamiltoniano) en el tiempo, y test de inestabilidad exponencial al violar la condición CFL bidimensional (demostrando la errata típica de aplicar la condición 1D).
- **Estado**: **Desarrollado**
