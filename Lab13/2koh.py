import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
def Koh(l,n):
    if n==0:
        turtle.forward(l)
    else:
        Koh(l/3,n-1)
        turtle.left(60)
        Koh(l/3,n-1)
        turtle.right(120)
        Koh(l/3,n-1)
        turtle.left(60)
        Koh(l/3,n-1)


turtle.speed('fastest')
Koh(300,3)
turtle.right(120)
Koh(300,3)
turtle.right(120)
Koh(300,3)
turtle.right(120)

turtle.mainloop()
