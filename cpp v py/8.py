import math
def prodR(k1):
    if k1>= 1:
        slag = ((abs(math.cos(pow(k1,2)-3.8)))/(4.5))-(9.7*math.sin(k1-3.1))
        return slag + prodR(k1-1)
    else:
        return 1

def prod(k1):
    x=1
    while(k1>=1):
        x+=((abs(math.cos(pow(k1,2)-3.8)))/(4.5))-(9.7*math.sin(k1-3.1))
        k1-=1
    return x

k=10
print("prodR= ", prodR(k))
print("prod= ", prod(k))
