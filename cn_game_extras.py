def print_map() :
    print("""
                          ,-.^._                 _
                        .'      `-.            ,' ;
            /`-.  ,----'         `-.   _  ,-.,'  `
          _.'   `--'                 `-' '-'      ;
        :                                        ; 
        ,'    o           o                     ;
        :  Strong Hold   Bridge                 ;
        :                                      ;
        :                                      :
        ;                                      :
      (                    o                  ;
        `-.            Medical Center        ,'
          ;                                  :
        .'                             .-._,'
      .'                               `.
    _.'                                .__;
    `._                 o             ;
      `.              Home          :   
        `.               ,..__,---._;    
          `-.__         :               
              `.--.____;           
    """)                                      

hidden_answers = ["help","map"]
def display_hidden( which) :
    if which == 0 :
        print("<help not available>")
    elif which == 1 :
        print_map()

def str_in_list( chk_str, valid_list):
    result = -1
    list_len = len( valid_list)
    for x in range( 0, list_len):
        if chk_str.upper() == valid_list[x].upper() :
            result = x
    return result


def qa( question, true_options, false_options) :
    answer = "  "

    while answer not in true_options.upper() and answer not in false_options.upper() and str_in_list( answer, hidden_answers) < 0:
        answer = input( question )
        answer = answer.upper()

    if answer in true_options.upper() :
        return True

    if answer in false_options.upper() :
        return False

def qa_until( question, valid_answers) :
    answer_prompt = ""
    result = -1

    #build visual list of valid answers to display
    for ans in valid_answers :
        answer_prompt += (ans + " ")
    for ans in hidden_answers :
        answer_prompt += (ans + " ")
    
    #loop until answer is valid
    while result < 0 :
        #get the user input after displaying the question, a newline and the valid answers
        ans = input( f"{question} \n ( {answer_prompt}) ?")

        # #search valid answers for uppercase match to ans from input above and update result
        result = str_in_list( ans, valid_answers)
        h_req = str_in_list( ans, hidden_answers)
        display_hidden( h_req)

        # for x in range( 0, max_answers):
        #     if ans.upper() == valid_answers[x].upper() :
        #         result = x

    #return result from search(which may have remained -1 meaning no match found)
    return result

def type_print( message, speed=0.01, pause=0.5):
    from sys import stdout
    from time import sleep

    #loop display each character in the message string pausing for 100millsec each time
    for char in message:
        stdout.write(char)
        stdout.flush()
        sleep(speed)

    #after typing the message, pause before proceeding
    sleep(pause)
    stdout.write('\n')
    stdout.flush()
