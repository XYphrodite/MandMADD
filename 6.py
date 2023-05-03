import math
#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


################################################
#Random_gen_congtuent(var_1-15)
#def rand(x):
#    return ((lamb1*x) % lamb2)/lamb2 - 0.5


#Random_gen_multiplications(var_16-19)
def rand(lamb1,lamb2):
    lamb3 = (lamb1*lamb2*100000000)//100
    lamb3 = lamb3 % 10000
    lamb3 = lamb3 / 10000
    return lamb3


#Random_gen_irrational(var_21-50)
#def rand(x):
#    return x*lamb2 % 1-0.5

#Find M-middle
def Middle(z):
    i = 0
    sum = 0
    for i in range(len(z)):
        sum += z[i]
    return sum/i


#Find middle-square
def Square(z):
    j = 0
    sum1 = 0
    for j in range(len(z)):
        sum1 += (z[j]-Middle(z))**2
    return sum1/j


#Gen_random_process
def Process(k):
    l = k
    sum2 = 0
    while l < k+Ns:
        sum2 += z[l]*((sigma_sqr_0 / (alfa0*A2* Square(z))) ** 0.5)*A1 * math.exp(- alfa0 *A2* (l-k))
        l+=1
    return (sum2/Ns)+M0


#Korrelation
def Korrel(S):
     p=0
     sum3=0
     for p in range(len(f)-S):
        sum3 += (f[p]-Middle(f))*(f[p+S]-Middle(f))
        #p+=1
     return sum3/p

###########################################

z = []
K = []
Kp = []
alfa = []
f = []


#################
lamb1 = 0.4211  #
lamb2 = 0.7371  #
M0 = 15        #
sigma_sqr_0 = 3 #
alfa0 = 0.15    #
#################
epsilon = 0.004   #
A1 = 1.7        #
A2 = 0.32       #
Ns = 15         #
#################


lamb3 = 0 #only (var_16-19)
S = 6 #или 5 или 6
N = 200

###########################################

#Generate random z[i]

#z.insert(0, ((lamb1*1) % lamb2)/lamb2 - 0.5)  #only var_1-15
#z.insert(0,lamb1%1-0.5)                       #only var_21-50
m = 0
while m < N-1:
    z.insert(m+1, lamb1-0.5)  #only var_16-19
    lamb3 = rand(lamb1,lamb2) #only var_16-19
    lamb1 = lamb2             #only var_16-19
    lamb2 = lamb3             #only var_16-19

  #  z.insert(m+1, rand(z[m]))  #only var_1-15 and var_21-50
    m += 1
m = 0


print("Среднее ряда=",Middle(z))
print("Мат.ожидание ряда=",Square(z))


#Generate random function f[i]
while m < N-Ns:
    f.insert(m, Process(m))
    m += 1
m = 0


# Korrelate teoretic f[i]
while m < S:
   K.insert(m, Korrel(m))
   m += 1


alfa_f = 0
m = 0
Fi = 10000
l = 0


print("Среднее случ. функции=",Middle(f))
print("Мат.ожидание функции=",Square(f))


## Korrelate practic and aproximate K teoretic
while Fi > epsilon:
    Fi = 0
    Kp.clear()
    while m < S:
        Fi += (Square(f)*math.exp(-alfa_f*m)-K[m])**2
        Kp.insert(m, Square(f)*math.exp(-alfa_f*m))
        m += 1
    l += 1
    alfa_f += 0.01
    Fi = Fi/S
  #  print(Fi)
    m = 0


alfa_f-=0.01
m=0

print("Параметр аппроксимации функции=",alfa_f)
##############################################


# graph
TN = []
TS = []
j=0
while j < N-Ns:
        TN.append(j)
        j+=1

j=0
while j < S:
        TS.append(j)
        j+=1



fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.set_ylabel('Знач. случ. процесса')
ax1.set_xlabel('N')

ax1.plot(TN, f)

ax2.set_ylabel('Знач. коррел. функции')
ax2.set_xlabel('S')

ax2.plot(TS, K,color="blue", marker=".")
ax2.plot(TS, Kp,color="red", marker=".")

plt.show()