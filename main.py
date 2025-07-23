import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    term1 = np.sin(16/15 * x1 - 1) + np.sin(16/15 * x1 - 1)**2 + 1/50 * np.sin(4*(16/15 * x1 - 1))
    term2 = np.sin(16/15 * x2 - 1) + np.sin(16/15 * x2 - 1)**2 + 1/50 * np.sin(4*(16/15 * x2 - 1))
    return 0.6 + term1 + term2

x1_min, x1_max = -1.0, 1.0
x2_min, x2_max = -1.0, 1.0
x10, x20 = 0.45834282, 0.45834282
step = 0.01

x1 = np.arange(x1_min, x1_max + step, step)
x2 = np.arange(x2_min, x2_max + step, step)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)
y_test = f(x10, x20)

fig = plt.figure(figsize=(16, 12))
fig.suptitle(f'Графики функции f(x1, x2)\nТестовая точка: (x10={x10:.8f}, x20={x20:.8f}), f(x10, x20)={y_test:.8f}', fontsize=16)

ax1 = fig.add_subplot(221, projection='3d')
ax1.plot_surface(X1, X2, Y, cmap='viridis')
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y=f(x1, x2)')
ax1.set_title('3D поверхность')

ax2 = fig.add_subplot(222)
contour = ax2.contourf(X1, X2, Y, levels=20, cmap='viridis')
plt.colorbar(contour, ax=ax2)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_title('Вид сверху')

ax3 = fig.add_subplot(223)
y_x1 = f(x1, x20)
ax3.plot(x1, y_x1)
ax3.set_xlabel('x1')
ax3.set_ylabel('y=f(x1, x20)')
ax3.set_title(f'График y=f(x1) при x2={x20:.8f}')
ax3.grid(True)

ax4 = fig.add_subplot(224)
y_x2 = f(x10, x2)
ax4.plot(x2, y_x2)
ax4.set_xlabel('x2')
ax4.set_ylabel('y=f(x10, x2)')
ax4.set_title(f'График y=f(x2) при x1={x10:.8f}')
ax4.grid(True)

plt.tight_layout()
plt.show()