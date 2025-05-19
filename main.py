import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Parámetros
r_max = 5.0
tau_vals = np.linspace(0, 20, 400)

# Movimiento radial con transición suave
r_vals = r_max * np.tanh(2 * (10 - tau_vals) / 10)

# Trayectoria curva usando ángulo
theta_vals = np.linspace(0, 4 * np.pi, len(tau_vals))  # giro de 2 vueltas

# Coordenadas 3D simuladas
x_vals = r_vals * np.cos(theta_vals)
y_vals = r_vals * np.sin(theta_vals)
z_vals = tau_vals  # tiempo propio como altura

# Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-r_max, r_max)
ax.set_ylim(-r_max, r_max)
ax.set_zlim(0, 20)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("Tiempo propio τ")
ax.set_title("🌌 Tránsito 3D a través del agujero de gusano")

line, = ax.plot([], [], [], lw=2)
point, = ax.plot([], [], [], 'ro')

# Inicializar animación
def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

# Función de animación
def animate(i):
    line.set_data(x_vals[:i], y_vals[:i])
    line.set_3d_properties(z_vals[:i])
    point.set_data(x_vals[i-1:i], y_vals[i-1:i])
    point.set_3d_properties(z_vals[i-1:i])
    return line, point

# Crear animación
ani = FuncAnimation(fig, animate, frames=len(tau_vals),
                    init_func=init, blit=True, interval=30)

plt.show()
