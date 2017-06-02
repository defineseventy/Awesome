from microbit import *
is_night = False # Night mode variable
while True:
    if button_a.is_pressed():
        sleep(2000)# waits 2 seconds for the result or value to be displayed
        if button_b.get_presses() > 0:
            display.scroll("1500mg") # emergency mode 
        else:
            level = button_a.get_presses() # counts the no. of times it is pressed
            if level > 5: # final level, if more than 5 the value would be returned as 5
                level = 5 # Prevents Overdosage
            if is_night:
                display.scroll(str(level*200)+"mg") # give increased dosage(at night)
            else:    
                display.scroll(str(level*100)+"mg") # normal dosage 
        
        sleep(500) # reset the value in 0.5 seconds
    else:
        display.clear() # clears the display
    if button_b.is_pressed():
        is_night = not is_night # toggle night mode
        if is_night:
            display.scroll("night mode on") # night mode on
        else:   
            display.scroll("night mode off") # night mode off
    
   
        