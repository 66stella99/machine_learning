import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from sklearn import datasets
import pandas as pd

# def regionQuery (row_data):
#
#     return num_of_neighbours
#
# def expandCluster (data):
#     return dict_clusters
#
# def dbscan(csv_data,radius):
#     data = []
#     for data_sample in range(len(csv_data)):
#         num_of_neighbours = regionQuery(csv_data[data_sample],radius)
#         data.append(num_of_neighbours , csv_data[data_sample])
#     clusters = expandCluster(data)

def calc_distance(data_matrix):
    return distance_matrix(data_matrix,data_matrix)

def get_indices(dist_matrix,radius):
    col = 0
    indices = []
    lenth_data = len(dist_matrix)
    while (col < lenth_data):
        row = 0
        while(row < col):
            if(dist_matrix[row][col]<radius):
                indices.append([col,row])
            row+=1
        col+=1
    return(indices)

def get_clusters(indices,data_matrix):
    clusters = []
    for row, col in indices:
        found = False
        for cluster in clusters:
            if (row in cluster) or (col in cluster):
                cluster.add(row)
                cluster.add(col)
                found = True
                break
        if not found:
            clusters.append({row, col})
        for
    print(clusters)
    return clusters

def dbscan(data, radius):
    dist_matrix = calc_distance(data)
    indices = get_indices(dist_matrix, radius)
    get_clusters(indices, data)

def main():
    iris = datasets.load_iris()
    data = iris.data[:, :4]
    radius = 1
    for i in range(1):
        dbscan(data,radius)

main()
