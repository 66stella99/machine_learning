import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


def get_sample_min_error(sample: np.array, mean_values: np.array):
    magnitudes = []
    for mean_val in mean_values:
        diff_vector = mean_val - sample
        magnitudes.append(np.sqrt(np.mean(np.square(diff_vector))))
    min_error = np.min(magnitudes)
    min_error_index = magnitudes.index(min_error)
    return min_error_index, min_error


def get_data_set_errors(data_set: np.array, mean_values: np.array):
    errors = {key: [] for key in range(len(mean_values))}
    for sample in data_set:
        min_error_index, min_error = get_sample_min_error(sample, mean_values)
        errors[min_error_index].append(min_error)
    mean_errors = []
    for key in errors:
        mean_errors.append(np.mean(errors[key]))
    return np.linalg.norm(mean_errors)


def get_clusters(data_set: np.array, mean_values: np.array):
    clusters = {}
    err = {}
    k = len(mean_values)
    for i in range(k):
        clusters[i] = []

    for data in data_set:
        index, _ = get_sample_min_error(data, mean_values)
        clusters[index].append(data)

    for key in clusters:
        clusters[key] = np.array(clusters[key])
    return clusters


def calc_means(clusters):
    return [np.mean(samples, 0) for samples in clusters.values()]


def calc_error(clusters):
    pass
    return


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
    #plt.show(block=False)

def plot_convergence(row_convergence):
    convergence=[]
    fig, ax = plt.subplots()
    #print(row_convergence)
    ax.plot(range(len(row_convergence)), row_convergence , '')
    ax.set(xlabel='range', ylabel='convergence')
    ax.grid()
    plt.show()

def k_mean(csv_data):
    data_set = csv_data.to_numpy()[:, :-3]
    k = 3
    mean_values = []
    sample_distance = np.ndarray([])
    sample_distance = [0,0,0]

    while(sample_distance[0]<0.1 or sample_distance[1]<0.1 or sample_distance[2]<0.1):
        for i in range(k):
            sample = csv_data.sample().to_numpy()[0][:-3]
            mean_values.append(sample)

        sample_distance[0] = np.linalg.norm(mean_values[1]-mean_values[0])
        sample_distance[1] = np.linalg.norm(mean_values[2]-mean_values[0])
        sample_distance[2] = np.linalg.norm(mean_values[2]-mean_values[1])
    converged = False
    clusters = []
    converged_diff= []
    while not converged:
        clusters = get_clusters(data_set, mean_values)
        new_mean_values = calc_means(clusters)
        converged = check_convergence(mean_values, new_mean_values, 1e-6)
        converged_diff.append(np.sqrt(np.mean(np.square(np.array(new_mean_values)-np.array(mean_values)))))
        mean_values = new_mean_values
        #abs_error = get_data_set_errors(data_set, mean_values)

    plot_clusters(clusters)
    plot_convergence(converged_diff)
    #plt.show()


def main():
    csv_data = pd.read_csv("datasets_17860_23404_IRIS.csv")
    for i in range(1):
        k_mean(csv_data)


main()
