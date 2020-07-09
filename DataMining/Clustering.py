import numpy as np
from math import sqrt

def distance_to_g(data, g):
    list_point = data[1:,1:].astype(np.float)
    g = g.astype(np.float)
    
    ls_distance = list()
    for point in list_point:
        ls_distance.append([sqrt(sum([(point - g_i)[i]**2 for i in range(len(g_i))])) for g_i in g])

    print(ls_distance)
    return ls_distance


def clustering(data, dist):
    clust = [[] for i in range(len(dist[0]))]
    i = 1
    for idx in dist:
        clust[idx.index(min(idx))].append(data[i][0])
        i += 1
    return clust


def pick_g(data, clust):
    new_g = list()
    for clust_i in clust:
        list_clust = list()
        for el in clust_i:
            for data_i in data:
                if data_i[0] == el:
                    list_clust.append(data_i[1:].astype(np.float))
        
        new_g.append([np.mean([list_clust[i][j] for i in range(len(list_clust))]) for j in range(len(list_clust[0]))])
        
    return np.array(new_g)


def k_clustering(data, k):
#     initial
    crr_g = data[1:k + 1,1:]
    crr_clust = list()
    
    while True:
        new_clust = clustering(data, distance_to_g(data, crr_g))
        print(new_clust)

        if new_clust == crr_clust:
            break
        
        crr_g = pick_g(data, new_clust)
        print(crr_g)
        crr_clust = new_clust

    return crr_clust


data = [['Custome', 'Age', 'Income'], 
        ['An', 40, 20],
        ['Binh', 10, 10],
        ['Linh', 22, 15],
        ['Loc', 10, 16],
        ['Nhan', 30, 10],
        ['Nghia', 20, 20],
        ['Phat', 32, 15],
        ['Trong', 10, 10]]

data = np.array(data)

def main():
    print(k_clustering(data, 3))
    
if __name__ == '__main__':
    main()
