""" some functions required in the simulation """

import scipy.io as sio
import numpy as np


def get_codebook():
    """ load the codebook file"""
    mdict = sio.loadmat('codebook/codebook.mat')
    code_book = mdict['W']
    return code_book


def dB2num(dB):
    num = 10 ** (dB / 10)
    return num


def num2dB(num):
    dB = 10 * np.log10(num)
    return dB


def get_azimuth(bs_location, ue_location):

    temp = ue_location - bs_location
    d = np.linalg.norm(temp)
    azimuth = np.arccos(temp[0] / d)
    if temp[1] < 0:
        azimuth = 2 * np.pi - azimuth

    return azimuth


def cal_throughput(H, W, noise_power):
    """ calculate the average throughput, given the global CSI, noise power and beamformer of each BS"""
    M = H.shape[0]
    r_power = np.zeros((M, M))
    SINR = np.zeros(M)
    for i in range(M):
        for j in range(M):
            r_power[i, j] = np.square(abs(np.matmul(H[i, j, :], W[:, i])))

    for i in range(M):
        IN = noise_power
        for j in range(M):
            if j != i:
                IN += r_power[j, i]
        SINR[i] = r_power[i, i] / IN
    U = np.log2(1 + SINR)
    return sum(U) / M
