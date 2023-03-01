import math
import matplotlib.pyplot as plt
import numpy as np

deltaC = 3.8
deltaM = 1.9
deltaT = 6

omega = 0.12
S = 0.75
P_0 = 7900
P_1 = 7600

tau_0 = 0
tau_max = 500
delta_tau = 0.1

T_rastvor = 90
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


def Get_dM_dt(m_input, m_output, T0):
    return (r(m_input - m_output) - kt * F * (T0 - T_rastvor) - (m_input - m_output) * C_tau * T_rastvor) / (
            r - C_tau * T_rastvor)


def find_dC_out(C_input, C_output, m_input, m_output, M, dM):
    return (m_input * C_input - m_output * C_output - C_output * dM) / M


def Get_M(m_input, m_second):
    return S * (math.pow((m_input - m_second) / omega, 2) + P_1 - P_0)
