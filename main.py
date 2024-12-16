#This is the Turtle Target Game coded by Sapna Patel on 11/10/2024 for CS 111 at UIC (Net ID is 653295462) (Hope (during office hours) and Zohaib (over Piazza) checked my project on friday letting me know that I've met all their criteria for the points (31 from auto-grade) and the rest from their manual grading, so I'm good to get a 100 on Project 5 (so I wanted to give a quick thank you for looking over it beforehand and helping a lot greatly during office hours))
#The functions I created: def draw_star() (line 94), def draw_patrick (line 106), and def draw_spongebob (line 122)

import turtle
import random

#Sets up the background screen and applies a kitchen image to show how I changed the metaphor of the game
background = turtle.Screen()
background.bgpic("gif1.gif")

#Pre-condition: User inputs a value or "quit" to exit
#Post-condition: Returns input
def turtle_input(window_title, prompt):

    val = turtle.textinput(window_title, prompt)
    if val is None:
        return 'quit'
    try:
        int_val = int(val)
        return int_val
    except ValueError:
        try:
            flt_val = float(val)
            return flt_val
        except ValueError:
            return val

#Sets up the dimensions for sceen
def screen_setup():
    global max_x, max_y
    s = turtle.getscreen()
    s.setup(width=1.0, height=1.0, startx=None, starty=None)
    print(f"Screen width, height: {s.window_width(), s.window_height()}")
    max_x = int(s.window_width()/2)
    max_y = int(s.window_height()/2)
    print(f"max x: {max_x}, max y: {max_y}")
    
#Initializes game turtles
game_turtle = turtle.Turtle()
target_turtle = turtle.Turtle()
displaya_turtle = turtle.Turtle()
max_x = None        
max_y = None        
num_attempts = 0    
score = 0  

#Sets up game with target size/color and positions
def setup_new_game(target_size):
    global num_attempts, score, max_x, max_y
    target_turtle.penup()
    target_turtle.goto(random.randint(-200, max_x), random.randint(-200, max_y))
    target_turtle.dot(target_size, "red") #Draws the red dot as the iniital target
    game_turtle.penup()
    game_turtle.goto(random.randint(-200, max_x), random.randint(-200, max_y))
    game_turtle.left(random.randint(0,360)) #Sets a random position
    game_turtle.color("purple")
    game_turtle.shape("triangle")
    display_turtle.penup()
    display_turtle.goto(-600,300)
    score = 64
    attempts = 0

#Each step of the game following the input controlling the turtle
#Pre-condition: Game waits for the next move
#Post-condition: The game score is updated
def game_step():
    global num_attempts, score, max_x, max_y
    angle = turtle_input("Angle", "Enter the angle to rotate the turtle (or 'quit' to exit): ")
    game_turtle.pendown()

    if angle != "quit":
        game_turtle.left(int(angle)) #Turns turtle by angle
    else: 
        return "quit"
    distance = turtle_input("Distance", "Enter the distance to move forward: ")
    if distance != "quit":
        game_turtle.forward(int(distance)) #Moves turtle by distance
    else:
        return "quit"

    num_attempts = num_attempts + 1
    score = int(score / 2)
    target_turtle.clear() #EXTRA CREDIT (clears previous target)
    target_turtle.goto(random.randint(-200, max_x), random.randint(-200, max_y)) #EXTRA CREDIT (sets new position)
    target_turtle.dot(40, "red") #EXTRA CREDIT (draws new target dot)
    return 'continue'

#Updates the board with current score and attempts
def update_scoreboard():
    global num_attempts, score
    display_turtle.clear()
    message = f'Attempts: {num_attempts}\nScore: {score}'
    display_turtle.write(message, align="center", font=("Arial", 20, "bold"))

#Checks if the game has been won or lost (otherwise in progress)
def check_win(dist_to_win):
    global score
    distance = game_turtle.distance(target_turtle)
    print(distance)
    if distance < dist_to_win:
        return "win"
    if score == 0 and distance > dist_to_win:
        return "loss"
    else: 
        return "in_progress"

#Draws a green star for the display for the win screen
def draw_star():
    turtle.fillcolor("green")    
    turtle.pencolor("green")
    turtle.begin_fill()
    for i in range(5):
        turtle.penup()
        turtle.speed(100)
        turtle.pendown()
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()

#Draws a pink patrick for the display for the loss screen
def draw_patrick():
    number_petals = 5
    turtle.fillcolor("pink")
    for i in range(number_petals):
        turtle.penup()
        turtle.speed(100)
        turtle.pendown()
        turtle.begin_fill()
        turtle.pencolor("pink")
        turtle.circle(100,60)
        turtle.left(90)
        turtle.circle(100,60)
        turtle.left(360/number_petals)
        turtle.end_fill()
        turtle.penup()

#Draws a yellow spongebob for the display for the quit screen
def draw_spongebob():
    turtle.fillcolor("yellow")
    turtle.pencolor("orange")
    turtle.begin_fill()
    for i in range(4):
        turtle.penup()
        turtle.speed(100)
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

#Shows final screen based on game outcome with specified message following metaphor
def display_final_screen(result):
    my_turtle = turtle.Turtle()
    display_turtle.goto(0,30)
    if result == "win":
        draw_star()
        display_turtle.write("Bon Appetit!\nCongratulations, chef! Your dish has amazed the judges and\nyou've been crowned the Champion!", align = "center", font = ("Calibri", 14, "bold"))
    elif result == "loss":
        draw_patrick()
        display_turtle.write("Out of ingredients!\nChef, your pantry is empty, and time is up!\nBetter luck next time in the kitchen!", align = "center", font = ("Calibri", 14, "bold"))
    elif result == "quit":
        draw_spongebob()
        display_turtle.write("Recipe Abandoned.\nThank you for your effort, Chef.\nEveryone needs a break from the heat of the kitchen.", align = "center", font = ("Calibri", 14, "bold"))

#Runs the main game loop       
def play_game():
    screen_setup()
    setup_new_game(40) #starts game with initial target sizx
    
    game = ""
    check = ""
    while game != "quit":
        game = game_step()
        update_scoreboard()
        check = check_win(1000)
        if check in ["win", "loss"]:
            display_final_screen(check)
            break
    if game == "quit":
        display_final_screen("quit")
       
    screen_setup() #restarts screen for next game
    play_game() 
    turtle.done()