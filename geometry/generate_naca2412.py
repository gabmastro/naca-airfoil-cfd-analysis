# %% NACA 2412



import numpy as np

import matplotlib.pyplot as plt
import pandas as pd

# NACA 2412 parameters
m = 0.02       # maximum camber
p = 0.4        # position of maximum camber
t = 0.12       # maximum thickness
c = 1.0        # chord [m]

# Chordwise points
x = np.linspace(0, 1, 150)

# Thickness distribution
yt = 5 * t * (
    0.2969 * np.sqrt(x)
    - 0.1260 * x
    - 0.3516 * x**2
    + 0.2843 * x**3
    - 0.1036 * x**4
)

# Camber line and its slope
yc = np.zeros_like(x)
dyc_dx = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < p:
        yc[i] = (m / p**2) * (2*p*x[i] - x[i]**2)
        dyc_dx[i] = (2*m / p**2) * (p - x[i])
    else:
        yc[i] = (m / (1-p)**2) * (
            (1 - 2*p) + 2*p*x[i] - x[i]**2
        )
        dyc_dx[i] = (2*m / (1-p)**2) * (p - x[i])

# Local angle of camber line
theta = np.arctan(dyc_dx)

# Upper surface
xu = x - yt * np.sin(theta)
yu = yc + yt * np.cos(theta)

# Lower surface
xl = x + yt * np.sin(theta)
yl = yc - yt * np.cos(theta)

# Complete airfoil perimeter:
# TE upper -> LE -> TE lower
x_airfoil = np.concatenate((xu[::-1], xl[1:]))
y_airfoil = np.concatenate((yu[::-1], yl[1:]))

# Force exact closure at trailing edge
x_airfoil[-1] = x_airfoil[0]
y_airfoil[-1] = y_airfoil[0]

# Discovery: mm, with z = 0
airfoil_data = pd.DataFrame({
    "z": np.zeros(len(x_airfoil), dtype=int),
    "x": x_airfoil * 1000,
    "y": y_airfoil * 1000
})

airfoil_data.to_csv(
    "naca2412.txt",
    index=False,
    header=False
)

print("File naca2412.txt created.")
plt.plot(x_airfoil, y_airfoil)
plt.axis("equal")
plt.show
