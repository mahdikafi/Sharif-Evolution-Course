import matplotlib.pyplot as plt

r_list = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
k1 = 100
k2 = 500
fig, ax = plt.subplots(4, 2, figsize=(20, 20))

for i, r in enumerate(r_list):
    x_pop = [10]
    y_pop = [10]
    generation = [0]
    for gen in range(1, 15):
        xt = x_pop[-1]
        yt = y_pop[-1]
        xt1 = (1+r)*xt - (xt+yt)**2/k1
        yt1 = (1+r)*yt - (xt+yt)**2/k2
        x_pop.append(0 if xt1 < 0 else xt1)
        y_pop.append(0 if yt1 < 0 else yt1)
        generation.append(gen)
    ax[i//2][i%2].plot(generation, x_pop, marker='o', label='x')
    ax[i//2][i%2].plot(generation, y_pop, marker='o', linestyle='dashed', color= 'orange', label=f'y\nr={r}')
    ax[i//2][i%2].axhline(y=k1)
    ax[i//2][i%2].axhline(y=k2, color='orange')
    ax[i//2][i%2].legend(fontsize='x-large')
    ax[i//2][i%2].grid(True)
    ax[i//2][i%2].set_facecolor("#f5f5f5")
    ax[i//2][i%2].set_xlabel('Time', fontsize='xx-large')
    ax[i//2][i%2].set_ylabel('Population', fontsize = 'xx-large')
