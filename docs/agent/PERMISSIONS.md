# Políticas de Permisos para Agentes de IA (PERMISSIONS.md)

Este documento detalla los alcances, restricciones y permisos de modificación asignados a los agentes de IA dentro de este repositorio.

---

## 1. Zonas del Repositorio

### A. Zonas Editables Sin Confirmación
El agente puede crear, editar y guardar de forma autónoma archivos en las siguientes ubicaciones:
* **Lecciones Planificadas de Nuevos Módulos:** Directorios de lecciones que aún no han sido desarrolladas y estén especificadas en el temario (ej. `04-fundamentos-de-electromagnetismo/introduccion/` o `04-fundamentos-de-electromagnetismo/leccion-11/` antes de su creación).
* **Archivos README de Módulos Nuevos:** Archivos `README.md` locales de módulos que se estén implementando actualmente, con el único fin de actualizar los índices de avance.

### B. Zonas Protegidas (Requieren Aprobación Humana)
Está estrictamente prohibido realizar modificaciones directas en las siguientes carpetas y archivos sin la aprobación explícita del usuario mediante el plan de implementación:
* **Lecciones ya Desarrolladas:** Cualquier cuaderno de Jupyter (`.ipynb`) correspondiente a lecciones completadas con anterioridad (ej. lecciones de los Módulos 1, 2, 3 o las lecciones 1 a 10 ya desarrolladas en el Módulo 4).
* **Documentación y Configuración del Repositorio:** 
  - `AGENTS.md`
  - `ARCHITECTURE.md`
  - `DEVELOPMENT_RULES.md`
  - `README.md` (Raíz del repositorio)
  - `docs/agent/` (Cualquier archivo de esta carpeta)

---

## 2. Acciones del Agente

### A. Operaciones Permitidas
* Leer y explorar de forma ilimitada cualquier archivo del repositorio para obtener contexto o reutilizar patrones.
* Crear y modificar planes de implementación en `implementation_plan.md` y tareas en `task.md`.
* Crear scripts auxiliares temporales en la carpeta de artefactos de la conversación (`scratch/`) para validar código o ejecutar simulaciones de prueba de solo lectura.

### B. Operaciones que Requieren Aprobación Humana
* Modificar la firma o los resultados teóricos/gráficos de lecciones históricas.
* Modificar archivos de configuración del entorno (ej. `.gitignore`).
* Borrar o renombrar cualquier archivo de cuaderno (`.ipynb`) o carpeta del proyecto.

### C. Operaciones Prohibidas
* **PROHIBIDO** crear archivos de script Python sueltos (`.py`) en las carpetas de las lecciones. Todo el código debe estar embebido en los cuadernos `.ipynb`.
* **PROHIBIDO** incluir comandos de terminal interactivos (p. ej. `!pip install`, `!wget`) en celdas de código activas de los cuadernos.
* **PROHIBIDO** almacenar secretos, credenciales o rutas absolutas locales en los cuadernos del repositorio.
* **PROHIBIDO** crear archivos `.gitkeep` u otros placeholders en directorios vacíos.
