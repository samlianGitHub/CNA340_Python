# Import the turtle module

In this project name call turtle module lab i need to extract the following python code and write comments explaining the steps, and et andy and lance initial distance to 0. 
 Use the variables andyTotalDistance and the appropriate location, you can add additional comments.Make a random distance for andy to move
use a cascading set of conditions to determine the winner. Make a random distance for lance to move, import the turtle module and import the random module. Create a third turtle object called start that will be used to display the winner of the game. 
use a cascading set of if conditions to determine the winner. To To started this project , i have to google and instill pJetBrains software PyCharm Edu and download python 3.7.



## Getting Started
To started this project , i have to google and instill pJetBrains software PyCharm Edu and download python 3.7. After that  
These instructions will run my code at local machine my laptop and at software call PyCharm Edu and visual studio. 
[development/experimentation/turtle module]



### Prerequisites
The project it requires of I need instill pJetBrains 
software PyCharm Edu 
additional packages 2018.3 x64
visual studio 2017 community X64 bit 



[upgrade and install the prerequisites, or do something else]
I to download python 3.7 
sudo apt update
sudo apt upgrade
sudo apt install package1 package2



## Running

I  will need to set andy and lance initial distance to 0.  Use the variables andyTotalDistance and lanceTotalDistance.
You need to use the following comments in the appropriate location, you can add additional comments.

Make a random distance for andy to move
Use a cascading set of conditions to determine the winner.
Make a random distance for lance to move
Import the turtle module 
Imort the random module
create a third turtle object called start that will be used to display the winner of the game 
use a cascading set of if conditions to determine the winner.
use a cascading set of if conditions to determine the winner below. 

When you have modified the file, zip it and save it to a location you can find.  Then go ahead and submit your zipped file here.
import the turtle module
import random
import the random module
reate a screen
label the screen


Oiterate through the loop to run the forward method on both turtles 150 times
move the turtles to their starting points -100 to 20
move the turtles to their starting points -100 to 20

create a third turtle object called start that will be used to display the winner of the game
 hide the third turtle object until the game is over for aesthetic purposes
this section is to determine the winner of the game and be used to print who the winner is.  It calculates total distance for lance and for andy.
Add any additional ways to run the program below
use a cascading set of if conditions to determine the winner below.

make a random distance for andy to move range of 1 to 5
move andy forward and use the andyDistance variable to determine the amount to move forward by.

use a cascading set of if conditions to determine the winner below
create two turtles

```
import turtle               
import random


lance = turtle.Turtle()     
andy = turtle.Turtle() 


wn = turtle.Screen()        
wn.bgcolor('lightblue')    
wn.title("Turtle Race")       
```

lance = turtle.Turtle()     
andy = turtle.Turtle()      
lance.color('red')          
andy.color('blue')          
lance.shape('turtle')       
andy.shape('turtle')        

andy.up()                   
lance.up()                  
andy.goto(-100, 20)         
lance.goto(-100, -20)



    lanceDistance = random.randrange(1, 5)                      
    andy.forward(andyDistance)                                  
    lance.forward(lanceDistance)                                
    andyTotalDistance = andyTotalDistance + andyDistance        
    lanceTotalDistance = lanceTotalDistance + lanceDistance     


start.hideturtle()  
```
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
```

## Thanks
Thank you for enjoying my turtle lab
