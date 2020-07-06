import sklearn.datasets

def get_classification_data(sd=6, m=10, n_features=2, n_clusters=2):
    X, Y = sklearn.datasets.make_blobs(n_samples=m, n_features=n_features, centers=n_clusters, cluster_std=sd)
    return X, Y
