# 1
print('*'*20)
print()

# 2
n = int(input('nhap n: '))
print('*'*n)
print()

# 3
for i in range(1,10):
    if (i % 2 == 0):
        print('*', end =' ')
    else:
        print('x', end = ' ')
print()

# 4
a = int(input('nhap a: '))
for i in range(1,a+1):
    if (i % 2 == 0):
        print('*', end =' ')
    else:
        print('x', end = ' ')
print()        

# 5
print()

# 6
for _ in range(3):
    print('*'*7)
print()

# 7
x = int(input('Enter x: '))
y = int(input('Enter y: '))
for _ in range(y):
    print('*'*x)
print()