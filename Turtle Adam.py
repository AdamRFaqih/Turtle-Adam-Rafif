import turtle

win = turtle.Screen()
win.bgcolor("cyan")
win.title("Adam Rafif")
win.setup(width=600, height=600)

t = turtle.Turtle()
t.shape("classic")
t.pensize(2)

t.penup()
t.backward(250)
t.pendown()
t.goto(-200,100)
t.goto(-150,0)
t.penup()
t.goto(-225,51.5)
t.pendown()
t.forward(50)
t.penup()
t.goto(-100,0)
t.pendown()
t.goto(-100,100)
t.circle(-32,180)
t.goto(-70,0)
t.right(180)
t.penup()
t.forward(50)
t.pendown()
t.goto(-20,100)
t.forward(50)
t.penup()
t.goto(-20,50)
t.pendown()
t.forward(40)
t.penup()
t.goto(70,80)
t.pendown()
t.goto(80,100)
t.goto(80,0)
t.penup()
t.goto(140,100)
t.pendown()
t.goto(110,50)
t.goto(160,50)
t.penup()
t.goto(150,90)
t.pendown()
t.goto(150,0)

turtle.mainloop()