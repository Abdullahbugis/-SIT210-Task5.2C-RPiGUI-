from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)




Red = LED(16)
Orange = LED(20)
Blue = LED(21)



win = Tk()
win.title("LED Toggle")
myFont = tkinter.font.Font(family = "Helvetica",size = 18, weight = "bold")



def Redled():
    if  Red.is_lit:
        Red.off()
  
    else:
        Red.on()
        Orange.off()
        Blue.off()
       
        
        
def Orangeled():
    if  Orange.is_lit:
        Orange.off()
        
    else:
        Orange.on()
        Red.off()
        Blue.off()
     
                
        
def Blueled():
    if  Blue.is_lit:
        Blue.off()
    
    else:
        Blue.on()
        Red.off()
        Orange.off()
     
        
        
        
def close():
       RPi.GPIO.cleanup()
       win.destroy()
        
        
        
        
Redbtn = Button(win, text = 'Turn Red On', font = myFont, command = Redled, bg = 'White', height = 1, width = 30)
Redbtn.grid( row = 1, column = 1)
    
Yellowbtn = Button(win, text = 'Turn Orange On', font = myFont, command = Orangeled, bg = 'White', height = 1, width = 30)
Yellowbtn.grid( row = 2, column = 1)
    
Bluebtn = Button(win, text = 'Turn Blue On', font = myFont, command = Blueled, bg = 'White', height = 1, width = 30)
Bluebtn.grid( row = 3, column = 1)
    
    
exitbtn = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 2, width = 8)
    
exitbtn.grid(row = 4, column = 1)
    
        
