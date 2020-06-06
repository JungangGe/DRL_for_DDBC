""" simulator for user equipments"""

from config import Config
import numpy as np


class UserEquipment:

    def __init__(self, bs):
        """ initialize the attributes of a user equipment """

        c = Config()

        self.azimuth = np.random.rand() * 2 * np.pi
        self.bs = bs
        self.index = bs.index
        self.distance_to_bs = np.random.rand() * (c.cell_radius - c.inner_cell_radius) + c.inner_cell_radius
        self.location = bs.location + self.distance_to_bs * np.array([np.cos(self.azimuth), np.sin(self.azimuth)])
