import math
from matplotlib import pyplot as plt

a = 1.3 * 10**-2 #m2/sec
delta_x = 0.1 #m
X = 1 #m
tau_max = 100 #s
t_max = 100
dt = 0.5*delta_x*delta_x*25

def fi(x):
    return 35 - math.pow(x + 2, 2)


def f_1(tau):
    return 11 + 2 / (0.1 * tau + 0.1)


def f_2(tau):
    return 26 - 10 * math.sin(tau)

def find_new_T(T2, T1, T0, dt, dx):
    return (a*dt/(dx*dx))*(T2 - 2*T1 + T0) + T1

Tji = [[]]

t = 0
x = 0
while x+delta_x < X:
    Tji[0].append(fi(x))
    x += delta_x
Tji[0].append(f_2(t))
t += dt

j = 1
while t < t_max:
    Tj = f_1(t)
    Tji.append([Tj])
    i = 1
    x = delta_x
    while x+delta_x < X:
        Ti = find_new_T(Tji[j - 1][i + 1], Tji[j - 1][i], Tji[j - 1][i - 1], dt, delta_x)
        Tji[j].append(Ti)
        x += delta_x
        i += 1
    Tji[j].append(f_2(t))
    t += dt
    j += 1

# graph
Tt = []
Tx = []
T_arr = []
for j in range(len(Tji)):
    for i in range(len(Tji[j])):
        Tt.append(dt*j)
        Tx.append(delta_x*i)
        T_arr.append(Tji[j][i])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(Tx, Tt, T_arr, marker=".")

plt.show()
