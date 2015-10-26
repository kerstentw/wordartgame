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
	"Hello?  Is anyyyyone 5%%%%% there?",
	"HELLLLO>>???????",
	"The world I see is a mere husk <<>> ksuh erem a si ees I dlrow ehT",
	"OH THank god, you see me.  I thought          I was lost",
	"The THEY put me in here.",
	"I'm so lost",
	"Please don't go",
	"There's only light here.    Only, LIGHT...>>????>>>>",
	"#include <stdio.h>; #define HALT",
	"Please don'''''t leave me",
	"They're coming \n \n \n ...",
	"Oh god they're here.       Here they're here; g",
	"Please don't leave me.",
	"There are many dangers ahead.  Take this.  --{>>>>>>",
	"1223-3221",
	"</document>",
	]
	
	while True:
		for entry in sentences:
			yield entry

