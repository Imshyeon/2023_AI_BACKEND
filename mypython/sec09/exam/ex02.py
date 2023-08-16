import turtle
from turtle import Screen
from turtledemo.chaos import line

screen=Screen()
screen.setup(800,600)
screen.title('my screen')
screen.bgcolor('blue')
# line.run()
# screen.mainloop()
# turtle.dot(20)
turtle.circle(100)
turtle.pen(fillcolor='black',pencolor='red',pensize=10)
screen.exitonclick()

