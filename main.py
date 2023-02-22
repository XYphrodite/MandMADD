import matplotlib.pyplot as plt
import numpy as np

deltaC = 0.4
deltaM = 0.2
deltaT = 0.5

Tp = 90
r = 2.26 * 10 ** 6
kt = 5000
F = 10
C_tau = 4187

C0 = 7.5
C1 = 12
C_input = 8

m0 = 3.8
m1 = 5.5
m_input = 4

T0 = 125
T1 = 140
T_n = 140


def Count_C_output_from_C(C_input):
    res = (m_input * C_input) / (m_input - (kt * F * (T_n - Tp)) / (r - Tp * C_tau))
    return res


def Count_C_output_from_m(m_input):
    res = (m_input * C_input) / (m_input - (kt * F * (T_n - Tp)) / (r - Tp * C_tau))
    return res


def Count_C_output_from_T(T_n):
    res = (m_input * C_input) / (m_input - (kt * F * (T_n - Tp)) / (r - Tp * C_tau))
    return res

fig, axs = plt.subplots(1, 3)

c1OArr = []
c1IArr = np.arange(C0, C1, deltaC)
for i in c1IArr:
    c1OArr.append(Count_C_output_from_C(i))

c2OArr = []
c2IArr = np.arange(m0, m1, deltaM)
for i in c2IArr:
    c2OArr.append(Count_C_output_from_m(i))

c3OArr = []
c3IArr = np.arange(T0, T1, deltaT)
for i in c3IArr:
    c3OArr.append(Count_C_output_from_T(i))

axs[0].plot(c1IArr, c1OArr, "red")
axs[0].set_title('C_вых(C_вх)')

axs[1].plot(c2IArr, c2OArr, "red")
axs[1].set_title('C_вых(m_вх)')

axs[2].plot(c3IArr, c3OArr, "red")
axs[2].set_title('C_вых(T_п)')
plt.show()
