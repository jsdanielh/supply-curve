import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data points
years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031,
                 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047])
values = np.array([2520000000, 4696558082.581287, 6616763076.0469, 8310808020.879533, 9805329847.913223, 11123828213.787481, 12287035006.33263, 13313240329.9377, 14218580096.64377, 15017289745.02168, 15721928076.255806, 16343574727.017124, 16892004384.151829, 17375840480.51872, 17802690788.673378,
                  18179267044.432022, 18511490481.29523, 18804584935.110928, 19063158982.952858, 19291278407.755295, 19492530128.127415, 19670078598.575684, 19826715566.945854, 19964903971.488857, 20086816667.7617, 20194370594.31337, 20289256914.362705, 20372967607.419846, 20446818928.962532, 20511972107.06315])

# Define the exponential model function

# r = 2520000000 + (y / k * (1.0 - e^(-z*x*31536000000)))


def exponential_model(t, a, b):
    return 2520000000 + (a / b * (1 - np.power(2, -b * (t - 2018)*31536000000)))


# Fit the exponential model to the data
params, covariance = curve_fit(
    exponential_model, years, values, p0=(1e9, 1e-10))

# Extract the parameters
a, b = params

# Generate model values for the given years
fitted_values = exponential_model(years, a, b)

# Plot the data and the fitted model
plt.figure(figsize=(10, 6))
plt.scatter(years, values, label='Data Points', color='red')
plt.plot(years, fitted_values, label='Fitted Exponential Model', color='blue')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Exponential Model Fit to Data')
plt.legend()
plt.grid(True)
plt.show()

# Print the parameters
print(f"Fitted parameters: a = {a}, b = {b}")
