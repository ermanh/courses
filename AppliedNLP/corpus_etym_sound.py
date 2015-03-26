##### i256 Final Project
##### Title: Poetic Search Engine: Sound, Semantics, and Syntax
##### Team members: Kyle Booten & Herman Leung
##### Code written by: Herman Leung
##### ** This is only half of the components of the final project submitted**

"""
This code contains:
(1) the corpus of poetry
(2) the etymology dictionary
(3) functions for extracting rhyme/initial consonants for alliteration

Please place the following files in your corresponding Python directory:
(A) etym4.py
(B) sounds.py
(C) Poetry.zip (unzip it to a folder of 11.5 MB) 
     * CHANGE corpus_dir BELOW TO WHERE YOU PUT THE Poetry FOLDER
     ** Files in Poetry.zip created from poetry_corpus_creation.py **
"""

####################################
##### IMPORTS, GLOBALS, SETUPS #####
####################################

import nltk, re, os
from nltk.corpus import CategorizedTaggedCorpusReader as CTCR

from etym4 import etym4		
etym = dict(etym4)			# this is the etymological dictionary
from etym4 import iso_dict	# this is the dictionary for decoding the 3-letter codes (in 'ori') 
							#      that represent the source language
from etym4 import cat_dict	# this is the dictionary for the category codes (in 'cat')
							#		these are language categories (such as German, Romance, Non-European)

from sounds import get_perfect_rhyme   	# These three are functions that take 
from sounds import get_last_rhyme		#      a word in string format as argument
from sounds import get_initial

corpus_dir = 'C:/Python27/Poetry/'  # <-- CHANGE THIS (wherever you place the unzipped Poetry folder)

##### CorpusReader Creation #####
poetry = CTCR(corpus_dir, r'.*\.txt', cat_pattern=r'(.*?)\_.*')


################################
##### DEMOs & EXPLANATIONS #####
################################

##### poetry - the CategorizedTaggedCorpusReader object
'''
The poetry corpus is a folder of 5645 files(/poems).
Each file is named in the format 'AuthorFullName_PoemTitle.txt', and were tagged using nltk.pos_tag().
Each file is also headed by two untagged lines, one being the poem title, the other being the author.
NOTE: Each tagged line also starts with an *untagged* line number
	(e.g., '10: Amid/NNP the/DT nebulous/JJ humanity/NN')
The categories are the authors' full names (without spaces).
'''
poetry.categories()		# returns all author names (76 total)
len(poetry.fileids())	# 5645

poetry.sents()[1000]
# ['115:', 'Bright', 'Spirit', ',', 'whose', 'illuminings', 'I', 'sought', ',']

poetry.tagged_sents()[1000]		# Note untagged first item (where tag value is None)
# [('115:', None), ('Bright', 'JJ'), ('Spirit', 'NN'), (',', ','), ('whose', 'WP$'), 
	('illuminings', 'NNS'), ('I', 'PRP'), ('sought', 'VBP'), (',', ',')]

poetry.paras()[1]	# poetry.paras() returns all the poems, each a list of lines
#[
#	['[TITLE]', 'After', 'an', 'Epigram', 'of', 'Clement', 'Marot'], 
#	['[AUTHOR]', 'Alan', 'Seeger'], 
#	['1:', 'The', 'lad', 'I', 'was', 'I', 'longer', 'now'], 
#	['2:', 'Nor', 'am', 'nor', 'shall', 'be', 'evermore', '.'], 
#	['4:', 'Have', 'shed', 'their', 'petals', 'on', 'the', 'floor', '.'], 
#	['5:', 'Thou', ',', 'Love', ',', 'hast', 'been', 'my', 'lord', ',', 'thy', 'shrine'], 
#	['6:', 'Above', 'all', 'gods', "'", 'best', 'served', 'by', 'me', '.'], 
#	['7:', 'Dear', 'Love', ',', 'could', 'life', 'again', 'be', 'mine'], 
#	['8:', 'How', 'bettered', 'should', 'that', 'service', 'be', '!']
	]

# Other standard functions: poetry.words(), poetry.raw()


##### etym, iso_dict #####

etym['little']		# Note, etym is a dictionary of dictionaries of *lists*
# {'cat': ['ger'], 'ori': ['enm']}

iso_dict['enm']
# 'Middle English (1100-1500)'

iso_dict[etym['forgive']['ori'][0]]		# Note, etym is a dict of dicts of *lists* (hence [0] at the end)
# 'Middle English (1100-1500)'			# The list may have more than 1 value stored sometimes

cat_dict['ger']
# 'Germanic languages'


##### get_perfect_rhyme, get_last_rhyme, get_initial #####

get_perfect_rhyme('forgive')	# Gets vowel of primary stress plus all following sounds
# ['IH1', 'V']					# NOTE: this is the part that determines a rhyme in traditional poetry

get_last_rhyme('apple')		# Gets last syllable rhyme (imperfect rhyme)
# ['AH0', 'L']

get_initial('stray')		# Gets initial consonant (cluster) sound(s)
# ['S', 'T', 'R']
