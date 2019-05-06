# for i in range(3):
#     print('Hello Word')

# def sum_two_number(a,b):
#     print( a + b)

# from turtle import*
# def draw_sape (lenght , color):
#     for i in range(4):
#         forward(lenght)
#         left(90)
# for i in range(30):
#     draw_sape(i * 5,'red')
#     speed(0.01)
#     left(17)
#     penup()
#     forward(i*2)
#     pendown()
        


from turtle import*
def draw_star(x,y, lenght):
    penup()
    vitri = (x,y)
    pendown()
    for i in range(5):
            forward(length)
            right(144)

speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

        

mainloop()