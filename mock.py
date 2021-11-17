#1

def stars(n):
    print("*"*n, end="")
    
stars(5)

#2

def inrange(n,x,y):
    if n in range(x,y):
        return "true"
    
print(inrange(3,2,5))

#3

def max4(n1,n2,n3,n4):
    if n1>n2 and n1>n3 and n1>n4:
        return n1
    elif n2>n3 and n2>n4 and n2>n1:
        return n2
    elif n3>n4 and n3>n1 and n3>n2:
        return n3
    elif n4>n1 and n4>n2 and n4>n3:
        return n4
    
print(max4(5,8,2,7))

#4

def coins(price):

    p=0
    d=0
    j=0
    suma=0

    while price>=5:
        price-=5
        p+=1
    while price>=2:
        price-=2
        d+=1
    while price>=1:
        price-=1
        j+=1
        
    print(f"Tyle potrzeba piatek: {p}")
    print(f"Tyle potrzeba dwojek: {d}")
    print(f"Tyle potrzeba jedynek: {j}")

    return p+d+j
    
print(coins(23))

#5

def bool():

    from random import*
        return ranodm("True", "False")

print(bool())

from random import randint
def bool():
    return randint(0,1)

#inaczej

print(bool())

from random import randint
def bool():
    x=randint(0,1)
    if x==1:
        return True
    else:
        return False
    

print(bool())

#6

from random import*
def rand(fromm,to):
    x=randint(fromm,to)
    while True:
        if x%2==0 and x%3==0:
            return x
        else:
            x=randint(fromm,to)
    
print(rand(10,50))

#inaczej

from random import*
def rand(fromm,to):
    while True:
        x=randint(fromm,to)
        if x%2==0 and x%3==0:
            return x
        
    
print(rand(10,50))



#7

def bonus(years):
    
    if years<=5:
        return years*100
    elif years<=8:
        return 5*100+(years-5)*200
    else:
        return 5*100+3*200+(years-8)*50
    
print(bonus(9))    

    