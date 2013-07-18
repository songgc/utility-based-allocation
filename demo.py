# By Guocong Song

import numpy as np
from utl_opt import arg_max, utiliy_opt_2_users
import matplotlib.pyplot as plt


def u_func(x):
    return np.log(0.001 + x)

def du_func(x):
    return 1.0 / (0.001 + x)

K = 200
item_count = [0] * 2
ratio = []
r_s = np.array([0.0, 0.0])
n_iter = 10000

for i in range(n_iter):
    r1 = np.random.exponential(1.00, (1, K))
    r2 = np.random.exponential(10.0, (1, K))
    r = np.append(r1, r2, axis=0)
    assign, r_tot = utiliy_opt_2_users(r, [u_func]*2, [du_func]*2)
#     assign, r_tot = arg_max(r)
    item_count[0] += len(assign[assign == 0])
    item_count[1] += len(assign[assign == 1])
    ratio.append((item_count[1] + 1.0) / (item_count[0] + 1.0))
    r_s += r_tot
print item_count
print r_s / n_iter
plt.plot(ratio)
plt.ylabel("assigned resource entity ratio")
plt.grid()
plt.show()

