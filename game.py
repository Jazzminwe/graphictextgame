from graphics import *
import time

# room one = Foyer
# room two = sports area, close to elevators
# rooom three = equipment room
# room four = rooftop

# ************************************************

# initial variables
# dec = variable storing the player's decisions
inventar = [] # inventar = list containing the elements player picked up
hc = 0 # hc = hint count; every time the player needs a hint, the count increases by 1

# general functions
def sep():
    print('\n**********\n')
    return sep

def s():
    time.sleep(2)
    return s

def add_to_inventory(item):
    inventar.append(item)

def game_over():
    print('wakes up from dream blabla')
    # screen with game over opens up
    return game_over

def title_screen(win):
    # print title screen

    # print title
    title = Text (Point (130 , 30) , 'Welcome to "Horror at IE"!')
    title.draw(win) 
    title = Text (Point (154 , 50) , "Please follow the concole's instructions.")
    s()
    
    # print IE logo
    # construct I
    i_line = Rectangle(Point(70, 120), Point(90, 180))
    i_line.setFill('blue')

    i_circle = Circle(Point(80, 100), 10)
    i_circle.setFill('blue')

    # construct E
    e_top = Rectangle(Point(110, 90), Point(170, 100))
    e_top.setFill('blue')
    
    e_back = Rectangle(Point(110, 90), Point(130, 170))
    e_back.setFill('blue')
    
    e_middle = Rectangle(Point(110, 130), Point(170, 140))
    e_middle.setFill('blue')
    
    e_bottom = Rectangle(Point(110, 170), Point(170, 180))
    e_bottom.setFill('blue')

    # print logo and title
    title.draw(win) 

    i_circle.draw(win)
    i_line.draw(win)

    e_top.draw(win)
    e_middle.draw(win)
    e_bottom.draw(win)
    e_back.draw(win)   


'''def show_pocket(inventar):
    if len(inventar) == 1:
        print('You have a', inventar[0], 'in your pocket.')
    if len(inventar) > 1:
        while i in inventar:
        print('You have a')
    else: 
        print('You have nothing in your pocket.')'''

# *************************************************

# functions room one

def riddle1():
    # open window
    win = GraphWin('Horror at IE', 500, 200)

    riddle = Text (Point (160 , 30) , 'There are four sheep, two dogs and a men.\nHow many feet are there? \nSelect the correct number.')
    riddle.draw(win)

def decision_tree1(dec):
    # decision structure scene one
    if dec == 'G':
        print('You get up. At first, you feel dizzy and have troubles orienting. 1, 2, 3 - you start counting in your head to better concentrate. Your sight gets clearer and you walk towards the light. It is a massive screen that almost fills the whole room.')
        s()
        print('\nRoom...?')
        s()
        print('\nYou look around. You know this building. You have been here before. And suddenly, it hits you: "I know these two letters, in dark blue with a lighter blue colored dot..."')
            
        # ask player where he/she is standing
        dec = input(str('\nWhere are you? Type it into the console!\n'))

        # validation of input
        # if they get it right -> next scene, if not -> hint
        while dec != 'IE':
            print('HINT: Where are you currently studying...?\n')
            s()
            dec = input(str('\nType it into the console!\n'))

        print('\nYou are in the Foyer of the IE tower. It must be night time - it is dark outside. What are you doing here?? You just be at home, in your cozy bed.\n')
        s()
        dec = input('Walk out (WO) or investigate environment (IE)?\n')

        if dec == 'IE':
            # player looks at screen and finds first riddle
            print('You take a look at the screen. It shows the sports program for the next three days.')
            s()
            print('Or... does it? You step closer.\nInstead of "yoga", and "football" you find the following: ')

            # open window with riddle
            riddle1()

            dec = input('Please type your answer: ')
            
            # decision structure
            if dec == '2':
                print('PING!') # GUI?
                s()
                print('\nYou turn around, condused of the sound.')
                s()
                print('\nThere! An elevator just arrived and is now waiting for you, with open doors. The light coming out of the cabins insight is weirdly enlightening the foyer...')
                s()
                dec = input('\nWhat do you do? Stay here (SH) or take the elevator (TE)?\n ')

                sep()

                # decision structure
                if dec == 'TE':
                    print('You enter the cabin and the doors close. "Weird, what is this?" There is a screw driver lying on the floor. ')
                    dec = input('\nPick it up (PU) or leave it (LT)?\n ')

                    # decision structure
                    if dec == 'PU':
                        print('\nYou pick it up. "One nevers knows what this might be useful for..."')
                        add_to_inventory('screw driver')
                        #show_pocket()
                    else:
                        game_over()

                else:
                        sep()
                        print('You arrive in the minus second floor. The doors open and you step out. "Weird, what am I doing in the sports area...?" You look around. First, everything seems ordinary. You turn your head again. "Wait - was this poster here yesterday?", you think. Step closer or look around the area.')
    
            else: 
                # hint for riddle 1
                print('\nHINT: Sheep have hooves; dogs have paws. Try again. ')
                # hc += 1
                riddle1()

        else: 
            # go to door, find it blocked and decide again
            print('\nYou confidently turn around and go straight to the door. "This is weird! But I have been working a lot over the past days... This programming assignment has been giving me sleepless nights."')
            # open window with BÄM
            print('\nPain shoots through your head.')
            s()
            print("This can't be!")
            s()
            print('You push the door again. But no matter how hard you push, the door is locked. "Damn it..."')
            s()

            dec = input('\nWhat now? Start screaming for help (SH) or go back to screen (BS)?\n')

            if dec == 'BS':
                # go back to screen
                riddle1()
            else: 
                # start screaming for help and wake up
                game_over()

    else: 
        game_over() 
      

# functions room two
def setting2():
    print('start scene two')


# main function
def main():
    # executes game

    # *******************************
    # print title_screen
    win = GraphWin('Horror at IE', 300, 300)
    title_screen(win)
    win.getMouse()
    win.close()

    # format console
    sep()

    # *******************************
    # enter first room - Foyer of the Tower

    # print description of the start setting
    print('Bubum, bubum, bubum. You slowly open your eyes. Bubum, bubum, bubum... Where are you? Bubum, bubum, bubum... I is dark around you. Bubum, bubum, bubum... \nYou can see a bright light. Bubum, bubum, bubum... This noise, it must be your heartbeat. Bubum, bubum, bubum... You realise that you are laying on the floor - a very luxurious shimmery floor.')

    # ask user for decision
    dec = input('\nGet up (G) or stay down (D)? Type the command into the console.\n')
    sep() # visual separator 
    decision_tree1(dec) # Get up/Stay down?
    sep()

    # *******************************
    # second room - Sports area, close to elevators
    setting2()

    # *******************************
    # thrid room - Equipment room

    # *******************************
    # fourth room - on the roof

main()

    
    
