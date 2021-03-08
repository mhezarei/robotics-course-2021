import numpy as np
import math
import sympy as sym
from sympy.solvers import solve
import part_one

CONVERSION = math.pi / 180
NUM_ITERATIONS = 100

def backward(constants: list) -> dict:
    x_dot_i, y_dot_i, theta_dot_i, r, d, theta = constants

    inertial_frame_loc = [x_dot_i, y_dot_i, theta_dot_i]

    r_theta = [[np.cos(theta), np.sin(theta), 0],
               [-np.sin(theta), np.cos(theta), 0],
               [0, 0, 1]]

    
    robot_frame_loc = np.matmul(r_theta, inertial_frame_loc)

    x_dot_r, y_dot_r, theta_dot_r = robot_frame_loc

    sym.init_printing()
    
    a, b = sym.symbols('a,b')

    eq_1 = sym.Eq((a + b) * r/2, x_dot_r)
    eq_2 = sym.Eq((a - b) * r/(2*d), theta_dot_r * CONVERSION)

    # print(solve([eq_1, eq_2], (a,b)))
    res = solve([eq_1, eq_2], (a,b))
    phi_dot_1, phi_dot_2 = res.values()

    return [phi_dot_1, phi_dot_2]


def prompt():
    print("Please enter the following information (in order and "
          "space-separated):\n"
          "1. Linear Velocity of x axis in cm/s\n"
          "2. Linear Velocity of y axis in cm/s\n"
          "3. Angular Velocity of the chassis in deg/s\n"
          "4. Radius of the wheels in cm\n"
          "5. Distance between the two wheels in cm\n"
          "6. Angle around the inertial frame in deg")
    # enter this for now 1 1 1 2.5 20 45
    args = list(map(float, input().split()))
    return args



def main():
    args = prompt()
    constants = args
    
    angolar_velocity_of_wheels = backward(constants)
    print(angolar_velocity_of_wheels)


if __name__ == '__main__':
    main()

