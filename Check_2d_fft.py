"""
Name  : Check_2d_fft.py
Author: Ajay Lotekar
e-mail: ablotekar@gmail.com
Date  : 2021-07-14 

DESC  :
"""
from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
import fluidplasma as fp

# Merge all small csv file into signel matrix
for i in range(99, 899, 100):
    fname = "./data/FFT/PH"+str(i)+".csv"
    print(fname)
    ph1 = genfromtxt(fname, delimiter=' ')
    ph1 = ph1.transpose()
    if i==99:
        ph2 = genfromtxt(fname, delimiter=' ')
        ph2 = ph2.transpose()
    if i > 99:
        ph2 = np.vstack((ph2, ph1))

# Save combined data matrix in csv file
np.savetxt('./data/FFT.csv', ph2, delimiter=" ")

# Some constants
dx = 0.2        # Spatial grid size
dt=0.1          # Temporal grid size

z2, k2, w2 = fp.wk2d(ph2, dx, dt)  # Compute 2d fft


# Plotting the result
tpc = plt.imshow(z2, aspect='auto', interpolation='none',
           extent=[k2.min(), k2.max(), w2.min(), w2.max()], origin='lower')
plt.colorbar(tpc)
plt.jet()
plt.ylim(0, 2)
plt.xlim(-3, 3)
plt.xlabel('$k$')
plt.ylabel("$\omega$")
plt.title("$\omega -$k plot")
plt.savefig("./figures/wkplot.png")
plt.show()


