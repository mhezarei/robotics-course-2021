import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


CONVERSION = math.pi / 180
NUM_ITERATIONS = 10000


def forward(constants: list, location: list) -> dict:
    phi_x, phi_y, r, d, f = constants
    x, y, theta = location
    
    dt = 1 / f
    theta_rad = CONVERSION * theta
    
    x_r = r * (phi_y * CONVERSION + phi_x * CONVERSION) / 2
    y_r = 0
    theta_dot = r * (phi_y - phi_x) / d
    sai_r = [x_r, y_r, theta_dot]
    
    r_minus_theta = [
        [math.cos(-theta_rad), math.sin(-theta_rad), 0],
        [-math.sin(-theta_rad), math.cos(-theta_rad), 0],
        [0, 0, 1],
    ]
    
    sai_i = np.matmul(r_minus_theta, sai_r)
    
    x_new = x + dt * sai_i[0]
    y_new = y + dt * sai_i[1]
    theta_new = theta + dt * sai_i[2]
    
    return {
        "new_loc": [x_new, y_new, theta_new],
        "sai_i": sai_i.tolist(),
        "sai_r": sai_r
    }


def prompt():
    # print("Please enter the following information (in order and "
    #       "space-separated):\n"
    #       "1. Angular Velocity of the left wheel (x) in deg/s\n"
    #       "2. Angular Velocity of the right wheel (y) in deg/s\n"
    #       "3. Radius of the wheels in cm\n"
    #       "4. Distance between the two wheels in cm\n"
    #       "5. Frequency of sampling in Hz\n"
    #       "6. Initial locations of the robot (x: cm, y: cm, theta: deg)")
    # enter this for now 7 -5 2.5 20 10 1 1 30
    # args = list(map(float, input().split()))
    args = [10, 5, 2, 20, 10, 0, 0, 30]
    return args


def plot(history: list, freq: int):
    timestamps = [i / freq for i in range(NUM_ITERATIONS + 1)]
    
    # plotting robot path
    x = [record["new_loc"][0] for record in history]
    y = [record["new_loc"][1] for record in history]
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='X (cm)', ylabel='Y (cm)', title='Robot Path')
    ax.grid()
    plt.show()
    
    # plotting x-hat and y-hat in sai I vs time
    # x = [record["sai_i"][0] for record in history]
    # fig, ax = plt.subplots()
    # ax.plot(timestamps, x)
    # ax.set(xlabel='time (s)', ylabel='X-hat (cm/s)',
    #        title='Motion Components of Inertial Frame')
    # ax.grid()
    # plt.show()

    # y = [record["sai_i"][1] for record in history]
    # fig, ax = plt.subplots()
    # ax.plot(timestamps, y)
    # ax.set(xlabel='time (s)', ylabel='Y-hat (cm/s)',
    #        title='Motion Components of Inertial Frame')
    # ax.grid()
    # plt.show()
    
    # plotting Xr and theta in sai R vs time
    # v = [record["sai_r"][0] for record in history]
    # fig, ax = plt.subplots()
    # ax.plot(timestamps, v)
    # ax.set(xlabel='time (s)', ylabel='Linear Velocity (cm/s)',
    #        title='Linear Velocity vs. Time')
    # ax.grid()
    # plt.show()

    # w = [record["sai_r"][2] for record in history]
    # fig, ax = plt.subplots()
    # ax.plot(timestamps, w)
    # ax.set(xlabel='time (s)', ylabel='Angular Velocity (deg/s)',
    #        title='Angular Velocity vs. Time')
    # ax.grid()
    # plt.show()


def main():
    args = prompt()
    constants = args[:5]
    base_loc = args[5:]
    history = [
        # {"new_loc": base_loc, "sai_i": [0, 0, 0], "sai_r": [0, 0, 0]},
        forward(constants, base_loc),
    ]
    
    for i in range(NUM_ITERATIONS):
        history.append(forward(constants, history[-1]["new_loc"]))
    
    plot(history, args[4])


if __name__ == '__main__':
    main()
