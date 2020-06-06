import json
import numpy as np
import scipy.io as sio


def json2mat():
    window = 500

    r = []
    data = np.array([])
    with open('fp_performance_1.json', 'r') as f:
        data_1 = np.array(json.load(f))
    with open('fp_performance_2.json', 'r') as f:
        data_2 = np.array(json.load(f))
    data = np.hstack((data_1[0:50000], data_2[0:50000]))
    
    for i in range(len(data) - window + 1):
        r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('fp_performance.mat', {'fp_performance': r})


    r = []
    data = np.array([])
    with open('drl_performance_1.json', 'r') as f:
        data_1 = np.array(json.load(f))
    with open('drl_performance_2.json', 'r') as f:
        data_2 = np.array(json.load(f))
    data = np.hstack((data_1[0:50000], data_2[0:50000]))
    
    for i in range(len(data) - window + 1):
        r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('drl_performance.mat', {'drl_performance': r})

    r = []
    data = np.array([])
    with open('greedy_performance_1.json', 'r') as f:
        data_1 = np.array(json.load(f))
    with open('greedy_performance_2.json', 'r') as f:
        data_2 = np.array(json.load(f))
    data = np.hstack((data_1[0:50000], data_2[0:50000]))
    
    for i in range(len(data) - window + 1):
        r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('greedy_performance.mat', {'greedy_performance': r})


    r = []
    data = np.array([])
    with open('random_performance_1.json', 'r') as f:
        data_1 = np.array(json.load(f))
    with open('random_performance_2.json', 'r') as f:
        data_2 = np.array(json.load(f))
    data = np.hstack((data_1[0:50000], data_2[0:50000]))
    
    for i in range(len(data) - window + 1):
        r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('random_performance.mat', {'random_performance': r})





json2mat()
