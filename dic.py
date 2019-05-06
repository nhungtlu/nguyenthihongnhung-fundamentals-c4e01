dict = {
    "mouse":"chuot",
    "computer":"may tinh",
    "keyboard":"ban phim",
   
}

while True:
    a = input('Nhap ten: ')
    if a in ['exit','quit']:
        break
    if a in dict:
        print('Tu nay co nghia: ',dict[a])
    else:
        print('Tu nay khong co nghia: ')
        dict = {
             "class":"lop",
             "lock":"khoa",
             "seen" :"xem"
        }
        b = input ('Them tu:')
        print('Tu nay co nghia:' ,dict[b])

    


    # print(peple[1][ ','sdt'][0])
