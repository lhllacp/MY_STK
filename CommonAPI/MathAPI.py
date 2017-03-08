from math import pow, sqrt
def del_zero(x):
    x_len = len(x)
    i = 0
    while i < x_len:
        if x[i] == 0:
            i = i + 1
        else:
            break
    if i != x_len:
        return x[i:]
    else:
        return None

def ema(e, x, n):
    try:
        if e == 0.0:
            return x
        a = 2 / (n+1)
        y = a * x + (1 - a) * e
        return y
    except:
        print("%f %f %f"%(e, x, n))

def EMA(x, n):
    x_len = len(x)
    y=[]    
    y.append(x[0])       
    i = 1
    while i < x_len:
        e = ema(y[-1], x[i], n)
        y.append(e)
    return y
def hhv(x):
    m = 0
    for i in x:
        if i > m:
            m = i
    return m
def HHV(x, n):
    x_len = len(x)
    y=[]
    y.append(x[0])
    i = 1
    while i < x_len:
        if i <= (n - 1):
            t = hhv(x[0:i+1])
            y.append(t)
        else:
            t = hhv(x[i-n+1:i+1])
            y.append(t)
        i = i + 1
    return y
def llv(x):
    m = x[0]
    for i in x:
        if i < m:
            m = i
    return m
def LLV(x, n):
    x_len = len(x)
    y=[]
    y.append(x[0])
    i = 1
    while i < x_len:
        if i <= (n - 1):
            t = llv(x[0:i+1])
            y.append(t)
        else:
            t = llv(x[i-n+1:i+1])
            y.append(t)
        i = i + 1
    return y
def SUM(x, n):
    x_len = len(x)
    y = []
    y.append(x[0])
    i = 1
    while i < x_len:
        if i < n:
            t = sum(x[0:i+1])
        else:
            t = sum(x[i-n+1:i+1])
        y.append(t)
        i = i + 1
    return y
def ma(x):
    n = len(x)
    s = sum(x)
    return s / n
        
def MA(x, n):
    x_len = len(x)
    y = []
    y.append(x[0])
    i = 1
    while i < x_len:
        if i < n:
            t = ma(x[0:i+1])
        else:
            t = ma(x[i-n+1:i+1])
        y.append(t)
        i = i + 1
    return y

def sma(s, x, n, m):
    y = (m * x + (n - m) * s) / n
    return y

def SMA(x, n, m):
    x_len = len(x)
    y=[]    
    y.append(x[0])       
    i = 1
    while i < x_len:
        e = sma(y[-1], n, m)
        y.append(e)
    return y
'''
Standard deviation
A(n) = (P(n) + P(n-1) + P(n-2)+...+P(1)) / n
B(n) = ((P(n) - A(n))*(P(n) - A(n)) +  (P(n-1) - A(n))*(P(n-1) - A(n)) + ...+(P(0) - A(n))*(P(0) - A(n))) / n
STD(n) = sqrt(B(n))
'''

def std(x):
    n = len(x)
    a = sum(x) / n
    b = 0
    for i in x:
        t = i - a
        b = b + pow(t, 2)
    b = b / n
    return sqrt(b)
    
def STD(x, n):
    x_len = len(x)
    y=[]
    i = 0
    while i < x_len:
        if i < n:
            t = std(x[0:i+1])
        else:
            t = std(x[i-n+1:i+1])
        y.append(t)
        i = i + 1
    return y

def CROSS(x, y):#
    if len(x) < 2 or len(y) < 2:
        return False
    if x[-1] > y[-1] and x[-2] < y[-2]:
        return True
    else:
        return False
def UPNDAY(x, n, m=0.0):#
    x_len = len(x)
    if x_len < n:
        return False
    else:
        i = x_len - n
        while i < x_len - 1:
            t = (x[i+1] - x[i]) / x[i]
            if t <= m:
                return False
            i = i + 1
        return True    

def DOWNNDAY(x, n, m= 0.0):#
    x_len = len(x)
    if x_len < n:
        return False
    else:
        i = x_len - n
        while i < x_len - 1:
            t = (x[i] - x[i+1]) / x[i]
            if t <= m:
                return False
            i = i + 1
        return True
def ref(x, n):
    if len(x) <= n:
        return None
    else:
        return x[-1 - n]
def REF(x, n):
    if len(x) > n:
        return x[0:-1-n]
    else:
        return None
def LAST(x, n):
    if len(x) >n:
        return x[-n:]
    else:
        return x
if __name__ == "__main__":
    x = [1.0, 2.0, 3.0, 4, 5, 5, 7]
    y = [1.0, 2.0, 2.0, 4, 5, 5, 7]
    t = [3, 3, 1]
    print(LAST(x, 9))