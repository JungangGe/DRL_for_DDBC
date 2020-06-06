""" export the locations of all BSs and UEs as .mat files"""

from cellular_network import CellularNetwork as CN
import random
import numpy as np
from config import Config
import scipy.io as sio


c = Config()
random.seed(c.random_seed)
np.random.seed(c.random_seed)
cn = CN()
bs_locations = cn.bs_locations
sio.savemat('data/bs_locations.mat', {'bs_locations': bs_locations})