

# def input_list():
#     ds = []
#     m = int(input('nhap so phan tu: '))
#     for v in range(m):
#         so = int(input('nhap so:'))
#         ds.append(so)
#     return ds
# ds1 = input_list()
# print(ds1)




# def say_hi():
#     print('hi')
#     print('bye')
# say_hi()
# say_hi()
# say_hi()


# def add_two_number():
#     a = int(input('nhap so thu nhat:'))
#     b = int(input('nhap so thu hai:'))
#     print('tong hai so la: ',a + b)
# d = add_two_number()
# print(d)



def add_two_number(a,b):
    return a + b
#     print('tong hai so la:',a + b)
num1 = int(input('nhap so thu nhat: '))
mum2 = int(input('nhap so thu hai: '))
mum3 = int(input('nhap so thu ba: '))

sum_3 = add_two_number(add_two_number(num1,mum2),mum3)
print('tong ba so la: ',sum_3)

# add_two_number(num1 , mum2)
# bài tập : liệt kê các kiến thức ,lưu ý trong bài học function