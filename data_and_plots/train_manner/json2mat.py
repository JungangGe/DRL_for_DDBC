import json
import numpy as np
import scipy.io as sio


def data_visualization():
    window = 500
    filename = 'CTDE.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))

    r = np.array(r)
    sio.savemat('CTDE.mat', {'CTDE': r})

    filename = 'DTDE.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('DTDE.mat', {'DTDE': r})

    filename = 'fp_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('fp_performance.mat', {'fp_performance': r})



data_visualization()
