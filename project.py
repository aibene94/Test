import numpy as np
import matplotlib.pyplot as plt

N = 1000

points = []
circle = lambda x : np.sqrt(1 - x*x)
x = np.linspace(0,1,101)
y = circle(x)


for k in range(N):
    i = np.random.random()
    j = np.random.random()


    p = np.array([i, j])


    points.append(p)


points = np.transpose(points)
plt.plot(x,y,'b--', linewidth=3.0)
plt.scatter(points[0], points[1], c='r', linewidth=0.01)
plt.show()

