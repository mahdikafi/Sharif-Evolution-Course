import string
import random
import numpy as np
import matplotlib.pyplot as plt

alphabet = string.ascii_lowercase + ' '
text = "ke eshgh asan nemud aval vali oftad moshkel ha"
print("reference text is:", text)
length = len(text)
g_1 = []
for i in range(100):
    g_1.append(random.choices(alphabet, k= len(text)))
g_1 = np.array(g_1)
ord_vec = np.vectorize(ord)
g_1 = ord_vec(g_1)
g_1_lamarck = np.copy(g_1)
reference = []
for char in text:
    reference.append(ord(char))
reference = np.array(reference)
iteration = 1000
darwin_min_scores = []
lamarck_min_scores = []
darwin_iterations = []
print("#########Darwin##########")
for it in range(iteration):
    scores = (np.absolute(g_1 - reference)).sum(axis= 1)
    # print(f"{it+1} iteration scores:", scores)
    min_score = scores.min()
    darwin_min_scores.append(min_score)
    darwin_iterations.append(it+1)
    if (it+1)%100 == 0:  
        print(f"#{it+1} iteration score:", min_score)
    if min_score < 1:
        print(f"solution is found after {it+1} generation")
        min_index = scores.argmin()
        solution = g_1[min_index]
        # print(solution)
        vec_chr = np.vectorize(chr)
        hafez = vec_chr(solution)
        # print(hafez)
        print("solution found by Darwin hypothesis:", ''.join(hafez))
        break
    k = 25
    best_g_1_mask = np.zeros(g_1.shape[0], dtype=np.bool)
    for i in range(k):
        argmin = scores.argmin()
        best_g_1_mask[argmin] = 1
        scores[argmin] = 10000
    # print(best_g_1_mask)
    g_1_best = g_1[best_g_1_mask]
    offsprings = np.empty((1, length), dtype= np.int16)
    ###mutation###
    mutation_list = list(range(97, 123))
    mutation_list.append(32)
    mutation_rate = 0.02
    for i in range(g_1_best.shape[0]):
        for k in range(4):
            child = np.copy(g_1_best[i])
            for j in range(g_1_best.shape[1]):
                if random.random() < mutation_rate:
                    child[j] = random.choice(mutation_list)
            offsprings = np.concatenate((offsprings, [child]), axis= 0)
    offsprings = np.delete(offsprings, 0, axis=0)
    # print(offsprings)
    g_1 = offsprings

"""Lamarck Hypothesis"""

g_1 = g_1_lamarck
iteration = 1000
lamarck_min_scores = []
lamarck_iterations = []
print("#########Lamarck#########")
for it in range(iteration):
    scores = (np.absolute(g_1 - reference)).sum(axis= 1)
    # print(f"{it+1} iteration scores:", scores)
    min_score = scores.min()
    lamarck_min_scores.append(min_score)
    lamarck_iterations.append(it+1)
    if (it+1)%100 == 0:  
        print(f"#{it+1} iteration score:", min_score)
    if min_score < 1:
        print(f"solution is found after {it+1} generation")
        min_index = scores.argmin()
        solution = g_1[min_index]
        # print(solution)
        vec_chr = np.vectorize(chr)
        hafez = vec_chr(solution)
        # print(hafez)
        print("solution found by Lamarck hypothesis:", ''.join(hafez))
        break
    k = 25
    best_g_1_mask = np.zeros(g_1.shape[0], dtype=np.bool)
    for i in range(k):
        argmin = scores.argmin()
        best_g_1_mask[argmin] = 1
        scores[argmin] = 10000
    # print(best_g_1_mask)
    g_1_best = g_1[best_g_1_mask]
    offsprings = np.empty((1, length), dtype= np.int16)
    ###mutation###
    learning_rate = 0.0005
    for i in range(g_1_best.shape[0]):
        for k in range(4):
            child = np.copy(g_1_best[i])
            for j in range(g_1_best.shape[1]):
                if random.random() < learning_rate:
                    child[j] = reference[j]
            offsprings = np.concatenate((offsprings, [child]), axis= 0)
    offsprings = np.delete(offsprings, 0, axis=0)
    # print(offsprings)
    g_1 = offsprings
fig, ax= plt.subplots(figsize=(10, 10))
ax.plot(darwin_iterations, darwin_min_scores, label="Darwin", color="#FF005E", linewidth=2)
ax.plot(lamarck_iterations, lamarck_min_scores, color= "#0099FF", label="Lamarck", linestyle="--", lw= 2)
ax.set_xlim(0, 500)
ax.grid(True)
ax.legend(fontsize="xx-large")
ax.set_facecolor('#f5f5f5')
ax.set_ylabel("Score", fontsize="xx-large")
ax.set_xlabel("Generation", fontsize="xx-large")
