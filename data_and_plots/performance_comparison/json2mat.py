import json
import numpy as np
import scipy.io as sio


def data_visualization():
    window = 500
    # Training data
    filename = 'drl_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))

    r = np.array(r)
    sio.savemat('drl_performance.mat', {'drl_performance': r})

    filename = 'fp_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('fp_performance.mat', {'fp_performance': r})

    filename = 'greedy_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('greedy_performance.mat', {'greedy_performance': r})

    filename = 'random_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('random_performance.mat', {'random_performance': r})



data_visualization()
