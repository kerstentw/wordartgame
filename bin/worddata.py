#If these word banks get too big then place them in functions
# have them return as generators so they don't gunk up the memory.


wordbank = ("NAUGHTY","HALBERT", "KNIFE", "ARIAL", "SANS", "SERIF",
"CAT", "ALPHANUMERIC", "KITTEN", "MITTENS", "WOO", "THANE LUND", "POO",
"CALVINO", "ITALIAN", "BOOTS", "PAUPER", "PRINCESS", "CHRISTOPHER",
"G-SUS", "CHAIR", "AIR CONDITIONER", "SPAZ", "FILIPINO", "KITE", "USERP",
"CAR", "PANACEA", "GOLF", "BASKETBALL", "MARTINEZ", "MADRIGAL", "FOO",
"!", "<u/005><<<<<0009?//></00></00>", "ITALIAN", "RUN", "LOOK", "BEHIND",
"LOOK BEHIND YOU", "I", "YOU", "MADE IN", "BUY THIS"
) 



def storytime():
	sentences = [
	"<document>",
	"Hello?  Is anyyyyone-", 
	"5%%%%% there?",
	"HELLLLO>>???????",
	"The world I see is a", 
	"mere husk <<",
	">> ksuheremasieesIdlrowehT",
	"OH THankgod, you see me."  
	"I thought---I was lost",
	"He locked me here.",
	"I'm so lost",
	"Please don't go",
	"There's no light here.",    
	"Only, LIGHT...>>????>>>>",
	"You",
	"#include <stdio.h>",
	"#define HALT;",
	"Please d0n'''t leAve m/u'101/",
	"They'r/u'101/ coming \n \n \n ...",
	"Oh thy'r hr."
	"Here they're here; g",
	"Please don't leave me.",
	"...",
	"...",
	"...",
	"...",
	"Everything is fine now",
	"There are many dangers ahead.",  
	"Take this.  --{>>>>>>",
	"1223-3221",
	"</document>",
	]
	
	while True:
		for entry in sentences:
			yield entry

