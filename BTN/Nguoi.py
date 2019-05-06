cc_cm = float(input('Nhap chieu cao: '))
cannang = float(input('Nhap can nang: '))
cc_m = cc_cm / 100
BMI = cannang/(cc_m**2)
if (BMI < 16):
    print('Thieu can nghiem trong.')
elif (BMI <= 18.5):
    print('Thieu can.')
elif (BMI <= 25) :
    print('Binh thuong.')
elif (BMI <= 30):
    print('Thua can.')
else :
    print('Beo phi.')
            