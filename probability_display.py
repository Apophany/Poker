import matplotlib.pyplot as plt
import numpy as np

import poker_hands as ph

WIDTH = 0.35


def graph_distribution(probabilities):
    sorted_probs = sorted(probabilities.items(), key=lambda entry: ph.hand_ranks()[entry[0]])

    x_labels = []
    y_values = []
    for probability in sorted_probs:
        x_labels.append(probability[0])
        y_values.append(probability[1])

    figure, ax = plt.subplots()

    ind = np.arange(len(probabilities))
    ax.bar(ind, y_values, WIDTH, color='r', align='center')

    ax.set_title('Hand Probability Distribution')
    ax.set_ylabel('Probability')
    ax.set_xticks(ind)
    ax.set_xticklabels(x_labels)

    plt.show()
