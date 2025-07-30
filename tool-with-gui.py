import tkinter as tk
import pyautogui as controller
# === Main Window ===
gui = tk.Tk()
gui.title("Auto Tool")
gui.geometry("750x400")
gui.configure(bg="#1C1C1C")
gui.resizable(False, False)



#fail safe (move mouse to the top left to cancel the prorgamm)
controller.FAILSAFE = True


#rebirth once
def rebirth():        
#move to genghis khan button
    
        controller.PAUSE = 0.2
        controller.leftClick(850, 912, 0)
#move to rebirth button
        
        controller.PAUSE = 0.2
        controller.leftClick(839,712,0)

#click once 
def auto_click():
    cps=int(txt.get("1.0", "end-1c"))
    x = int(x_auto.get("1.0", "end-1c"))
    y = int(y_auto.get("1.0", "end-1c"))
    
    while cps<=50:
        controller.PAUSE = 1/(cps*2.3)
        controller.leftClick(x, y)




#auto clicker buttons (cps, x and y)   
txt = tk.Text(gui, height=1, width=10)
txt.place(x=100,y=100)

x_auto = tk.Text(gui, height=1, width=4)
x_auto.place(x=100,y=140)

y_auto = tk.Text(gui, height=1, width=4)
y_auto.place(x=144,y=140)

#all lables
clicker = tk.Label(gui, text="Auto clicker")
clicker.place(x=100,y=50)

cps_text = tk.Label(gui, text="CPS:")
cps_text.place(x=50,y=100)

coordinates = tk.Label(gui, text="X , Y:")
coordinates.place(x=50,y=140)

 
start_click = tk.Button(gui, text="Start" ,command=auto_click, width=2, height=1)
start_click.place(x= 110, y=180)







gui.mainloop()
    





    
    


