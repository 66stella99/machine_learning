import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def get_clusters(data_set: np.array, mean_values: np.array):
    clusters = {}
    k = len(mean_values)
    for i in range(k):
        clusters[i] = []

    for data in data_set:
        magnitudes = []
        for mean_val in mean_values:
            diff_vector = mean_val - data
            magnitudes.append(np.sqrt(np.mean(np.square(diff_vector))))
        i = magnitudes.index(np.min(magnitudes))
        clusters[i].append(data)

    for key in clusters:
        clusters[key] = np.array(clusters[key])

    return clusters


def calc_means(clusters):
    return [np.mean(samples, 0) for samples in clusters.values()]


def check_convergence(old_means, new_means, epsilon):
    return np.all([abs(i - j) < epsilon for i, j in zip(old_means, new_means)])


def plot_clusters(clusters):
    fig, ax = plt.subplots()
    for samples in clusters.values():
        ax.plot(samples[:, 0], samples[:, 1], '.')
        mean = np.mean(samples, 0)
        ax.plot(mean[0], mean[1], '.')
    ax.set(xlabel='data variable 1', ylabel='data variable 2',
           title='')
    ax.grid()
    plt.show(block=False)


def main():
    csv_data = pd.read_csv("datasets_17860_23404_IRIS.csv")
    data_set = csv_data.to_numpy()[:, :-3]
    k = 3
    mean_values = []
    for i in range(k):
        sample = csv_data.sample().to_numpy()[0][:-3]
        mean_values.append(sample)

    converged = False
    while not converged:
        clusters = get_clusters(data_set, mean_values)
        # for key, values in clusters.items():
        #     print(f"{key} = {values}\n")
        new_mean_values = calc_means(clusters)
        converged = check_convergence(mean_values, new_mean_values, 1e-6)
        mean_values = new_mean_values
        plot_clusters(clusters)
    plt.show()

main()

