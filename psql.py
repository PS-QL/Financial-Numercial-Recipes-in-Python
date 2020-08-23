import math

# Code 3.1 Present value with discrete dicounting
def pv_discrete(cflow,time,rate):
    return sum([cf / (1+rate)**t for cf,t in zip(cflow,time) ])

# Code 3.4 Present value with continous dicounting
def pv_continous(cflow, time, rate):
    return sum([cf * math.exp(-rate*t) for cf,t in zip(cflow,time) ])

# Code 3.2 Internal rate of returns
def irr(cf, t):
    ERROR = -1e30
    if len(t) != len(cf): return ERROR
    ACCURACY = 1.0e-5 ; MAX_ITER = 50
    x1, x2 = [0.0, 0.4]
    f1, f2 = list(map(lambda r: pv_discrete(cf,t,r),[x1,x2]))
    
    for i in range(MAX_ITER):
        if (f1*f2 < 0): break
        if math.abs(f1) < math.abs(f2):
            x1 += 1.6* (x1-x2)
        else:
            x2 += 1.6 * (x2 - x1)

        f1, f2 = list(map(lambda r: pv_discrete(cf, t, r),[x1,x2]))
        #print("iteration no. ", i , " results is : ", x1,x2, f1,f2)

    if f1*f2 > 0 : return ERROR
    f = pv_discrete(cf, t, x1); dx = 0
    
    if f < 0:
        rtb = x1 ; dx = x2 - x1
    else:
        rtb = x2 ; dx = x1 - x2
    
    for i in range(MAX_ITER):
        dx *= 0.5
        x_mid = rtb + dx
        f_mid = pv_discrete(cf, t, x_mid)
        if f_mid <= 0:
            rtb = x_mid
        if (abs(f_mid) < ACCURACY) or (abs(dx) < ACCURACY):
            return x_mid
        else:
            pass #print("iteration no. :" , i , " and result is : ", x_mid)


