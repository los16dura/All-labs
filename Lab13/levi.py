__author__ = 'student'
__author__ = 'student'
import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
def Koh(l,n):
    if n==0:
        turtle.left(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        #turtle.left(45)
    else:
        turtle.left(45)
        Koh(l,n-1)
        turtle.right(45)
        Koh(l,n-1)
        turtle.left(45)




#turtle.speed('fastest')
Koh(30,10)
turtle.mainloop()

