i256 Applied Natural Language Processing
Instructor: Prof. Marti Hearst
Fall 2013 Final Project

Title: Poetic Search Engine: Sound, Semantics, and Syntax
Team: Kyle Booten, Herman Leung


The files in this folder contain only half of the project (the parts written by Herman Leung).

* i256_FinalProject_Description.txt -- describes details of the project including references to data sources

* corpus_etym_sound.py -- the main python code that utilizes the other .py files

* EAT_etym_extraction_code.py -- extracts data from the Edinburgh Associative Thesaurus and the Etymological Wordnet into formats useful for the project

* etym4.py -- one of the outputs of EAT_etym_extraction_code.py, specifically a reformatted subset of the Etymological Wordnet

* sounds.py -- rhyming functions utilizing the Carnegie Mellon University Pronouncing Dictionary (nltk.corpus.cmudict)

* poetry_corpus_creation.py -- webscraping code which extracts poems from http://famouspoetsandpoems.com/ and writes to a folder of files which can be turned into an nltk corpus reader object

* Poetry.tar.gz -- the zipped output of the folder of poems created by poetry_corpus_creation.py