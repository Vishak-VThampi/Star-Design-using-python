import  turtle
col =('yellow','red','green','orange','wheat','white','aqua','violet')
t=turtle.Turtle()
screen= turtle.Screen()
screen.bgcolor('black')
t.speed(30)

for i in range(100):
        t.color(col[i%8])
        t.forward(i*4)
        t.left(150)
        t.width(2)
