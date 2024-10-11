from turtle import *

def draw_flower():
    penup()
    goto(0, -100)
    pendown()
    color("green")
    pensize(2)
    
    left(90)
    forward(150)
    
    for i in range(12):
        if i % 2 == 0:
            color("yellow")
        else:
            color("pink")
        begin_fill()
        circle(50, 60)
        left(120)
        circle(50, 60)
        left(120)
        end_fill()
        right(30)
    
    penup()
    goto(0, -200)
    color("white")

def move_text(text):
    penup()
    goto(0, 130)  # Menentukan posisi untuk teks, di atas bunga
    color("white")
    write(text, align="center", font=("Arial", 24, "bold"))  # Menampilkan teks

bgcolor("black")

draw_flower()
move_text("I LOVE YOU")  # Menampilkan teks di atas bunga

done()
