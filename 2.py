import math

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


C_ins = [(7.5+12)/2, 8, 8]
m_ins = [4, (3.8+5.5)/2, 4]
Tvs = [140, 140, 140]
C_outs = [11.3, 12.3, 10.5]
C_outs2 = [17.81, 10.61, 11.91]
Cs1, Cs2, Cs3 = [], [], []

deltaC_in = 3.8
deltaM_in = 1.9
deltaTv = 6

ts = [0, 500]
_dt = 1

#######################################

'''
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
'''
