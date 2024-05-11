import turtle

def hilbert_curve(t, order, size, direction):
    if order == 0:
        return
    t.right(direction * 90)
    hilbert_curve(t, order - 1, size, -direction)
    t.forward(size)
    t.left(direction * 90)
    hilbert_curve(t, order - 1, size, direction)
    t.forward(size)
    hilbert_curve(t, order - 1, size, direction)
    t.left(direction * 90)
    t.forward(size)
    hilbert_curve(t, order - 1, size, -direction)
    t.right(direction * 90)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    # Positioning the turtle
    t.penup()
    t.goto(-200, -40)
    t.pendown()

    # t.right(10)
    hilbert_curve(t, 3, 20, 1)

    # t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
