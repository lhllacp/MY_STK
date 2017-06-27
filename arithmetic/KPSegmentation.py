
import numpy as np
import matplotlib.pyplot as plt

BETA=0.5;
DISTANCE=0
def KPSegmentation(x):
    y=[]
    x_ie=[0]
    x_t=[]
    x_e=[]
    for i in range(1, len(x)-1):
        if (x[i] > x[i-1] and x[i] > x[i + 1]) or (x[i] < x[i-1] and x[i] < x[i+1]):
            x_ie.append(i)
        
        if x[i] - abs((x[i+1] - x[i-1])) / 2 > BETA:
            x_t.append(i)
    x_e.append(0)
    for i in range(1, len(x_ie)):
        if x_ie[i] - x_ie[i -1] > DISTANCE:
            x_e.append(x_ie[i])
    x_e.append(len(x) -1)
    x0 = list(set(x_e).union(set(x_t)))
    x0.sort()
    print(x0)
    for i in x0:
        y.append(x[i])
    return x0, y

if __name__ == "__main__":
    #numbers = [ int(x) for x in numbers ]
    x=[5, 1, 3, 2, 6, 10, 8, 7, 2, 9, 4, 2, 5, 8, 9, 10, 20, 15, 3, 2, 2, 6, 10]
    t = np.arange(len(x))
    for i in range(1,3):
        print(i)
    print(len(t))
    plt.plot(t, np.array(x))
    x0, y0 = KPSegmentation(x)
    plt.plot(x0, y0)
    plt.show()
    print(x0)
    print(y0)
    pass