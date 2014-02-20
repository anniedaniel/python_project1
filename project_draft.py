import re
import string

#emma is a smaller, placeholder file
fairyTale = open("emma.txt", "r")
#grimm is the actual file I'll be working with later
#grimm_file = open("grimms.txt", "r")
stopwords = open("stopwords.txt","r")
grimm = {}

def process_file(fairyTale):
	for line in fairyTale:
		process_line(line,grimm)		
	return grimm