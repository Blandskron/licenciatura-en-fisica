import json
import traceback

def run_notebook_cells(path):
    print(f"Abriendo cuaderno: {path}")
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # Namespace compartido para las celdas
    import matplotlib
    matplotlib.use('Agg')
    globals_dict = {}
    
    code_cell_index = 0
    success = True
    
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            code_cell_index += 1
            source_code = "".join(cell["source"])
            print(f"\n--- Ejecutando Celda de Código #{code_cell_index} ---")
            try:
                # Ejecutar la celda
                exec(source_code, globals_dict)
                print(f"Celda #{code_cell_index} ejecutada con éxito.")
            except Exception as e:
                print(f"Error en Celda #{code_cell_index}:")
                traceback.print_exc()
                success = False
                break
                
    if success:
        print("\n==================================================")
        print("¡Todas las celdas de código se ejecutaron con éxito!")
        print("==================================================")
    else:
        print("\n==================================================")
        print("ERROR: La ejecución del cuaderno falló.")
        print("==================================================")
        raise RuntimeError("Fallo en la ejecución de celdas de código.")

if __name__ == "__main__":
    notebook_path = r"c:\Users\BlandskronNotebook\Documents\blandskron\licenciatura-en-fisica\05-calculo-2\leccion-2\integrales-impropias-y-transformada-de-laplace.ipynb"
    run_notebook_cells(notebook_path)
