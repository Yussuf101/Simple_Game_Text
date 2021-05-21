def print_hospital():
    print("                                                     ___")
    print("                                             ___..--'  .`.")
    print("                                    ___...--'     -  .` `.`.")
    print("                           ___...--' _      -  _   .` -   `.`.")
    print("                  ___...--'  -       _   -       .`  `. - _ `.`.")
    print("           __..--'_______________ -         _  .`  _   `.   - `.`.")
    print("        .`    _ /\    -        .`      _     .`__________`. _  -`.`.")
    print("      .` -   _ /  \_     -   .`  _         .` |cdc medical|`.   - `.`.")
    print("    .`-    _  /   /\   -   .`        _   .`   |___Center__|  `. _   `.`.")
    print("  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|")
    print("    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |")
    print("    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |")
    print("    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |")
    print("    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |")
    print(" ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|")
    print(" -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|")
    print("`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|")
    print("_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|")
    print("----------`--._          ''      ``--.._|:::::::::::::::::::::::|")
    print("`--._ _________`--._'        --     .   ''-----..............LGB'")
    print("     `--._----------`--._.  _           -- . :''           -    ''")
    print("          `--._ _________`--._ :'              -- . :''      -- . ''")
    print(" -- . ''       `--._ ---------`--._   -- . :''")
    print("          :'        `--._ _________`--._:'  -- . ''      -- . ''")
    print("  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''")
    print("                              `--._ _________`--._")
    print(" -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''")
    print("          -- . ''       -- . ''         `--._ _________`--._   -- . ''")
    print(":'                 -- . ''          -- . ''  `--._----------`--._")
def print_pothole():
    print(" ___  ,--.  __________________________/   ,   /_______")
    print("     'O---O'    .-----.")
    print("                `-- --'")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _   ,--.   _ _ _ _ _")
    print("       _____                       ~'O---O'")
    print("_______<      |_____        __________________________")
    print("           ||      /   ,   /    ")

from cn_game_extras import qa, type_print

def play_green_section( p_name):
    # question 3
    a= qa(f"You drive out of your house, you have two choices to go left or right. {p_name} choose a direction (left, right)?", "left", "right")
    if a == True:
        type_print("You have chosen to go left",pause=1)
        print_pothole()
        type_print("While drive along, hit a pot hole and crashed, the loud noise alerted the Zombies and they eat you alive.",pause=1)
        #player_is_alive == True for alive and False for dead. We died so 
        return False

    print_hospital()
    type_print("Your decided to go right. On your way, you come to Medical Research Centre where an old") 
    type_print("Doctor has found a Cure for the Zombie Virus but is trapped. He entrusts you to deliver") 
    type_print("the Cure to the human Survival strong hold")

    # Question 4
    a = qa("After leaving the Medical Research Centre you come to a fork in the road do you go right or left?", "right", "left")
    if a == False:
        print_pothole()
#nigel@202105121318 picture moved to above, repetitive verage replaced:
#        type_print("after leaving the Medical research centre and driving to deliver the virus cure, ")
        type_print("You notice the other route goes up a ramp then somewhere into the city, but the")
        type_print("road you are on is a straight road to the bridge before the strong hold.")
        type_print("The road is clear except a single Zombie off into the distance, so you decide")
        type_print("to accelerate and run it down. At high speed you start seeing obstructions and holes")
        type_print("in the road, but before you can turn around...")
#end additions
        type_print("you hit a pot hole and crash. The loud noise draws Zombies to you.")
        type_print("They over run and eat you alive.",pause=3)
#nigel@202105121347 commented out because it was unnessary
#        type_print("You have chosen to go left",speed=0.1,pause=1)
        #player_is_alive == True for alive and False for dead. We died so 
        return False

    #nigel@202105121303 Commentary into next section is disjointed so added a little extra verbage
    type_print("As you drive up a ramp, out of the Medical Research Centre complex, you notice that")
    type_print("far down the other route Zombies are digging potholes in road...")
    type_print("'Lucky escape!!' you think to yourself",pause=3)
    type_print("You wonder: 'How much of the infrastructure have the Zombies damaged?'",pause=2)
    type_print("'Anyway, the strong hold is at the edge of town, the otherside of Dry Creek Bridge'")
    type_print("So you continue on your way through the city...",pause=2)
    #player_is_alive == True for alive and False for dead. We are still alive
    return True