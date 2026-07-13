# Guía de Ejecución y Desarrollo (RUNBOOK.md)

Este documento detalla el procedimiento operativo para desarrollar y mantener de forma consistente los cuadernos de Jupyter del repositorio.

---

## 1. Procedimiento de Desarrollo para Nuevos Cuadernos

Dada la cantidad de expresiones matemáticas en LaTeX utilizadas en las lecciones, escribir el archivo JSON de un cuaderno `.ipynb` de forma manual o mediante concatenación de texto crudo es altamente propenso a errores de formateo, comillas rotas e invalidaciones de secuencias de escape (ej. en fórmulas matemáticas con `\s`, `\c`, `\o` o `\d`).

Para mitigar esto, se establece el siguiente flujo de desarrollo obligatorio para agentes:

### Paso 1: Diseño y Programación de Simulaciones
* El agente debe programar y probar primero las simulaciones y el código de Python en un script temporal de prueba dentro del directorio de artefactos (`scratch/test_<simulacion>.py`).
* Se debe ejecutar el script localmente para verificar que las funciones matemáticas y los cálculos den resultados físicamente consistentes.

### Paso 2: Generación Programática del Cuaderno
* En lugar de escribir el archivo `.ipynb` directamente, el agente creará un script generador en Python (`scratch/generate_<leccion>.py`).
* Este script construirá la estructura del cuaderno como un diccionario de Python (`dict`) con las celdas de Markdown y Código correspondientes, y utilizará la librería estándar `json` para volcarlo de forma segura y codificado en UTF-8:
  ```python
  import json
  with open("conceptos-esenciales.ipynb", "w", encoding="utf-8") as f:
      json.dump(notebook_dict, f, indent=2, ensure_ascii=False)
  ```
* Se debe ejecutar este script para crear el cuaderno en la carpeta correspondiente.

---

## 2. Flujo de Validación de Cambios

Una vez generado o modificado el cuaderno, el agente debe ejecutar las siguientes fases:

1. **Chequeo de Integridad JSON:** Ejecutar el parser de validación de JSON en Python sobre el archivo `.ipynb` generado (ver detalles en `docs/agent/TESTS.md`).
2. **Ejecución y Verificación de Gráficos:** El agente debe asegurar que el cuaderno corre secuencialmente en su totalidad.
3. **Actualización de Índices:** Actualizar el archivo `README.md` del módulo correspondiente (añadir el enlace de la nueva lección y su estado) y verificar que no queden enlaces rotos.
