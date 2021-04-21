import numpy as np
import matplotlib.pyplot as plt


file = open("Hw_Accel_Voltage_Data.txt", 'r')
records = file.read().splitlines()


ZERO_G_VOLTAGE = 2.375
SENSITIVITY = 0.5                       # 500 mv/g = 0.5 v/g
G_VALUE = 9.8                           # g = 9.8 m/s^2

delta_x = []
delta_v = []
delta_a = []
prev_x = 0
prev_v = 0
a0 = 0

delta_x.append(prev_x)
delta_v.append(prev_v)
delta_a.append(a0)

def calculate_accel(v):
    """
    Calculates accel based on current voltage and input sensitivity.

    Parameters
    ----------
    v: sensor's output voltage, float type

    Returns
    -------
    float: returns acceleration in current time interval.
    """

    accel = (v - ZERO_G_VOLTAGE) / SENSITIVITY
    accel = accel * G_VALUE
    return accel


def calculate_next_velocity(prev_v, accel, time_interval=0.1):

    velocity = accel * time_interval / 2 + prev_v
    return velocity

def calculate_next_x(prev_v, accel, prev_x, time_interval=0.1):

    x = accel * (time_interval ** 2) / 2 + prev_v * time_interval + prev_x
    return x


for index, record in enumerate(records):
    voltage = float(record)
    accel = calculate_accel(voltage)

    x0 = delta_x[index]
    v0 = delta_v[index]
    x1 = calculate_next_x(v0, accel, x0)
    v1 = calculate_next_velocity(v0, accel)

    delta_x.append(x1)
    delta_v.append(v1)
    delta_a.append(accel)
    print('Iteration number: ', index)
    print('accel: ', accel)
    print('next v: ', v1)
    print('next x: ', x1)
    print('---------------------------------------------------------------------')


# Plot
x_axis = np.linspace(0, 30, 3002)
y1 = np.array(delta_x)
y2 = np.array(delta_v)
y3 = np.array(delta_a)

fig, axes = plt.subplots(3)
fig.suptitle('Changes of motion variables over time')

axes[0].plot(x_axis, y1, label='Δx')
axes[1].plot(x_axis, y2, '-r', label='Δv')
axes[2].plot(x_axis, y3, '-g', label='Δa')

for a in axes:
    a.grid()
    a.legend()

plt.show()
    

