import matplotlib.pyplot as plt
import numpy
import random
import sys

MAX=100
MIN=0
POINT_NUM=20
step=0.01
C = 0.1

class Point:
    def __init__(self):
        self.x = random.uniform(MIN, MAX)
        self.y = random.uniform(MIN, MAX)

        if self.x > self.y:
            self.label = 1
            self.color = 'b'
        else:
            self.label = -1
            self.color = 'r'
class Point2:
    def __init__(self):
        self.x = random.randint(MIN, MAX)
        if self.x > MAX // 2:
            self.y = random.randint(0, MAX // 4)
        else:
            self.y = random.randint(MAX * 2 // 4, MAX)

        if self.x > self.y:
            self.label = 1
            self.color = 'b'
        else:
            self.label = -1
            self.color = 'r'

class Point3:
    def __init__(self):
        self.x = random.gauss(50, 10)
        self.y = random.gauss(50, 10)

        self.label = -1
        self.color = 'r'

class Point4:
    def __init__(self):
        self.x = random.gauss(90, 10)
        self.y = random.gauss(90, 10)

        self.label = 1
        self.color = 'b'
class Line:
    def __init__(self):
        self.x1 = random.randint(MIN, MAX//2)
        self.x2 = random.randint(MAX//2, MAX)
        self.y1 = 0
        self.y2 = 100

        self.x = [self.x1, self.x2]
        self.y = [self.y1, self.y2]

        self.w1 = -(self.y2 - self.y1) / (self.x2 - self.x1)
        self.w2 = 1
        self.b = -(self.w1 * self.x1) + self.w2 * self.y1

    def sign(self, point):
        return point.label * (self.w1 * point.x + self.w2 * point.y + self.b)

    def update(self):
        self.x1 = -self.b / self.w1
        self.x2 = (-self.b - self.w2 * self.y2) / self.w1
        self.x = [self.x1, self.x2]
        self.y = [self.y1, self.y2]


def initialPoint():
    plt.figure()
    all_point = []
    for idx in range(POINT_NUM):
        p = Point3()
        plt.plot(p.x, p.y, p.color + 'o', label="point")
        all_point.append(p)

    for idx in range(POINT_NUM):
        p = Point4()
        plt.plot(p.x, p.y, p.color + 'o', label="point")
        all_point.append(p)
    return all_point

def preceptron_base_dis(all_points):
    line = Line()
    plt.plot(line.x, line.y, 'g--', linewidth=1)
    Flag = True
    while True:
        Flag = True
        for point in all_points:
            if line.sign(point) < 1:
                line.w1 = (1 - step) * line.w1 + step * C * point.label * point.x
                line.w2 = (1 - step) * line.w2 + step * C * point.label * point.y
                line.b = line.b + step * C *  point.label
                Flag = False
        if Flag:
            break
        line.update()
        #plt.plot(l.x, l.y, 'y--', linewidth=1)
    plt.plot(line.x, line.y, '.-', linewidth=1)
    plt.show()

def preceptron(all_points):
    line = Line()
    plt.plot(line.x, line.y, 'g--', linewidth=1)
    Flag = True
    while True:
        Flag = True
        for point in all_points:
            if line.sign(point) <= 0:
                line.w1 +=  step * point.label * point.x
                line.w2 += step * point.label * point.y
                line.b += step * point.label
                Flag = False
        if Flag:
            break
        line.update()
        #plt.plot(line.x, line.y, 'y--', linewidth=1)
    plt.plot(line.x, line.y, 'o-', linewidth=1)
    plt.show()

all_points = initialPoint()
preceptron_base_dis(all_points)
