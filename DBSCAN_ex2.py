import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from sklearn import datasets
import pandas as pd


def calc_distance(data_matrix):
    return distance_matrix(data_matrix, data_matrix)


def get_indices(dist_matrix, radius):
    col = 0
    indices = []
    num_of_neighbors = []
    lenth_data = len(dist_matrix)
    index_neighbors = []
    while col < lenth_data:
        row = 0
        while row < col:
            if dist_matrix[row][col] < radius:
                indices.append([col, row])
                num_of_neighbors.append(col)
                num_of_neighbors.append(row)
            row += 1
        col += 1
    for data_ind in range(lenth_data):
        index_neighbors.append([data_ind, num_of_neighbors.count(data_ind)])

    return indices, index_neighbors


def get_clusters(indices,data_matrix):
    clusters = []
    final_clusters=[]
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
    print(len(clusters))
    # for cluster in clusters:
    #     if cluster in clusters:
    #         final_clusters.append(cluster.union(clusters))
    #         #print(cluster1.union(cluster2))
    #     else:
    #
    #         final_clusters.append(cluster1)
    return clusters


def get_type(neighbors , edge_density):
    types = {"core":[],"edge":[],"noise":[]}
    for sample in neighbors:
        if sample[1] > edge_density:
            types["core"].append(sample[0])
        elif sample[1] == edge_density:
            types["edge"].append(sample[0])
        else:
            types["noise"].append(sample[0])

    print("types",types)
    return types


def get_point_index(point, points):
    points_list = points.tolist()
    return points_list.index(point.tolist())


def get_neighbors(point_index, dist_matrix, radius):
    neighbors = []
    # Iterate over the column of the point
    for i in range(point_index):
        distance = dist_matrix[i][point_index]
        if distance < radius:
            neighbors.append(i)
    # Iterate over the row of the point
    for i in range(point_index + 1, len(dist_matrix)):
        distance = distance_matrix[point_index][i]
        if distance <= radius:
            neighbors.append(i)
    return neighbors


def get_all_neighbors(distance_matrix, radius):
    neighbors = {}
    for i in range(len(distance_matrix)):
        neighbors[i] = get_neighbors(i, distance_matrix, radius)
    return neighbors



def dbscan(data, radius, edge_density):
    dist_matrix = calc_distance(data)
    #np.savetxt('dist_matrix.txt', dist_matrix)

    #neighbors = get_all_neighbors(dist_matrix, radius)
    #num_neighbors = {point_id: len(point_neighbors) for point_id, point_neighbors in neighbors.items()}
    #print(neighbors)
    #print(num_neighbors)

    indices, neighbors = get_indices(dist_matrix, radius)
    sorted_data = get_type(neighbors, edge_density)
    return sorted_data

def plot_data (data_clusters):
    len_clusters = len(data_clusters)
    while(len_clusters):
        fig, ax = plt.subplots()
        ax.plot(data_clusters, row_convergence , '')
    ax.set(xlabel='range', ylabel='convergence')
    ax.grid()

def main():
    iris = datasets.load_iris()
    data = iris.data[:, :2]
    radius = [0.3]
    edge_density = 3
    final_clusters = []

    for i in range(len(radius)):
        final_clusters.append(dbscan(data, radius[i],edge_density))
        #print("radius",radius[i],"final cluster",final_clusters[0])
main()
