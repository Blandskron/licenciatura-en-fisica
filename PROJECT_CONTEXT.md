# Contexto del Proyecto (PROJECT_CONTEXT.md)

Este documento sirve como la memoria a largo plazo del repositorio `Foundations-of-Physics`. Registra los objetivos estratégicos, el estado actual del desarrollo, las decisiones de diseño clave, las limitaciones identificadas y la ruta para futuras expansiones académicas.

---

## 1. Objetivo del Sistema

El objetivo de `Foundations-of-Physics` es construir una biblioteca de referencia académica digital, rigurosa e interactiva, que abarque las bases matemáticas y físicas de nivel universitario. 

A diferencia de los libros de texto impresos tradicionales, este repositorio busca **unificar la teoría matemática/física con el modelado computacional**. De esta manera, el estudiante o investigador no solo lee las deducciones matemáticas de una ley física, sino que puede ejecutar simulaciones numéricas y comprobar empíricamente los resultados, analizando los límites físicos y computacionales de cada modelo.

---

## 2. Estado Actual del Proyecto

El repositorio cuenta actualmente con la base matemática y de análisis numérico completada en su totalidad, organizada en dos módulos iniciales:

### Módulo 1: Álgebra Lineal Computacional (`01-algebra-lineal`)
* **Estado:** Completado (100%).
* **Contenido:** 12 cuadernos (Introducción + 11 Lecciones).
* **Alcance:** Lógica proposicional, cuantificadores, teoría de conjuntos, aritmética modular, operaciones de matrices, relaciones binarias (clausura de Warshall), eliminación gaussiana (pivoteo escalado parcial), programación lineal (optimización primal-dual con SciPy), algoritmo Simplex paso a paso, teoría de grafos, árboles binarios de búsqueda y un proyecto unificado de telecomunicaciones.

### Módulo 2: Cálculo I (`02-calculo-1`)
* **Estado:** Completado (100%).
* **Contenido:** 12 cuadernos (Introducción + 11 Lecciones).
* **Alcance:** Análisis real, límites $\epsilon-\delta$, derivación, teoremas del valor medio, polinomios de Taylor, integral definida (sumas de Riemann, Barrow) e indefinida (métodos de sustitución e integrales no elementales), sucesiones y series infinitas, principios combinatorios (inclusión-exclusión, explosión combinatoria), análisis de errores en punto flotante, sistemas de numeración (conversión de bases, Von Neumann) y algoritmos de raíces no lineales (Newton-Raphson, Schröder, Steffensen y aceleración de Aitken).

---

## 3. Decisiones de Diseño Importantes

* **Foco en Google Colab:** Se decidió estructurar los cuadernos para que sean compatibles con Colab (cargando librerías científicas estándar de Python) de modo que cualquier estudiante universitario pueda interactuar con el código sin configurar complejos entornos locales.
* **Algoritmos Didácticos "A Mano":** Se prefiere implementar algoritmos complejos (ej., método Simplex, eliminación gaussiana, algoritmo de Warshall, bisección/secante) línea por línea en celdas de código en lugar de utilizar librerías de caja negra de inmediato. Esto asegura que el estudiante entienda el funcionamiento interno y los límites de precisión del algoritmo.
* **Uso Riguroso de LaTeX:** Todas las ecuaciones están descritas formalmente usando la sintaxis de MathJax/LaTeX para emular la calidad de un artículo científico o libro de física formal.
* **Corrección de Erratas:** Una directiva clave de este proyecto es identificar, documentar y corregir de manera interactiva las erratas comunes que aparecen en los libros de texto de referencia tradicionales de la literatura (ej., erratas de tableaus en Simplex, o intersección de funciones de optimización).

---

## 4. Limitaciones del Sistema

* **Restricción de Entorno Jupyter:** Al estar limitado exclusivamente a cuadernos de Jupyter, las interfaces gráficas avanzadas o flujos de usuario complejos no se pueden desarrollar fuera de los límites de `matplotlib`, `networkx` o elementos básicos HTML interactivos que soporte Colab.
* **Rendimiento de Células:** Debido a que el usuario debe poder realizar un "Restart and Run All", las simulaciones computacionales pesadas (ej. simulaciones de Monte Carlo con muestras masivas o análisis numéricos intensivos) no deben requerir tiempos de cómputo que superen unos pocos segundos por celda.
* **Sin Persistencia Externa:** Los cuadernos son efímeros; no hay bases de datos backend o almacenamiento persistente acoplado. Todo el estado se almacena en la memoria del kernel de ejecución de Python durante la sesión.

---

## 5. Próximos Pasos y Regla de Creación

1. **Próximos Módulos:** El plan académico contempla extender el repositorio hacia áreas puras de la Física (Física Mecánica, Electromagnetismo, Ondas y Óptica, Termodinámica y Mecánica Estadística) y Matemáticas Avanzadas (Cálculo Multivariable, Ecuaciones Diferenciales).
2. **Regla de Creación de Módulos (REGLA DE ORO):** Ningún agente de IA debe inventar el temario ni la estructura de los próximos módulos desde instrucciones genéricas de chat. **La creación de nuevos módulos queda suspendida y solo se reanudará cuando el usuario proporcione un documento PDF formal con los requerimientos específicos de la materia.**
