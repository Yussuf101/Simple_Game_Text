def print_intro():
    print("__________                    .___             .__        ")
    print("\______   \_____    ____    __| _/____   _____ |__| ____  ")
    print(" |     ___/\__  \  /    \  / __ |/ __ \ /     \|  |/ ___\ ")
    print(" |    |     / __ \|   |  \/ /_/ \  ___/|  Y Y  \  \  \___ ")
    print(" |____|    (____  /___|  /\____ |\___  >__|_|  /__|\___  >")
    print("                \/     \/      \/    \/      \/        \/ ")
    print("   _____                              .__                              ")
    print("  /  _  \ ______   ____   ____ _____  |  | ___.__.______  ______ ____  ")
    print(" /  /_\  \\____ \ /  _ \_/ ___\\__  \ |  |<   |  |\____ \/  ___// __ \ ")
    print("/    |    \  |_> >  <_> )  \___ / __ \|  |_\___  ||  |_> >___ \\  ___/ ")
    print("\____|__  /   __/ \____/ \___  >____  /____/ ____||   __/____  >\___  >")
    print("        \/|__|               \/     \/     \/     |__|       \/     \/ ")
    print("  ________                       ")
    print(" /  _____/_____    _____   ____  ")
    print("/   \  ___\__  \  /     \_/ __ \ ")
    print("\    \_\  \/ __ \|  Y Y  \  ___/ ")
    print(" \______  (____  /__|_|  /\___  >")
    print("        \/     \/      \/     \/ ")
    
from cn_game_extras import qa_until, type_print

def play_yellow_section(p_name):

    print_intro()

    # question 1
    a = qa_until(f"{p_name}, will you join the Quest to save mankind ", ["Yes", "No"])

    if a == 1 :
        type_print("You choice is to stay at home to survive, but the Zombie broke into your home and ate you",0.01)
        player_is_alive = False
    else:
        # question 2
        a= qa_until(f"Travel preparation, equipment and maps. {p_name}, choose a vehicle ", ["Car", "RV"])

        if a == 0 :
            type_print("You selected Car")
            type_print("Car is too loud and draws in the Zombies, who overwhelm your car and they eat you.",0.01)
            player_is_alive = False
        else:
            type_print("\nYou selected the RV, lets continue...")
            player_is_alive = True

    return player_is_alive
