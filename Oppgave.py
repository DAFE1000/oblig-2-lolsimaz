import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x/4) * np.arctan(x)

def g(x):
    return -1/4 * np.exp(-x/4) * np.arctan(x) + np.exp(-x/4) * 1/(1 + x**2)

#Finner toppunktet med halveringsmetoden

def halveringsmetoden(a,b,tol):
    while True:
        mid = (a + b) / 2
        g_mid = g(mid)
        if abs(g_mid) < tol:
            return mid
        elif g(a) * g_mid < 0:
            b = mid
        else:
            a = mid
print(halveringsmetoden(0,3,1e-10))

#Toppunkter er 1.6907 med 4 desimaler

#Plotter topp punktet
x_topp = 1.6907081552781165
y_topp = f(x_topp)

x = np.linspace(0.1, 10, 100)
plt.plot(x, f(x), label='f(x)')
plt.scatter(x_topp,y_topp, label = 'Toppunkt')
plt.title ('Plot of f(x) = exp(-x/4) * tan(x)^-1')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()


