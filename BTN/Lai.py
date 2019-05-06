Gianha = 120000000
Tiengui = 21000000
nam = 1
while (nam <= 9):
    Tiengui = Tiengui + Tiengui * 6.5/100
    nam += 1
print('So tien thu duoc sau 9 nam',Tiengui)
b = 1
while (Tiengui <= Gianha):
    Tiengui = Tiengui + Tiengui * 6.5/100
    b += 1
print('So tien mua duoc nha: ',Tiengui)