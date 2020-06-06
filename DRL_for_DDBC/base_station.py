"""simulator for base stations """

import numpy as np
import random
import functions as f
from config import Config
from dqn_for_singleagent import DQN


class BaseStation:

    def __init__(self, location, index):
        """ initialize the attributes of BS """

        self.location = location
        self.index = index
        self.n_antennas = Config().n_antennas
        self.dqn = DQN()
        self.max_power = f.dB2num(Config().bs_power)
        self.codebook = f.get_codebook()
        self.powerbook = np.arange(Config().n_power_levels) * self.max_power / (Config().n_power_levels - 1)
        self.code_index = random.randint(0, Config().codebook_size-1)
        self.power_index = random.randint(0, Config().n_power_levels-1)

        self.code = self.codebook[:, self.code_index]
        self.power = self.powerbook[self.power_index]

        self._init_params_()

    def _init_params_(self):
        """ initialize some variables to save the historical actions """

        self.code_index1, self.code_index2 = None, None
        self.power_index1, self.power_index2 = None, None
        self.power1, self.power2 = None, None

    def _save_params_(self):
        """ save the historical actions by variables """

        self.code_index2 = self.code_index1
        self.code_index1 = self.code_index

        self.power_index2 = self.power_index1
        self.power_index1 = self.power_index

        self.power2 = self.power1
        self.power1 = self.power

    def take_action(self, action=None, weight=None):
        """ save the historical actions by variables before updating beamformer and take action according
        to the input parameters, 'weight' for FP, 'action' for the other schemes. """
        self._save_params_()
        if action is not None:
            self.power_index = action % Config().n_power_levels
            self.code_index = action // Config().n_power_levels
            self.code = self.codebook[:, self.code_index]
            self.power = self.powerbook[self.power_index]
        if weight is not None:
            if np.linalg.norm(weight) != 0:
                self.code = weight / np.linalg.norm(weight)
                self.power = np.square(np.linalg.norm(weight))
            else:
                self.code = np.zeros(Config().n_antennas, dtype=np.complex)
                self.power = 0


