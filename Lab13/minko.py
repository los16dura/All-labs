__author__ = 'student'
import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
def Koh(l,n):
    if n==0:
        turtle.forward(l)
    else:
        Koh(l/4,n-1)
        turtle.left(90)
        Koh(l/4,n-1)
        turtle.right(90)
        Koh(l/4,n-1)
        turtle.right(90)
        Koh(l/2,n-1)
        turtle.left(90)
        Koh(l/4,n-1)
        turtle.left(90)
        Koh(l/4,n-1)
        turtle.right(90)
        Koh(l/4,n-1)



turtle.speed(9)
Koh(700,2)
# turtle.right(120)
# Koh(300,3)
# turtle.right(120)
# Koh(300,3)
# turtle.right(120)

turtle.mainloop()
