import numpy as np
import matplotlib.pyplot as plt

r_values = np.linspace(0.2, 4, num=100000)
points_y = []
points_r = []
for r in r_values:
    x = 0.4
    for i in range(50):
        y = r*x*(1-x)
        if i >= 40:
            points_r.append(r)
            points_y.append(y)
        x = y
fig, ax = plt.subplots(figsize=(17, 10))
ax.scatter(points_r, points_y, alpha=0.07, edgecolors='none', s=21,
           marker='.', color='#4da4eb', label=r'$x_{n+1} = r x_n(1-x_n)$')
ax.grid(True)
ax.set_facecolor("#f5f5f5")
ax.set_xlabel("r", fontsize="xx-large")
ax.set_ylabel("x", fontsize="xx-large")
ax.set_title("Bifurcation Diagram of Logistic Map", fontsize="xx-large")
ax.legend(loc='upper left', fontsize='xx-large')
