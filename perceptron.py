import matplotlib.pyplot as plt
import random
import sys

MAX=100
MIN=0
POINT_NUM=100
step=1

class Point:
    def __init__(self):
        self.x = random.randint(MIN, MAX)
        self.y = random.randint(MIN, MAX)

        if self.x > self.y:
            self.label = 1
            self.color = 'b'
        else:
            self.label = -1
            self.color = 'r'
class Line:
    def __init__(self):
        self.x1 = random.randint(MIN, MAX)
        self.x2 = random.randint(MIN, MAX)
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



plt.figure()
all_point = []
for idx in range(POINT_NUM):
    p = Point()
    plt.plot(p.x, p.y, p.color + 'o', label="point")
    all_point.append(p)
l = Line()
plt.plot(l.x, l.y, 'g-', linewidth=1)

Flag = True
while True:
    Flag = True
    for p in all_point:
        if l.sign(p) <= 0:
            l.w1 +=  step * p.label * p.x
            l.w2 += step * p.label * p.y
            l.b += step * p.label
            Flag = False
    if Flag:
        break
    l.update()
    plt.plot(l.x, l.y, 'y--', linewidth=1)
plt.plot(l.x, l.y, 'p-', linewidth=1)
plt.show()


