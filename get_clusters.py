# neighbors: dict:              {0: [1, 2, 3], 1: [0, 4, 5], 2: [0, 7, 8, 9], 13: [10, 11, 12]}
# clusters:  list of sets:      [{0, 1, 2}, {13}]
def get_clusters(neighbors: dict):
    clusters = []
    points = list(neighbors.keys())
    while len(points) > 0:
        point = points.pop(0)
        cluster = {point}
        for neighbor in neighbors[point]:
            if neighbor in points:
                cluster.add(neighbor)
                points.remove(neighbor)
        clusters.append(cluster)
    return clusters
