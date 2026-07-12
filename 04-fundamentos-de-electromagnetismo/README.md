# Módulo 4: Fundamentos de Electromagnetismo

Este módulo abarca el estudio formal del electromagnetismo, partiendo desde la electrostática y magnetostática en el vacío y en medios materiales, hasta la formulación unificada de las ecuaciones de Maxwell y la inducción electromagnética. Cada lección conecta la deducción matemática de las leyes fundamentales de la física con simulaciones y modelos numéricos interactivos en Python.

El módulo está estructurado en una lección introductoria de nivelación, 10 lecciones temáticas teórica-computacionales y un proyecto final integrador de unificación.

---

## Índice del Módulo

### [Introducción: Fundamentos de Análisis Vectorial y Métodos de Rejilla (Desarrollado)](./introduccion/conceptos-esenciales.ipynb)
- **Conceptos**: Operadores diferenciales vectoriales (gradiente, divergencia, rotacional, laplaciano), teoremas integrales fundamentales (teorema de Gauss/divergencia y teorema de Stokes), y parametrización de mallas cartesianas discretas.
- **Código**: Visualización interactiva 2D/3D de campos escalares y vectoriales en Python; resolutor numérico de gradientes por diferencias finitas centradas sobre rejillas discretas evaluando el perfil de error; y verificación simbólica de identidades vectoriales tridimensionales con SymPy.

### [Lección 1: Campo Eléctrico I (Desarrollado)](./leccion-1/campo-electrico-y-ley-de-coulomb.ipynb)
- **Conceptos**: Carga eléctrica puntual, historia del electromagnetismo, conductividad y resistividad, ley de Coulomb, principio de superposición de fuerzas, potencial electrostático e integrales de línea, distribución continua de cargas, placas paralelas y Ley de Gauss.
- **Código**: Simulación de la fuerza resultante de Coulomb sobre una carga de prueba 2D, trazado interactivo de líneas de campo y superficies equipotenciales en dipolos, y modelado numérico con efectos de borde de un capacitor de placas paralelas discreto.

### [Lección 2: Campo Eléctrico II (Desarrollado)](./leccion-2/campo-electrico-distribuciones-continuas-y-gauss.ipynb)
- **Conceptos**: Principio de superposición en el continuo, campo de un cable recto y de un disco cargado, flujo eléctrico, formas integral y diferencial de la Ley de Gauss, campo de esferas cargadas uniformes y no uniformes, campo de cilindros, discontinuidad normal del campo y conductores en equilibrio electrostático (efecto puntas y microscopio FIM).
- **Código**: Simulación comparativa de cable cargado finito vs. cable infinito, modelado del campo axial de un disco cargado y límite de plano infinito, graficación de perfiles radiales de campo en esferas conductoras, dieléctricas uniformes y no uniformes, y validación simbólica de integrales con SymPy.

### [Lección 3: Potencial Eléctrico (Desarrollado)](./leccion-3/potencial-electrico-y-energia-electrostatica.ipynb)
- **Conceptos**: Potencial eléctrico y diferencia de potencial, operadores diferenciales vectoriales (operador laplaciano y Ecuación de Poisson), potencial de cargas discretas y aproximación binomial del dipolo (momento dipolar), potencial de distribuciones continuas (cable recto, anillo, disco), superficies equipotenciales y su ortogonalidad con el campo, energía potencial de interacción de cargas (redes de ensamblaje) y energía acumulada en capacitores.
- **Código**: Simulación de error porcentual del potencial dipolar exacto frente al modelo aproximado del momento dipolar, comparación gráfica de perfiles de potencial axial continuo (disco y cable) frente al decaimiento de carga puntual ($1/z$), y simulador dinámico del ensamblaje electrostático discreto evaluando la energía potencial acumulada. Verificación simbólica en SymPy de la expansión en serie de Taylor del dipolo.

### [Lección 4: Condensadores (Desarrollado)](./leccion-4/condensadores-dielectricos-y-circuitos.ipynb)
- **Conceptos**: Capacitancia y dimensiones geométricas, almacenamiento de energía electrostática, transitorio de carga y descarga RC (identificación y corrección de la errata física del libro guía), tipos de condensadores y baterías modernas, Leyes de Kirchhoff para mallas mixtas, dieléctricos (polarización molecular, permitividad, rigidez y pérdida dieléctrica) y tabla de constantes dieléctricas.
- **Código**: Simulación de curvas exponenciales temporales de voltaje y corriente en transitorios RC, resolutor de redes de Kirchhoff mixtas de mallas por álgebra lineal matricial, y perfil del campo eléctrico atenuado en condensadores parcialmente llenos por efecto de polarización. Verificación simbólica en SymPy de la EDO del transitorio RC.

### [Lección 5: Circuitos de Corriente Continua (Desarrollado)](./leccion-5/circuitos-de-corriente-continua.ipynb)
- **Conceptos**: Definición de corriente y fem, clasificación de baterías y rectificadores de CA a CC (identificación y corrección de erratas teóricas del libro guía), Ley de Ohm y resistividad, reducción serie-paralelo de redes de resistores complejas, Leyes de Kirchhoff de nodos (LCK) y mallas (LVK) para circuitos de múltiples lazos, transitorio RC de carga y descarga y marcas de constante de tiempo \(\tau\).
- **Código**: Algoritmo en Python de reducción serie-paralelo paso a paso de una red mixta compleja, resolutor matricial de mallas de Kirchhoff usando álgebra lineal con cálculo del balance de potencia (\(P_{entregada} = P_{disipada}\)), y perfiles de voltaje, carga y corriente en transitorios RC. Verificación simbólica en SymPy del sistema algebraico de mallas.

### [Lección 6: Campo Magnético y Fuerzas Magnéticas (Desarrollado)](./leccion-6/campo-magnetico-y-fuerzas-magneticas.ipynb)
- **Conceptos**: Definición de campo magnético, polos y líneas de campo, magnetismo terrestre y ausencia de monopolos. Fuerza de Lorentz sobre cargas puntuales móviles, identificando y corrigiendo múltiples erratas (exponente del Ejemplo 2, confusión de protón/electrón y signo de energía potencial magnética dipolar). Dinámica de ciclotrón circular y trayectoria helicoidal sesgada con paso (pitch). Fuerzas y torque sobre conductores y espiras, y deducción matemática del Efecto Hall.
- **Código**: Simulación y trazado 3D de la trayectoria helicoidal de un protón en campo uniforme rotulando sus parámetros de ciclotrón, perfiles de torque y energía potencial del dipolo magnético mostrando equilibrios estables/inestables, y modelado 3D de la superficie de voltaje Hall para cobre. Validación simbólica en SymPy de la ortogonalidad tridimensional de la fuerza de Lorentz y el torque.

### [Lección 7: Ley de Biot-Savart y Ley de Ampère (Desarrollado)](./leccion-7/ley-de-biot-savart-y-ley-de-ampere.ipynb)
- **Conceptos**: Campo magnético de cargas en movimiento y de elementos de corriente, Ley de Biot-Savart, conductor recto de longitud finita e infinita, fuerza magnética entre conductores paralelos y definición del Ampere, campo en el eje de espiras y bobinas (identificación y corrección de la errata de omisión de \(\pi\) en la Fórmula 13 del libro), Ley de Gauss para el magnetismo (divergencia nula) y Ley de Ampère en forma integral.
- **Código**: Simulación e integración numérica tridimensional de Biot-Savart para espira circular de corriente con líneas de flujo en el plano transversal XZ, gráfico comparativo de perfil de campo axial de bobina frente a dipolo con error relativo logarítmico, y curva de corriente de equilibrio para suspensión magnética. Validación simbólica con SymPy de la integral definida del conductor recto finito.

### [Lección 8: Inducción Electromagnética y Ley de Faraday (Desarrollado)](./leccion-8/induccion-electromagnetica-y-ley-de-faraday.ipynb)
- **Conceptos**: Flujo magnético, Ley de Faraday para inducción de fem, Ley de Lenz, fem de movimiento en conductores móviles y campo eléctrico inducido no conservativo, inductancia (autoinductancia e inductancia mutua), almacenamiento de energía magnética y densidad de energía, y transitorios en circuitos RL (crecimiento y decaimiento de corriente). Identificación y corrección de la errata de transposición del Ejemplo 2 (de \(0.453\text{ V}\) a \(0.436\text{ V}\)).
- **Código**: Simulación temporal de transitorios RL (carga/descarga de corriente y tensiones en componentes con marcas de constante de tiempo \(\tau\)), y simulación visual del ingreso de una espira a campo uniforme (flujo, fem de movimiento y fuerza amortiguadora de Lenz). Validación simbólica con SymPy de la EDO lineal del circuito RL en crecimiento.

### [Lección 9: Circuitos de Corriente Alterna (Desarrollado)](./leccion-9/circuitos-de-corriente-alterna.ipynb)
- **Conceptos**: Alternancia armónica, periodo, frecuencia y valores eficaces (rms). Reactancias y desfases de resistores, inductores (corrección de la errata de amplitud negativa) y condensadores (corrección de la errata dimensional de la Fórmula 21). Transformadores ideales, relaciones de espiras y acoplamiento de impedancias. Representación fasorial en el plano complejo y resolución completa del circuito RLC serie (impedancia Z, desfase y frecuencia de resonancia natural).
- **Código**: Simulación animada de diagramas de fasores rotatorios complejos proyectados armónicamente en el tiempo, y barrido de frecuencias para curvas de resonancia de impedancia Z(f) y corriente I_max(f).  Validación simbólica con SymPy del módulo y fase de la impedancia compleja.

### [Lección 10: Ecuaciones de Maxwell y Ondas Electromagnéticas (Desarrollado)](./leccion-10/ecuaciones-de-maxwell-y-ondas-electromagneticas.ipynb)
- **Conceptos**: Corriente de desplazamiento de Maxwell y Ley de Ampère-Maxwell, las cuatro ecuaciones de Maxwell en formato integral y diferencial, y la Ley de Fuerza de Lorentz. Deducción matemática de la ecuación de onda electromagnética unidimensional en el vacío y cálculo exacto de la velocidad de la luz \(c = 1/\sqrt{\mu_0 \epsilon_0}\). Propiedades de las ondas planas (transversalidad, ortogonalidad y vector de Poynting) y el espectro electromagnético (identificación y corrección de la errata de rangos de microondas de la Tabla I).
- **Código**: Simulación y trazado 3D de la propagación de una onda electromagnética armónica plana mostrando los vectores ortogonales de campo eléctrico y magnético, y visualizador logarítmico del espectro electromagnético con zoom lineal a la banda visible y mapeo de colores RGB reales. Validación analítica con SymPy de las soluciones sinusoidales de la ecuación de onda.

### [Lección 11: Consolidado y Conclusión del Módulo 4 (Desarrollado)](./leccion-11/consolidado-y-conclusion-del-modulo-4.ipynb)
- **Conceptos**: Resumen y mapa conceptual del Módulo 4; propiedades magnéticas de la materia: magnetización, diamagnetismo, paramagnetismo (función de Langevin), ferromagnetismo (ciclo de histéresis, coercitividad y remanencia) y temperatura de Curie; estudio de caso integrador multifísico de un freno magnético por corrientes de Foucault (Eddy currents).
- **Código**: Simulación de la función de Langevin paramagnética y comparación con la ley de Curie; modelado del ciclo de histéresis ferromagnética no lineal; simulación de la dinámica de frenado electromagnético (velocidad angular y balance energético de potencia disipada) y validación simbólica del desarrollo de Taylor de Langevin con SymPy.
