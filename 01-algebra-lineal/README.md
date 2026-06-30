# Módulo 1: Álgebra Lineal Computacional

Este módulo abarca el estudio formal del Álgebra Lineal y la Matemática Discreta aplicadas a la computación científica y a los modelos físicos. Se compone de un cuaderno introductorio de nivelación, 10 cuadernos de Jupyter Colab dedicados a temas específicos de la teoría con código ejecutable en Python, y un cuaderno final de unificación.

---

## Índice del Módulo

### [Introducción: Bases y Fundamentos](./introduccion/bases-y-fundamentos.ipynb)
- **Conceptos**: Ecuaciones de rectas ($y = mx + b$), plano cartesiano 2D/3D, distancia euclidiana y concepto físico de vectores.
- **Álgebra Booleana**: Conectivos lógicos básicos (`and`, `or`, `not`) y tablas de verdad.
- **Python**: Variables, listas, diccionarios, condicionales (`if`/`else`), bucles (`for`/`while`) y definición de funciones (`def`).
- **NumPy**: Arreglos en 1D/2D, operaciones vectorizadas y agregaciones.
- **Matplotlib**: Graficación de funciones continuas (seno/coseno) y vectores.

### [Lección 1: Métodos de Prueba, Inducción y Recursión](./leccion-1/metodos-de-prueba-induccion-y-recursion.ipynb)
- **Conceptos**: Lógica matemática, tablas de verdad, cuantificadores, inducción matemática y recursión.
- **Código**: Lógica proposicional con SymPy, tablas de verdad interactivas y simulación del Call Stack recursivo.

### [Lección 2: Conjuntos y Funciones](./leccion-2/conjuntos-y-funciones.ipynb)
- **Conceptos**: Teoría de conjuntos, cardinalidad, diagramas de Venn, funciones inyectivas/sobreyectivas/biyectivas y bijección infinita de Cantor.
- **Código**: Diagramas de Venn con Matplotlib, composición e inversión de funciones complejas y mapeos infinitos.

### [Lección 3: Teoría de Números y Aritmética Modular](./leccion-3/teoria-de-numeros-y-aritmetica-modular.ipynb)
- **Conceptos**: Algoritmo de división, primos, Euclides extendido, aritmética modular, Teorema Chino del Resto y criptografía Diffie-Hellman.
- **Código**: MCD, Bezout, CRT de cartas, Carmichael y simulación de intercambio de claves Diffie-Hellman.

### [Lección 4: Operaciones con Matrices](./leccion-4/operaciones-con-matrices.ipynb)
- **Conceptos**: Vectores en física, álgebra de matrices, multiplicación, inversas, determinantes por Sarrus y matrices booleanas.
- **Código**: Multiplicación de matrices ingenua vs vectorizada, cálculo de determinantes y matrices de adyacencia de dígrafos.

### [Lección 5: Relaciones Binarias, Propiedades y Clausuras](./leccion-5/relaciones-binarias-propiedades-y-clausuras.ipynb)
- **Conceptos**: Relaciones binarias, propiedades (reflexiva, simétrica, transitiva), clausuras y algoritmo de Warshall.
- **Código**: Analizador de relaciones, relaciones representadas mediante matrices booleanas, cierres transitivos y cálculo computacional de Warshall.

### [Lección 6: Eliminación Gaussiana](./leccion-6/eliminacion-gaussiana.ipynb)
- **Conceptos**: Clasificación de sistemas lineales, rango, eliminación gaussiana ingenua, errores de redondeo en aritmética de coma flotante y estrategias de pivotaje parcial y parcial escalado.
- **Código**: Trazado geométrico, eliminador gaussiano con pivoteo parcial escalado y simulación de errores en sistemas mal condicionados.

### [Lección 7: Programación Lineal](./leccion-7/programacion-lineal.ipynb)
- **Conceptos**: Construcción de modelos de optimización, región factible y vértices (puntos esquina), conversión a forma estándar/holgura, y teoría de dualidad (Teorema Fuerte de la Dualidad).
- **Código**: Graficación interactiva de regiones factibles acotadas y no acotadas, y optimización primal-dual automatizada con SciPy.

### [Lección 8: Algoritmo Simplex](./leccion-8/algoritmo-simplex.ipynb)
- **Conceptos**: Mecánica del Simplex, base factible, regla de entrada y regla de salida (prueba de la razón mínima), métodos de penalización (Gran M y Dos Fases).
- **Código**: Simulador Simplex paso a paso imprimiendo tableaus ordenados y limpios, corrección de erratas de tablas del texto original y visualización interactiva 3D del poliedro de las Cocinetas.

### [Lección 9: Grafos](./leccion-9/grafos.ipynb)
- **Conceptos**: Tipos de grafos, teoremas de grado (Handshaking Lemma), representaciones (lista de adyacencia, matriz de adyacencia e incidencia), isomorfismo de grafos y conectividad.
- **Código**: Multiplicación de matrices de adyacencia para hallar dominancia de segundo orden y liderazgo (Daniela), comprobación interactiva de isomorfismo del cubo 3D y recorridos BFS/DFS.

### [Lección 10: Árboles](./leccion-10/arboles.ipynb)
- **Conceptos**: Árboles generadores, árboles m-arios y completos, árboles binarios de búsqueda (ABB/BST) y operaciones de inserción/búsqueda/borrado, y recorridos (preorden, inorden, postorden).
- **Código**: Clase ABB interactiva con borrado robusto de nodos, y simulación de recorridos recursivos sobre árboles binarios complejos.

### [Lección 11: Conclusión y Unificación](./leccion-11/conclusion-y-unificacion.ipynb)
- **Conceptos**: Unificación de las 10 lecciones en un proyecto integrador: el diseño, seguridad y optimización de una red de telecomunicaciones.
- **Código**: Implementación del Algoritmo de Warshall, árbol generador BFS, protocolo Diffie-Hellman de encriptado, eliminación gaussiana de flujos estacionarios y optimización Simplex (Max-Flow).
