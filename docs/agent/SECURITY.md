# Políticas de Seguridad para Agentes (SECURITY.md)

Este documento establece las directrices de seguridad obligatorias que los agentes de IA deben cumplir al interactuar con el código, datos y configuraciones de este repositorio.

---

## 1. Protección de Datos Sensibles y Credenciales

* **Sin Secretos:** No se permite agregar variables que contengan claves de API, tokens de autenticación, contraseñas o credenciales de ningún tipo a los cuadernos.
* **Aislamiento de Rutas:** Está prohibido incluir rutas de archivo absolutas del sistema operativo del usuario o del agente (ej. `C:\Users\NombreUsuario\...` o `/home/agent/...`) en las celdas activas de los cuadernos. Toda referencia a archivos locales del repositorio debe ser relativa (ej. `./leccion-1/datos.csv` o `../README.md`).

---

## 2. Inyección de Código y Ejecución Segura

* **Ejecución Insegura:** Queda terminantemente prohibido el uso de las funciones nativas `eval()` y `exec()` de Python para parsear o simplificar expresiones matemáticas ingresadas de forma dinámica en las simulaciones.
* **Alternativa Segura:** Para evaluar simbólicamente fórmulas, se debe utilizar el motor analítico seguro de SymPy mediante `sympy.sympify()` o evaluar numéricamente mediante arrays de NumPy de forma explícita.

---

## 3. Seguridad en el Versionado y Commits

* **Exclusión de Temporales:** El agente debe asegurarse de que ningún archivo temporal de ejecución, carpetas de checkpoints de Jupyter (`.ipynb_checkpoints/`) o entornos virtuales locales (`.venv/`) sean indexados en el control de versiones, respetando estrictamente las exclusiones del archivo `.gitignore` raíz.
* **Confirmación de Cambios:** Cualquier modificación de archivos de infraestructura, licencias legales o políticas del repositorio requiere aprobación humana previa explícita.
