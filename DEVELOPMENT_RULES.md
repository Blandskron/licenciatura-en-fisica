# Reglas de Desarrollo (DEVELOPMENT_RULES.md)

Este documento establece las reglas y estándares obligatorios para la nomenclatura, codificación, seguridad, testing y control de versiones que deben cumplir todos los agentes de IA y colaboradores en el repositorio `Foundations-of-Physics`.

---

## 1. Reglas de Nomenclatura (Naming Rules)

### A. Directorios y Carpetas
* **Carpetas de Módulos:** Deben nombrarse en formato `xx-nombre-modulo` en minúsculas y con guiones donde:
  - `xx` es el número correlativo de dos dígitos relleno con ceros a la izquierda (ej. `03`, `04`, `10`).
  - `nombre-modulo` utiliza minúsculas y guiones (kebab-case), sin espacios ni caracteres especiales o tildes (ej. `03-fisica-mecanica`, `04-termodinamica`).
* **Carpetas de Lecciones:** Deben nombrarse secuencialmente en español usando minúsculas y guiones:
  - `introduccion` (sin tilde).
  - `leccion-1`, `leccion-2` ... `leccion-11` (con guión).

### B. Archivos de Cuaderno (`.ipynb`)
* Los cuadernos deben nombrarse utilizando **kebab-case** en minúsculas, describiendo de forma descriptiva el contenido principal de la lección basándose en su título oficial (ej. `derivacion-de-funciones-y-sus-aplicaciones.ipynb`, `calculo-de-raices-algoritmos-de-resolucion-y-aceleracion.ipynb`).
* Se debe evitar la inclusión de caracteres con tilde, la letra `ñ` o caracteres especiales en los nombres de archivos para evitar incompatibilidades de codificación entre distintos sistemas operativos (Linux, macOS, Windows).

### C. Variables, Funciones y Clases en Python
* Seguir las directrices de la guía de estilo **PEP 8**:
  - **Variables y Funciones:** En `snake_case` con letras minúsculas (ej. `x_discreto`, `calcular_simplex()`).
  - **Constantes:** En `UPPER_CASE` con mayúsculas y guiones bajos (ej. `TOLERANCIA_SCARBOROUGH`, `PI_APROX`).
  - **Clases:** En `PascalCase` (ej. `ClaseArbolBinario`, `NodoGrafico`).
  - **Variables Matemáticas:** Se permite el uso de variables de una sola letra en el código de simulación si se corresponden directamente con la notación física/matemática del texto (ej. `M` para costo, `P` para predicado, `A` para matrices).

---

## 2. Reglas de Arquitectura y Estructura

* **Autocontención:** Cada cuaderno de Jupyter debe poder ejecutarse de forma aislada. Todas las importaciones (`import numpy as np`, etc.) y definiciones de funciones deben declararse dentro del propio cuaderno. No debe haber importaciones cruzadas entre archivos `.ipynb`.
* **Progresión Didáctica:** Las celdas deben estar ordenadas lógicamente:
  - Celda 1: Título e Introducción.
  - Celda 2: Objetivos de Aprendizaje.
  - Celdas intermedias: Alternancia lógica de una celda teórica (Markdown) y una celda práctica (Código Python) para cada sección.
  - Celdas finales: Ejemplos de unificación o verificación y conclusiones.

---

## 3. Reglas de Seguridad

* **Sin Comandos del Sistema en Commit:** Está estrictamente prohibido guardar cuadernos que contengan comandos de terminal interactivos (p. ej. `!pip install numpy`, `!wget ...`, `!apt-get ...`) en celdas de código activas, a menos que sea una instrucción indispensable documentada en Markdown.
* **Seguridad de Datos:** No se deben solicitar ni escribir credenciales, claves de API, rutas absolutas personales o datos sensibles en las celdas de los cuadernos.
* **Código Seguro:** Evitar el uso de funciones propensas a inyecciones de código o inestabilidad como `eval()` o `exec()` al procesar expresiones matemáticas complejas. En su lugar, utilizar el motor analítico de `sympy.sympify()`.

---

## 4. Reglas de Modificación y Preservación de Código

* **Preservación de Estilo:** Mantener intactas las descripciones científicas, notas históricas, metodologías y referencias bibliográficas de los cuadernos existentes.
* **Edición No Destructiva:** Si se detecta un error o errata matemática en un cuaderno existente, el agente debe proponer la corrección de forma quirúrgica en una celda de reemplazo específica, justificando el cambio de acuerdo a la literatura estándar, sin alterar el resto de las celdas del cuaderno.

---

## 5. Reglas de Testing y Verificación

Antes de considerar que el trabajo en un cuaderno o módulo ha finalizado, se debe verificar lo siguiente:
1. **Ejecución Completa (Restart & Run All):** Reiniciar el kernel de Jupyter y ejecutar todas las celdas de principio a fin de manera secuencial. Ninguna celda debe arrojar errores o excepciones en tiempo de ejecución.
2. **Representación de Gráficos:** Confirmar que todos los gráficos generados por Matplotlib se renderizan de forma correcta y que no se superponen títulos, etiquetas o leyendas.
3. **Validación Numérica:** Comprobar que los resultados de las funciones artesanales coinciden con los resultados de las librerías científicas (`SciPy` / `SymPy`) bajo límites razonables de tolerancia por redondeo en coma flotante (ej. `np.allclose(resultado_artesanal, resultado_scipy, atol=1e-5)`).

---

## 6. Reglas de Control de Versiones (Commits)

* **Exclusión de Archivos Temporales y Placeholders:** Asegurarse de que carpetas del sistema como `.ipynb_checkpoints/`, entornos virtuales `.venv/` o cachés de compilación no sean rastreados por Git, respetando el archivo `.gitignore` raíz. **Queda estrictamente prohibido crear archivos `.gitkeep` o cualquier otro archivo placeholder temporal dentro de las carpetas del proyecto.**
* **Mensajes de Commit Claros:** Escribir los mensajes de commit en español, con un formato claro y descriptivo (ej. `feat: agregar modulo 03 de fisica clasica`, `fix: corregir formula de tolerancia en leccion 8 de calculo`).
