import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def calculate_height_over_time(a, b, c, d, t):
    """returns the y value of the function for the input t"""
    return a * np.sin((b * t) - c) + d


# create plots to graph on
fig, ax = plt.subplots()
# kinda unnecessary, but I assigned the numpy.pi value to its own variable
pi = np.pi

# defining the period of the function
period = 5.0

# defining the diameter of the ferris wheel
diameter = 40.0
# defining the height above the ground of the loading platform
height_over_ground = 3.0

# determining the amplitude as half the diameter of the ferris wheel
amplitude = diameter / 2.0
vertical_shift = amplitude + height_over_ground

# not currently used
phase_shift = -(3.0 * pi / 2.0) / ((2.0 * pi) / period)

# assigning values to the familiar coefficient variable names of a periodic
# function in standard form
A = amplitude
B = (2.0 * pi) / period
C = -(3 * pi) / 2  # radians
D = vertical_shift

# list variables to hold all the values of x and y (t, and h(t))
xs = []
ys = []

# for loop to provide the function with many inputs 't' to the function h(t)
for i in np.arange(0, 101, 0.1):
    h_of_t = calculate_height_over_time(A, B, C, D, i)
    # append values to the lists defined above
    xs.append(i)
    ys.append(h_of_t)
    # print to console for debugging
    print("t = " + str(i))
    print("h(t) = " + str(calculate_height_over_time(A, B, C, D, i)))

# setting labels on the plot
ax.set_xlabel("time in minutes")
ax.set_ylabel("height in meters")
ax.set_title("height of a person on a ferris wheel")
ax.plot(xs, ys)

# setting plot formatting
ax.set_xticks(np.arange(0, 100, 5))
ax.set_yticks(np.arange(0, 50, 2))
# adding an annotation to point out the start and end of a period
ax.annotate('p1', xy=(0, 1), xytext=(3, 1.5),
            xycoords='data', textcoords='offset points')
ax.annotate('p2', xy=(10, 1), xytext=(3, 1.5),
            xycoords='data', textcoords='offset points')

# generates the resulting plot
plt.show()
