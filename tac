#!/usr/bin/awk -f
#
# awk replacement for missing tac command in OSX
#
# Credit: http://tipstricks.itmatrix.eu/?p=305
#
1 { 
	last = NR; 
	line[last] = $0; 
}

END { 
	for (i = last; i > 0; i--) { 
		print line[i]; 
	} 
}

