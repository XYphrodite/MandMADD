import math
import matplotlib.pyplot as plt
import numpy

lamb_1 = 0.4211  #
lamb_2 = 0.7371  #
M_0 = 15  #
sigma_Sqr_0 = 3  #
alfa_0 = 0.15  #

epsilon = 0.004  #
A1 = 1  # 1.7  #
A2 = 1  # 0.32  #
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


def Square(arr):
    _sum = 0
    for i in arr:
        _sum += (i - Middle(arr)) ** 2
    return _sum / len(arr)


def Process(k):
    i = k
    sum2 = 0
    while i < k + Ns:
        sum2 += rand_arr[i] * math.pow((sigma_Sqr_0 / (alfa_0 * A2 * Square(rand_arr))), 0.5) * A1 * math.exp(
            -A2 * alfa_0 * (i - k))
        i += 1
    return (sum2 / Ns) + M_0


def Korrel(z, S):
    p = 0
    sum3 = 0
    for p in range(len(z) - S):
        sum3 += (z[p] - Middle(z)) * (z[p + S] - Middle(z))
        p += 1
    return sum3 / p


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

while abs(Square(randProcessArr) - sigma_Sqr_0) > 0.3:
    print(Square(randProcessArr))
    randProcessArr.clear()
    A2 -= 0.01
    A1 += 0.01
    randProcessArr = GetRandomArr()

i = 0
# Korrelate teoretic f[i]
while i < S:
    Corr_arr.insert(i, Korrel(randProcessArr, i))
    i += 1

alfa_f = 0
i = 0
Fi = 10000

while Fi > epsilon:
    Fi = 0
    Corr_arr_.clear()
    while i < S:
        Fi += (Square(randProcessArr) * math.exp(-alfa_f * i) - Corr_arr[i]) ** 2
        Corr_arr_.insert(i, Square(randProcessArr) * math.exp(-alfa_f * i))
        i += 1
    alfa_f += 0.01
    Fi = Fi / S
    i = 0

alfa_f -= 0.01

print("Среднее ряда=", Middle(rand_arr))
print("Мат.ожидание ряда=", Square(rand_arr))
print("Среднее случ. функции=", Middle(randProcessArr))
print("Мат.ожидание функции=", Square(randProcessArr))
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
