# helloworld.py file for UAT Bit by Bit coding club
# greetings, coding traveller!
# this program will output the text 'Hello World' to the terminal
# i have added comments to explain the code
# comments are denoted with the crunchbang (or hashtag, for you twitter-addicted children) ==> '#'

try: # try is a function that allows us to pass code after it, and exit the try structure if the code fails
	print('Hello World\n') # Python operates off of keywords. 
	# Print is a very commonly used keyword that tells the interpreter to display a line of text in the console
	# \n in the above print statement tells the interpreter to skip to a newline. 
	# This is helpful when trying to space out text. 
	# Nobody wants to look at huge blocks of text output!
except: # except is the secondary part of the try functionality. It catches any exceptions, or errors/unexpected results, that result from the code within the 'try' block
	print('Looks like there was an error somewhere. Sorry about that!') 
	# printing error messages is a very good practice
	# you will find it very valuable when you are troubleshooting your code and trying to track down and destroy bugs

print('Awesome!! You just ran your first Python program! If you want to see the source code for this program:')
print('- In Windows, type \'notepad helloworld.py\' or \'type helloworld.py\'') 
	# notepad is the default GUI text editor on Windows
	# type allows you to display the contents of a file to the terminal
print('- In MacOS, type \'open -e helloworld.py\', \'cat helloworld.py\', or \'vim helloworld.py\'') 
	# open -e opens a file in TextEdit, the default GUI text editor on MacOS
	# cat displays the contents of a file to the terminal
	# vim is a terminal-based text editor
print('- In Linux, type \'vim helloworld.py\', \'nano helloworld.py\', or \'cat helloworld.py\'') 
	# vim and nano are both terminal based text editors that natively exist on all Linux distros
	# cat displays the contents of a file to the terminal
input('Press ENTER to EXIT this program. . .') 
	# the input keyword in Python allows the user to type text in the terminal. 
	# It can even be saved to a variable or data structure for future use! More on that later, though. . .