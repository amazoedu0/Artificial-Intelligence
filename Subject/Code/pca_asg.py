import numpy as np
from numpy.lib.function_base import cov


class PCA:
    def __init__(self, nComps):
        self.nComps = nComps
        self.comps = None
        self.mean = None

    def fit(self, X):
        # mean
        self.mean = np.mean(X, axis=0)
        X = X-self.mean
        # covar
        cov=np.cov(X,T)
        #egVect, egVal
        egVal,egVect=np.linalg.eig(cov)
        
        # sort egVect
        egVect=egVect.T
        idxs=np.argsort(eg)

    def transform(self, X):
        pass

        