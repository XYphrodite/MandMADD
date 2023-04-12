import math

# l — hor
# tau — 135grad for T and l axis
k_T = 6500  # Wt/m2
c_t = 4190  # J/(kg*grad)
p = 1000  # kg/m3
T_T = 80  # gradCel
D = 0.05  # m
u = 0.2  # m/s
tau_max = 10  # s

delta_alpha = 0.3
delta_beta = 0.2


def countT_0(l):
    return 35 - math.pow(l + 2, 2)


def countT_inp(tau):
    return 11 + 2 / (0.1 * tau + 0.1)
