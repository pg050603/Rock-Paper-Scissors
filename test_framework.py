"""
OPTIONAL TODO: Testing

This function implements testing that can (and should) be extended for the
communications lab.

This is primarily so you can execute unit tests on your code without needing
to be a part of a network of devices.

It contains an example that tests the communication protocol parsing for
recieving messages. Also included is some mocking functionality in the folder
testing_modules. These mimic the behaviour of the micro:bit modules. You can
and should extend those, especially if you use new functions in your code.
"""
import sys
import random
from testing_modules import radio, microbit, utime

"""
Here we are setting up the mock libraries so that when we do import our code
that would be flashed, it can actually find and use these modules.

Note that this isn't the actual functionality of those modules - but we are
creating something functionally similar that we can test on. For example, the
radio module on the micro:bit doesn't have a push_message function - we just
need to somehow create a message to read.

"""
sys.modules['radio'] = radio
sys.modules['microbit'] = microbit
sys.modules['utime'] = utime

import commlab
"""
Note: We need to heed the scope of the modules - we must call prototype.radio,
instead of just radio, even though they point to the same module, because
there is a prototype scope that contains its own radio module.

Also note we have only tested happy paths (ideal/standard inputs) here.
"""
def test_choose_opponent():
    """ Test the choose_opponent function with a random ID number """
    # Setup
    opponent_id = random.randint(0, 99)
    str_id = bytes(str(opponent_id), 'UTF-8')
    if opponent_id < 10:
        str_id = b'0' + str_id
    ida, idb = (opponent_id//10, opponent_id%10)
    commlab.microbit.button_history.load_history(['a']*ida + ['b'] + ['a']*idb + ['b'])
    # Run test
    got_opponent_id = commlab.choose_opponent()
    assert got_opponent_id == str_id

def test_choose_play():
    """ Test the choose_play function with a given play """
    # TODO: write test
    assert True # Replace this with your assert for the test

def test_send_choice():
    """ Test the play message sending capabilities with a given message """
    # Setup
    commlab.MYID = b'17'
    opponent_id = b'42'
    the_play = b'R'
    round_number = 7
    # Run test
    commlab.send_choice(opponent_id, the_play, round_number)
    assert commlab.radio.get_last_out() == b'4217R7'

def test_acknowledge_message():
    """ Test the acknowledgement message construction and send functionality """
    # Setup
    commlab.MYID = b'17'
    opponent_id = b'42'
    round_number = 7
    # Run test
    commlab.send_acknowledgement(opponent_id, round_number)
    assert commlab.radio.get_last_out() == b'4217X7'

def test_parse_message():
    """ Test the ability to parse an incoming message """
    # Setup
    opponent_id = b'42'
    commlab.MYID = b'17'
    round_number = 7

    # Case 1: Received a play
    received_message_case_1 = b'1742R7'
    commlab.radio.push_message(received_message_case_1)
    assert commlab.parse_message(opponent_id, round_number) == b'R', "Case 1 play"
    assert commlab.radio.get_last_out() == b'4217X7', "Case 1 ACK"
    
    # Case 2: Received an acknowledgement
    received_message_case_2 = b'1742X7'
    commlab.radio.push_message(received_message_case_2)
    assert commlab.parse_message(opponent_id, round_number) == b'X', "Case 2 play"
    assert commlab.radio.get_last_out() is None, "Case 2 ACK"
    
    # Case 3: Received an old play
    received_message_case_3 = b'1742P6'
    commlab.radio.push_message(received_message_case_3)
    assert commlab.parse_message(opponent_id, round_number) is None, "Case 3 play"
    assert commlab.radio.get_last_out() == b'4217X6', "Case 3 ACK"
    
    # Case 4: Received a message for someone else
    received_message_case_4 = b'6921S3'
    commlab.radio.push_message(received_message_case_4)
    assert commlab.parse_message(opponent_id, round_number) is None, "Case 4 play"
    assert commlab.radio.get_last_out() is None, "Case 4 ACK"
