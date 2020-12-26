# Canvas

# import
import turtle
import math

# create board to play on GUI
board = []

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
    for i in range(2):  # draw lines two times
        drawer.penup()  # pick pen
        # goto a specific spot x will be -300 both times but y will change both times loop repeats
        drawer.goto(100 - 200 * i, 300)
        drawer.pendown()  # put pen down on board
        drawer.forward(600)  # move forward for 600 pixels

        # label numbers to each squares
        num = 1
        for i in range(3):
            for j in range(3):
                drawer.penup()
                # x           #y
                # draw at specific locations
                drawer.goto(-290 + j*200, 280-i * 200)
                drawer.pendown()

                # write num at specific locations
                drawer.write(num, font=("Arial", 12))
                num += 1

    # update screen
    screen.update()


# Draw X and O
def drawX(x, y):  # co-ordinates for input\
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(60)

    # draw an X in turtle
    for i in range(2):
        drawer.forward(75)
        drawer.backward(150)
        drawer.forward(75)
        drawer.left(60)
    # update screen
    screen.update()


def drawO(x, y):  # co-ordinates for input
    drawer.penup()
    drawer.goto(x, y + 75)  # little above co-ordinates to
    drawer.pendown()
    drawer.setheading(0)  # where to start

    # draw circle in turtle
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)
    # update screen
    screen.update()
\

# to activate event listners
def activate(function):
    for i in range(9):
        # means (functions value, its numeric value)
        screen.onkey(function[i], str(i + 1))

# to dectivate event listners when game is over

def dectivate():
    for i in range(9):
        # means (functions value, its numeric value)
        screen.onkey(None, str(i + 1))



# Add X to the inputted location

def addX(row, column):  # where to put X

    announcer.clear() # remove when clicking another button

    #first check if its already full or not

    if board[row][column] == "x" or board[row][column] == "o":
        announcer.write("Spot already taken", font=("Arial", 36))
        screen.update()
    else:
        drawX(-200 + 200 * column, 200 - 200 * row)
        #now add x for computer
        board[row][column] = "x"
    
    if checkWon('x'):
        announcer.goto(-97,0)
        announcer.write("You Won", font = ("Arial",36))

        screen.update() # update after announcer
        dectivate() #deactivate event listners
    else: # if not won add o
        addO()
        if checkWon('o'):
            announcer.goto(-90, 0)
            announcer.write("You Lost ", font=("Arial", 36))
            
            screen.update() # update after announcer
            dectivate() #deactivate event listners
        elif checkDraw():
            announcer.goto(-90, 0)
            announcer.write("Its a tie", font=("Arial", 36))
            
            screen.update() # update after announcer
            dectivate() #deactivate event listners



#check if thier is a tie

def checkDraw():
    #check numberof x if thier are 4 means its a draw
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count+= 1
    if count > 3:
        return True
    else:
        return False

# now function for each square
def squareOne():
    addX(0, 0)


def squareTwo():
    addX(0, 1)


def squareThree():
    addX(0, 2)


def squareFour():
    addX(1, 0)


def squareFive():
    addX(1, 1)


def squareSix():
    addX(1, 2)


def squareSeven():
    addX(2, 0)


def squareEight():
    addX(2, 1)


def squareNine():
    addX(2, 2)

#function to check if someone won or not

def checkWon(letter):

    for i in range(3):
        #check if 3 same in horizontal 
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True
        #check if 3 same in vertical
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True
        
        #check if 3 same in diagonal down
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
        return True
        #check if 3 same in diagonal up
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
        return True
    return False

# computer's turn put O
def addO():

    for i in range(3):
        for j in range(3):

            if board[i][j] == " " :
                 #check if thier is any place left
                board[i][j] = "o" #temporary put o thier
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " " # if not put set it back to null
    
    # now block X from wining
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                 #check if thier is any place left
                board[i][j] = "x" #temporary put x thier
                if checkWon("x"): # check if x wins
                    board[i][j]= "o" 
                    drawO(-200 + 200 * j, 200 - 200 * i)
                    return
                board[i][j] = " "  # if not put set it back to null
    
    #Try to place o in first available corner
    #computer only look into the corners
    for i in range(0,3,2):
        for j in range(0,3,2):
            if board [i][j] == " ":
                board = "o" 
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

    #computer if corners not availabe
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return


# Creating event listeners
functions = [squareOne, squareTwo, squareThree, squareFour,
             squareFive, squareSix, squareSeven, squareEight, squareNine]


# create turtles
drawer = turtle.Turtle()  # turtle window

announcer = turtle.Turtle() # will tell messages to user
announcer.penup()
announcer.ht()
announcer.goto(-200,0)
announcer.color("red")


# incrase drawer pensize and hide it
drawer.pensize(10)
drawer.ht()  # hide pensize

# create screen
screen = turtle.Screen()

# update rather than throwing drawings
screen.tracer(0)  # turn animation off


# Since computer don't know what going on in game so we represnt him in this way
# creating the board for computer 



for i in range(3):
    row =[]
    for j in range(3):
        row.append(" ")
        board.append(row)

# Calling Functions

drawBoard()

activate(functions) #activate event listeners
screen.listen()


# hold screen
turtle.done()
