# Módulo 3: Fundamentos de Óptica

Este módulo abarca el estudio formal de las oscilaciones, ondas y fenómenos ópticos, vinculando las leyes físicas clásicas y electromagnéticas con el modelado computacional y la simulación interactiva. Se compone de un cuaderno de nivelación, 10 cuadernos temáticos en Jupyter Colab con teoría rigurosa y simulaciones en Python, y un proyecto final integrador.

---

## Índice del Módulo

### [Introducción: Bases de Ondas y Óptica Geométrica](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Introduccion)
- **Conceptos**: Ecuación de onda elemental, representación de ondas senoidales, velocidad de propagación, longitud de onda, fase y espectro electromagnético visible.
- **Código**: Visualización de ondas viajeras y estacionarias unidimensionales y mapeo cromático del espectro visible.

### [Lección 1: Movimiento Oscilatorio](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion1)
- **Conceptos**: Movimientos periódicos y funciones trigonométricas, identidades trigonométricas y exponenciales, series de Taylor, Movimiento Armónico Simple (MAS), dinámica de resortes y conservación de energía, péndulo simple y aproximación de ángulo pequeño, péndulo físico, oscilaciones amortiguadas (sub, crítico, sobre) y forzadas/resonancia.
- **Código**: Simulación de la evolución temporal y transformaciones de energía en MAS, análisis del error en la aproximación de ángulo pequeño en péndulos, decaimiento de amplitud en osciladores amortiguados y curvas de ganancia y resonancia de amplitud.

### [Lección 2: Movimiento Ondulatorio](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion2)
- **Conceptos**: Perturbación y propagación, parámetros de onda, derivación de la ecuación de onda en el límite continuo, ondas transversales y longitudinales, polarización elíptica/circular, armónicos y ondas estacionarias, espectro electromagnético e intensidad.
- **Código**: Resolutor numérico de la ecuación de onda 1D en diferencias finitas, modelado 3D de polarizaciones y simulación del corrimiento Doppler relativista en el hidrógeno.

### [Lección 3: Superposición de Ondas: Fenómenos](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion3)
- **Conceptos**: Experimento de Young, principio de superposición, interferencia constructiva/destructiva coherente y corrección de erratas teóricas, batidos (beats), ondas estacionarias en cuerdas (energía, potencia, velocidad física, extremos fijos y libres), ROE/SWR, acústica en tubos y el Tubo de Rubens.
- **Código**: Simulación del patrón de franjas de doble rendija de Young, graficación de la modulación de amplitud en batidos, modelado de ondas estacionarias elásticas con extremos fijos/libres y representación de presión en el Tubo de Rubens.

### [Lección 4: El Sonido como Onda Mecánica y sus Características](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion4)
- **Conceptos**: Ondas de sonido (longitudinales de presión, compresiones y rarefacciones), reflexión y refracción acústica (desviación de frentes de onda por inversión térmica y gradientes de temperatura), derivación de la velocidad del sonido en gases ideales bajo procesos adiabáticos ($v = \sqrt{\gamma R T / M}$), interferencia de ondas coherentes, batidos (pulsaciones), ondas estacionarias en tubos abiertos y cerrados, escalas musicales y armónicos (escala temperada, timbre), y efecto Doppler clásico (signos) y supersónico (ondas de choque, cono de Mach, número Mach).
- **Código**: Representación discreta de partículas oscilando longitudinalmente, trazado geométrico diferencial de rayos de sonido refractados en la atmósfera, graficación de la velocidad del sonido vs temperatura, análisis de modulación y batidos en el tiempo, perfiles de presión estacionaria en tubos, síntesis armónica de timbres y simulación de frentes de onda Doppler y Cono de Mach.


### [Lección 5: La Luz como Onda Electromagnética](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion5)
- **Conceptos**: Repaso de electrostática y magnetostática, ecuaciones de Maxwell en forma diferencial, derivación formal de la ecuación de onda en el vacío, velocidad de la luz en el vacío ($c = 1/\sqrt{\mu_0 \epsilon_0}$) y en medios materiales ($v = 1/\sqrt{\mu \epsilon}$), ondas planas sinusoidales, estados de polarización de la luz (lineal, circular y elíptica), densidad de energía de los campos, vector de Poynting ($\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$), intensidad media, presión de radiación, ondas electromagnéticas estacionarias por reflexión en conductores perfectos, cavidades resonantes, bandas del espectro electromagnético, radiación de cuerpo negro y ley de Wien.
- **Código**: Simulación de líneas de campo y potencial de un dipolo eléctrico, validación analítica de la solución de onda de Maxwell usando SymPy, modelado interactivo 3D de polarizaciones lineal, circular y elíptica, graficación de la onda estacionaria con nodos eléctricos y antinodos magnéticos alternantes, y simulación de curvas de emisión de cuerpo negro (Ley de Planck) mostrando el desplazamiento del pico (Ley de Wien).


### [Lección 6: Estudio de la Luz y sus Fenómenos Fundamentales](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion6)
- **Conceptos**: Evolución de las teorías de la luz (Newton vs Huygens), experimento de la doble rendija de Young, dualidad onda-partícula en fotones y electrones (de Broglie), principio de incertidumbre de Heisenberg, principio de correspondencia de Bohr, velocidad de la luz (Roemer, Bradley y Maxwell), reflexión (especular y difusa), refracción y ley de Snell, dispersión cromática y ecuación de Cauchy, reflexión total interna y ángulo crítico, física del arcoíris primario y secundario (desviación angular en gotas), y polarización/birrefringencia (calcita, rayo ordinario y extraordinario).
- **Código**: Simulación de la probabilidad de interferencia de electrones en doble rendija, modelado del retraso temporal de Roemer en la órbita de Ío, trazado de rayos dispersivos (rojo, verde, azul) a través de un prisma de vidrio usando la ecuación de Cauchy, simulación de la reflexión total interna y ángulo crítico, graficación del ángulo de salida vs parámetro de impacto en gotas de lluvia (comprobación del pico del arcoíris a $42^\circ$), y trazado de la doble refracción en un medio birrefringente.


### [Lección 7: Óptica Geométrica: Espejos y Lentes](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion7)
- **Conceptos**: Aproximación de rayos, trazado de rayos característicos, imágenes reales y virtuales, reflexión y refracción en superficies planas, absorción selectiva de longitudes de onda (color de objetos), reflexión en espejos esféricos (cóncavos y convexos), trazado de rayos en lentes delgadas (convergentes y divergentes), ecuación de lentes/espejos delgadas ($\frac{1}{d_o} + \frac{1}{d_i} = \frac{1}{f}$), aumento lateral, ecuación del fabricante de lentes (Lensmaker), dioptrías, lentes compuestas en contacto y separadas, distancias focales frontales (DFF) y traseras (DFT), y física del telescopio refractor (sistema afocal).
- **Código**: Simulación gráfica del trazado de rayos para espejos cóncavos con formación de imágenes, modelado de curvas de reflectancia selectiva para el color de objetos, simulación de la posición y magnificación de imágenes vs posición del objeto, resolutor óptico interactivo para lentes delgadas, graficación de dioptrías en la ecuación del fabricante de lentes, y simulación de trazado de rayos en un telescopio refractor afocal.


### [Lección 8: Instrumentos Ópticos y Ecuaciones de Fresnel](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion8)
- **Conceptos**: Coeficientes de Fresnel para polarizaciones s y p ($R_s, R_p, T_s, T_p$), impedancia de onda ($Z = \sqrt{\mu/\epsilon}$), reflectividad en incidencia normal, ángulo de Brewster, dioptrios ópticos esféricos e invariante de Abbe, aberración cromática y esférica, doblete acromático, telescopio refractor galileano y kepleriano, telescopios reflectores (newtoniano, Cassegrain, gregoriano y Schmidt-Cassegrain), microscopio simple y microscopio compuesto, y tipos especiales (estereomicroscopio, de comparación, invertido y petrográfico).
- **Código**: Graficación de los coeficientes de reflectancia de Fresnel vs ángulo de incidencia y marcado del ángulo de Brewster, modelado de la refracción en dioptrios con el invariante de Abbe, simulación de la aberración esférica y su corrección, panel comparativo de trazado de rayos para telescopios galileano y kepleriano, y simulación del camino óptico en un microscopio compuesto.


### [Lección 9: Fenómenos de Interferencia Óptica e Interferometría](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion9)
- **Conceptos**: Coherencia espacial y temporal, diferencia de fase y diferencia de camino óptico, interferencia constructiva y destructiva en fase y contrafase, interferencia en películas delgadas, reflexión con salto de fase (interfaces dieléctricas), recubrimientos antirreflejantes, experimento de doble rendija de Young, distribución de intensidad de franjas, espaciamiento angular y espacial, difracción de Fraunhofer por ranura única, patrón de difracción-interferencia combinado, e interferómetro de Michelson (anillos concéntricos, espectrómetro FTIR y detectores LIGO).
- **Código**: Simulación de ondas en fase y contrafase con su superposición, modelado de colores de interferencia en películas de aceite sobre agua según el espesor de la capa, simulación del perfil de intensidad de Young y el espaciamiento de franjas para diferentes colores de láser, simulación del patrón combinado de rendija de ancho finito (interferencia modulada por difracción), y simulación 2D de los anillos de interferencia del interferómetro de Michelson.


### [Lección 10: Difracción y Redes de Difracción](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion10)
- **Conceptos**: Principio de Huygens-Fresnel, concepto de difracción vs interferencia, difracción de Fresnel (campo cercano) y de Fraunhofer (campo lejano), número de Fresnel ($F = a^2 / L\lambda$), difracción de Fraunhofer por una rendija y por apertura rectangular, discos de Airy (apertura circular), resolución angular y criterios de limitación de difracción de Abbe y Rayleigh ($\theta = 1.22\lambda/D$), redes de difracción (transmisión y reflexión), dispersión cromática por redes y superposición de órdenes.
- **Código**: Simulación numérica de la difracción de Fresnel de campo cercano de una rendija (resolviendo la integral de Fresnel), graficación 2D del patrón de difracción de una apertura rectangular, visualización del disco de Airy 2D (usando funciones de Bessel), simulación interactiva del criterio de Rayleigh para resolver dos fuentes puntuales cercanas, y simulación de la dispersión angular de longitudes de onda en una red de difracción con múltiples rendijas ($N$).


### [Lección 11: Consolidado y Conclusión del Módulo 3](file:///c:/Users/BlandskronNotebook/Documents/blandskron/Foundations-of-Physics/03-FundamentosDeOptica/Leccion11/consolidado_optica.ipynb)
- **Conceptos**: Síntesis y unificación del módulo en un proyecto integrador: el viaje de un haz electromagnético desde el origen estelar (polarización, Vector de Poynting, Faraday en Maxwell) pasando por refracción acusto-óptica atmosférica (Cauchy dispersivo, gradientes de ondas sonoras, Snell) y enfoque óptico (ABCD en Crown-Flint) hasta análisis de modulación (película delgada, Michelson) y detección espectroscópica (red de difracción N-ranuras, Criterio de Rayleigh para doblete de Sodio).
- **Código**: Simulación end-to-end interactiva de las 5 fases en Python, trazando la elipse de polarización, deflexión de rayos por sonido, corrección cromática con doblete, anillos interferométricos de Michelson y resolución del doblete de Sodio.

