import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Read data from file
data = np.loadtxt('cfd.txt')

# Separate data into Mach numbers and Cd values
Mach_numbers = data[:, 0]
Cd_values = data[:, 1]

# Create a linear interpolation function
CdFun = interpolate.interp1d(Mach_numbers, Cd_values, kind='linear', fill_value="extrapolate")

# Plot the function for values of 0, 0.1, 0.2, ..., 1.4, 1.5
x = np.arange(0, 1.6, 0.2)
y = CdFun(x)

plt.plot(x, y, '-o')  # 'o' specifies small circles as markers
plt.xlabel('Mach Number')
plt.ylabel('Cd Value')
plt.title('Linear Interpolation of Cd vs. Mach Number')
plt.grid(True)
plt.show()
