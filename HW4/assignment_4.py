import random
import matplotlib.pyplot as plt


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


for f in range(10):
    population = [0, 1]*15
    populations = [population]
    generation = [0]
    for i in range(1, 50):
        generation.append(i)
        populations.append(random.choices(populations[-1], k=30))
    a_gene_counts = [population.count(0) for population in populations]
    b_gene_counts = [population.count(1) for population in populations]

    width = 0.8
    x_label = [f'G{i}' for i in range(1, len(a_gene_counts)+1)]
    x = list(range(1, 2*len(a_gene_counts)+1, 2))
    a_x = list(map(lambda x: x - width/2, x))
    b_x = list(map(lambda x: x + width/2, x))
    fig, ax = plt.subplots(figsize=(20, 10))
    rects_1 = ax.bar(a_x, a_gene_counts, width, label='a')
    rects_2 = ax.bar(b_x, b_gene_counts, width, label='b')
    autolabel(rects_1)
    autolabel(rects_2)
    ax.set_xticks(x)
    ax.set_xticklabels(x_label)
    ax.legend(fontsize='xx-large')
    ax.set_facecolor("#f5f5f5")
    ax.set_ylabel("Number of Genes", fontsize='xx-large')
    ax.set_xlabel("Generation", fontsize='xx-large')
