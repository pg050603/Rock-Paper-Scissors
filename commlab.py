import microbit # Do not change these to star imports, the test code neds them
import utime    # like this to work properly!
import radio

# Global constants

ROCK = microbit.Image('00000:09990:09990:09990:00000')
PAPER = microbit.Image('99999:90009:90009:90009:99999')
SCISSORS = microbit.Image('99009:99090:00900:99090:99009')
RPS = (b'R', b'P', b'S')

MYID = b'00' # TODO: change this to be the same as your assigned micro:bit number

def choose_opponent():
    # """ Return the opponent id from button presses
    #
    # Returns
    # -------
    # byte string:
    #     A two-character byte string representing the opponent ID
    #
    # Notes
    # -------
    # Button A is used to increment a digit of the ID
    # Button B is used to 'lock in' the digit and move on
    # """
    #
    # This function is complete.
    
    # Initialization
    num = [0]*2
    idx = 0
    
    # Main loop over digits
    while idx < len(num):
        microbit.sleep(100)
        # Display only the last character of the hex representation (skip the 0x part)
        microbit.display.show(hex(num[idx])[-1], wait=False)
        # The button increments the digit mod 16, to make sure it's a single hex digit
        if microbit.button_a.was_pressed():
            num[idx] = (num[idx] + 1)%16
        # Show a different character ('X') to indicate a selection
        if microbit.button_b.was_pressed():
            microbit.display.show('X')
            idx += 1
    microbit.display.clear()
    
    # Make sure we return a byte string, rather than a standard string.
    return bytes(''.join(hex(n)[-1] for n in num), 'UTF-8')

def choose_play():
    # """ Returns the play selected from button presses
    #
    # Returns
    # -------
    # byte string:
    #     A single-character byte string representing a move, 
    # as given in the RPS list at the top of the file.
    # """
    #
    # TODO: write code
    return b''

def send_choice(opponent_id, play, round_number):
    # """ Sends a message via the radio
    #
    # Parameters
    # ----------
    # opponent_id  : byte string
    #     The id of the opponent
    # play         : byte string
    #     One of b'R', b'P', or b'S'
    # round_number : int
    #     The round that is being played
    #
    # Returns
    # -------
    # int:
    #     Time that the message was sent
    # """
    #
    # TODO: write code
    return 0

def send_acknowledgement(opponent_id, round_number):
    # """ Sends an acknowledgement message
    #
    # Parameters
    # ----------
    # opponent_id  : bytes
    #     The id of the opponent
    # round_number : int
    #     The round that is being played
    # """
    #
    # TODO: write code
    pass

def parse_message(opponent_id, round_number):
    # """ Receive and parse the next valid message
    #
    # Parameters
    # ----------
    # opponent_id  : bytes
    #     The id of the opponent
    # round_number : int
    #     The round that is being played
    #
    # Returns
    # -------
    # bytes :
    #     The contents of the message, if it is valid
    # None :
    #     If the message is invalid or does not need further processing
    #
    # Notes
    # -----
    # This function sends an acknowledgement using send_acknowledgement() if
    # the message is valid and contains a play (R, P, or S), using the round
    # number from the message.
    # """
    #
    # TODO: write code
    return b''

def resolve(my, opp):
    # """ Returns the outcome of a rock-paper-scissors match
    # Also displays the result
    #
    # Parameters
    # ----------
    # my  : bytes
    #     The choice of rock/paper/scissors that this micro:bit made
    # opp : bytes
    #     The choice of rock/paper/scissors that the opponent micro:bit made
    #
    # Returns
    # -------
    # int :
    #     Numerical value for the outcome as listed below
    #      0: Loss/Draw
    #     +1: Win
    #
    # Notes
    # -----
    # Input parameters should be one of b'R', b'P', b'S'
    #
    # Examples
    # --------
    # solve(b'R', b'P') returns 0 (Loss)
    # solve(b'R', b'S') returns 1 (Win)
    # solve(b'R', b'R') returns 0 (Draw)
    #
    # """
    #
    # This function is complete.
    
    # Use fancy list indexing tricks to resolve the match
    diff = RPS.index(my) - RPS.index(opp)
    result = [0, 1, 0][diff]
    
    # Display a cute picture to show what happened
    faces = [microbit.Image.ASLEEP, microbit.Image.HAPPY, microbit.Image.SAD]
    microbit.display.show(faces[diff])
    # Leave the picture up for long enough to see it
    microbit.sleep(333)
    return result

def display_score(score, times=3):
    # """ Flashes the score on the display
    #
    # Parameters
    # ----------
    # score : int
    #     The current score
    # times : int
    #     Number of times to flash
    #
    # Returns
    # -------
    # None
    #
    # Notes
    # -----
    # If the score is greater than 9 it scrolls, rather than flashing.
    # """
    #
    # This function is complete.
    
    screen_off = microbit.Image(':'.join(['0'*5]*5))
    if score < 9 and score >= 0:
        microbit.display.show([screen_off, str(score)]*times)
    elif score > 9:
        for n in range(times):
            microbit.display.scroll(str(score))
            microbit.display.show(screen_off)
            microbit.sleep(333)

def main():
    # """ Main control loop"""
    #
    # TODO: fill in parts of code below as marked.
    
    # set up the radio for a moderate range
    radio.config(power=6, queue=50)
    radio.on()
    
    # initialise score and round number
    score = 0
    round_number = 0
    
    # select an opponent
    opponent_id = choose_opponent()
    
    # Run an arbitrarily long RPS contest
    while True:
        # get a play from the buttons
        choice = choose_play()
        # send choice
        send_time = send_choice(opponent_id, choice, round_number)
        
        acknowledged, resolved = (False, False)
        # passive waiting display
        microbit.display.show(microbit.Image.ALL_CLOCKS, wait=False, loop=True)
        while not (acknowledged and resolved):
            # get a message from the radio
            message = parse_message(opponent_id, round_number)
            
            # TODO: if is a play
            if False:
                # resolve the match and display the result
                result = resolve(choice, message)
                
                # TODO: update score

                # display the score
                display_score(score)
                
            # TODO: if is acknowledgement
            if False:
                pass
                
            # TODO: handle situation if not acknowledged
            if False:
                pass
                
        # TODO: Update round number

# Do not modify the below code, this makes sure your program runs properly!

if __name__ == "__main__":
    main()
    