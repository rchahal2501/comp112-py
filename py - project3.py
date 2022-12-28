#PROJECT3: TURTLE NIM GAME 

'''

NIM GAME USING TURTLE PYTHON:
1 -- player1 vs player2 idle ver. commented out
2 -- player1 vs player2 turtle ver. for visual gameplay

'''




#(1)____________NIM Player vs Player

'''

def nim_game ():
#set player to 1
    player= 1
#set initial state of squares
    state= 16
    print("The number of objects now is ", state)
    while True:
        #get valid move
        print ("Player ", player)
        while True: 
            move=int(input("What is your move? \n"))
            validmoves=[1,2,3]
            if move in validmoves and move<state:
                break
            print ("Invalid move. Choose number between 1-3")


        #update state/ current number of objects
        state=state-move


        #show state
        print("The number of objects now is ", state)


        #check win status - win or lose
        if state==1:
            print("Player ", player," wins!")
            break 


        #switch players 2->1, 1->2?? go back to valid move line (while loop?yes )
        if player ==1:
            player=2
        else:
            player=1
            
    print ("Game over.")

'''



# (2)______________NIM Player vs Player TURTLE Version

import turtle
import time
nimscreen= turtle.Screen()
nimscreen.title("Game of NIM")
nimscreen.setup(900,400, startx=0, starty=0)



t=turtle.Turtle()

t.hideturtle()

Yesresponse=['Yes','yes']


#rules and game play fxn

def begin_game (): 
    nimscreen=turtle.Screen()
    t=turtle.Turtle()
    t.hideturtle()
    YorN_response= nimscreen.textinput("Game of NIM", "Would you like to play? Please type Yes or No" )
    if YorN_response in Yesresponse:
        rules_text=" This is the Game of Nim:\n There are 16 squares.\n 2 Players take turns removing squares until there are none left.\n You may only remove 1, 2 or 3 squares at a time. \n The player who is forced to take the last square LOSES. Press SPACE to START."
        t.write(rules_text,font=('Arial', 15, 'bold'), align='center') 
        t.hideturtle() 
        nimscreen.onkeypress(nim_game_setup, "space" )
        nimscreen.listen()
    elif YorN_response not in Yesresponse:
        nimscreen.bye()



def rowof16 (state): 
    square=turtle.Turtle()
    square.hideturtle()
    
    nimscreen= turtle.Screen()
    nimscreen.reset() 
    
    y=0
    x=-280

    square.penup()
    for i in range(state): 
        square=turtle.Turtle()
        square.ht()
        square.penup()
        square.speed(0)
        square.setpos((x,y))
        square.shape("square")
        x=x+(40)
        square.pendown()
        square.st()


def nim_game_setup():
    t=turtle.Turtle()
    t.hideturtle()
    nimscreen= turtle.Screen()
    #if nimscreen.onkeypress(nim_game_setup, "space" )== "space":
    rowof16(16)
    nim_game()


def nim_game ():
    player=1
    
    state= 16
    
    nimscreen= turtle.Screen()
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0,100)
    statetext=" The number of squares now is: ", state
    t.write(statetext ,font=('Arial', 14, 'bold'), align='center') 
    t.hideturtle()


    while True:
        nimscreen= turtle.Screen()
        
        #player 1 vs 2 text
        time.sleep(3)
        t.clear()
        t.goto(0,80)
        playertext= "Player", player
        t.write(playertext ,font=('Arial', 14, 'bold'), align='center')
        
        while True: 
            nimscreen= turtle.Screen()
            t=turtle.Turtle()
            t.hideturtle()
            
            #valid move
            move=int(nimscreen.textinput(" Enter move.", 'Enter 1, 2 or 3 to remove squares. Cannot remove more squares than currently visible. What is your move?'))
            validmoves=[1,2,3]
            if move in validmoves and move<state:
                break


        #update state/ current number of objects
        state=state-move

        #update turtle visual state        
        rowof16(state)

        
        #text update state
        t.clear()
        
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,100)
        statetext="The number of squares now is: ", state
        t.write(statetext ,font=('Arial', 14, 'bold'), align='center') 
        t.hideturtle()

        #check win status - win or lose
        if state==1:
            nimscreen= turtle.Screen()
            nimscreen.reset()

            t.penup()
            t.hideturtle()
            t.goto(0, 60)
            textwinner= "Player", player, "wins!!!"
            t.write(textwinner, font=('Arial', 20, 'bold'), align='center')
            break

        if player==1:
            player=2
        else:
            player=1
        


begin_game()





