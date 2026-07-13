# Guía de Agentes de Inteligencia Artificial (AGENTS.md)

Este documento es el punto de entrada principal para cualquier agente de IA que trabaje en el repositorio `Foundations-of-Physics`. Su objetivo es proporcionar una referencia operativa rápida del proyecto y redirigir a guías especializadas para evitar la dispersión y desorganización de las reglas de desarrollo.

---

## 1. Descripción General del Proyecto

`Foundations-of-Physics` es un repositorio académico diseñado para documentar de forma rigurosa y formal estudios universitarios en Física y Matemáticas en español. Su estructura está compuesta por **módulos educativos**, donde cada módulo aborda una rama específica del conocimiento y se implementa a través de **cuadernos de Jupyter (Jupyter Notebooks)**.

---

## 2. Stack Tecnológico

El entorno de ejecución del proyecto es exclusivamente Python orientado a la ciencia y visualización de datos:
* **Lenguaje:** Python (3.x)
* **Entorno:** Jupyter Notebooks (`.ipynb`)
* **Librerías principales:** NumPy, SymPy, SciPy, Matplotlib y NetworkX.

Para más detalles de versiones y requerimientos de entorno, lee la **[Guía de Configuración (CONFIG.md)](./docs/agent/CONFIG.md)**.

---

## 3. Estructura de Documentación para Agentes

Para operar de forma segura y eficiente, lee y sigue los lineamientos de los siguientes documentos especializados:

1. **[Políticas de Permisos y Modificaciones (PERMISSIONS.md)](./docs/agent/PERMISSIONS.md):** Define qué archivos y carpetas puedes modificar libremente y qué acciones requieren aprobación humana explícita.
2. **[Procedimiento Operativo y Flujo de Desarrollo (RUNBOOK.md)](./docs/agent/RUNBOOK.md):** Describe cómo generar y mantener cuadernos de Jupyter programáticamente para evitar errores de codificación en LaTeX.
3. **[Estrategia de Pruebas y Verificación (TESTS.md)](./docs/agent/TESTS.md):** Suite de validaciones obligatorias (ejecución secuencial, chequeo JSON y fidelidad física) antes de cerrar una tarea.
4. **[Políticas de Seguridad y Aislamiento (SECURITY.md)](./docs/agent/SECURITY.md):** Reglas para evitar la fuga de secretos, inyección de código y el uso de rutas absolutas locales.
5. **[Arquitectura Teórica y Técnica (ARCHITECTURE.md)](./ARCHITECTURE.md):** Describe el flujo conceptual de datos y el modelo arquitectónico de capas de abstracción educativa.
6. **[Reglas de Desarrollo y Estilo (DEVELOPMENT_RULES.md)](./DEVELOPMENT_RULES.md):** Estándares de nombrado de carpetas, variables, comentarios en español y estilo visual de gráficos.

---

## 4. Definición de Terminado (Definition of Done)

Una tarea se considera finalizada únicamente cuando:
1. El cuaderno de Jupyter creado o modificado aprueba todas las verificaciones descritas en **[TESTS.md](./docs/agent/TESTS.md)**.
2. Se actualiza el archivo `README.md` del módulo correspondiente con el enlace directo y descripción de la lección (cambiando su estado a `Desarrollado`).
3. Se registra el avance en la lista de tareas `task.md` y se crea el reporte `walkthrough.md` en la carpeta de la conversación.
