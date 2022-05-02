
#Spigot
import math
def Multiplication(Num):
    M=1
    for x in Num:
        M*=x
    return M


Sp_list = []
def Spigot(x):
    Term = 0
    Ans = 0
    while Ans < abs(math.pi-x):
        Term = Term +1
        Result = Term/(2*Term+1)
        Sp_list.append(Result)
        Ans = (Sp_list) * 2
        
    return Ans, Term

print(Spigot(0.1))

#Basel

import math

pi = float(math.pi)
B_list=[]
def basel(x):
    Term =0
    Ans=0
    while Ans < abs(math.pi-x):
        Term = Term + 1
        Result = (1/(Term**2))
        B_list.append(Result)
        Ans = math.sqrt((sum(B_list)) * 6)
    return Ans, Term

print(basel(0.1),"Basel")

#taylor
import math

pi = float(math.pi)
Tay_list =[]
def Taylor(x):
    Term = 0
    Ans=0
    while True:
        if abs(math.pi - Ans) <= x:
            break
        Term = Term +1
        Result =(-1)**(Term+1)/(2*Term-1)
        Tay_list.append(Result)
        Ans = (sum(Tay_list))*4
        #print(Ans, x, Tay_list)
        
        
    return Ans, Term
print(Taylor(0.2),"taylor")

#wallis

import math

def Multiplication(Num):
    M=1
    for x in Num:
        M*=x
    return M

def wallis(x):
    wallis_list=[]
    Term = 0
    Ans = 0
    while Ans < abs(math.pi-x):
        Term = Term +1
        Result=(2*Term)/(2*Term-1)*(2*Term)/(2*Term+1)
        wallis_list.append(Result)   
        Ans =2 * Multiplication(wallis_list)
    return Ans,Term

print(wallis(0.2),"Wallis")

def race(x):
    race_list=[]
    A=basel(x)
    C=Taylor(x)
    D=Spigot(x)
    W=wallis(x)
    #race_list.append(A,C,D,W)
    return C,A,D,W#A,C,D,W

#print(race(0.01),"lol")

