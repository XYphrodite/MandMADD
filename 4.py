import math

from matplotlib import pyplot as plt

# l — hor
# tau — 135grad for T and l axis
k_T = 6500  # Wt/m2
c_t = 4190  # J/(kg*grad)
p = 1000  # kg/m3
T_T = 80  # gradCel
D = 0.05  # m
u = 0.2  # m/s
tau_max = 10  # s
L = 1  # m

delta_alpha = 0.3
delta_beta = 0.2


def countT_0(l):
    return 35 - math.pow(l + 2, 2)


def countT_inp(tau):
    return 11 + 2 / (0.1 * tau + 0.1)


def findNewT(T, delta_a):
    return ((T_T - T) * 4 * k_T / (c_t * p * D)) * delta_a + T


def appendVals(T, a, b):
    T_arr.append(T)
    a_arr.append(a)
    b_arr.append(b)
    l_arr.append(u * (a - b))
    t_arr.append(a + b)


# initial values
T_arr, a_arr, b_arr, l_arr, t_arr = [], [], [], [], []
ts = L / u

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# computing

# first domain
b = -ts / 2  # [-ts/2,0]
a = -b
T = countT_0(-2 * u * b)
while b <= 0:
    a = -b
    T = countT_0(-2 * u * b)
    while a <= b + ts:
        appendVals(T, a, b)
        T = findNewT(T, delta_alpha)
        a += delta_alpha
    b += delta_beta
ax.scatter(l_arr, t_arr, T_arr, edgecolor="green")
T_arr, a_arr, b_arr, l_arr, t_arr = [], [], [], [], []
# second domain
b = 0
a = b
T = countT_inp(2 * b)
while b <= (tau_max - ts) / 2:
    a = b
    T = countT_inp(2 * b)
    while a <= b + ts:
        appendVals(T, a, b)
        T = findNewT(T, delta_alpha)
        a += delta_alpha
    b += delta_beta
ax.scatter(l_arr, t_arr, T_arr, edgecolor="yellow")
T_arr, a_arr, b_arr, l_arr, t_arr = [], [], [], [], []
# third domain
b = (tau_max - ts) / 2
a = b
T = countT_inp(2 * b)
while b <= tau_max / 2:
    a = b
    T = countT_inp(2 * b)
    while a <= -b + ts:
        appendVals(T, a, b)
        T = findNewT(T, delta_alpha)
        a += delta_alpha
    b += delta_beta
ax.scatter(l_arr, t_arr, T_arr, marker='^', edgecolors='black')
print(T_arr)


plt.show()
