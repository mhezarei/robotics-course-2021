from math import sin, cos

import matplotlib.pyplot as plt
import numpy as np


# def radian


def polar_to_cartesian(theta: list, rho: list):
    assert len(theta) == len(rho), "The length does not match!"
    x = []
    y = []
    for i in range(len(theta)):
        x.append(rho[i] * cos(theta[i]))
        y.append(rho[i] * sin(theta[i]))
    
    return x, y


def split_merge_helper(points, d_thresh=1):
    plt.scatter(np.array(points)[:, 0], np.array(points)[:, 1])
    s = points.copy()
    first = s[0]
    last = s[-1]
    distances = [np.abs(np.cross(last - first, p - first) /
                        np.linalg.norm(last - first)) for p in s]
    max_d, max_i = max(distances), distances.index(max(distances))
    
    if max_d < d_thresh:
        plt.plot([first[0], last[0]], [first[1], last[1]])
        ret = [first, last]
    else:
        res1 = split_merge_helper(points[:max_i + 1])
        res2 = split_merge_helper(points[max_i:])
        ret = [res1, res2]
    
    return ret


def split_merge(theta: list, rho: list):
    x, y = polar_to_cartesian(theta, rho)
    
    # second
    points = [np.array([x[i], y[i]]) for i in range(len(x))]
    plt.scatter(x, y)
    res = split_merge_helper(points)
    print(np.array(res).shape)
    # plt.scatter(np.array(res)[:, 0], np.array(res)[:, 1])
    plt.show()
    # for h in res:
    #     print(h)
    #     plt.scatter(np.array(h)[:, 0], np.array(h)[:, 1])
    # plt.show()
    
    # first
    # hist = []
    # d_thresh = 7
    # points = [[np.array([x[i], y[i]]) for i in range(len(x))]]
    # i = 0
    # while True:
    #     if i == len(points):
    #         break
    #     print(np.array(points).shape)
    #     print(points)
    #     s = points[i]
    #     first = s[0]
    #     last = s[-1]
    #     # if first[0] == last[0] and first[1] == last[1]:
    #     #     i += 1
    #     #     continue
    #     distances = [np.abs(np.cross(last - first, p - first) /
    #                         np.linalg.norm(last - first)) for p in s]
    #     max_d, max_i = max(distances), distances.index(max(distances))
    #     if max_d < d_thresh:
    #         hist.append(s)
    #         i += 1
    #         continue
    #
    #     print(len(s), max_i)
    #     points.remove(s)
    #     points.insert(i, s[:max_i + 1])
    #     points.insert(i + 1, s[max_i:])
    #
    #     print("asdf", max_d, max_i, s[max_i])
    #     plt.scatter(x, y)
    #     print(s[max_i])
    #     plt.scatter(np.array(s)[:, 0], np.array(s)[:, 1])
    #     plt.scatter(s[max_i][0], s[max_i][1])
    #     plt.plot([first[0], last[0]], [first[1], last[1]], 'r-')
    #     plt.show()
    #
    # for h in hist:
    #     plt.scatter(np.array(h)[:, 0], np.array(h)[:, 1])
    # plt.show()


def main():
    with open("lidar_scan_theta.txt") as f:
        data = f.readlines()
        theta = list(map(float, data))
    
    with open("lidar_scan_rho.txt") as f:
        data = f.readlines()
        rho = list(map(float, data))
    
    # theta.sort()
    # rho = [x for _, x in sorted(zip(theta, rho))]
    split_merge(theta, rho)
    print(theta)
    print(rho)


if __name__ == '__main__':
    main()
