import math
import matplotlib.pyplot as plt
import numpy

lamb_1 = 0.4211  #
lamb_2 = 0.7371  #
M_0 = 15  #
sigma_Sqr_0 = 3  #
alfa_0 = 0.15  #

epsilon = 0.004  #
A1 = 1.68  # 1.7
A2 = .32  # 0.32
Ns = 15  #

lamb_3 = 0
S = 6  # 5 или 6
N = 200


def rand(l1, l2):
    l3 = (l1 * l2 * 1e8) // 100
    l3 = l3 % 10000
    l3 = l3 / 10000
    return l3


Middle = lambda arr: sum(arr) / len(arr)


def Dispersion(arr):
    _sum = 0
    for i in arr:
        _sum += (i - Middle(arr)) ** 2
    return _sum / len(arr)


def Process(k):
    i = k
    sum2 = 0
    while i < k + Ns:
        sum2 += rand_arr[i] * math.pow((sigma_Sqr_0 / (alfa_0 * A2 * Dispersion(rand_arr))), 0.5) * A1 * math.exp(
            -A2 * alfa_0 * (i - k))
        i += 1
    return (sum2 / Ns) + M_0


def Corell(z, S):
    p = 0
    sum3 = 0
    for p in range(len(z) - S):
        sum3 += (z[p] - Middle(z)) * (z[p + S] - Middle(z))
        p += 1
    return sum3 / p


def Corell2(S, alpha):
    return Dispersion(randProcessArr) * math.exp(-alpha * S)


def GetRandomArr():
    arr = []
    i = 0
    while i < N - Ns:
        arr.append(Process(i))
        i += 1
    return arr


rand_arr = []
Corr_arr = []
Corr_arr_ = []
alfa = []
randProcessArr = []

oldA = 0
aldM = 0

# random
for i in range(N - 1):
    rand_arr.append(lamb_1 - 0.5)
    lamb_3 = rand(lamb_1, lamb_2)
    lamb_1 = lamb_2
    lamb_2 = lamb_3

i = 0
# random f
randProcessArr = GetRandomArr()

oldS = Dispersion(randProcessArr)
dd = abs(Dispersion(randProcessArr) - sigma_Sqr_0)
h = 0.1

# co f[i]
i = 0
while i < S:
    Corr_arr.insert(i, Corell(randProcessArr, i))
    i += 1

alfa_f = 0
Fi = 10000

i = 0
while Fi > epsilon:
    Fi = 0
    Corr_arr_.clear()
    while i < S:
        Fi += (Corell2(i,alfa_f) - Corr_arr[i]) ** 2
        Corr_arr_.insert(i, Corell2(i,alfa_f))
        i += 1
    alfa_f += 0.01
    Fi = Fi / S
    i = 0

alfa_f -= 0.01

print("Мат. ожидания ряда = ", Middle(rand_arr))
print("Дисперсия ряда = ", Dispersion(rand_arr))
print("Мат. ожидание  = ", Middle(randProcessArr))
print("Дисперсия = ", Dispersion(randProcessArr))
print("Параметр аппроксимации функции = ", alfa_f)

# graph
TN = numpy.arange(0, N - Ns)
TS = numpy.arange(0, S)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.set_ylabel('Знач. случ. процесса')
ax1.set_xlabel('N')

ax1.plot(TN, randProcessArr)

ax2.set_ylabel('Знач. коррел. функции')
ax2.set_xlabel('S')

ax2.plot(TS, Corr_arr, color="blue", marker=".")
ax2.plot(TS, Corr_arr_, color="red", marker=".")

plt.show()
