for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")
        elif():
            pass
        else:
            print(" ",end=" ")
    print()
    
import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle() # Assigning "Red" as name of the turtle

def curve(): # Method to draw curve
    for i in range(200): # To draw the curve step by step
        red.right(1)
        red.forward(1)

def heart():  # Method to draw full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve() # Left Curve
    red.left(120)
    curve() # Right Curve
    red.forward(112)
    red.end_fill()

heart()
red.ht() # Hiding Turtle
turtle.done()
