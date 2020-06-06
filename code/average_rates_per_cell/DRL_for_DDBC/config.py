""" the configuration of the simulation parameters """

import functions as f
import numpy as np


class Config:

    def __init__(self):
        # Base Station
        self.n_antennas = f.get_codebook().shape[0]  # number of transmit antennas
        self.codebook_size = f.get_codebook().shape[1]  # number of codes
        self.n_power_levels = 5  # number of discrete power levels
        self.n_actions = self.codebook_size * self.n_power_levels   # number of available actions to choose
        self.bs_power = 38  # maximum transmit power of base stations

        # Channel
        self.angular_spread = 3 / 180 * np.pi  # angular spread
        self.multi_paths = 4  # number of multi-paths
        self.rho = 0.64  # channel correlation coefficient
        self.noise_power = f.dB2num(-114)  # noise power

        # Cellular Network
        self.cell_radius = 200  # cell radius
        self.n_links = 19  # number of simulated direct links in the simulation
        self.inner_cell_radius = 10  # inner cell radius

        # Simulation
        self.slot_interval = 0.02  # interval of one time slot
        self.random_seed = 2019  # random seed to control the simulated cellular network
        self.total_slots = 100000   # total time slots in the simulation
        self.U = 5  # number of neighbors taken into consideration
