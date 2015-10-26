# wordartgame
This is a mock arcade game written with the library pygame for use in an art show by one T.L. in BK, NYC.


This is my first attempt at pygame and there are some optimization issues that need to be worked out.

Likewise, since I am still learning, I took the opportunity to write two different versions of this code.  

The main.py in the primary /bin is the first iteration of the code.  It took about 5 days, most of which was playing around with pygame and reading documentation.  

The second, also found in the primary /bin is the OOP version wherein I encapsulate the entire project in a single 
class.  I also tried to make use of the scoping of the class to allow individual functions to make fast changes in the primary loop of the 'game'.  It also was an opportunity to clean up the code and try to make some things prettier.  That said, there are some problems with the dictionary implementation I tried to use to streamline the long line of if-else loops I had to detect key-press events.  Further changes and fixes will be added eventually.

Remaining Tasks as of 10/25/2015:
  -Create a frozen binary for usage on a RasPi B
  -Further optimize the code to be faster, namely, fewer calls and writes outside of the class and taking some of the mote convoluted loops, especially that damn KEYUP check for held down buttons.  Also figure out if you are actually purging out the former words.  
  - Rebuild the getTitle() method because it is messy as hell.   
  -initialize the word list in chunks and/or place it in a generator to make sure it's not being dumped into memory as a giant blob at runtime.
  -Create a function that allows for input from a customizable .config file so the user doesn't have to make configuration changes to the source itself.  
  -Add music/sounds.

