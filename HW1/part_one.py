import math
import numpy as np


CONVERSION = math.pi / 180
NUM_ITERATIONS = 100


def forward(constants: list, location: list) -> list:
    phi_x, phi_y, r, d, f = constants
    x, y, theta = location
    
    dt = 1 / f
    theta_rad = CONVERSION * theta
    
    x_r = r * (phi_y * CONVERSION + phi_x * CONVERSION) / 2
    y_r = 0
    theta_dot = r * (phi_y - phi_x) / d
    sai_r = [x_r, y_r, theta_dot]
    
    r_minus_theta = [
        [np.cos(-theta_rad), np.sin(-theta_rad), 0],
        [-np.sin(-theta_rad), np.cos(-theta_rad), 0],
        [0, 0, 1],
    ]
    
    sai_i = np.matmul(r_minus_theta, sai_r)
    
    x_new = x + dt * sai_i[0]
    y_new = y + dt * sai_i[1]
    theta_new = theta + dt * sai_i[2]
    
    return [x_new, y_new, theta_new]


def prompt():
    print("Please enter the following information (in order and "
          "space-separated):\n"
          "1. Angular Velocity of the left wheel (x) in deg/s\n"
          "2. Angular Velocity of the right wheel (y) in deg/s\n"
          "3. Radius of the wheels in cm\n"
          "4. Distance between the two wheels in cm\n"
          "5. Frequency of sampling in Hz\n"
          "6. Initial locations of the robot (x: cm, y: cm, theta: deg)")
    # enter this for now 7 -5 2.5 20 10 1 1 30
    args = list(map(float, input().split()))
    return args


def main():
    args = prompt()
    constants = args[:5]
    base_loc = args[5:]
    loc_update = forward(constants, base_loc)
    for i in range(NUM_ITERATIONS):
        loc_update = forward(constants, loc_update)
        print(loc_update)


if __name__ == '__main__':
    main()
