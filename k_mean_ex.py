import numpy as np
import matplotlib
import pandas as pd


def get_data (Data_set , Mean_values):
    init_dict = {}
    data_set = Data_set
    mean_values = Mean_values

    return init_dict
def calc_means (init_dict):
    means_vector = []
    return means_vector

def check_convergence ():
    convergence = False
    return convergence

def main ():
    claster = [1,2,3]
    row_data = pd.read_csv("datasets_17860_23404_IRIS.csv")
    init_mean_values = row_data.sample()
    print((init_mean_values))
    get_data(row_data,init_mean_values)

main()

