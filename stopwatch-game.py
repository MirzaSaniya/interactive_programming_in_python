# Implementation of the game "Stopwatch"

import simplegui

# define global variables
second = 0
success = 0
total = 0
counter = str(success) + "/" + str(total)
isStopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t > 600:
        A = t/600
    else:
        A = "0"
    B = (t % 600) / 10
    C = (t % 600) % 10
    if t % 600 > 100:
        return str(A) + ":" + str(B) + "." + str(C)
    else:
        return str(A) + ":" + "0" + str(B) + "." + str(C)
       
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global isStopped
    timer.start()
    isStopped = False
        
def stop():
    timer.stop()
    global success, total, counter, isStopped
    if isStopped == False:
        total += 1
        if second % 10 == 0:
            success += 1
    counter = str(success) + "/" + str(total)
    isStopped = True
    
    
def reset():
    global second, success, total, counter, isStopped
    timer.stop()
    second = 0
    success = 0
    total = 0
    counter = str(success) + "/" + str(total)
    isStopped = True
    
   
# define event handler for timer with 0.1 sec interval
def increment():
    global second
    second += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(second), [100, 100], 50, "Red")
    canvas.draw_text(counter, [230, 40], 40, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
timer = simplegui.create_timer(100, increment)
button1 = frame.add_button("Start", start)
button2 = frame.add_button("Stop", stop)
button3 = frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# start frame
frame.start()
