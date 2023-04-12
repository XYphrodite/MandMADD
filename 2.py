import math

from matplotlib import pyplot as plt

kt = 5000
F = 10
Ts = 90
r = 2260000
ct = 4187
S = 0.75
sig = 0.12
P0 = 7900
P1 = 7600


def count_m_sv(Tv):
    return (kt * F * (Tv - Ts)) / (r - ct * Ts)


def count_M(m_in, m_sv):
    return S * (((m_in - m_sv) / sig) ** 2 + P1 - P0)


def count_m_out(M):
    return sig * math.sqrt(P0 + M / S - P1)


def count_prime(y2, y1, dx):
    return (y2 - y1) / dx


def count_new_M(m_in, m_out, Tv, M, dt):
    return ((r * m_in - r * m_out - kt * F * (Tv - Ts) - (m_in - m_out) * ct * Ts) * dt) / (r - ct * Ts) + M


def count_new_C_out(C_in, C_out, m_in, m_out, M, dM, dt):
    return ((m_in * C_in - m_out * C_out - C_out * dM) * dt) / M + C_out


def count(C_in, C_out, m_in, M, Tv, dt):
    m_out = count_m_out(M)
    M2 = count_new_M(m_in, m_out, Tv, M, dt)
    dM = count_prime(M2, M, dt)
    C_out2 = count_new_C_out(C_in, C_out, m_in, m_out, M2, dM, dt)

    return [C_out2, M2]


C_ins = [(7.5 + 12) / 2, 8, 8]
m_ins = [4, (3.8 + 5.5) / 2, 4]
Tvs = [140, 140, 140]
C_outs = [11.3, 12.3, 10.5]
C_outs2 = [17.81, 10.61, 11.91]
C_1, C_2, C_3 = [], [], []

deltaC_in = 3.8
deltaM_in = 1.9
deltaTv = 6

borders = [0, 500]
dt = 0.1

C_input = C_ins[0] + deltaC_in
M_sv = count_m_sv(Tvs[0])
M1 = count_M(m_ins[0], M_sv)
C_output = C_outs[0]
time = borders[0]
while time <= borders[1]:
    C_output, M1 = count(C_input, C_output, m_ins[0], M1, Tvs[0], dt)
    C_1.append(C_output)
    time += dt

M_input = m_ins[1] + deltaM_in
M_sv = count_m_sv(Tvs[1])
M2 = count_M(M_input, M_sv)
C_output = C_outs[1]
time = borders[0]
while time <= borders[1]:
    C_output, M2 = count(C_ins[1], C_output, M_input, M2, Tvs[1], dt)
    C_2.append(C_output)
    time += dt

T_input = Tvs[2] + deltaTv
M_sv = count_m_sv(T_input)
M3 = count_M(m_ins[2], M_sv)
C_output = C_outs[2]
time = borders[0]
while time <= borders[1]:
    C_output, M3 = count(C_ins[2], C_output, m_ins[2], M3, T_input, dt)
    C_3.append(C_output)
    time += dt



tt = []
time = borders[0] - 100
while time <= borders[1] + 100:
    tt.append(time)
    time += dt

ChC, ChM, ChT = [], [], []
CCs1, CCs2, CCs3 = [], [], []
#первые 100 секунд и последние
for i in range(1000):
    C_1.append(C_1[len(C_1) - 1]) #конеченое значение
    C_2.append(C_2[len(C_2) - 1])
    C_3.append(C_3[len(C_3) - 1])
    CCs1.append(C_outs[0]) #начальное значение
    CCs2.append(C_outs[1])
    CCs3.append(C_outs[2])
    ChC.append(C_ins[0])
    ChM.append(m_ins[1])
    ChT.append(Tvs[2])
C_1 = CCs1 + C_1
C_2 = CCs2 + C_2
C_3 = CCs3 + C_3

for i in range(6000):
    ChC.append(C_ins[0] + deltaC_in)
    ChM.append(m_ins[1] + deltaM_in)
    ChT.append(Tvs[2] + deltaTv)

fig, axis = plt.subplots(2, 3)

axis[0][0].plot(tt, C_1)
axis[0][0].set_title("От концентрации")
axis[0][0].set_xlabel("Время")
axis[0][0].set_ylabel("Концентрация")
axis[1][0].plot(tt, ChC)
axis[1][0].set_xlabel("Время")
axis[1][0].set_ylabel("Концентрация на входе")

axis[0][1].plot(tt, C_2)
axis[0][1].set_title("От массы")
axis[0][1].set_xlabel("Время")
axis[0][1].set_ylabel("Концентрация")
axis[1][1].plot(tt, ChM)
axis[1][1].set_xlabel("Время")
axis[1][1].set_ylabel("Масса")

axis[0][2].plot(tt, C_3)
axis[0][2].set_title("От температуры пара")
axis[0][2].set_xlabel("Время")
axis[0][2].set_ylabel("Концентрация")
axis[1][2].plot(tt, ChT)
axis[1][2].set_xlabel("Время")
axis[1][2].set_ylabel("Температура пара")

plt.show()
