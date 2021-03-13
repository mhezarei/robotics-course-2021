import math
import matplotlib.pyplot as plt
import sympy as sym
from sympy.solvers import solve

CONVERSION = math.pi / 180
NUM_ITERATIONS = 100


def backward_kinematics(constants: list) -> list:
    x_dot_r, y_dot_r, theta_dot_r, r, d, f = constants
    sym.init_printing()
    
    a, b = sym.symbols('a,b')
    
    eq_1 = sym.Eq((a + b) * r / 2, x_dot_r)
    eq_2 = sym.Eq((a - b) * r / (2 * d), theta_dot_r * CONVERSION)
    
    # print(solve([eq_1, eq_2], (a,b)))
    res = solve([eq_1, eq_2], (a, b))
    phi_dot_1, phi_dot_2 = res.values()
    
    return [phi_dot_1, phi_dot_2]


def prompt():
    print("Please enter the following information (in order and "
          "space-separated and in robot frame):\n"
          "1. Linear Velocity of x axis in cm/s\n"
          "2. Linear Velocity of y axis in cm/s\n"
          "3. Angular Velocity of the chassis in deg/s\n"
          "4. Radius of the wheels in cm\n"
          "5. Distance between the two wheels in cm\n"
          )
    # enter this for now 1.4 0 1 2.5 20 10
    
    # for first plot enter this: 1.4 0 0 2.5 20 10
    # for second plot enter this: 0 0 10 2.5 20 10
    
    args = list(map(float, input().split()))
    return args


def draw_plot(wheels_velocities: list):
    y1 = [wheels_velocities[0] for i in range(10)]
    y2 = [wheels_velocities[1] for i in range(10)]
    
    plt.figure(1)
    plt.subplot(211)
    plt.plot(y1)
    plt.ylabel("φ'1(rad/s)")
    plt.xlabel('time(s)')
    
    plt.subplot(212)
    plt.plot(y2)
    plt.ylabel("φ'2(rad/s)")
    plt.xlabel('time(s)')
    
    plt.show()


def main():
    args = prompt()
    constants = args
    
    wheels_velocities = backward_kinematics(constants)
    print(wheels_velocities)
    
    draw_plot(wheels_velocities)


if __name__ == '__main__':
    main()
