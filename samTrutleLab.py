

import turtle               #import the turtle module
import random               #import the random module

wn = turtle.Screen()        #create a screen
wn.bgcolor('lightblue')     #
wn.title("Turtle Race")     #label the screen

lance = turtle.Turtle()     #create two turtles
andy = turtle.Turtle()      #create two turtles
lance.color('red')          # 
andy.color('blue')          #
lance.shape('turtle')       #
andy.shape('turtle')        #

andy.up()                   #
lance.up()                  #
andy.goto(-100, 20)         #move the turtles to their starting points -100 to 20
lance.goto(-100, -20)       #move the turtles to their starting points -100 to 20

start = turtle.Turtle()     #create a third turtle object called start that will be used to display the winner of the game
start.hideturtle()          #hide the third turtle object until the game is over for aesthetic purposes

andyTotalDistance = 0       #set andy and lance initial distance to 0.
lanceTotalDistance = 0      #

for i in range(150):        #iterate through the loop to run the forward method on both turtles 150 times
    #Indent to begin the loop

    andyDistance = random.randrange(1, 5)                       #make a random distance for andy to move range of 1 to 5
    lanceDistance = random.randrange(1, 5)                      #make a random distance for lance to move range of 1 to 5
    andy.forward(andyDistance)                                  #move andy forward and use the andyDistance variable to determine the amount to move forward by.
    lance.forward(lanceDistance)                                #move lance forward and use the lanceDistance variable to determine the amount to move forward by.
    andyTotalDistance = andyTotalDistance + andyDistance        #this section is to determine the winner of the game and be used to print who the winner is.  
    lanceTotalDistance = lanceTotalDistance + lanceDistance     #It calculates total distance for lance and for andy.
    #De-indent to end the loop

#use a cascading set of if conditions to determine the winner below. 
for eachInt in range(145):
    #Indent to begin the loop
    if andyTotalDistance > lanceTotalDistance:
        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    elif lanceTotalDistance > andyTotalDistance:
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
        #Display out put
    else: print("Tie Game")
    #De-indent to end the loop
wn.exitonclick()

