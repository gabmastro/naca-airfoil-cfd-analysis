import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "alpha_deg": [0, 4, 8, 12, 14, 16, 17, 18],
    "Cl": [0.2174, 0.6176, 1.0246, 1.3415, 1.4651, 1.5241, 1.4888, 1.4175],
    "Cd": [0.0100, 0.0125, 0.0196, 0.0334, 0.0441, 0.0605, 0.074805, 0.096064]
})
df["Cl_over_Cd"] = df["Cl"] / df["Cd"]

# CL vs alpha
plt.figure()
plt.plot(df["alpha_deg"], df["Cl"], marker="o")
plt.xlabel("Angle of attack α [deg]")
plt.ylabel("Lift coefficient Cl [-]")
plt.title("NACA 2412 - Lift curve")
plt.grid(True)
plt.tight_layout()
plt.show()

# CD vs alpha
plt.figure()
plt.plot(df["alpha_deg"], df["Cd"], marker="o")
plt.xlabel("Angle of attack α [deg]")
plt.ylabel("Drag coefficient Cd [-]")
plt.title("NACA 2412 - Drag coefficient vs angle of attack")
plt.grid(True)
plt.tight_layout()
plt.show()

# Polar
plt.figure()
plt.plot(df["Cd"], df["Cl"], marker="o")
plt.xlabel("Drag coefficient Cd [-]")
plt.ylabel("Lift coefficient Cl [-]")
plt.title("NACA 2412 - Drag polar")
plt.grid(True)
plt.tight_layout()
plt.show()

# Efficiency
plt.figure()
plt.plot(df["alpha_deg"], df["Cl_over_Cd"], marker="o")
plt.xlabel("Angle of attack α [deg]")
plt.ylabel("Cl/Cd [-]")
plt.title("NACA 2412 - Aerodynamic efficiency")
plt.grid(True)
plt.tight_layout()
plt.show()

df

# %%
