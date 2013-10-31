nnod = len(dview)

def cluster_pi(n):
    m = sum(dview.map_sync(sample_circle, nnod*[n/nnod]))
    return 4.*m/n

cluster_pi(n)
