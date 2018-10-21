from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import animation
from optimization import FireflyOptimizer
import numpy as np
from optimization import Ackley


#def animate_firefly_convergence(min_bound=-32, max_bound=32):
f_alg = FireflyOptimizer(population_size=50, problem_dim=200, generations=10000, beta_min=0.65, alpha=0.05)
func = Ackley(2)

N = 100
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
z = func.get_y_2d(X, Y)
# dt = 1. / 30

fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(111, aspect='equal', xlim=(-5, 5), ylim=(-5, 5))  # autoscale_on=False)
cs = ax.contourf(X, Y, z, cmap=cm.PuBu_r)
cbar = fig.colorbar(cs)

particles, = ax.plot([], [], 'bo', ms=6)

rect = plt.Rectangle([-5, 5], 10, 10, ec='none', lw=2, fc='none')
ax.add_patch(rect)

def init():
    global f_alg, rect
    particles.set_data([], [])
    rect.set_edgecolor('none')
    return particles, rect

def animate(i):
    global f_alg, rect, ax, fig
    f_alg.step()
    ms = int(fig.dpi * 2 * 0.04 * fig.get_figwidth()
         / np.diff(ax.get_xbound())[0])
    rect.set_edgecolor('k')
    x = []
    y = []
    for ind in f_alg.population:
        x.append(ind.position[0])
        y.append(ind.position[0])
    particles.set_data(x, y)
    particles.set_markersize(ms)
    return particles, rect

ani = animation.FuncAnimation(fig, animate, frames=600, interval=10,
                              blit=True, init_func=init)
ani.save('particle_box.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()


#animate_firefly_convergence()
