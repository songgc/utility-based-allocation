# By Guocong Song

import numpy as np


def arg_max(r):
    u_num = r.shape[0]
    assign = np.argmax(r, axis=0)
    r_tot = [r[i, :][assign == i].sum() for i in range(u_num)]
    return assign, r_tot


def utiliy_opt_2_users(r, u_func, du_func):
    ratio = r[1, :] / r[0, :]
    idx_sort = np.argsort(ratio)
    
    low, high = 0, len(ratio)
    while high - low > 1:
        mid = low + (high - low) / 2
        _, r_tot = assign_from_mid(r, idx_sort, mid)
        if du_func[0](r_tot[0]) / du_func[1](r_tot[1]) < ratio[mid]:
            low, high = low, mid
        else:
            low, high = mid, high

    assign_low, r_tot_low = assign_from_mid(r, idx_sort, low)
    assign_high, r_tot_high = assign_from_mid(r, idx_sort, high)
    if u_func[0](r_tot_low[0]) + u_func[0](r_tot_low[1]) > u_func[1](r_tot_high[0]) + u_func[1](r_tot_high[1]):
        return assign_low, r_tot_low
    else:
        return assign_high, r_tot_high


def assign_from_mid(r, idx_sort, mid):
    assign = np.array([1] * len(idx_sort))
    assign[idx_sort[0 : mid]] = 0
    r_tot = np.array([r[i, :][assign == i].sum() for i in range(2)])
    return assign, r_tot
