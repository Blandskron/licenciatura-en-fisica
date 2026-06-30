# Plantilla de Módulo (MODULE_TEMPLATE.md)

Este documento define la estructura y el formato obligatorio que debe seguir cualquier nuevo módulo que se añada al repositorio `Foundations-of-Physics`. Cualquier agente de IA debe basar sus nuevos desarrollos en este estándar formal.

---

## 1. Estructura de Directorios del Módulo

Cuando se crea un nuevo módulo, su estructura de carpetas debe ser la siguiente:

```
xx-nombre-modulo/                       # xx es el número de módulo correlativo (ej. 03, 04)
├── README.md                           # Índice y conceptos del módulo
├── introduccion/                       # Carpeta de nivelación
│   └── nombre-descriptivo.ipynb        # Cuaderno de nivelación
├── leccion-1/                          # Carpeta de la lección 1
│   └── nombre-descriptivo.ipynb        # Cuaderno de la lección 1
│   ...
└── leccion-11/                         # Carpeta de la lección 11 (Unificación)
    └── nombre-descriptivo.ipynb        # Cuaderno de conclusión y unificación
```

---

## 2. Archivos Requeridos y sus Responsabilidades

### A. Archivo `README.md` del Módulo
Este archivo debe actuar como el programa de estudios y mapa conceptual del módulo. Su estructura debe ser la siguiente:

```markdown
# Módulo XX: [Nombre del Módulo en Español]

[Un párrafo corto que resuma el alcance académico y los objetivos del módulo, mencionando que se compone de un cuaderno introductorio, 10 lecciones temáticas y un cuaderno final de unificación].

---

## Índice del Módulo

### [Introducción: [Nombre de la Introducción]](./introduccion/nombre-descriptivo.ipynb)
- **Conceptos**: [Lista de conceptos teóricos y matemáticos nivelados]
- **Código**: [Lista de bibliotecas y scripts desarrollados en el cuaderno]

### [Lección 1: [Nombre de la Lección]](./leccion-1/nombre-descriptivo.ipynb)
- **Conceptos**: [Conceptos teóricos y matemáticos detallados]
- **Código**: [Detalles de implementaciones y simulaciones en Python]

... [Repetir para Lección 2 a Lección 10] ...

### [Lección 11: Conclusión y Unificación](./leccion-11/nombre-descriptivo.ipynb)
- **Conceptos**: [Conceptos de síntesis y unificación del módulo]
- **Código**: [Explicación del proyecto integrador final y cómo conecta las lecciones]
```

### B. Cuadernos de Jupyter (`.ipynb`)
Cada una de las 12 carpetas debe contener **exactamente un** archivo `.ipynb` con un nombre representativo en kebab-case en minúsculas (ej. `metodos-de-prueba-induccion-y-recursion.ipynb`).

---

## 3. Estructura Interna del Cuaderno (`.ipynb`)

Para mantener la consistencia estética y didáctica con los cuadernos ya desarrollados, cada nuevo notebook debe estructurarse secuencialmente de la siguiente manera:

### 1. Cabecera del Notebook (Markdown)
```markdown
# Lección Y: [Nombre de la Lección]
### [Nombre del Módulo o Subárea de Estudio]

---

[Párrafo de introducción formal en español que describa el contenido de la lección y su importancia académica/física].

---
```

### 2. Objetivos de Aprendizaje (Markdown)
```markdown
## Objetivos de Aprendizaje

Al finalizar esta lección, serás capaz de:
1. **[Verbo en infinitivo y negrita]** [Descripción del objetivo].
2. **[Verbo en infinitivo y negrita]** [Descripción del objetivo].
...
```

### 3. Desarrollo Temático (Markdown + Código alternados)
El contenido debe dividirse en secciones lógicas numeradas (p. ej., `1. Primer Tema`, `2. Segundo Tema`). Dentro de cada sección, se debe seguir la siguiente alternancia de celdas:

* **Celda Markdown (Teoría):**
  - Explicación teórica rigurosa de los conceptos.
  - Fórmulas matemáticas escritas en LaTeX, utilizando bloques de visualización `$$...$$` para fórmulas importantes e inline `$...$` para variables o términos en el texto.
  - Citas bibliográficas si corresponden (p. ej., "Siguiendo a Autor et al...").

* **Celda de Código (Simulación/Cálculo):**
  - Importación local de dependencias requeridas para la celda si es la primera.
  - Código legible, con variables con nombres significativos y comentarios en español explicativos.
  - Graficación de los resultados obtenidos con leyendas, rejillas y etiquetas.

* **Celda de Código (Validación):**
  - Validación del algoritmo o cálculo contra una biblioteca estándar (SymPy, SciPy).
  - Impresión formal de los resultados comparados.

---

## 4. Estilos de Graficación de Matplotlib

Para asegurar que todos los gráficos compartan una estética premium, se debe utilizar el siguiente patrón de configuración en las celdas de graficación:

```python
import numpy as np
import matplotlib.pyplot as plt

# Usar el estilo seaborn-whitegrid si está disponible, o default con rejilla explícita
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujo de las curvas o elementos
ax.plot(x, y, label='Modelo Teórico', color='royalblue', linewidth=2)

# Configuración formal de etiquetas y títulos
ax.set_title('Título Claro de la Simulación en Español', fontsize=13, fontweight='bold')
ax.set_xlabel('Etiqueta del Eje X (Unidades)', fontsize=11)
ax.set_ylabel('Etiqueta del Eje Y (Unidades)', fontsize=11)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(frameon=True)

plt.tight_layout()
plt.show()
```
