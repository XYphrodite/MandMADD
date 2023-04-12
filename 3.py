import math

import matplotlib
from matplotlib import pyplot as plt

C_inp = 0.35
C2_init = 0
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


def countMol(C):
    return C * p / (100 * u_et)


def countPercent(C):
    return C * 100 * u_et / p


def count_k1():
    return A1 * math.exp(-E1 / (R * T))


def count_k2():
    return A2 * math.exp(-E2 / (R * T))


def count_C_u():
    return C_inp * p / (100 * u_et)


def count_C1(C1, m, dl):
    return (-count_k1() * C1 * ((math.pi * D ** 2) / 4) * p) / m * dl + C1


def count_C2(C1, m, dl, C2):
    return (count_k1() * C1 - count_k2() * C2) * (math.pi * D ** 2 / 4) * p / m * dl + C2


l_arr2 = []
c_arr2 = []
c2_arr2 = []
m_arr = []

m_now = m0
while m_now < m1:
    m_arr.append(m_now)
    L_init = 0
    l_arr = []
    c_arr = []
    c2_arr = []
    C_init = countMol(C_inp)
    newC2 = C2_init
    while L_init < L:
        l_arr.append(L_init)
        newC1 = count_C1(C_init, m_now, deltaL)
        C_init = newC1
        c_arr.append(countPercent(newC1) * 100)
        newC2 = count_C2(C_init, m_now, deltaL, newC2)
        c2_arr.append(countPercent(newC2) * 100)
        L_init += deltaL
    l_arr2.append(l_arr)
    c_arr2.append(c_arr)
    c2_arr2.append(c2_arr)
    m_now += delta_m

fig, axs = plt.subplots(1, 2)

for i in range(len(c_arr2)):
    axs[0].plot(l_arr2[i], c_arr2[i], label=f"M = {round(m_arr[i], 2)}")
    axs[1].plot(l_arr2[i], c2_arr2[i], label=f"M = {round(m_arr[i], 2)}")
    axs[0].set_title("Концентрация этилена")
    axs[0].set_xlabel("L, м")
    axs[0].set_ylabel("C1, %")
    axs[1].set_title("Концентрация ацитилена")
    axs[1].set_xlabel("L, м")
    axs[1].set_ylabel("C2, %")
axs[0].legend()
axs[1].legend()

plt.show()
