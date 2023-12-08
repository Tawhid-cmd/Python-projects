import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter


def plot_parabola(a, x_range):
    # Calculate y-values based on the equation x = sqrt(4ay)
    x_values = np.linspace(-x_range, x_range, 1000)
    y_values_positive = (x_values ** 2) / (4 * a)
    y_values_negative = -(x_values ** 2) / (4 * a)

    # Plotting the parabola
    plt.figure(figsize=(8, 6))
    plt.title('Parabola: x = ±sqrt(4ay)')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    plt.plot(x_values, y_values_positive, label='Parabola (+)', color='blue')
    plt.plot(x_values, y_values_negative, label='Parabola (-)', color='red')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.legend()
    plt.grid()
    plt.show()


# Get user input for 'a' and the range of x-values
a_value = float(input("Enter the value of 'a' (non-zero): "))
x_range_value = float(input("Enter the range of x-values (positive number): "))

if a_value != 0 and x_range_value > 0:
    plot_parabola(a_value, x_range_value)
elif a_value == 0:
    print("Please enter a non-zero value for 'a'.")
else:
    print("Please enter a positive number for the range of x-values.")