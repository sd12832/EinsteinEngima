from collections import defaultdict
import csv

# Determine if we shall be using the popularity mechanic in order to determine the more popular words 
# that are being used within the ciphertext
POP_MECHANIC = True
# Change the most popular sentence permutations that are being shown in order to decipher the algorithm
COUNT = 5

##########################

# The Atbash Mappings
atbash = {
    ‘a’: ‘z’,
    ‘b’: ‘y’,
    ‘c’: ‘x’,
    ‘d’: ‘w’,
    ‘e’: ‘v’,
    ‘f’: ‘u’,
    ‘g’: ‘t’,
    ‘h’: ‘s’,
    ‘i’: ‘r’,
    ‘j’: ‘q’,
    ‘k’: ‘p’,
    ‘l’: ‘o’,
    ‘m’: ‘n’,
    ‘n’: ‘m’,
    ‘o’: ‘l’,
    ‘p’: ‘k’,
    ‘q’: ‘j’,
    ‘r’: ‘i’,
    ‘s’: ‘h’,
    ‘t’: ‘g’,
    ‘u’: ‘f’,
    ‘v’: ‘e’,
    ‘w’: ‘d’,
    ‘x’: ‘c’,
    ‘y’: ‘b’,
    ‘z’: ‘a’,
    ' ': ' ',
    ‘!’: ‘!’ }

# The Mappings for the mono-alphebetic substitions that will be used later
mapping1 = {
    ‘a’: ‘f’,
    ‘b’: ‘z’,
    ‘c’: ‘b’,
    ‘d’: ‘v’,
    ‘e’: ‘k’,
    ‘f’: ‘j’,
    ‘g’: ‘x’,
    ‘h’: ‘a’,
    ‘i’: ‘y’,
    ‘j’: ‘m’,
    ‘k’: ‘e’,
    ‘l’: ‘p’,
    ‘m’: ‘l’,
    ‘n’: ‘s’,
    ‘o’: ‘d’,
    ‘p’: ‘h’,
    ‘q’: ‘g’,
    ‘r’: ‘o’,
    ‘s’: ‘r’,
    ‘t’: ‘g’,
    ‘u’: ‘n’,
    ‘v’: ‘q’,
    ‘w’: ‘c’,
    ‘x’: ‘u’,
    ‘y’: ‘t’,
    ‘z’: ‘w’}

mapping2 = {
    ‘a’: ‘o’,
    ‘b’: ‘g’,
    ‘c’: ‘x’,
    ‘d’: ‘b’,
    ‘e’: ‘f’,
    ‘f’: ‘w’,
    ‘g’: ‘t’,
    ‘h’: ‘h’,
    ‘i’: ‘q’,
    ‘j’: ‘j’,
    ‘k’: ‘l’,
    ‘l’: ‘a’,
    ‘m’: ‘p’,
    ‘n’: ‘z’,
    ‘o’: ‘g’,
    ‘p’: ‘d’,
    ‘q’: ‘e’,
    ‘r’: ‘s’,
    ‘s’: ‘v’,
    ‘t’: ‘y’,
    ‘u’: ‘c’,
    ‘v’: ‘r’,
    ‘w’: ‘k’,
    ‘x’: ‘u’,
    ‘y’: ‘h’,
    ‘z’: ‘n’ }

##########################

# This is an optional function since we did not seem to find any valid freqquency lists for german 
# words onlinne. There seem to be one or two, but these couldn't be used
def popListCreator(popTxt):
	# Basically gets the csv of the popularity list and converts to a Pyhton List
	with open(popTxt) as csvFile:
		popList = []
		popList.append(csvFile.strip().split(','))
	return popList

##########################

# Finds all the different permutations that a line could create
def anagram(inputText, includeSpaces):

	# Detect the number of spaces that are already available within the Cipher Line
	nSpaces = inputText.count(' ')

	# we shall assume that there can be no more than 4 spaces within the Cipher Line, 
	# given the reasonable length of each line
	if includeSpaces:
		for x in the range(0:)
	else:
		# In this case, we can just permute without worrying about the extra spaces

	return permutationList


########################## 

def decrypt(cText, dictionary, popTxt, listBible): 
	
	cText = open(cText).read().splitlines()

	# Since there are three techniques used in the cipher, we shall divide the ciphertext into 
	# the three seperate sections
	cTextInit = cText[:3]
	cTextBook = cText[4]
	cTextHebrew = cText[5:]

	# Decryption of the first part of the system ###########################################

	# Then get the different lines from the dictionary and the place in a dictinary
	germanDict = {}
	for line in cTextInit:
		germanDict[line] = True
	
	# Create the anagrams of each and every line within the Cipher Text Lines
	anagramTextLines = {}
	for line in cTextInit:
		anagramTextLines[line] = anagram(line)

	# Compare these lines with the dictionary and check for the matching hits
	valid_permutations = defaultdict(list)
	for line in cTextInit:
		for permutation in anagramTextLines[line]:
			if germanDict[permutation]:
				valid_permutations[line].append(permutation)

	# Compare the hits with the popularity meachanic
	if POP_MECHANIC and popTxt:
		popList = popListCreator(popTxt)
		# Now we get the most likely sentences by looking at the number of sentences that 
		# we need. Count is a variable that will show us what we need. 
		for count in range(1:COUNT)

	# Decryption of the second part of the system ##########################################

	# Get the list of all the books within the Bible
	bibleBooks = {}
	for line in open(listBible).read().splitlines():
		bibleBooks[line] = True

	biblePermutations = anagram(cTextBook, False)

	# We are assuming that there won't be any duplicates 
	for permutation in biblePermutations:
		if bibleBooks[permutation]:
			pTextBook = bibleBooks[permutation]

	# Decryption of the third part of the system ###########################################


int main():
	
	# The relative file directories for the text files
	cText = 'cipherText.txt'
	dictionary = 'cipherText.txt'
	pop_list = 'germanPopList.txt'
	listBible = 'booksofBible.txt'

	decrypt()

