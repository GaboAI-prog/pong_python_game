import turtle

#Ventana
wn = turtle.Screen()
wn.title("Pong by Gabriel")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#Marcador
marcadorA = 0
marcadorB = 0


#JugadorA
JugadorA = turtle.Turtle()
JugadorA.speed(0)
JugadorA.shape("square")
JugadorA.color("blue")
JugadorA.penup()
JugadorA.goto(-350, 0)
JugadorA.shapesize(stretch_wid = 5, stretch_len = 1)

#JugadorB
JugadorB = turtle.Turtle()
JugadorB.speed(0)
JugadorB.shape("square")
JugadorB.color("green")
JugadorB.penup()
JugadorB.goto(350, 0)
JugadorB.shapesize(stretch_wid = 5, stretch_len = 1)

#Pelota
Pelota = turtle.Turtle()
Pelota.speed(0)
Pelota.shape("circle")
Pelota.color("purple")
Pelota.penup()
Pelota.goto(0, 0)
Pelota.dx = 2
Pelota.dy = 2

#Linea division
división = turtle.Turtle()
división.color("grey")
división.goto(0, 400)
división.goto(0, -400)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("JugadorA: 0      JugadorB: 0", align = "center", font = ("Courier", 24, "normal"))

#Funciones
def JugadorA_up():
    y = JugadorA.ycor()
    y += 20
    JugadorA.sety(y)

def JugadorA_down():
    y = JugadorA.ycor()
    y -= 20
    JugadorA.sety(y)

def JugadorB_up():
    y = JugadorB.ycor()
    y += 20
    JugadorB.sety(y)

def JugadorB_down():
    y = JugadorB.ycor()
    y -= 20
    JugadorB.sety(y)


#Teclado
wn.listen()
wn.onkeypress(JugadorA_up, "w")
wn.onkeypress(JugadorA_down, "s")

wn.listen()
wn.onkeypress(JugadorB_up, "Up")
wn.onkeypress(JugadorB_down, "Down")


while True:
    wn.update()

    Pelota.setx(Pelota.xcor() + Pelota.dx)
    Pelota.sety(Pelota.ycor() + Pelota.dy)

#Bordes
    if Pelota.ycor() > 290:
        Pelota.dy *= -1
    if Pelota.ycor() < -290:
        Pelota.dy *= -1

#Bordes der/izq
    if Pelota.xcor() > 390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("JugadorA: {}      JugadorB: {}".format(marcadorA, marcadorB), align = "center", font = ("Courier", 24, "normal"))

    if Pelota.xcor() < -390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("JugadorA: {}      JugadorB: {}".format(marcadorA, marcadorB), align = "center", font = ("Courier", 24, "normal"))
    
    if ((Pelota.xcor() > 340 and Pelota.xcor() < 350)
        and (Pelota.ycor() < JugadorB.ycor() + 50
        and Pelota.ycor() > JugadorB.ycor() - 50 )):
        Pelota.dx *= -1

    if ((Pelota.xcor() < -340 and Pelota.xcor() > -350)
        and (Pelota.ycor() < JugadorA.ycor() + 50 
        and Pelota.ycor() > JugadorA.ycor() - 50 )):
        Pelota.dx *= -1
        



     


