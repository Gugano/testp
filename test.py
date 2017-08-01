low=0
high=100
print "Please think of a number between 0 and 100!"
guess = 50

while True:
	print 'Is your secret number ' + str(guess) + '?'
	#try:
	ans = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
	if ans == 'c':
		break
	elif ans == 'h':
		high = guess
		guess = (high + low) / 2
	elif ans == 'l':
		low = guess
		guess = (high + low) / 2
	else :
		print 'Sorry, I did not understand your input.'
			
print "Game over. Your secret number was:" + str(guess)