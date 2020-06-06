from cellular_network import CellularNetwork as CN
from dqn_for_multiagent import DQN
from config import Config
import json
import random
import numpy as np
import os
import scipy.io as sio
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
random.seed(c.random_seed)
np.random.seed(c.random_seed)
cn = CN()
dqn = DQN()
utility = []
cn.draw_topology()
Actions = []
for _ in range(c.total_slots):
    print(_)
    s = cn.observe()
    actions = dqn.choose_actions(s)
    cn.update(ir_change=False, actions=actions)
    utility.append(cn.get_ave_utility())
    cn.update(ir_change=True)
    r = cn.give_rewards()
    s_ = cn.observe()
    dqn.save_transitions(s, actions, r, s_)

    if _ > 256:
        dqn.learn()
    if _ > c.total_slots - 10000:
        Actions.append(actions)


# save data
Actions = np.array(Actions)
sio.savemat('data/CTDEactions.mat', {'Actions': Actions})

filename = 'data/CTDEdrl_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)

