__author__ = 'student'
import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
#turtle.left(180)

def ris(l,k, an=45):
    if k != 0:
        turtle.left(an)
        ris(l ,k-1, 45)
        turtle.right(an*2)
        ris(l ,k-1, -45)
        turtle.left(an)

    else:
        turtle.forward(l)

k = 11
ris(9,k)

turtle.speed('fastest')

turtle.mainloop()