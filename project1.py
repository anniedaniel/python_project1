import re
import string

fairyTale = open("emma.txt", "r")
stopwords = open("stopwords.txt","r")
grimm = {}

def process_file(filename):
	for line in fairyTale:
		process_line(line,grimm)		
	return grimm


def process_line(line, grimm):
	line = line.replace('-',' ')
	linenum = 0
	title = "something"

	for line in fairyTale:
		match = re.search(r'[A-Z]++',line)
		if match:
			storytitle = match.group()

	
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
	
	for line in fairyTale:
		linenum += 1
		# if line is storytitle:
		# 	new_storytitle = current_line
		# 	for line in fairyTale:
				
	grimm.setdefault(word,{}).setdefault(line,[]).append(linenum)
	# print grimm

		# if word in stopwords:
		# 	del grimm[word]

		# for line in fairyTale:
		# 	linenum += 1
		# 	has_match = line.find(word)
		# 	if has_match >= 0:
		# 		return linenum, line

		

print process_file(fairyTale)


#d[word][storytitle]
# and/or queries, break it into indices. __ and __ (0,1,2)- if 1 is and do whatever


	
