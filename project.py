import numpy as np
import matplotlib.pyplot as plt

N = 10000
r = 0

points = []

circle = lambda x : np.sqrt(1 - x*x)
x = np.linspace(0,1,101)
y = circle(x)


for k in range(N):
    i = np.random.random()
    j = np.random.random()


    p = np.array([i, j])
    points.append(p)
    if i*i + j*j < 1:
        r = r + 1

print("pi is roughtly", (r/N)*4)

points = np.transpose(points)
plt.plot(x,y,'b--', linewidth=3.0)
plt.scatter(points[0], points[1], c='r', linewidth=0.01)
plt.show()

