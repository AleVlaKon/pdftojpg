# put your python code here
import random
import turtle

colors = ('darkorchid1', 'chartreuse2', 'darkblue', 'lawngreen', 'white')   #Назначаем кортеж с набором цветов снежинок
turtle.Screen().bgcolor('cyan1') #Назначаем цвет фона



def sneg(size):
    '''Рисуем одну снежинку размера "size"'''
    turtle.pensize(2)
    for i in range(8):
        turtle.forward(size)
        turtle.backward(size * 3 // 4)
        for j in range(3):
            turtle.left(45)
            turtle.forward(size // 4)
            turtle.backward(size // 4)
            turtle.right(90)
            turtle.forward(size // 4)
            turtle.backward(size // 4)
            turtle.left(45)
            turtle.forward(size // 4)
        turtle.backward(size)
        turtle.right(45)

def draw(kolich):
    '''Рисуем снежинки количеством kolich'''
    for i in range(kolich):
        coords = []   #Назначаем список с координатами уже нарисованных снежинок
        size = random.randrange(30, 70, 2)
        if coords: #Если список пустой, назначаем случайную координату
            x = random.randrange(0, 200, 2)
            y = random.randrange(0, 200, 2)

        elif abs(coords[-1][0] + size) < x and abs(coords[-1][1] + size) < y:
            #Если координата попадает в квадрат, где уже есть снежинка - назначаем заново
            x = random.randrange(0, 200, 2)
            y = random.randrange(0, 200, 2)
        else:
            # Если координата не попадает в квадрат, где уже была снежинка - рисуем здесь
            coords.append((x, y))
            turtle.penup()
            turtle.goto(x, y)
            turtle.pencolor(random.choice(colors))
            turtle.pendown()
            sneg(size)


draw(5)