# Arquitectura del Sistema (ARCHITECTURE.md)

Este documento describe la arquitectura de software y la estructura conceptual del repositorio `Foundations-of-Physics`. Esta documentación está basada exclusivamente en los patrones y componentes existentes en los módulos `01-AlgebraLineal` y `02-Calculo1`.

---

## 1. Modelo Arquitectónico General

El repositorio no sigue una arquitectura de software tradicional de n-capas (como MVC o Microservicios) debido a su naturaleza académica e investigativa. En su lugar, implementa un patrón de **Capas de Abstracción Educativa** dentro de documentos interactivos ejecutables (Jupyter Notebooks).

El sistema se divide en las siguientes capas dentro de cada lección:

```
┌────────────────────────────────────────────────────────┐
│ 1. CAPA TEÓRICA Y FORMAL (Markdown / LaTeX)            │
│    - Definiciones rigurosas, teoremas, citas científicas. │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 2. CAPA ALGORÍTMICA (Código Python Puro / Numpy)       │
│    - Implementación directa del modelo matemático.     │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 3. CAPA DE MODELADO Y VISUALIZACIÓN (Matplotlib)       │
│    - Graficación interactiva, subplots, animaciones.    │
└──────────────────────────┬─────────────────────────────┘
                           ▼
┌────────────────────────────────────────────────────────┐
│ 4. CAPA DE VERIFICACIÓN (SymPy / SciPy)                │
│    - Validación simbólica y numérica de resultados.    │
└────────────────────────────────────────────────────────┘
```

---

## 2. Responsabilidades por Componente

### A. Estructura del Repositorio (Nivel Superior)
* **Raíz del Repositorio:** Define el índice general y la descripción unificada de las áreas académicas de la Licenciatura en Física.
* **Módulos (`XX-NombreModulo`):** Agrupan una disciplina específica (p. ej., Álgebra Lineal, Cálculo). Contienen un índice temático detallado y las subcarpetas de las lecciones.
* **Lecciones (`Introduccion` o `LeccionXX`):** Unidades didácticas independientes que corresponden a clases o temas concretos. Contienen un único archivo `.ipynb`.

### B. Estructura Interna del Cuaderno (Nivel de Lección)
Cada archivo `.ipynb` es responsable de:
1. **Establecer Objetivos:** Declarar las metas de aprendizaje de la lección al inicio.
2. **Definir el Dominio Físico/Matemático:** Explicar el modelo físico o matemático rigurosamente.
3. **Traducir Teoría a Código:** Implementar algoritmos (como el Algoritmo Simplex, el Algoritmo de Warshall, el método de Newton-Raphson, etc.) sin depender de cajas negras al principio.
4. **Graficar Resultados:** Utilizar visualizaciones comprensibles para ilustrar comportamientos (como errores de punto flotante, convergencia de series o regiones de optimización).
5. **Verificar Corrección:** Usar funciones estándar de bibliotecas consolidadas (`scipy.optimize.linprog`, `sympy.solve`) para contrastar con las implementaciones artesanales/didácticas.

---

## 3. Flujo de Datos Científicos

El flujo de datos dentro de cada cuaderno es lineal, secuencial y local:

1. **Definición de Parámetros de Entrada:** Se establecen variables en celdas superiores (como dominios numéricos discretos o continuos mediante `np.linspace` o `np.arange`).
2. **Transformación Algorítmica:** El flujo pasa por funciones de cálculo puro desarrolladas en el cuaderno (procesando matrices, evaluando polinomios o recorriendo grafos).
3. **Visualización Gráfica:** Los arreglos resultantes son mapeados a coordenadas cartesianas o polares y renderizados con Matplotlib.
4. **Validación:** Se comparan las salidas con funciones nativas y se imprimen análisis de errores (absolutos, relativos, porcentuales).

---

## 4. Comunicación e Interconexión entre Módulos

La interconexión de módulos en este repositorio no se realiza mediante APIs de red o dependencias de código, sino de forma **secuencial y acumulativa en el plan de estudios**:

* **Base de Álgebra Lineal:** Las lecciones de Cálculo I y Física Matemática asumen que el agente y el usuario dominan la lógica proposicional, la teoría de conjuntos y el álgebra de matrices definidos en el Módulo 1.
* **Unificación de Conceptos:** Las lecciones finales de cada módulo (Lección 11) actúan como integradores de todas las lecciones del módulo. Por ejemplo, en Álgebra Lineal, el proyecto final une grafos (Warshall), criptografía (Diffie-Hellman), sistemas de ecuaciones (Gauss) y optimización (Simplex).
* **Consolidación de Cálculo:** En Cálculo I, la lección final unifica el análisis numérico (Scarborough, Taylor), la computación de raíces y las funciones patológicas.

---

## 5. Decisiones Técnicas Clave Detectadas

* **Enfoque de Documento Único:** Cada lección está contenida en un único cuaderno para garantizar que la explicación teórica y la simulación interactiva no se divorcien en archivos separados.
* **Uso Intensivo de LaTeX/MathJax:** Se prioriza la visualización formal de la matemática sobre la notación puramente informática en las descripciones de texto.
* **Cero Configuración de Entorno:** El código no utiliza dependencias externas complejas o compiladas fuera de la suite científica estándar de Python, facilitando la ejecución directa en Google Colab con un solo clic.
* **Simulaciones Didácticas frente a Librerías:** Se programan métodos didácticos a mano (como la bisección de raíces, el simplex en tableaus o el Warshall de relaciones transitivas) para demostrar la comprensión de los algoritmos y la propagación de errores en coma flotante.
