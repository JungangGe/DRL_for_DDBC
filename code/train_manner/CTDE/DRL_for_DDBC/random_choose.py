from cellular_network import CellularNetwork as CN
import json
import random
import numpy as np
from config import Config
import os
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
np.random.seed(c.random_seed)
random.seed(c.random_seed)
cn = CN()
utility = []
cn.draw_topology()
for _ in range(Config().total_slots):
    actions = cn.random_choose_actions()
    cn.update(ir_change=False, actions=actions)
    utility.append(cn.get_ave_utility())
    cn.update(ir_change=True)

# save data
filename = 'data/random_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)



