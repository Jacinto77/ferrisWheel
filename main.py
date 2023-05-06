import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def calculate_height_over_time(a, b, c, d, t):
    """returns the y value of the function for the input t"""
    return a * np.sin((b * t) - c) + d


def get_dimensions_of_wheel():
    diameter_of_wheel = float(input("Enter the diameter of the ferris wheel: "))
    rotational_speed = float(input("Enter the time it takes for one full revolution: "))
    starting_position = float(input("Enter the starting position "
                                    "of the wheel (degrees): "))
    height_over_ground = float(input("Enter the starting height of the person: "))

    print(diameter_of_wheel, rotational_speed, starting_position, height_over_ground)

    return [diameter_of_wheel, rotational_speed, starting_position, height_over_ground]


def calculate_coefficients(diameter_of_wheel, rotational_speed,
                           starting_position, height_over_ground):
    a = find_a(diameter_of_wheel)
    b = find_b(rotational_speed)
    c = find_c(starting_position)
    d = find_d(a, height_over_ground)

    print(a, b, c, d)

    return [a, b, c, d]


def convert_degrees_to_radians(degrees):
    return degrees * np.pi / 180


def find_a(diameter_of_wheel):
    return diameter_of_wheel / 2.0


def find_b(rotational_speed):
    return 2 * np.pi / rotational_speed


def find_c(starting_position):
    return convert_degrees_to_radians(starting_position) * -1


def find_d(amplitude, height_over_ground):
    return amplitude + height_over_ground


# create plots to graph on
fig, ax = plt.subplots()
# kinda unnecessary, but I assigned the numpy.pi value to its own variable
pi = np.pi

# # defining the period of the function
# period = 5.0
#
# # defining the diameter of the ferris wheel
# diameter = 40.0
# # defining the height above the ground of the loading platform
# height_over_ground = 3.0
#
# # determining the amplitude as half the diameter of the ferris wheel
# amplitude = diameter / 2.0
# vertical_shift = amplitude + height_over_ground
#
# # not currently used
# phase_shift = -(3.0 * pi / 2.0) / ((2.0 * pi) / period)


# assigning values to the familiar coefficient variable names of a periodic
# function in standard form
# A = amplitude
# B = (2.0 * pi) / period
# C = -(3 * pi) / 2  # radians
# D = vertical_shift

# list variables to hold all the values of x and y (t, and h(t))
xs = []
ys = []

diameter, period, start_position, height_above_ground = get_dimensions_of_wheel()
A, B, C, D = calculate_coefficients(diameter, period, start_position, height_above_ground)

sample_size = 101

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
ax.set_xticks(np.arange(0, sample_size, 5))     # setting x-axis to be the sample size
ax.set_yticks(np.arange(0, diameter + 10, 2))   # set y-axis to be the
# diam. of wheel plus 10

# adding an annotation to point out the start and end of a period
# ax.annotate('p1', xy=(int(xs[0]), int(ys[0])), xytext=(3, 1.5),
#             xycoords='data', textcoords='offset points')
# ax.annotate('p2', xy=(int(xs[period] + 1), int(ys[period + 1])), xytext=(3, 1.5),
#             xycoords='data', textcoords='offset points')

# generates the resulting plot
plt.show()
