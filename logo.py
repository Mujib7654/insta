from turtle import*
speed(5)
def om(x,y):
    penup()
bgcolor('black')
pencolor('yellow')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(34,90)
om1(-150,-120,350,"black",20,90)

om1(-110,-70,260,"white",20,90)

om1(-90,-50,220,"black",20,90)

om2("white",20,10,70)

om2("black",20,30,50)

om2("white",110,160,15)       

penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)
