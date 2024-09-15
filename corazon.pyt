from turtle import *
import time


bgcolor("black")
color("red")
title("Heart")
begin_fill()
pensize(3)

left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()


def escribir_animado(texto, posicion, delay=0.2):
    penup()
    color("red")
    
   
    espaciado = 45  
    ancho_total = len(texto) * espaciado
    
   
    goto(posicion[0] - ancho_total / 2, posicion[1])  
    
    setheading(0)
    
    pendown()
    
    for letra in texto:
        write(letra, align="left", font=("Comic Sans MS", 45, "normal"))
        penup()
        forward(espaciado)  
        pendown()
        time.sleep(delay)
    
    penup()
    goto(posicion)  
    pendown()


escribir_animado("TKM CAMILA", (0, -120))

hideturtle()
done()