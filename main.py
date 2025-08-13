import  numpy as ny
import matplotlib.pyplot as  pt
from matplotlib.image import  imread


def NAND(x1 , x2):
    x = ny.array([x1, x2])
    w = ny.array([-0.5, -0.5])
    b = 0.7
    tmp = ny.sum(x* w) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

def AND(x1 , x2):
    x = ny.array([x1, x2])
    w = ny.array([0.5, 0.5])
    b = -0.7
    tmp = ny.sum(x* w) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

def OR(x1 , x2):
    x = ny.array([x1, x2])
    w = ny.array([0.5, 0.5])
    b = -0.4
    tmp = ny.sum(x* w) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

def XOR(x1 , x2):
    s1 = NAND(x1,x2)
    s2 =OR(x1,x2)
    s = AND(s1,s2)
    return s

print(XOR(0,1))
print(XOR(1,0))
print(XOR(0,0))
print(XOR(1,1))

哈哈哈哈哈哈


