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


def process_line(line, grimm):
	line = line.replace('-',' ')
	linenum = 0
	storytitle = ""
	
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		# if word in stopwords:
		# 	del grimm[word]
		grimm[word] = grimm.get(word, 0)

	# for line in fairyTale:
	# 	linenum += 1
	# 	match = re.search(r'CHAPTER*',line)
	# 	if match:
	# 		storytitle = match.group()
		# grimm(word) = storytitle
		# if line is storytitle:
		# 	new_storytitle = current_line

	#grimm.setdefault(word,{}).setdefault(storytitle,[]).append(linenum)
	print grimm

print process_file(fairyTale)


#d[word][storytitle]
# and/or queries, break it into indices. __ and __ (0,1,2)- if 1 is and do whatever


	
