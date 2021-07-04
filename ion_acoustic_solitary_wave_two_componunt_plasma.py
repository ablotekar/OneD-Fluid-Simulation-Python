"""
Name  : ion_acoustic_solitary_wave_two_componunt_plasma.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-03 

DESC  : This program simulate evolution of the ion acoustic solitary
        tow componunt plasma system. The plasma system consist of fluid
        ions and superthermal electrons. The electron follows the Kappa
        velocity distribution hence its density is given by kappa
        density function and ion are governed by fluid equation.
"""
import numpy as np
import matplotlib.pyplot as plt
import fluidplasma as fp
import time as tp

# Input parameters
lx = 500  # System length
dx = 0.2  # Spatial grid size
dt = 0.1  # Temporal grid size
ne0 = 1.0  # Equilibrium electron density
ni0 = 1.0  # Equilibrium ion density
nx = int(lx / dx)  # Number of grid points
x0 = 0.5 * nx * dx  # Position of the perturbation
wd = 5  # Width of the perturbation
a0 = 0.5  # Amplitude of perturbation (same in this case)
kp = 2
w = 0.70
tol = 1.e-10
ntime = 1000000

nx4 = nx + 4

x = np.linspace(-1, nx4 - 2, nx4) * dx
x[0] = 0.0
x[1] = 0.0
x[-1] = 0.0
x[-2] = 0.0

# Initializing variables
ne = np.zeros((nx4, 2))  # Electron density
ni = np.zeros((nx4, 2))  # Ion density
vi = np.zeros((nx4, 2))  # Ion velocity
ph = np.zeros((nx4, 2))  # Electrostatic potential
Ex = np.zeros((nx4, 1))  # Electric field

# Perturbing system
ne[:, 0] = 1 + fp.gaussian(x, a0, wd, x0)
ne[:, 1] = 1 + fp.gaussian(x, a0, wd, x0)

ni[:, 0] = 1 + fp.gaussian(x, a0, wd, x0)
ni[:, 1] = 1 + fp.gaussian(x, a0, wd, x0)

# computing electrostatic potential when system get perturb
for i in range(3, nx4 - 3):
    ph[i + 1, 0] = 2 * ph[i, 0] - ph[i - 1, 0] \
                   - dx * dx * (ni[i, 0] - ne[i, 0])
ph[:, 1] = ph[:, 0]

# plt.ion()
# figure, ax = plt.subplots(figsize=(10, 8))
# line1, = ax.plot(x[2:nx4 - 3], ph[2:nx4 - 3, 0])

for j in range(0, ntime):
    # TODO: Remove numerical error
    # TODO: Check for the periodic boundary update and filter
    # TODO: Check Poisson solver, this mya be messing up.
    # Continuity equation
    vi, ni = fp.continuity_equation(vi, ni, ph, 1, dx, dt)
    # Poisson's equation solution (kappa density)
    ph[:, 1] = fp.poissons_solution(ph[:, 1], ni[:, 1], kp, dx, w, tol)

    # Continuity equation
    vi, ni = fp.continuity_equation(vi, ni, ph, 0, dx, dt)
    # Poisson's equation solution (kappa density)
    ph[:, 0] = fp.poissons_solution(ph[:, 0], ni[:, 0], kp, dx, w, tol)

    # Plot the results
    # line1.set_ydata(ph[2:nx4 - 3, 0])
    # figure.canvas.draw()
    # figure.canvas.flush_events()

    if np.mod(j, 100) == 0:
        # TODO: Need to find way to reused same figure window
        plt.plot(x[2:nx4 - 3], ph[2:nx4 - 3, 0])
        # plt.xlim(400, 600)
        # plt.ylim(-2, 2)
        plt.title("Linear graph" + str(j))
        plt.show()
        tp.sleep(0.5)
