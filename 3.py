import math

import matplotlib
from matplotlib import pyplot as plt

C_inp = 0.35
T = 1300
L = 210
m0 = 1.5
m1 = 2.0

R = 8.31
E1 = 251000
E2 = 297000
A1 = 2 * math.pow(10, 11)
A2 = 8 * 10 ** 12
p = 1.4
D = 0.1
deltaL = 0.5
delta_m = 0.15
u_et = 35.65


def count_k1():
    #print(A1 * math.exp(-E1 / (R * T)))
    return A1 * math.exp(-E1 / (R * T))


def count_k2():
    return A2 * math.e * (-E2 / R * T)


def count_C_u():
    return C_inp * p / (100 * u_et)


def count_C1(C1, m, dl):
    #print(count_k1())
    return (-count_k1() * C1 * (math.pi * D ** 2) / 4 * p) / m * dl


def count_C2(C1, m, dl, C2):
    return (count_k1() * C1 - count_k2() * C2) * (math.pi * D ** 2 / 4) * p / m * dl


l_arr2 = []
c_arr2 = []

m_now = m0
while m_now < m1:
    L_init = 0
    l_arr = []
    c_arr = []
    C_init = C_inp
    while L_init < L:
        l_arr.append(L_init)
        newC1 = count_C1(C_init, m_now, deltaL)
        print(newC1)
        C_init = newC1
        c_arr.append(newC1)
        L_init += deltaL
    l_arr2.append(l_arr)
    c_arr2.append(c_arr)
    m_now += delta_m

# print(l_arr2, c_arr2)

fig, axs = plt.subplots(1, 2)

axs[0].plot(l_arr2[0], c_arr2[0], "red")

plt.show()
