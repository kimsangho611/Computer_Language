from turtle import *
from math import *
reset()
a = atan(2/3)/0.01745
length = int(input("태극기의 크기를 입력하세요: "))
speed(0)
# 태극기 틀
def taegeuktool(n):
    pu()
    goto(-n*3/2,-n)
    pd()
    lt(90)
    for i in range(2):
        fd(n*2)
        rt(90)
        fd(n*3)
        rt(90)
    pu()
    goto(0,0)
    rt(90)
    pd()

def taegeukcircle(n):
    fillcolor("blue")
    begin_fill()
    lt(90-a)
    circle(-n/4,180)
    circle(-n/2,180)
    lt(180)
    circle(n/4,180)
    end_fill()
    fillcolor("red")
    begin_fill()
    circle(-n/4,180)
    lt(180)
    circle(n/2,180)
    circle(n/4,180)
    end_fill()
    
def blackSquare(n):
    width(1)
    pencolor("black")
    fillcolor("black")
    begin_fill()
    lt(90)
    fd(n/4) #200/4
    rt(90)
    fd(n/3) #200/3
    rt(90)
    fd(n/2) #200/2
    rt(90) 
    fd(n/3) # 200/3
    rt(90)
    fd(n/4) #200/4
    end_fill()

def whiteline(n):
    pencolor("white")
    width(n/24)
    pu()
    fd(n/4)
    rt(90)
    fd(n/48*5)
    rt(90)
    pd()
    fd(n/2)
    pu()
    lt(90)
    fd(n/24*3)
    lt(90)
    pd()
    fd(n/2)
    
def df_fd(n,n1):
    if n == '감괘' or n == '이괘':
        pu()
        lt(a)
        fd(n1*3/4)
        pd()
    else:
        pu()
        rt(a)
        fd(n1*3/4)
        pd()
        
def df_home():
    pu()
    home()
    pd()        
        
###########실행##############
taegeuktool(length)
taegeukcircle(length)

#감괘
df_home()
df_fd('감괘',length)

blackSquare(length)
whiteline(length)
bk(length/4)
lt(90)
bk(length/48*5)
pu()
fd(length/48*11)
pd()
fd(length/48*5)
df_home()

# 곤괘
df_fd('곤괘',length)

blackSquare(length)
whiteline(length)
bk(length/4)
lt(90)
bk(length/48*5)
fd(length/3)
df_home()

rt(180)

# 건괘
df_fd('건괘',length)

blackSquare(length)
whiteline(length)
df_home()

rt(180)

# 이괘
df_fd('이괘',length)

blackSquare(length)
whiteline(length)
bk(length/4)
lt(90)
fd(length/24*3)
df_home()

ht()
done()
