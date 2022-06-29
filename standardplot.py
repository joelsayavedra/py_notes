# Para instalar los paquetes en un entorno virtual de intérprete, en vez de en el entorno global, es necesario utilizar los siguientes comandos:

# --- Cambiando las políticas para todo el sistema (powershell abierto en la carpeta de user, desde el inicio de W10)
# (terminal python)         python -m venv .venv
# (En windows powershell)   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
# (terminal python)         .venv\scripts\activate
# (En windows powershell)   Set-ExecutionPolicy -ExecutionPolicy Restricted
# Select your new environment by using the Python: Select Interpreter command from the Command Palette.

# --- Cambiando las políticas para la carpeta actual (comandos en ventana de VSCode)
# python -m venv .venv
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .venv\scripts\activate

# Más detalles sobre environments: https://code.visualstudio.com/docs/python/environments#_creating-environments

# Por último, para instalar el paquete: 
# python -m pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi*2, 1000)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot