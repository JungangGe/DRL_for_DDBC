""" DTDE DRL-based scheme """
from cellular_network import CellularNetwork as CN
import json
import random
import numpy as np
import scipy.io as sio
from config import Config
import os
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
random.seed(c.random_seed)
np.random.seed(c.random_seed)
cn = CN()
utility = []
cn.draw_topology()
rate_m = []
for _ in range(c.total_slots):
    print(_)
    s = cn.observe()
    actions = cn.choose_actions(s)
    cn.update(ir_change=False, actions=actions)
    utility.append(cn.get_ave_utility())
    rate_m.append(cn.get_all_rates())
    cn.update(ir_change=True)
    r = cn.give_rewards()
    s_ = cn.observe()
    cn.save_transitions(s, actions, r, s_)

    if _ > 256:
        cn.train_dqns()


# save data
filename = 'data/drl_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)
rate_m = np.array(rate_m)
sio.savemat('rates/drl_rates.mat', {'drl_rates': rate_m})
