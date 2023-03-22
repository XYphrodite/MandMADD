import math
import matplotlib.pyplot as plt

kt = 5000
F = 10
Ts = 90
r = 2260000
ct = 4187

S = 0.75
sig = 0.12

P0 = 7900
P1 = 7600


def find_m_sv(Tv):
    return (kt * F * (Tv - Ts)) \
        / (r - ct * Ts)


def find_M(m_in, m_sv):
    return S * (((m_in - m_sv) / sig) ** 2 + P1 - P0)


def find_m_out(M):
    return sig * math.sqrt(P0 + M / S - P1)


def find_prime(y2, y1, dx):
    return (y2 - y1) / dx


def find_new_M(m_in, m_out, Tv, M, dt):
    return ((r * m_in - r * m_out - kt * F * (Tv - Ts) - (m_in - m_out) * ct * Ts) * dt) / (r - ct * Ts) + M


def find_new_C_out(C_in, C_out, m_in, m_out, M, dM, dt):
    return ((m_in * C_in - m_out * C_out - C_out * dM) * dt) / M + C_out


def f(C_in, C_out, m_in, M, Tv, dt):
    m_out = find_m_out(M)
    M2 = find_new_M(m_in, m_out, Tv, M, dt)
    dM = find_prime(M2, M, dt)
    C_out2 = find_new_C_out(C_in, C_out, m_in, m_out, M2, dM, dt)

    return [C_out2, M2]


C_ins = [(7.5+12)/2, 8, 8]
m_ins = [4, (3.8+5.5)/2, 4]
Tvs = [140, 140, 140]
C_outs = [11.3, 12.3, 10.5] #
C_outs2 = [17.8, 10.625, 11.9] #
Cs1, Cs2, Cs3 = [], [], []

deltaC_in = 3.8
deltaM_in = 1.9
deltaTv = 6

ts = [0, 500]
_dt = 0.1

# finding C_in to C_out
_C_in = C_ins[0] + deltaC_in
_m_sv = find_m_sv(Tvs[0])
M1 = find_M(m_ins[0], _m_sv)
_C_out = C_outs[0]
t = ts[0]
while t <= ts[1]:
    _C_out, M1 = f(_C_in, _C_out, m_ins[0], M1, Tvs[0], _dt)
    Cs1.append(_C_out)
    t += _dt

_m_in = m_ins[1] + deltaM_in
_m_sv = find_m_sv(Tvs[1])
M2 = find_M(_m_in, _m_sv)
_C_out = C_outs[1]
t = ts[0]
while t <= ts[1]:
    _C_out, M2 = f(C_ins[1], _C_out, _m_in, M2, Tvs[1], _dt)
    Cs2.append(_C_out)
    t += _dt

_Tv = Tvs[2] + deltaTv
_m_sv = find_m_sv(_Tv)
M3 = find_M(m_ins[2], _m_sv)
_C_out = C_outs[2]
t = ts[0]
while t <= ts[1]:
    _C_out, M3 = f(C_ins[2], _C_out, m_ins[2], M3, _Tv, _dt)
    Cs3.append(_C_out)
    t += _dt

print("C:\nОт ", C_outs[0], " к ", Cs1[len(Cs1) - 1], " (истинное значение = ", C_outs2[0], ")")
print("M:\nОт ", C_outs[1], " к ", Cs2[len(Cs2) - 1], " (истинное значение = ", C_outs2[1], ")")
print("T:\nОт ", C_outs[2], " к ", Cs3[len(Cs3) - 1], " (истинное значение =  ", C_outs2[2], ")")

#графики
tt = []
t = ts[0] - 100
while t <= ts[1] + 100:
    tt.append(t)
    t += _dt

C1, C2, C3 = [], [], []
CCs1, CCs2, CCs3 = [], [], []
for i in range(1000):
    Cs1.append(Cs1[len(Cs1) - 1])
    Cs2.append(Cs2[len(Cs2) - 1])
    Cs3.append(Cs3[len(Cs3) - 1])
    CCs1.append(C_outs[0])
    CCs2.append(C_outs[1])
    CCs3.append(C_outs[2])
    C1.append(C_ins[0])
    C2.append(m_ins[1])
    C3.append(Tvs[2])
Cs1 = CCs1 + Cs1
Cs2 = CCs2 + Cs2
Cs3 = CCs3 + Cs3

for i in range(6000):
    C1.append(C_ins[0] + deltaC_in)
    C2.append(m_ins[1] + deltaM_in)
    C3.append(Tvs[2] + deltaTv)

fig, axis = plt.subplots(2, 3)
fig.tight_layout()

axis[0][0].plot(tt, Cs1)
axis[0][0].set_title("От концентрации")
axis[0][0].set_xlabel("Время")
axis[0][0].set_ylabel("Концентрация")
axis[1][0].plot(tt, C1)
axis[1][0].set_xlabel("Время")
axis[1][0].set_ylabel("Концентрация на входе")

axis[0][1].plot(tt, Cs2)
axis[0][1].set_title("От массы")
axis[0][1].set_xlabel("Время")
axis[0][1].set_ylabel("Концентрация")
axis[1][1].plot(tt, C2)
axis[1][1].set_xlabel("Время")
axis[1][1].set_ylabel("Масса")

axis[0][2].plot(tt, Cs3)
axis[0][2].set_title("От температуры пара")
axis[0][2].set_xlabel("Время")
axis[0][2].set_ylabel("Концентрация")
axis[1][2].plot(tt, C3)
axis[1][2].set_xlabel("Время")
axis[1][2].set_ylabel("Температура пара")

plt.show()
