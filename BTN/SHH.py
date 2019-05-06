        
a = int(input("Nhap vao mot so: "))
if a <= 1:
    print(a, " khong phai la so hoan hao")
else:
    sum = 0
    for i in range(1, a):
        
        if a % i == 0:
            sum += i    
    
    if sum == a:
        
        print(a, " la so hoan hao")
    else:
        
        print(a, " khong phai la so hoan hoa")  