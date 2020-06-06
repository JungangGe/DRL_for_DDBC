""" random scheme for the formulated DDBC problem"""

from cellular_network import CellularNetwork as CN
import json
import random
import numpy as np
from config import Config
import scipy.io as sio
import os
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
np.random.seed(c.random_seed)
random.seed(c.random_seed)
cn = CN()
utility = []
rate_m = []
cn.draw_topology()
for _ in range(c.total_slots):
    print(_)
    actions = cn.random_choose_actions()
    cn.update(ir_change=False, actions=actions)
    utility.append(cn.get_ave_utility())
    rate_m.append(cn.get_all_rates())
    cn.update(ir_change=True)

# save data
filename = 'data/random_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)
rate_m = np.array(rate_m)
sio.savemat('rates/random_rates.mat', {'random_rates': rate_m})


