# Guía de Agentes de Inteligencia Artificial (AGENTS.md)

Este documento sirve como el punto de partida principal para cualquier agente de IA que trabaje en el repositorio `Foundations-of-Physics`. Su objetivo es proporcionar un contexto completo del proyecto, detallar las convenciones técnicas existentes, delinear la arquitectura del código y establecer directrices estrictas para el desarrollo incremental futuro.

---

## 1. Descripción General del Proyecto

`Foundations-of-Physics` es un repositorio académico diseñado para documentar de forma rigurosa y formal estudios universitarios en Física y Matemáticas. El contenido está redactado en español y sigue un formato de estilo artículo científico. 

El repositorio no contiene aplicaciones web ni servicios backend tradicionales. Su estructura está compuesta por **módulos educativos**, donde cada módulo aborda una rama específica del conocimiento y se implementa a través de **cuadernos de Jupyter (Jupyter Notebooks)**. Estos cuadernos combinan:
1. **Teoría Rigurosa:** Explicada en celdas de Markdown y formateada matemáticamente con LaTeX.
2. **Modelado Computacional:** Código en Python interactivo que simula, resuelve y visualiza los problemas estudiados.

---

## 2. Stack Tecnológico Detectado

El entorno de ejecución del proyecto es exclusivamente Python orientado a la ciencia y visualización de datos.

* **Lenguaje:** Python (3.x)
* **Entorno de Ejecución:** Jupyter Notebooks (`.ipynb`), diseñados para ser totalmente compatibles con Google Colab y entornos locales de Jupyter.
* **Bibliotecas Clave:**
  - **NumPy:** Para cálculo numérico de alto rendimiento, operaciones de álgebra lineal vectorizadas, y manejo de arreglos multi-dimensionales.
  - **SymPy:** Para álgebra simbólica, resolución de ecuaciones lógicas, tablas de verdad y derivación/integración exacta.
  - **Matplotlib:** Para la generación de gráficos 2D y 3D, diagramas de Venn, curvas de nivel y subplots interactivos.
  - **SciPy:** Para optimización matemática (p. ej., programación lineal con `scipy.optimize.linprog`), cuadratura de integración numérica (`scipy.integrate`), y funciones especiales (`scipy.special`).
  - **NetworkX:** Para el modelado, análisis y graficación de grafos, redes y árboles discretos.

---

## 3. Arquitectura Detectada

El proyecto sigue una arquitectura de **documentación y modelado por lecciones jerárquicas**. No hay capas de base de datos ni servidores API; en su lugar, el flujo de datos se define a nivel de ejecución secuencial en cada cuaderno.

### Estructura de Directorios

```
Foundations-of-Physics/
│
├── .gitignore                          # Exclusiones de Git (Jupyter checkpoints, venv, etc.)
├── README.md                           # Índice general del repositorio y presentación académica
├── AGENTS.md                           # Guía para agentes de IA (este archivo)
├── ARCHITECTURE.md                     # Descripción de la arquitectura teórica y técnica
├── MODULE_TEMPLATE.md                  # Plantilla para nuevos módulos
├── DEVELOPMENT_RULES.md                # Reglas estrictas de desarrollo y nombrado
├── PROJECT_CONTEXT.md                  # Contexto, objetivos y estado actual
│
├── 01-algebra-lineal/                  # Módulo 1: Álgebra Lineal Computacional
│   ├── README.md                       # Índice y conceptos del Módulo 1
│   ├── introduccion/
│   │   └── bases-y-fundamentos.ipynb
│   ├── leccion-1/
│   │   └── metodos-de-prueba-induccion-y-recursion.ipynb
│   │   ...
│   └── leccion-11/
│       └── conclusion-y-unificacion.ipynb
│
└── 02-calculo-1/                       # Módulo 2: Cálculo I
    ├── README.md                       # Índice y conceptos del Módulo 2
    ├── introduccion/
    │   └── conceptos-esenciales.ipynb
    ├── leccion-1/
    │   └── introduccion-al-analisis-real-funciones-y-limites.ipynb
    │   ...
    └── leccion-11/
        └── consolidado-y-conclusion-del-modulo-2.ipynb
```

---

## 4. Reglas Obligatorias del Proyecto

1. **Mantener la Estructura de Lecciones:** Cada módulo debe contener exactamente una lección de nivelación/introducción (`introduccion`) y 11 lecciones temáticas (`leccion-1` a `leccion-11`), totalizando 12 cuadernos.
2. **Independencia de Cuadernos:** Cada cuaderno de Jupyter debe ser autocontenido. Debe importar sus propias bibliotecas necesarias en las primeras celdas de código de cada lección y no depender del estado de ejecución de otros cuadernos.
3. **Estilo Científico y Formal:** Las explicaciones matemáticas deben ser detalladas y usar LaTeX/MathJax para todas las ecuaciones, símbolos y fórmulas.
4. **Comentarios de Código:** El código en Python dentro de las celdas debe estar comentado en español, explicando la intención física o matemática de la operación.
5. **Configuración de Gráficos:** Matplotlib debe configurarse consistentemente para un diseño visual limpio (ej. usando `'seaborn-v0_8-whitegrid'` o el estilo por defecto con rejillas visibles) y con títulos y etiquetas de ejes claros en español.

---

## 5. Patrones Comunes en Lecciones

* **Sección de Objetivos:** Cada cuaderno comienza con una celda Markdown que especifica los "Objetivos de Aprendizaje" de la lección de manera numerada.
* **Flujo Conceptual-Computacional:** Un concepto teórico se presenta formalmente, seguido de inmediato por una celda de código interactiva que simula o calcula dicho concepto para verificar la teoría empíricamente.
* **Uso de Subplots:** Para comparar fenómenos (por ejemplo, discretos frente a continuos, o diferentes polinomios de Taylor), se utiliza `plt.subplots` ordenados con leyendas y escalas correspondientes.
* **Celdas de Verificación:** Al final de algoritmos complejos (ej., Eliminación Gaussiana o Simplex), se incluye una validación de resultados usando la función analítica correspondiente de SymPy o SciPy.

---

## 6. Prohibiciones Estrictas (Cosas Prohibidas)

* **PROHIBIDO** crear archivos de script Python sueltos (`.py`) en las carpetas de las lecciones. Todo el código debe estar embebido en los cuadernos `.ipynb`.
* **PROHIBIDO** agregar bibliotecas de terceros no científicas (ej. frameworks web, bases de datos ORM) a menos que se especifique en los requerimientos del módulo.
* **PROHIBIDO** reescribir o refactorizar cuadernos existentes sin la aprobación explícita del usuario. Mantener la consistencia histórica del código es prioritario.
* **PROHIBIDO** inicializar nuevos módulos o lecciones basados únicamente en instrucciones del chat. **Los nuevos módulos solo se crearán si el usuario proporciona un PDF formal con los requerimientos académicos del módulo.**
* **PROHIBIDO** crear archivos `.gitkeep` o cualquier otro archivo placeholder temporal en las carpetas de las lecciones o módulos. Las carpetas deben albergar única y exclusivamente el archivo de cuaderno `.ipynb` correspondiente cuando sea desarrollado.

---

## 7. Flujo Correcto de Desarrollo para Nuevos Módulos

Cuando el usuario solicite la creación de un nuevo módulo, el agente de IA debe seguir este orden secuencial:

1. **Recepción del PDF:** Esperar a que el usuario entregue el PDF de requerimientos del módulo.
2. **Lectura y Comparación:** Leer el PDF y contrastar sus contenidos con `AGENTS.md`, `ARCHITECTURE.md`, `MODULE_TEMPLATE.md` y `DEVELOPMENT_RULES.md`.
3. **Planificación:** Diseñar el plan en `implementation_plan.md` y esperar la aprobación del usuario.
4. **Estructura del Módulo:** Crear la carpeta del módulo `xx-nombre-modulo` siguiendo el patrón exacto establecido en `MODULE_TEMPLATE.md`.
5. **Implementación de Cuadernos:** Desarrollar los 12 cuadernos (Introducción + 11 lecciones) secuencialmente, asegurando que se cumplan las convenciones de código y estilo matemático.
6. **Actualización de Índices:** Actualizar el archivo `README.md` del nuevo módulo y el `README.md` en la raíz del repositorio.
7. **Verificación:** Ejecutar secuencialmente todas las celdas de los cuadernos creados para comprobar que no existan errores en tiempo de ejecución.
