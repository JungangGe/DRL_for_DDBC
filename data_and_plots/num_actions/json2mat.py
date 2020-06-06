import json
import numpy as np
import scipy.io as sio


def json2mat():
    window = 500

    filename = 'fp_performance.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('fp_performance.mat', {'fp_performance': r})

    filename = 'a5times4.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a5times4.mat', {'a54': r})

    filename = 'a5times6.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a5times6.mat', {'a56': r})

    filename = 'a5times8.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a5times8.mat', {'a58': r})
    
    filename = 'a5times10.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a5times10.mat', {'a510': r})

    filename = 'a8times4.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a8times4.mat', {'a84': r})
    
    filename = 'a8times6.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a8times6.mat', {'a86': r})
    
    filename = 'a8times8.json'
    r = []
    with open(filename, 'r') as f:
        data = np.array(json.load(f))
        for i in range(len(data) - window + 1):
            r.append(np.mean(data[i:i + window]))
    r = np.array(r)
    sio.savemat('a8times8.mat', {'a88': r})


json2mat()
