from cellular_network import CellularNetwork as CN
import json
import random
import numpy as np
from config import Config
import functions as f
import os
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
np.random.seed(c.random_seed)
random.seed(c.random_seed)
K = c.n_antennas
M = c.n_links
p_max = f.dB2num(c.bs_power)
cn = CN()
utility = []
codebook = f.get_codebook()
cn.draw_topology()
for _ in range(c.total_slots):
    print(_)
    H = cn.get_H()
    W = np.zeros((K, M), dtype=np.complex)
    for i in range(M):
        temp_h = H[i, i, :]
        r = abs(np.matmul(temp_h, codebook))
        code_index = np.argmax(r)
        W[:, i] = np.sqrt(p_max) * codebook[:, code_index]

    cn.update(ir_change=False, weights=W)
    utility.append(cn.get_ave_utility())
    cn.update(ir_change=True)

# save data
filename = 'data/greedy_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)

