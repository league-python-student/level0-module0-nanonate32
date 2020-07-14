import turtle

nathan = turtle.Turtle()

nathan.color('green')

nathan.begin_fill()
nathan.circle(100, steps=50)
nathan.forward(100)
nathan.right(100)
nathan.backward(100)
nathan.left(100)
nathan.end_fill()


turtle.done()