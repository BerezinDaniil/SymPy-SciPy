import sympy
import numpy as np
import matplotlib.pyplot as plt

f = open('large.txt', 'r')
k = 0
while True:
    line = f.readline()
    if not line:
        break
    if len(line.split()) == 1:
        N = int(line.split()[0])
        A = np.zeros((N, N))
        b = np.zeros((N,))
    if (k < N) and (len(line.split()) == N):
        m = 0
        while m != N:
            for i in line.split():
                A[k][m] = float(i)
                m += 1
        k += 1
    elif (k >= N):
        m = 0
        while m != N:
            for i in line.split():
                b[m] = float(i)
                m += 1

print(np.linalg.solve(A, b))
objects = np.arange(1,N+1)
y_pos = np.arange(len(objects))
performance = np.linalg.solve(A, b)

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.grid()
plt.show()
f.close()
