from random import randint
from tkinter import W
from turtle import Turtle, distance
import turtle

def draw(turtle1,turtle2,distance):
    colors = ["black","blue","purple"]
    if distance<500:
        turtle1.color(colors[randint(0,len(colors)-1)])
        turtle2.color(colors[randint(0,len(colors)-1)])
        turtle1.right(135)
        turtle1.forward(distance)
        turtle1.right(100)
        turtle1.forward(distance)
        turtle2.right(135)
        turtle2.forward(distance)
        turtle2.right(100)
        turtle2.forward(distance)
        distance+=5
        draw(turtle1,turtle2,distance)
    else:
        return


def main():

    ANIMATION_SPEED = 0
    distance=0
    turtle1 = Turtle()
    turtle2 = Turtle()
    turtle2.sety(10)
    turtle1.width(3)
    turtle2.width(3)
    turtle1.speed(ANIMATION_SPEED)
    turtle2.speed(ANIMATION_SPEED)
    draw(turtle1,turtle2,distance)

main()