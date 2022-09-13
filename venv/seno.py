from turtle import Screen, Turtle
from math import sin, pi

x1 = float(input("Dime el limite inferior del intervalo: "))
x2 = float(input("Dime el limite superior del intervalo: "))
puntos = int(input("Dime cuantos puntos eh de mostrar: "))


pantalla = Screen()
pantalla.setup(825, 425)
pantalla.screensize(800, 400)
pantalla.setworldcoordinates(x1, -1, x2, 1)

tortuga = Turtle()

x = x1
dx = (x2-x1)/puntos
tortuga.penup()

tortuga.goto(x, sin(x))
tortuga.pendown()

while x <= x2:
    tortuga.goto(x, sin(x))
    x += dx

pantalla.exitonclick()