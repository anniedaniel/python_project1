import re
import string
#emma is a smaller, placeholder file
# fairyTale = open("emma.txt", "r")
#grimm is the actual file I'll be working with later
fairyTale = open("grimms.txt", "r")
stopwords = open("stopwords.txt","r")
grimm = {} #big dictionary of words
storyDict = {} #dictionary within dictionary of words of story titles
linelist = [] 
stopwordlist = [] #list of stopwords from stopwords.txt to remove from dictionary
linenum = 0 #line number
storytitle = ""
querylines = {}


def process_file(fairyTale):
	""" Processes the file and breaks the lines into a list """
	for line in stopwords:
		line = line.strip()
		stopwordlist.append(line)

	for line in fairyTale:
		global linenum 
		linenum += 1 
		process_line(line,grimm)
	
	return grimm


def process_line(line, grimm):
	# global linenum
	# match = re.search(r'THE', line)
	# if match:
	# 	beginningline = linenum	
	# 	print linenum
	# 	print beginningline
	# 	if linenum > beginningline & beginningline != 0:  #finds the beginning
	if linenum > 120:
		title = re.search(r'^[A-Z]+[^a-z]+$', line) #finds story titles
		
		if linenum < 9182:
			if title: #if it's a title, defines it as a story title and strips them
				global storytitle 
				storytitle = line
				storytitle = storytitle.strip()
			else: #parses through the stories
				global querylines
				querylines[linenum] = line.strip()
				for word in line.split():
					word = word.strip(string.punctuation + string.whitespace)
					word = word.lower()
					if word not in stopwordlist: #gets rid of the stopwords yuck
						grimm.setdefault(word,{}).setdefault(storytitle,[]).append(linenum)

grimmDictionary = process_file(fairyTale)
#print querylines
##### search stuff

query = ""
while query != "qquit":
	query = raw_input("Please enter your query: ")
	query = query.lower()
	querylist = query.split()


	def search(grimmDictionary, query): 
		""" Search function to search the keys, or words, of the dictionary and pick up
		its line number and line it occurs. """
		if query in grimmDictionary.keys():
			for qtitle, qlinenum in grimmDictionary[query].items():
				print qtitle
				print "  ",query
				for listlinenum in qlinenum:
					print "    ",listlinenum, querylines[listlinenum].replace(query, "**"+query.upper()+"**")
		else:
			print "--"

	def multiple_search(querylist):
		querylen = len(querylist) 
		if querylen == 1: #if the user inputs only one query
			query = querylist[0]
			search(grimmDictionary,query)
		elif 'or' in querylist: #if the user inputs two queries separated by "or"
			query = querylist[0]
			search(grimmDictionary, query)
			query1 = querylist[2]
			search(grimmDictionary, query1)
		elif "and" in querylist: #if the user inputs two queries separated by "and"
			query1 = querylist[0]
			query2 = querylist[2]
			if query1 in querylines.values():
				if query2 in querylines[query1].values():
					search(grimmDictionary, query2)
			else: 
				print "--"
		elif querylen > 2: #more than two objects, functions the same as "and"
			if 'or' not in querylist:
				if 'and' not in querylist:
					for i in range(0, querylen):
						query = querylist[i]
						search(grimmDictionary,query)
		# if "near" in querylist:
		# 	query1 = querylist[0]
		# 	query2 = querylist[2]
		# 	if query1 in grimmDictionary.keys():
		# 		for qtitle, qlinenum in grimmDictionary[query].items():
		# 			print qtitle
		# 			print "  ",query
		# 			for listlinenum in qlinenum:
		# 				print "    ",listlinenum, querylines[listlinenum]
		# 	else:
		# 		print "--"

	multiple_search(querylist)







#d[word][storytitle]
# and/or queries, break it into indices. __ and __ (0,1,2)- if 1 is and do whatever


	
