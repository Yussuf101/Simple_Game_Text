def print_high_rise():
    print("""
             _,---.                                     
          ,-'       )                                   
          (          )            __________________    
            `-.__, -'             | |------------| |    
                                  | |  High Rise | |    
                                  | |  Building  | |    
                                  | |  ___  ___  | |    
                                  | |  | |  | |  | |    
                                  | |  |_|  |_|  | |    
                                  | |  ___  ___  | |    
                          ___     | |  | |  | |  | |        
            _     _      (   )    | |  |_|  |_|  | |    
           ( ): ((`)    (. `-/ )  | |  ___  ___  | |    
          ` | '(-.,')  ('_\`/-')  | |  | |  | |  | |     
            `   (_.)  (_._ \|,-_) | |  |_|  |_|  | |    
         `.   `. || `   (_\||_)   | |  ___  ___  | |    
           `.   `.    ` .  ||     | |  | |  | |  | |    
             `.    `.      ||-.   | |  |_|  |_|  | |    
               `.     `.   ||     | |    _____   | |    
                 `.       `.      | |    | | |   | |    
        \          `.       `.    |_|____|_|_|___|_|    
         \           `.        `.                       
          \        ,----.---------- .                          
           \      |.`.,' `.           `.                       
            \     \ _|`. / `.            `.                      
             \     | \  `.   \.-----------.\            
              \    `.|.`| `./ \\  c__)___/ \\             
               \       `.   `. \\____\___)__\\          
                \        `. _ `.\`____________\         
                 \         | \  |_|   ____   |_| `.     
                  \        `.|\ |#|__[YOU ]__|_|   `.   
                   \          `================'     `. 
    """)

def print_medal() :
    print("""
         _______________  
        |@@@@|     |####| 
        |@@@@|     |####| 
        |@@@@|     |####| 
        \@@@@|     |####/ 
         \@@@|     |###/ 
          `@@|_____|##'   
               (O)        
            .-'''''-.     
          .'  * * *  `.   
         :  *  SOH  *  :  
        : ~  G O L D  ~ : 
        : ~ A W A R D ~ : 
         :  *       *  :  
          `.  * * *  .'   
            `-.....-'     
    """)

from cn_game_extras import qa_until, type_print
import time

def play_purple_section( p_name):
#nme@202105121356 Changes made for Kat as she had a interview
# Next comment removed as you can either go offroad or drive fast to get here
#    print("You selected Off Road.")
#    type_print("Being Off Road is unpleasently bumpy and it is the long way around the Bridge. You are lucky, it is not obstructed.",0.01) 
#nme@202105121433 Added pause BEFORE printing picture
    input("Press enter to continue...")
    print_high_rise()
    time.sleep(2)
    type_print("You rejoin the main road, but there is a tall building blocking your way.")
    type_print("You can only go around it. Do you go around the left or right side?")

#NME@202105121526 changed the commentary text
    a = qa_until(f"{p_name}, choose a direction?", ["Left", "Right"])
    if a == 0 :
        type_print("You selected Left.")
        type_print("After going the left way around the tall building you can see the Strong Hold up ahead, so you continue to keep driving until",0.01)
        type_print("you get there. When you get there you let people know that you have found the cure and they welcome you with open arms.",0.01)
        type_print("The cure is mass produced and mixed into the air. It rains and the Zombies are cured. You are given the Saviour of Humanity medal",0.01)
        time.sleep(3)
        print_medal()
        #player_is_alive == True for alive and False for dead. We died so...
        return True
    elif a == 1 :
        print("You selected Right.")
        type_print("You decided to go the right way around the tall building. This way leads to a dead end parking lot that is full of zombies.",0.01)
        type_print("The zombies are drawn to your vehicle due to movement, the zombies over run you and eat you",0.01)
        #player_is_alive == True for alive and False for dead. We died so...
        return False
