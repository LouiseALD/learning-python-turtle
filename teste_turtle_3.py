import turtle
import time
  
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
  
def curva():
    for i in range(200):
        tartaruga.right(1)
        tartaruga.forward(1)
  
def coracao():
    tartaruga.fillcolor('red')
    tartaruga.begin_fill()
    tartaruga.left(140)
    tartaruga.forward(113)
    curva()
    tartaruga.left(120)
    curva()
    tartaruga.forward(112)
    tartaruga.end_fill()
  
def txt():
  
    tartaruga.up()
    tartaruga.setpos(-68, 95)
    tartaruga.down()
    tartaruga.color('white')
    tartaruga.write("te amo lindo", font=("Verdana", 12, "bold"))
  
coracao()
txt()
tartaruga.ht()
time.sleep(10)