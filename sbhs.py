import serial

INCOMING_HEAT = 254
INCOMING_FAN  = 253
OUTGOING_TEMP = 255

board = {} # Initializing empty dictionary

def start(whichBoard):
    global board
    board[whichBoard] = serial.Serial('/dev/ttyUSB'+str(whichBoard), 9600)

def write(character, whichBoard):
    board[whichBoard].write(chr(character))
    return 0

def read(character, whichBoard):
    board[whichBoard].read(chr(character))
    return 0

def heat(amount, whichBoard):
    board[whichBoard].write(chr(INCOMING_HEAT))
    board[whichBoard].write(chr(amount))
    return 0

def fan(amount, whichBoard):
    board[whichBoard].write(chr(INCOMING_FAN))
    board[whichBoard].write(chr(amount))
    return 0

def temp(whichBoard):
    board[whichBoard].flushInput()
    board[whichBoard].write(chr(OUTGOING_TEMP))
    return ord(board[whichBoard].read(1)) + 0.1*ord(board[whichBoard].read(1))

def finish(whichBoard):
    fan(100, whichBoard)
    heat(0, whichBoard)
    board[whichBoard].close()
