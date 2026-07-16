import numpy as np
import matplotlib.pyplot as plt

def solve_wave_equation(Lx, Ly, Nx, Ny, T_max, v, CFL_factor, initial_type='gaussian'):
    # Discretización espacial
    dx = Lx / Nx
    dy = Ly / Ny
    x = np.linspace(0, Lx, Nx + 1)
    y = np.linspace(0, Ly, Ny + 1)
    X, Y = np.meshgrid(x, y, indexing='ij')
    
    # CFL condition: dt <= dx / (v * sqrt(2)) if dx == dy
    h = min(dx, dy)
    dt_cfl = h / (v * np.sqrt(2))
    dt = dt_cfl * CFL_factor
    Nt = int(T_max / dt)
    
    # Parámetros físicos ficticios
    rho = 1.0  # Densidad
    T = rho * v**2  # Tensión
    
    # Coeficientes numéricos
    rx2 = (v * dt / dx)**2
    ry2 = (v * dt / dy)**2
    
    # Inicialización de matrices u (tiempo n+1, n, n-1)
    u_new = np.zeros((Nx + 1, Ny + 1))
    u = np.zeros((Nx + 1, Ny + 1))
    u_old = np.zeros((Nx + 1, Ny + 1))
    
    # Estado inicial: f(x, y)
    if initial_type == 'gaussian':
        # Pulso gaussiano en el centro
        xc, yc = Lx / 2.0, Ly / 2.0
        sigma = 0.1
        u = np.exp(-((X - xc)**2 + (Y - yc)**2) / (2 * sigma**2))
    elif initial_type == 'mode':
        # Modo normal (3, 2)
        m, n = 3, 2
        u = np.sin(m * np.pi * X / Lx) * np.sin(n * np.pi * Y / Ly)
        
    # Aplicar condiciones de frontera de Dirichlet (u = 0 en los bordes)
    u[0, :] = 0.0
    u[Nx, :] = 0.0
    u[:, 0] = 0.0
    u[:, Ny] = 0.0
    
    u_old = np.copy(u)
    
    # Primer paso de tiempo (usando u_t = 0)
    for i in range(1, Nx):
        for j in range(1, Ny):
            laplacian = (
                rx2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +
                ry2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1])
            )
            u_new[i, j] = u[i, j] + 0.5 * laplacian
            
    u_old = np.copy(u)
    u = np.copy(u_new)
    
    energy_history = []
    
    # Bucle temporal
    for step in range(1, Nt):
        u_new = np.zeros((Nx + 1, Ny + 1))
        for i in range(1, Nx):
            for j in range(1, Ny):
                laplacian = (
                    rx2 * (u[i+1, j] - 2*u[i, j] + u[i-1, j]) +
                    ry2 * (u[i, j+1] - 2*u[i, j] + u[i, j-1])
                )
                u_new[i, j] = 2 * u[i, j] - u_old[i, j] + laplacian
                
        # Asegurar condiciones de frontera
        u_new[0, :] = 0.0
        u_new[Nx, :] = 0.0
        u_new[:, 0] = 0.0
        u_new[:, Ny] = 0.0
        
        # Calcular energía en el paso actual
        # Energía cinética: 0.5 * rho * (du/dt)^2 * dx * dy
        # du/dt aproximada por (u - u_old) / dt
        v_t = (u - u_old) / dt
        Ek = 0.5 * rho * np.sum(v_t[1:Nx, 1:Ny]**2) * dx * dy
        
        # Energía potencial: 0.5 * T * ((du/dx)^2 + (du/dy)^2) * dx * dy
        # Aproximación por diferencias finitas hacia adelante
        du_dx = (u[1:, :Ny] - u[:-1, :Ny]) / dx
        du_dy = (u[:Nx, 1:] - u[:Nx, :-1]) / dy
        Ep = 0.5 * T * (np.sum(du_dx**2) + np.sum(du_dy**2)) * dx * dy
        
        E_total = Ek + Ep
        energy_history.append((step * dt, Ek, Ep, E_total))
        
        # Actualizar variables de tiempo
        u_old = np.copy(u)
        u = np.copy(u_new)
        
        # Si explota, terminar
        if np.any(np.isnan(u)) or np.max(np.abs(u)) > 1e3:
            return None, None
            
    return u, np.array(energy_history)

def run_tests():
    Lx, Ly = 1.0, 1.0
    Nx, Ny = 40, 40
    T_max = 2.0
    v = 1.0
    
    print("Test 1: Ejecutando simulación estable (CFL = 0.9)...")
    u_stable, energy_stable = solve_wave_equation(Lx, Ly, Nx, Ny, T_max, v, 0.9, 'mode')
    if u_stable is not None:
        print("¡Estable!")
        times = energy_stable[:, 0]
        E_tot = energy_stable[:, 3]
        std_energy = np.std(E_tot) / np.mean(E_tot)
        print(f"Conservación de energía (desviación estándar / media): {std_energy:.6f}")
    else:
        print("Fallo en la simulación estable.")
        
    print("\nTest 2: Ejecutando simulación inestable (CFL = 1.5)...")
    u_unstable, energy_unstable = solve_wave_equation(Lx, Ly, Nx, Ny, T_max, v, 1.5, 'mode')
    if u_unstable is None:
        print("¡Correcto! La simulación explotó como se esperaba por violar la condición CFL.")
    else:
        print("ADVERTENCIA: La simulación inestable no explotó.")

if __name__ == '__main__':
    run_tests()
