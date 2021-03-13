import math
import matplotlib.pyplot as plt
from HW1.part_one import forward
from HW1.part_two import backward_kinematics


def prompt():
    # print("Please enter the following information (in order and "
    #       "space-separated):\n"
    #       "1. Radius of the wheels in cm\n"
    #       "2. Distance between the two wheels in cm\n"
    #       "3. Frequency of sampling in Hz\n")
    # constants = list(map(float, input().split()))
    constants = [1, 10, 100]
    return constants


def calc_polar(loc: list, goal: list) -> list:
    delta_x = goal[0] - loc[0]
    delta_y = goal[1] - loc[1]
    p = math.sqrt(delta_x * delta_x + delta_y * delta_y)
    a = math.atan2(delta_y, delta_x) * 180 / math.pi - loc[2]
    b = -loc[2] - a
    return [p, a, b]


def calc_v_omega(p, a, b, kp, ka, kb):
    v = kp * p
    w = ka * a + kb * b
    return v, w


def plot(history):
    x = [record[0] for record in history]
    y = [record[1] for record in history]
    fig, ax = plt.subplots()
    fig.set_size_inches(6.4, 6)
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])
    ax.xaxis.set_ticks(range(-6, 6))
    ax.yaxis.set_ticks(range(-6, 6))
    ax.scatter(x, y, s=2)
    ax.set(xlabel='X (cm)', ylabel='Y (cm)', title='Robot Trajectory')
    ax.grid()

    circle1 = plt.Circle((0, 0), 5, color='r', fill=False)
    plt.gca().add_patch(circle1)
    plt.show()


def calc_dist(loc, goal):
    delta_x = goal[0] - loc[0]
    delta_y = goal[1] - loc[1]
    p = math.sqrt(delta_x * delta_x + delta_y * delta_y)
    return p


def computation(goal: list, base: list):
    constants = prompt()
    kp, ka, kb = [3, 8, -2]
    step_history = [base]
    for _ in range(300):
        p, a, b = calc_polar(step_history[-1], goal)
        v, w = calc_v_omega(p, a, b, kp, ka, kb)
        phi_y, phi_x = backward_kinematics([v, 0, w] + constants)
        phi_x = phi_x * 180 / math.pi
        phi_y = phi_y * 180 / math.pi
        step_history.append(
            forward([phi_x, phi_y] + constants, step_history[-1])["new_loc"])
    
    # step_history.remove([0, 0, 90])
    return step_history


def main():
    # first scenario
    # goals = [
    #     # [-5, 0, 0],
    #     [5, 0, 0],
    #     [0, 5, 0],
    #     [0, -5, 0],
    #     [3, 4, 0],
    #     [4, 3, 0],
    #     [-3, 4, 0],
    #     [-4, 3, 0],
    #     [-3, -4, 0],
    #     [-4, -3, 0],
    #     [3, -4, 0],
    #     [4, -3, 0],
    # ]
    # bases = [
    #     # [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    #     [0, 0, 90],
    # ]
    
    # second scenario
    bases = [
        [-5, 0, 0],
        # [5, 0, 0],
        [0, 5, 0],
        [0, -5, 0],
        [3, 4, 0],
        [4, 3, 0],
        [-3, 4, 0],
        [-4, 3, 0],
        [-3, -4, 0],
        [-4, -3, 0],
        [3, -4, 0],
        [4, -3, 0],
    ]
    goals = [
        [0, 0, 0],
        # [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    total_history = []
    
    for i, goal in enumerate(goals):
        total_history += computation(goal, bases[i])
        plot(total_history)


if __name__ == '__main__':
    main()
