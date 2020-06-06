import functions as f
import numpy as np

class Config:

    def __init__(self):
        # Base Station
        self.n_antennas = f.get_codebook().shape[0]
        self.codebook_size = f.get_codebook().shape[1]
        self.n_power_levels = 5
        self.n_actions = self.codebook_size * self.n_power_levels
        self.bs_power = 38

        # Channel
        self.angular_spread = 3 / 180 * np.pi
        self.multi_paths = 4
        self.rho = 0.64
        self.noise_power = f.dB2num(-114)

        # Cellular Network
        self.cell_radius = 200
        self.n_links = 19
        self.inner_cell_radius = 10

        # Simulation
        self.slot_interval = 0.02
        self.random_seed = 2019
        self.total_slots = 100000
        self.U = 4
