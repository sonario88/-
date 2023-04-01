import turtle
from turtle import *
import math


class Drawer:
    @staticmethod
    def resetTurtle():
        tracer(0)
        hideturtle()
        pensize(0.5)
        color("gray")
        speed(0)
        up()
        home()
        down()

    @staticmethod
    def drawAstroid(r, R):
        h = r / 0.8
        m = r / R

        pu()
        turtle.goto(0, -R)
        pd()
        tracer(1)
        pencolor('red')
        pensize(2)
        turtle.circle(R)
        pu()
        rad = math.radians(0)

        turtle.goto(
            R*(m + 1) * math.cos(m * rad) - h * math.cos(( m + 1) * rad ), 
            R*(m + 1) * math.sin(m * rad) - h * math.sin(( m + 1) * rad ),
            )
        pd()
        pencolor('purple')
        turtle.speed(None)

        
        for deg in range(1, 3000, 1):
            rad = math.radians(deg)
            turtle.goto(
                R*(m + 1) * math.cos(m * rad) - h * math.cos(( m + 1) * rad ), 
                R*(m + 1) * math.sin(m * rad) - h * math.sin(( m + 1) * rad ),
            )
            

    @staticmethod
    def drawDecarte(coordsLength):
        Drawer.resetTurtle()
        for ang in range(0, 361, 90):
            for i in range(0, coordsLength, 25):
                setx(turtle.xcor() + 5)
                write(i)
                setx(turtle.xcor() - 5)
                forward(25)
                dot(3)
            stamp()
            home()
            right(ang)

    @staticmethod
    def drawPolar(coordsLength):
        Drawer.resetTurtle()

        for i in range(0, coordsLength, 25):
            up()
            goto(0, -i)
            down()
            circle(i)
            up()
            goto(i, 0)
            goto(turtle.xcor() + 5, turtle.ycor() - 15)
            write(i)
        setheading(0)
        j = 0
        while j < 360:
            j = j + 30
            up()
            goto(0, 0)
            down()
            forward(coordsLength)
            write(j - 30)
            right(30)
        up()
        home()
        down()
        goto(coordsLength, 0)
        stamp()
        up()
        tracer(1)


class Builder:
    @staticmethod
    def userDialog():
        print("Введите радиус подвижной окружности ( от 10 до 60 )")

        r = int(input())
        while (r < 10) | (r > 60 ):
            print("Число должно быть от 10 до 60. ")
            r = int(input())
        print("Введите радиус неподвижной окружности  (от 100 до 300)")    
        R = int(input())
        
        while (R < 100) | (R > 300):
            
            R = int(input())    
        coordsLength = int(20*R)
        print("Выберите систему координат  \n1. Декартовая\n2. Полярная")
        n = int(input())
        while 1:
            if n == 1:
                Drawer.drawDecarte(coordsLength)
                break
            elif n == 2:
                Drawer.drawPolar(coordsLength)
                break
            else:
                print("Number must be 1 or 2")
                n = int(input())

        
        Drawer.drawAstroid(r, R)

        turtle.exitonclick()


Builder.userDialog()
