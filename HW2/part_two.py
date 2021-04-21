from math import sin, cos

import matplotlib.pyplot as plt
import numpy as np


def polar_to_cartesian(theta: list, rho: list):
    assert len(theta) == len(rho), "The length does not match!"
    x = []
    y = []
    for i in range(len(theta)):
        x.append(rho[i] * cos(theta[i]))
        y.append(rho[i] * sin(theta[i]))
    
    return x, y


def split_merge_helper(points, d_thresh=1):
    if len(points) < 3:
        return [points]
    
    s = points.copy()
    first = s[0]
    last = s[-1]
    distances = [np.abs(np.cross(last - first, p - first) /
                        np.linalg.norm(last - first)) for p in s]
    max_d, max_i = max(distances), distances.index(max(distances))
    
    if max_d < d_thresh:
        ret = [points]
    else:
        res1 = split_merge_helper(points[:max_i + 1])
        res2 = split_merge_helper(points[max_i:])
        ret = res1 + res2
    
    return ret


def line_length(p1, p2):
    return np.sqrt(abs(p1[0] - p2[0]) * abs(p1[0] - p2[0])
                   + abs(p1[1] - p2[1]) * abs(p1[1] - p2[1]))


def split_merge(theta: list, rho: list):
    x, y = polar_to_cartesian(theta, rho)
    points = [np.array([x[i], y[i]]) for i in range(len(x))]
    res = split_merge_helper(points)
    for r in res:
        plt.scatter(np.array(r)[:, 0], np.array(r)[:, 1])
        first = r[0]
        last = r[-1]
        plt.plot([first[0], last[0]], [first[1], last[1]])
    plt.show()
    
    # merging
    final = []
    for i in range(0, len(res) - 1, 2):
        d1 = res[i]
        d2 = res[i + 1]
        e1 = sum([np.abs(np.cross(d1[-1] - d1[0], p - d1[0]) /
                         np.linalg.norm(d1[-1] - d1[0])) for p in
                  d1]) / line_length(d1[0], d1[-1])
        e2 = sum([np.abs(np.cross(d1[-1] - d1[0], p - d1[0]) /
                         np.linalg.norm(d1[-1] - d1[0])) for p in
                  d2]) / line_length(d2[0], d2[-1])
        e3 = sum([np.abs(np.cross(d2[-1] - d1[0], p - d1[0]) /
                         np.linalg.norm(d2[-1] - d1[0])) for p in
                  d1 + d2]) / line_length(d1[0], d2[-1])
        
        if e1 + e2 > e3:
            final.append(d1 + d2)
        else:
            final.append(d1)
            final.append(d2)
    
    for r in final:
        plt.scatter(np.array(r)[:, 0], np.array(r)[:, 1])
        first = r[0]
        last = r[-1]
        plt.plot([first[0], last[0]], [first[1], last[1]])
    plt.show()


def main():
    with open("lidar_scan_theta.txt") as f:
        data = f.readlines()
        theta = list(map(float, data))
    
    with open("lidar_scan_rho.txt") as f:
        data = f.readlines()
        rho = list(map(float, data))
    
    split_merge(theta, rho)


if __name__ == '__main__':
    main()
