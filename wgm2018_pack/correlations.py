import numpy as np
import scipy.stats as stt

def spearmanr_(x,y):
    # this version returns only r, which will be used for making the network
    x = np.array(x)
    y = np.array(y)
    [r,p] = stt.spearmanr(x,y)
    return r


def d_semicorr(x, y):
    x = np.array(x)
    y = np.array(y)

    numer = np.sum(x == y).astype("float")
    return numer / len(x)

def d_corr(x,y):
    sem = d_semicorr(x,y)
    corr = (sem*2)-1
    return corr


def corr2distance(corr, method='linear', min_=0, max_=1):
    if method == 'linear':
        d = ((-corr + 1) / 2)

    elif method == 'sqrt':
        d = np.sqrt(0.5 * (1 - corr))

    elif method == 'square':
        d = np.sqrt((1 - corr ** 2))

    else:
        raise Exception("Method not found")

    d = (d * (max_ - min_)) + min_

    return d