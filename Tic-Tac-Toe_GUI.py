# Canvas

# import
import turtle

# create board to play on


def drawBoard():
    # draw horizontal lines
    for i in range(2):  # draw lines to times
        drawer.penup()  # pick pen
        # goto a specific spot x will be -300 both times but y will change both times loop repeats
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()  # put pen down on board
        drawer.forward(600)  # move forward for 600 pixels

    # Draw vertical line
    drawer.right(90)  # turn drawer 90 degree
    for i in range(2):  # draw lines to times
        drawer.penup()  # pick pen
        # goto a specific spot x will be -300 both times but y will change both times loop repeats
        drawer.goto(100 - 200 * i, 300)
        drawer.pendown()  # put pen down on board
        drawer.forward(600)  # move forward for 600 pixels
        # update screen
        screen.update()
        # label numbers to each squares
        num = 1
        for i in range(3):
            for j in range(3):
                drawer.penup()
                # x           #y
                # draw at specific locations
                drawer.goto(-290 + j*200, 280-i * 200)
                drawer.pendown()

                # write num at specidc locations
                drawer.write(num, font="Arial", 12)
                num += 1


# create turtle
drawer = turtle.Turtle()  # turtle window

# incrase drawer pensize and hide it
drawer.pensize(10)
drawer.ht()  # hide pensize

# create screen
screen = turtle.Screen()

# update rather than throwing drawings
screen.tracer(0)  # turn animation off


# Calling Functions

drawBoard()
