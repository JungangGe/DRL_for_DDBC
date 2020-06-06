""" visualize the simulation results """

import json
import matplotlib.pyplot as plt
import numpy as np


def data_visualization():
    window = 500
    # Training data
    filename = 'data/drl_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))

    r = np.array(r)
    plt.plot(r, label='DRL')

    filename = 'data/fp_performance.json'

    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    plt.plot(r, label='ideal FP')

    filename = 'data/greedy_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    plt.plot(r, label='greedy')

    filename = 'data/random_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    plt.plot(r, label='random')

    plt.xlabel('number of time slots')
    plt.ylabel('average achievable spectrum efficiency (bps/Hz)')
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()


data_visualization()
