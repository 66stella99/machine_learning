import numpy as np
import matplotlib
import pandas as pd


def get_data(data_set: [float], mean_values: [float] ):
    dict = {}
    k=len(mean_values)
    for i in range(k):
        dict[i] = []
    for data in data_set:
        magnitudes = []
        for mean_val in mean_values:
            diff_vector = mean_val - data
            magnitudes.append(np.sqrt(np.mean(np.square(diff_vector))))
        i = magnitudes.index(np.min(magnitudes))
        dict[i].append(data)
    return dict

def calc_means(init_dict):
    means_vector = []
    return means_vector

def check_convergence():
    convergence = False
    return convergence

def main():
    csv_data = pd.read_csv("datasets_17860_23404_IRIS.csv")
    data_set = csv_data.to_numpy()[:,:-1]
    k = 3
    mean_values = []
    for i in range(k):
        sample = csv_data.sample().to_numpy()[0][:-1]
        mean_values.append(sample)
    mean_values = np.array(mean_values)
    output = get_data(data_set, mean_values)
    for key, values in output.items():
        print(f"{key} = {values}\n\n\n")

main()
