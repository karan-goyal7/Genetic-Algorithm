import math as m
#-------------------------------------------------------------
# Fitness Function parameters
#-------------------------------------------------------------
D       = 100    # Problem Dimension
LB      = -100   # Set Size Lower Bound
UB      = 100    # Set Size Upper Bound


#-------------------------------------------------------------
# Fitness Function
#-------------------------------------------------------------

def FitnessFunction(x):
    s=0
    y=0
    z=0

    for i in range(D):
        s = s + i*(x[i]**2)
    for i in range(1,D-1):
        y = y + 20*i*(m.sin(x[i-1]*m.sin(x[i]) + m.sin(x[i+1]))**2)
        z = z + i*m.log10(1+i*(((x[i-1]**2) - 2*x[i] + 3*x[i+1] - m.cos(x[i]) + 1))**2)

    p = s + y + z

    return round(p,4)
