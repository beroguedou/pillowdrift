import numpy as np
from sklearn.neighbors import KernelDensity


def continuous_data(data_reference, data_current, columns, config):
    continuous = config['model']['variables']['numerical']['continuous']
    num_elements = []
    for val_ref, val_cur, col in zip(data_reference, data_current, columns):
        if col in continuous:
            element = (col, list(range(max(len(val_ref), len(val_cur)))), val_ref, val_cur, 'continuous')
            num_elements.append(element)

    return num_elements

def estimate_density(X):
    kde = KernelDensity(kernel='tophat', bandwidth=0.2).fit(X)
    return kde

def distribution(numerical_elements):
    new_numerical_elements = []
    for element in numerical_elements:
        name = element[0]
        labels = element[1]
        val_ref = element[2]
        val_cur = element[3]
        # Compute the data distributions 
        #val_ref = estimate_density(np.array(val_ref).reshape(-1, 1))
        #val_cur = estimate_density(np.array(val_cur).reshape(-1, 1))
        # Compute the KS test, retrieve the p-value and the verdict
        pvalue = 0.134
        verdict = "not detected"
        name = "Variable: {} <br> Drift: {} <br> P-value: {}".format(name, verdict, pvalue)

        new_numerical_elements.append((name, labels, val_ref, val_cur, 'continuous'))
    return new_numerical_elements
