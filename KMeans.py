import math
import copy

class Floot:
    def __init__(self, value):
        self.val = value
    def __eq__(self, other):
        return (math.isclose(self.val, other.val, rel_tol=1e-11))
    def __ne__(self, other):
        return not(self.__eq__(other))
    def __lt__(self, other):
        return (self.val < other.val and self.__ne__(other))
    def __gt__(self, other):
        return (self.val > other.val and self.__ne__(other))
    def __le__(self, other):
        return (self.__lt__(other) or self.__eq__(other))
    def __ge__(self, other):
        return (self.__gt__(other) or self.__eq__(other))
    
Nk = input().split()
N = int(Nk[0])
k = int(Nk[1])

data_list = []
for i in range(N):
    data_list.append([float(x) for x in input().split()])
    data_list[i].append(i)

dimensions = len(data_list[0])-1

centroid_list = []
for i in range(k):
    centroid_list.append([float(x) for x in input().split()])

cluster_assignment = {}
    
for i in range(N):
    nearest_centroid_id = None
    nearest_centroid_dist = None
    for j in range(k):
        euclidean_distance = 0
        for d in range(dimensions):
            euclidean_distance += pow((data_list[i][d]-centroid_list[j][d]), 2)
        euclidean_distance = math.sqrt(euclidean_distance)
        if nearest_centroid_dist is None or Floot(euclidean_distance) < Floot(nearest_centroid_dist):
            nearest_centroid_dist = euclidean_distance
            nearest_centroid_id = j
    if nearest_centroid_id not in cluster_assignment:
        cluster_assignment[nearest_centroid_id] = []
    cluster_assignment[nearest_centroid_id].append(i)
    
    
while True:
    new_centroid_list = []
    for cluster_id in sorted(cluster_assignment):
        num_data = 0
        new_centroid = []
        for d in range(dimensions):
            new_centroid.append(0)
        for data_id in cluster_assignment[cluster_id]:
            num_data += 1
            for d in range(dimensions):
                new_centroid[d] += data_list[data_id][d]
        for d in range(dimensions):
            new_centroid[d] /= num_data
        new_centroid_list.append(new_centroid)
        
    new_cluster_assignment = {}
    for i in range(N):
        nearest_centroid_id = None
        nearest_centroid_dist = None
        for j in range(k):
            euclidean_distance = 0
            for d in range(dimensions):
                euclidean_distance += pow((data_list[i][d]-new_centroid_list[j][d]), 2)
            euclidean_distance = math.sqrt(euclidean_distance)
            if nearest_centroid_dist is None or Floot(euclidean_distance) < Floot(nearest_centroid_dist):
                nearest_centroid_dist = euclidean_distance
                nearest_centroid_id = j
        if nearest_centroid_id not in new_cluster_assignment:
            new_cluster_assignment[nearest_centroid_id] = []
        new_cluster_assignment[nearest_centroid_id].append(i)
        
    if cluster_assignment == new_cluster_assignment:
        break
        
    cluster_assignment = new_cluster_assignment
    
for cluster_id, data in cluster_assignment.items():
    for data_id in data:
        data_list[data_id][dimensions] = cluster_id 
for data in data_list:
    print(data[dimensions])
