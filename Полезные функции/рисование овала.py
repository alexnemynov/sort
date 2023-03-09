import turtle
pen = turtle.Turtle()

# Вертикальный овал
def talloval(pen, r):
    pen.left(45)
    for _ in range(2):
# длинная изогнутая часть
       pen.circle(r,90)
# короткая изогнутая часть
       pen.circle(r/2,90)

# Горизонтальный овал
def flatoval(pen, r):
    pen.right(45)
    for _ in range(2):
        pen.circle(r,90)
        pen.circle(r/2,90)


talloval(pen, 50)
pen.home()
flatoval(pen, 50)

turtle.done()
