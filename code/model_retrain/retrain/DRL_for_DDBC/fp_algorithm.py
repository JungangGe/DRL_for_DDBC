from cellular_network import CellularNetwork as CN
import json
import numpy as np
from config import Config
import random
import functions as f
import time
import os
os.environ['MKL_NUM_THREADS'] = '1'


c = Config()
random.seed(c.random_seed)
np.random.seed(c.random_seed)
K = c.n_antennas
M = c.n_links
p_max = f.dB2num(c.bs_power)
codebook = f.get_codebook()
noise_power = c.noise_power
cn = CN()
utility = []
cn.draw_topology()

for _ in range(c.total_slots):
    H = cn.get_H()
    # fp algorithm
    y, y_next = np.zeros(M, dtype=np.complex), np.zeros(M, dtype=np.complex)
    W, W_next = np.zeros((K, M), dtype=np.complex), np.zeros((K, M), dtype=np.complex)
    gamma, gamma_next = np.zeros(M), np.zeros(M)

    sum_throughput, sum_throughput_next = 0, 0
    start = time.clock()
    for i in range(M):
        # initialized W and gamma
        temp = random.randint(0, c.codebook_size-1)
        W[:, i] = codebook[:, temp] * random.random() * np.sqrt(p_max)
        gamma[i] = np.square(abs(np.matmul(H[i, i, :], W[:, i]))) / \
                   (np.square(np.linalg.norm(np.diag(np.matmul(H[:, i, :], W)))) + noise_power - np.square(abs(np.matmul(H[i, i, :], W[:, i]))))

        y[i] = np.sqrt(1 + gamma[i]) * np.matmul(H[i, i, :], W[:, i]) / \
               (np.square(np.linalg.norm(np.diag(np.matmul(H[:, i, :], W)))) + noise_power)
    sum_throughput = f.cal_throughput(H, W, noise_power)
    n_iter1 = 0
    while abs(sum_throughput - sum_throughput_next) > 1e-2 and n_iter1 < 100:
        sum_throughput = sum_throughput_next
        # update y
        for i in range(M):
            y_next[i] = np.sqrt(1 + gamma[i]) * np.matmul(H[i, i, :], W[:, i]) / \
                   (np.square(np.linalg.norm(np.diag(np.matmul(H[:, i, :], W)))) + noise_power)
        # update W
        for i in range(M):

            eta_min, eta_max = 0, 1e4
            f_min, f_max = 0, 100
            n_iter2 = 0
            while abs(f_max - f_min) > 1e-2 and n_iter2 < 100:
                eta = eta_min
                m = eta * np.eye(K)
                for j in range(M):
                    x = H[i, j, :].reshape(1, K)
                    m = m +  np.square(np.linalg.norm(y[j])) * np.matmul(x.conj().T, x)

                W_next[:, i] = np.matmul(np.linalg.inv(m), np.sqrt(1 + gamma[i]) * y_next[i] * H[i, i, :].conj().T)
                f_min = np.square(np.linalg.norm(W_next[:, i]))

                eta = eta_max
                m = eta * np.eye(K)
                for j in range(M):
                    x = H[i, j, :].reshape(1, K)
                    m = m + np.square(np.linalg.norm(y[j])) * np.matmul(x.conj().T, x)

                W_next[:, i] = np.matmul(np.linalg.inv(m), np.sqrt(1 + gamma[i]) * y_next[i] * H[i, i, :].conj().T)
                f_max = np.square(np.linalg.norm(W_next[:, i]))

                eta_mid = (eta_max + eta_min) / 2
                eta = eta_mid
                m = eta * np.eye(K)
                for j in range(M):
                    x = H[i, j, :].reshape(1, K)
                    m = m + np.square(np.linalg.norm(y[j])) * np.matmul(x.conj().T, x)

                W_next[:, i] = np.matmul(np.linalg.inv(m), np.sqrt(1 + gamma[i]) * y_next[i] * H[i, i, :].conj().T)
                f_mid = np.square(np.linalg.norm(W_next[:, i]))

                if f_mid > p_max:
                    eta_min = eta_mid
                else:
                    eta_max = eta_mid

                n_iter2 = n_iter2 + 1
        # update gamma
        for i in range(M):
            gamma_next[i] = np.square(abs(np.matmul(H[i, i, :], W_next[:, i]))) / \
                       (np.square(np.linalg.norm(np.diag(np.matmul(H[:, i, :], W_next)))) + noise_power - np.square(
                           abs(np.matmul(H[i, i, :], W_next[:, i]))))

        y = y_next
        W = W_next
        gamma = gamma_next
        sum_throughput_next = f.cal_throughput(H, W, noise_power)
        n_iter1 = n_iter1 + 1
    end = time.clock()
    # print(str(end-start))
    cn.update(ir_change=False, weights=W)
    utility.append(cn.get_ave_utility())
    cn.update(ir_change=True)


# save data
filename = 'data/fp_performance.json'
with open(filename, 'w') as f:
    json.dump(utility, f)

