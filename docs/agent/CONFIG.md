# Configuración del Entorno y Dependencias (CONFIG.md)

Este documento detalla las dependencias de software, el runtime y las configuraciones de entorno obligatorias para ejecutar las simulaciones de este repositorio.

---

## 1. Runtime y Entorno de Ejecución

* **Entorno Principal:** Jupyter Notebooks (`.ipynb`).
* **Runtime:** Python 3.x (compatible con versiones estables de Google Colab y distribuciones estándar de Anaconda).
* **Portabilidad:** Los cuadernos deben estar diseñados para ser portables por defecto. No se deben utilizar rutas absolutas locales del disco del agente ni configuraciones específicas de sistema operativo en las celdas activas.

---

## 2. Dependencias Científicas Requeridas

Los cuadernos dependen exclusivamente de la suite científica estándar de Python. No se permite agregar dependencias de terceros no estándar o comerciales (ej. bases de datos tradicionales, frameworks web, ORMs).

Las librerías obligatorias y sus alias de importación convencionales son:

| Librería | Propósito | Alias Convencional |
| :--- | :--- | :--- |
| **NumPy** | Cálculo numérico de alto rendimiento y álgebra lineal vectorizada | `import numpy as np` |
| **SymPy** | Cálculo simbólico, derivadas exactas y lógica proposicional | `import sympy as sp` |
| **SciPy** | Funciones de optimización y cuadratura de integración numérica | `import scipy` (o subcomponentes específicos) |
| **Matplotlib** | Graficación 2D/3D y visualizaciones estáticas/animadas | `import matplotlib.pyplot as plt` |
| **NetworkX** | Modelado y análisis de grafos y árboles discretos | `import networkx as nx` |

---

## 3. Directrices de Instalación y Seguridad

* **Instalación Limpia:** Para evitar ensuciar los entornos locales, el agente no debe incluir comandos interactivos de instalación (`!pip install <libreria>`) dentro de las celdas activas del cuaderno. Si se requiere una dependencia específica no estándar, debe documentarse en Markdown al inicio de la lección.
* **Cero Configuración:** El código de simulación debe ejecutarse directamente tras importar las librerías científicas indicadas en la primera celda, sin requerir compilación previa de binarios o configuración de servidores backend.
