def factorial6(n):
    if n == 1:
        return n
    else:
        return n * factorial6(n - 1)

def factorial5(n):
    if n == 1:
        return n
    else:
        return n * factorial5(n - 1)

def factorial4(n):
    if n == 1:
        return n
    else:
        return n * factorial4(n - 1)

def factorial3(n):
    if n == 1:
        return n
    else:
        return n * factorial3(n - 1)

def factorial2(n):
    if n == 1:
        return n
    else:
        return n * factorial2(n - 1)

def factorial1(n):
    if n == 1:
        return n
    else:
        return n * factorial1(n - 1)

res = []
n = int(input())

for i in range (n):
    cm = int(input())
    if cm == 6:
        print(factorial6(6))
        res.append(factorial6(6))
    elif cm == 5:
        print(factorial5(5))
        res.append(factorial5(5))
    elif cm == 4:
        print(factorial4(4))
        res.append(factorial4(4))
    elif cm == 3:
        print(factorial3(3))
        res.append(factorial3(3))
    elif cm == 2:
        print(factorial2(2))
        res.append(factorial2(2))
    elif cm == 1:
        print(factorial1(1))
        res.append(factorial1(1))


print(res)