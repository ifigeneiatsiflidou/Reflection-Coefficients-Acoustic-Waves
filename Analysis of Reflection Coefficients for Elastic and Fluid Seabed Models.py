#External Imports
import numpy as np
import matplotlib.pyplot as plt

# Given parameters
c1 = 1500           # Speed of sound in water (m/s)
rho1 = 1000         # Density of water (kg/m^3)
c2_p = 1800         # Speed of compressional waves in the seabed (m/s)
c2_s = 1000         # Speed of shear waves in the seabed (m/s)
rho2 = 1200         # Density of the seabed (kg/m^3)
f = 500             # Frequency (Hz)

# Create array of various incidence angles
angles = np.linspace(0, 89, 1000)   # From 0 to 89 degrees
theta_1 = np.radians(angles)       # Convert from degrees to radians

# Find critical angle
theta_cr_p = np.arcsin(c1/c2_p)     # Critical angle for compressional waves (rad)
theta_cr_p = np.degrees(theta_cr_p) # Convert to degrees
print('Critical angle (degrees) for compressional waves:', theta_cr_p)

# Sine and cosine of incidence angles
sin_1 = np.sin(theta_1)
cos_1 = np.cos(theta_1)

# Convert to complex numbers
sin_1 = sin_1 + 0j
cos_1 = cos_1 + 0j

# Snell's Law
cos_2_p = np.sqrt(1 - ((c2_p * sin_1)/c1)**2)
cos_2_s = np.sqrt(1 - ((c2_s * sin_1)/c1)**2)

# Characteristic impedance
Z_1 = rho1 * c1
Z_2_p = rho2 * c2_p
Z_2_s = rho2 * c2_s

# Reflection coefficient for semi-infinite elastic material
R_p = (Z_2_p * cos_1 - Z_1 * cos_2_p) / (Z_2_p * cos_1 + Z_1 * cos_2_p)
R_s = (Z_2_s * cos_1 - Z_1 * cos_2_s) / (Z_2_s * cos_1 + Z_1 * cos_2_s)

# Magnitude and phase of reflection coefficient
R_p_magnitude = np.abs(R_p)
R_p_phase = np.angle(R_p, deg=True)
R_s_magnitude = np.abs(R_s)
R_s_phase = np.angle(R_s, deg=True)

# -- Plots for elastic material --

# Semi-infinite material - Compressional waves
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(angles, R_p_magnitude)
plt.title("Magnitude of Reflection Coefficient (Compressional - Elastic)")
plt.ylabel("Magnitude")
plt.grid()
plt.ylim([-0.1, 1])
plt.xlim([-5, 95])

plt.subplot(2, 1, 2)
plt.plot(angles, R_p_phase)
plt.xlabel("Incidence Angle (Degrees)")
plt.ylabel("Phase (Degrees)")
plt.grid()
plt.ylim([-200, 20])
plt.xlim([-5, 95])

# Semi-infinite material - Shear waves
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(angles, R_s_magnitude)
plt.title("Magnitude of Reflection Coefficient (Shear - Elastic)")
plt.ylabel("Magnitude")
plt.grid()
plt.ylim([-0.1, 1])
plt.xlim([-5, 95])

plt.subplot(2, 1, 2)
plt.plot(angles, R_s_phase)
plt.xlabel("Incidence Angle (Degrees)")
plt.ylabel("Phase (Degrees)")
plt.grid()
plt.xlim([-5, 95])

# Reflection coefficient for fluid material
R_fluid = (Z_2_p - Z_1) / (Z_2_p + Z_1)
R_fluid_magnitude = np.abs(R_fluid)
R_fluid_phase = np.angle(R_fluid, deg=True)

# -- Plot (only for compressional waves) --
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(angles, [R_fluid_magnitude]*len(angles))
plt.title("Magnitude of Reflection Coefficient (Compressional - Fluid)")
plt.ylabel("Magnitude")
plt.grid()
plt.ylim([-0.1, 1])

plt.subplot(2, 1, 2)
plt.plot(angles, [R_fluid_phase]*len(angles))
plt.xlabel("Incidence Angle (Degrees)")
plt.ylabel("Phase (Degrees)")
plt.grid()
plt.ylim([-200, 20])

plt.show()