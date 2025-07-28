#
#IMPORTS
#

import pyautogui as controller


#
#VARIABLES
#

#fail safe (move mouse to the top left to cancel the prorgamm)
controller.FAILSAFE = True


#intro 
print('Hello ;)')
print('Move mouse to top left of screen if you want to cancel the programm whilst running')
print("i think this programm only works for screens with a resolution of 2560x1600 (need to test out)")

#checking if user wants to farm clicks or rebirths
farm_clicks = int(input("do you want to farm clicks in genghis khan feet clicker?\n (0 for no 1 for yes):"))
farm_rebirths = int(input("do you want to farm rebirths in genghis khan feet clicker?\n (0 for no 1 for yes):"))

                  


#
#FUNCTIONS 
#

#rebirth once
def rebirth():        
#move to genghis khan button
    
        controller.PAUSE = 0.2
        controller.leftClick(850, 912, 0)
#move to rebirth button
        
        controller.PAUSE = 0.2
        controller.leftClick(839,712,0)

#click once 
def genghis_click():
    controller.PAUSE = 1/15
    controller.leftClick(850, 912, 0)
    




#
#MAIN CODE (idk what to call lol)
# 
if farm_clicks== 1:

    num_clicks = int(input("enter the number of clicks"))
    print("this will take", round(num_clicks*(1/15)) ,"seconds")

    #give time for player to switch to game
    controller.PAUSE = 5

    for i in range(num_clicks):
        genghis_click()



if farm_rebirths == 1:
    
    num_rebirth = int(input("enter the number of rebirths you want"))
    
    #give time for player to switch to game
    controller.PAUSE = 3

    
    for i in range (num_rebirth):
        rebirth()


    
    
