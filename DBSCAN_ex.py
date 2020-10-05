import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from sklearn import datasets
import matplotlib.cm as cm
import pandas as pd


def calc_distance(data_matrix):
    return distance_matrix(data_matrix, data_matrix)


def get_type(neighbors , edge_density):
    types = {"core":[],"edge":[],"noise":[]}
    for sample in neighbors:
        if sample[1] > edge_density:
            types["core"].append(sample[0])
        elif sample[1] == edge_density:
            types["edge"].append(sample[0])
        else:
            types["noise"].append(sample[0])

    return types


def get_data_point(index,data_set):
    return data_set[index]


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
        distance = dist_matrix[point_index][i]
        if distance <= radius:
            neighbors.append(i)
    return neighbors


def get_all_neighbors(distance_matrix, radius):
    neighbors = {}
    for i in range(len(distance_matrix)):
        neighbors[i] = get_neighbors(i, distance_matrix, radius)
    return neighbors


def connect_clusters(core_neighbors_dict, core_and_neighbors):
    core_set = set(core_neighbors_dict.keys())
    connected_clusters = []
    clusters_len = len(core_and_neighbors)
    connecting_flag = False
    for i in range(clusters_len):
        connecting = False
        if i == clusters_len-1:
            break
        for j in range(i+1, clusters_len):
            if core_and_neighbors[i] & core_and_neighbors[j] & core_set:
                connected_clusters.append(core_and_neighbors[i] | core_and_neighbors[j])
                #print("connecting", i, j)
                #print(core_and_neighbors[i] & core_and_neighbors[j] & core_set)
                connecting = True
                connecting_flag = True
                break

        if connecting:
            break
        else:
            connected_clusters.append(core_and_neighbors[i])
    assert len(connected_clusters) < clusters_len , "get bigger"

    return connected_clusters, connecting_flag


def get_clusters(core_neighbors_dict):
    core_and_neighbors = []

    clusters, updated_core_dict, flag = connect_core_points(core_neighbors_dict)
    print("core_neighbors_dict",len(core_neighbors_dict),"updated_core_dict", len(updated_core_dict),"flag",flag)
    for core_set, i in zip(clusters, range(len(clusters))):
        neighbors = set()
        for core in core_set:
            set_neighbors = set(core_neighbors_dict[core])
            neighbors = neighbors | set_neighbors
        core_and_neighbors.append(neighbors)
    connecting_flag = True
    #while connecting_flag:
    #    core_and_neighbors, connecting_flag = connect_clusters(core_neighbors_dict, core_and_neighbors)
    return [core_and_neighbors, updated_core_dict, flag]

def connect_core_points(core_dict):
    sorted_clusters = []
    updated_core_dict = {}
    core_points = list(core_dict.keys())
    # sorted
    while len(core_points):
        core = core_points.pop(0)
        values = core_dict[core]
        cluster = {core}
        flag = False
        for neighbor in core_dict[core]:
            if neighbor in core_points:
                updated_core_dict[neighbor] = set(values) | set(core_dict[neighbor])
                flag = True
                cluster.add(neighbor)
                core_points.remove(neighbor)
                break
        if not flag:
            updated_core_dict[core] = values
        sorted_clusters.append(cluster)
    return sorted_clusters, updated_core_dict, flag


def get_core_neighbors(neighbors, edge_density):
    core_neighbors = {}
    for point_id, point_neighbors in neighbors.items():
        if len(point_neighbors) > edge_density:
            core_neighbors[point_id] = point_neighbors
    return core_neighbors


def get_data_clusters(index_clusters, data_set):
    data_clusters = []
    for cluster in index_clusters:
        data_cluster = []
        for index in cluster:
            point_xy = list(data_set[index])
            data_cluster.append(point_xy)
        data_clusters.append(data_cluster)
    return data_clusters


def plot_data(data_xy):
    data_x = []
    data_y = []
    for x, y in data_xy:
        data_x.append(x)
        data_y.append(y)
    plt.scatter(data_x, data_y)
    plt.show()


def plot_clusters(data_clusters):
    colors = cm.rainbow(np.linspace(0, 1, len(data_clusters)))
    for cluster, color in zip(data_clusters, colors):
        data_x = []
        data_y = []
        for data in cluster:
            data_x.append(data[0])
            data_y.append(data[1])
        plt.scatter(data_x, data_y, color=color)


def dbscan(data, radius, edge_density):
    dist_matrix = calc_distance(data)
    #np.savetxt('dist_matrix.txt', dist_matrix)

    neighbors = get_all_neighbors(dist_matrix, radius)
    core_neighbors = get_core_neighbors(neighbors, edge_density)
    clusters, updated_Dict, flag = get_clusters(core_neighbors)
    #clusters, updated_Dict, flag = get_clusters(updated_Dict)
    clusters = get_clusters(core_neighbors)
    data_clusters = get_data_clusters(clusters, data)
    plot_clusters(data_clusters)
    plt.show()
    #plot_data(data_clusters)
    return clusters


def main():
    iris = datasets.load_iris()
    data = iris.data[:, :2]
    radius = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    edge_density = [1,2,3,4,5,6,7,8,9,10]
    final_clusters = []
    final_clusters = dbscan(data, 0.3, 3)
    '''
    for i in range(len(radius)):
        for j in range(len(edge_density)):
            final_clusters = dbscan(data, radius[i],edge_density[j])
            if len(final_clusters) == 3:
                plt.show()
    '''
main()

