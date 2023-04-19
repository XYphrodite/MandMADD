import math

a = 1.3 * 10e-2 #m2/sec
delta_x = 0.1 #m
X = 1 #m
tau_max = 100 #s

def fi(x):
    return 35 - math.pow(x + 2, 2)


def f_1(tau):
    return 11 + 2 / (0.1 * tau + 0.1)


def f_2(tau):
    return 26 - 10 * math.sin(tau)
