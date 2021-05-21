def print_drown():
    print("""
                  ___
                /`  _z
                |  / 0|--.
            -   / \_|0`/ /.`'._/)
        \u001b[31m- ~ -^_\u001b[0m| /\u001b[31m-_~ ^- ~_` - -~ _
        \u001b[31m-  ~  -\u001b[0m| |\u001b[31m   - ~ -  ~  -
        \u001b[31m|gs     \u001b[0m\ |\u001b[31m, ~   -   ~
                \u001b[0m\_|
    """)

def print_bridge():
    
        print ("""
        \u001b[32m         @\_______/@
                @|XXXXXXXX |
               @ |X||    X |
              @  |X||    X |
             @   |XXXXXXXX |
            @    |X||    X |             \u001b[0mV\u001b[32m
           @     |X||   .X |
          @      |X||.  .X |                      \u001b[0mV\u001b[32m
         @      |0XXXXXXXX0||
        @       |X||  . . X||
                |X||   .. X||                               @     @
                |X||  .   X||.                              ||====%
                |X|| .    X|| .                             ||    %
                |X||.     X||   .                           ||====%
               |XXXXXXXXXXXX||     .                        ||    %
               |XXXXXXXXXXXX||         .                 .  ||====% .
               |XX|        X||                .        .    ||    %  .
               |XX|        X||                   .          ||====%   .
               |XX|        X||              .          .    ||    %     .
               |XX|======= X||============================+ || .. %  ........
        ===== /            X||                              ||    %
                           X||           /)                 ||    %
        \u001b[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\u001b[0m
        """)

import time,sys
from cn_game_extras import qa, type_print

def play_blue_section(p_name):

    type_print("While on your way, you come to another fork in the road.", 0.01)
    type_print("One a road leading to a bridge, the second leading to an off road path.", 0.01)
    time.sleep(1)
    a = qa(f"{p_name}, which way do you go (Offroad, Bridge)? ", "Bridge", "Offroad")
    # text after right path after off road
    if a == True :
        print_bridge()
        time.sleep(3) # text after choosing to go over the bridge
        type_print("You decide that the bridge is the best way, you can see the strong hold in the distance.", 0.01)
        time.sleep(0.5)
        type_print("But while in the middle of the bridge you come to a lot of parked cars", 0.01)
        time.sleep(0.5)
        type_print("The parked cars make you feel nervous. You can decide to drive faster and create more noise, or keep your speed steady.", 0.01)
        a = qa(f"{p_name}, how will you proceed, do you push for ('speed', or keep things 'steady')?", "speed", "steady")
        if a == False :
            type_print("The bridge creaks under the weight of the RV as you slowly cross the bridge.", 0.01)
            type_print("Suddenly the RV lurches and the bridge starts to twist.", 0.01)
            type_print("The added weight of your RV and the parked cars causes the bridge to collapse.", 0.01)
            time.sleep(1)
            print_drown()
            message = "You fall from a great height, \u001b[31mleading to your death.\u001b[0m"
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            # return false is we died and true if still alive
            return False
        type_print("The RV accellerates hard, zombies start to climb out of the cars, but the bridge starts to shake.", 0.01)
        type_print("The RV dashes along the rumbling bridge and climbs the last collapsing section using it's built up momentum.", 0.01)
        time.sleep(3)
        return True    
    type_print("You end up going Off-Road", 0.01)
    return True
