# Estrategia de Pruebas y Verificación para Agentes (TESTS.md)

Este documento describe la suite de validaciones obligatorias que el agente debe ejecutar sobre cualquier cuaderno de Jupyter nuevo o modificado antes de finalizar una tarea.

---

## 1. Validación Estructural y Formato JSON

Antes de dar por concluida la creación o edición de un cuaderno, el agente debe verificar que el archivo `.ipynb` posea un formato JSON válido y no contenga errores de codificación ni caracteres de escape rotos (un problema frecuente al redactar ecuaciones en LaTeX).

El agente debe correr el siguiente comando de verificación desde la terminal (Powershell):
```powershell
python -c "import json; json.load(open(r'c:\Users\BlandskronNotebook\Documents\blandskron\licenciatura-en-fisica\<ruta-al-cuaderno>.ipynb', encoding='utf-8'))"
```
* **Resultado Esperado:** Ejecución exitosa con código de salida `0` y sin mensajes de error.

---

## 2. Validación en Tiempo de Ejecución (Restart & Run All)

Cada cuaderno debe ser totalmente autocontenido y poder ejecutarse de forma aislada de principio a fin sin dependencias de estado externas.

* **Requisito:** Todas las importaciones de bibliotecas (ej. `import numpy as np`, `import matplotlib.pyplot as plt`) y la inicialización de variables de entrada deben ocurrir en las primeras celdas del cuaderno.
* **Prueba:** Se debe poder reiniciar el Kernel y correr todas las celdas secuencialmente de inicio a fin. Ninguna celda de código activa debe arrojar excepciones o errores.

---

## 3. Validación de Modelado Físico y Matemático

Para garantizar la precisión académica de las simulaciones y evitar "alucinaciones" teóricas:
* **Validación contra Bibliotecas Científicas:** Las simulaciones o resolutores didácticos (ej. diferencias finitas, aproximaciones de series) deben compararse numéricamente contra las soluciones analíticas exactas correspondientes calculadas con `SymPy` o con funciones consolidadas de `SciPy`.
* **Tolerancia:** Se debe verificar que los errores absolutos o relativos medios estén bajo límites razonables de precisión por redondeo en coma flotante:
  $$\text{Error} < 10^{-5} \quad \text{o} \quad \text{np.allclose(resultado\_didactico, resultado\_libreria, atol=1e-5)}$$

---

## 4. Validación de Estilo y Visualización Gráfica

Los gráficos generados por Matplotlib deben ser limpios y legibles para humanos:
* **Estilo Consistente:** Configurar el estilo usando `'seaborn-v0_8-whitegrid'` o el estilo por defecto con rejillas visibles (`plt.grid(True, ls='--', alpha=0.5)`).
* **Etiquetas Claros:** Incluir títulos descriptivos, etiquetas de ejes con unidades físicas y leyendas explicativas, todo redactado en español.
* **Sin Solapamiento:** Ajustar los márgenes de los gráficos para evitar el solapamiento de textos o leyendas mediante `plt.tight_layout()`.
