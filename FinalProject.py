from machine import Pin
import utime

inputPin = Pin(15,Pin.IN,Pin.PULL_DOWN)             #Initialise pin 15 as the input from the receiver circuit 

A1=Pin(0,Pin.OUT)                                   #Initialise all pins required for the outputs to display numbers on the display
B1=Pin(1,Pin.OUT)
C1=Pin(2,Pin.OUT)
D1=Pin(3,Pin.OUT)
E1=Pin(4,Pin.OUT)
F1=Pin(5,Pin.OUT)
G1=Pin(6,Pin.OUT)
A2=Pin(7,Pin.OUT)
B2=Pin(8,Pin.OUT)
C2=Pin(9,Pin.OUT)
D2=Pin(10,Pin.OUT)
E2=Pin(11,Pin.OUT)
F2=Pin(12,Pin.OUT)
G2=Pin(13,Pin.OUT)

clear = 10                                          #When value reaches 10 clears the display (Makes code more readable)
numbig = clear
numsmall = clear

setIntegerDisplay=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1],[0,0,0,0,0,0,0]]
#List with each element representing LED configuration for each digit
display = [[A2,B2,C2,D2,E2,F2,G2],[A1,B1,C1,D1,E1,F1,G1]]               #Mapping of the LED configuration for left and right of the display 

count = 0

def setNumber(numsmall):                        
    if(numsmall < 0):                   #Don't really need this
        numsmall = clear                 
        numbig = clear
    elif(numsmall > 99):  # Comment these 2 lines to remove 99 cap - When count reaches 99 it stays at 99
        return            # and display 2 most significant digits
    elif(numsmall > 9):                 
        strint = str(numsmall)              #When number is > 9 e.g. 12
        numbig = int(strint[0])             #Converts into string '12'
        numsmall = int(strint[1])           #Index taking numbig to be 1, numsmall to be 2
    else:
        numbig = clear                      #Or else no big (leftmost) number
        
    for i in range(7):                  #Now to display the numbers
        display[1][i].value(setIntegerDisplay[numbig][i])               #7 LEDs in display so loop through, every iteration 
        display[0][i].value(setIntegerDisplay[numsmall][i])

def interruptFunc(pin):                 #Interrupt (Input signal), once activated count goes up by one
    global count
    count += 1
    setNumber(count)                    #Calls function to map the number to the correct LED configuration 

setNumber(0)  #Initial display number 0

inputPin.irq(trigger=Pin.IRQ_RISING, handler=interruptFunc)
#When input voltage > threshold voltage interrupt is triggered and the handler is called 