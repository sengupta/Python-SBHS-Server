def start(whichBoard):
	print "Started board ", whichBoard

def write(character, whichBoard):
	print "Wrote", character, "to Board", whichBoard
	return 0

def read(character, whichBoard):
	print "Read", character, "from", whichBoard
	return 0

def heat(amount, whichBoard):
	print "heated", whichBoard, "by amount", amount
	return 0

def fan(amount, whichBoard):
	print "put fan on", whichBoard, "by amount", amount
	return 0

def temp(whichBoard):
	return 10

def finish(whichBoard):
	print "Finished"
