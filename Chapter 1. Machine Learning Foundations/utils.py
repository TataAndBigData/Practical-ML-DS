import sklearn.datasets
import numpy as np
import matplotlib.pyplot as plt
from get_colors import colors

def get_classification_data(sd=6, m=10, n_features=2, n_clusters=2):
    X, Y = sklearn.datasets.make_blobs(n_samples=m, n_features=n_features, centers=n_clusters, cluster_std=sd)
    return X, Y

def calc_accuracy(predictions, labels):
    return np.mean((predictions == labels).astype(int)) * 100

def visualise_predictions(H, X, n=50):
    xmin, xmax, ymin, ymax = min(X[:, 0]), max(X[:, 0]), min(X[:, 1]), max(X[:, 1])
    meshgrid = np.zeros((n, n))
    for x1_idx, x1 in enumerate(np.linspace(xmin, xmax, n)): # for each column
        for x2_idx, x2 in enumerate(np.linspace(ymin, ymax, n)): # for each row
            h = H(np.array([[x1, x2]])).astype(int)[0]
            meshgrid[n-1-x2_idx, x1_idx] = h # axis 0 is the vertical direction starting from the top and increasing downward
    plt.imshow(meshgrid, extent=(xmin, xmax, ymin, ymax), cmap='viridis')


def show_data(X, Y, predictions=None):
    for i in range(min(Y), max(Y)+1):
        y = Y == i
        x = X[y]
        plt.scatter(x[:, 0], x[:, 1], c=colors[i])
        if predictions is not None:
            y = predictions == i
            x = X[y]
            plt.scatter(x[:, 0], x[:, 1], c=colors[i], marker='x', s=100)
    plt.show()

    