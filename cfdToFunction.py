import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Read data from file
data = np.loadtxt('cfd.txt')

# Separate data into Mach numbers and Cd values
Mach_numbers = data[:, 0]
Cd_values = data[:, 1]

# Input: Temperature [K], velocity [m/s]
# Output: Cd value
def CdFun(Temperature, velocity):
    Mach = velocity / np.sqrt(1.4 * 287.05 * Temperature)
    return interpolate.interp1d(Mach_numbers, Cd_values, kind='linear', fill_value="extrapolate")(Mach)
