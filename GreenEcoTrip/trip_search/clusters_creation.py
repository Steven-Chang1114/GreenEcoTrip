from google_api_calls import nearby_airports


def nearby_cities(lat, lng, radius):

def raw_clusters(departure, arrival):
    #departure is the departure city
    # arrival is the departure city
    return nearby_airports(departure), nearby_airports(arrival)

def expand_cluster_to_k(cluster, k=7):
    #giving a cluster, expand it for more than 50 km
    #k is the maximum size of the cluster

    visited = cluster[0]

    for i in range(1,len(cluster)-1):
        visited.append(cluster[i])
        for city in nearby_airports(cluster[i]) and city not in visited:
            if len(cluster) < k:
                cluster.append[city]

    return cluster

def expand_cluster_one(cluster,  k=7):
    #giving a cluster, expand it for more than 50 km
    #k is the maximum size of the cluster

    visited = cluster[0]

    for i in range(1,len(cluster)-1):
        visited.append(cluster[i])
        city = nearby_airports(cluster[i])
        if city not in visited:
            if len(cluster) < k:
                cluster.append[city]

    return cluster