##### i256 Final Project
##### Corpus Creation
##### Team members: Kyle Booten & Herman Leung
##### Code written by: Herman Leung

'''
##### DATA SOURCE #####
19th Century American Poetry
- http://famouspoetsandpoems.com/country-6/America/19th_century_American_poets.html
- web-scraped
'''

import re
import urllib2

## AUTHORS (73)

html_19th = urllib2.urlopen('http://famouspoetsandpoems.com/country-6/America/19th_century_American_poets.html').read()
poets = re.findall('title\=\"(.*?)\"', html_19th)

# len(poets)
# 73

poets_19c = []
for p in poets:
	new = p.lower()
	new = re.sub(' ', '_', new)
	poets_19c.append(new)

## POEM URLS (5720)
# URLs in poem_urls list don't include the string 'http://famousepoetsandpoems.com' 

poem_urls = []
for p in poets_19c:
	html = urllib2.urlopen('http://famouspoetsandpoems.com/poets/' + p + '/poems').read()
	poem_url = re.findall('href\=\"(\/poets\/.*?\/poems\/.*?)\"', html)
	poem_urls += poem_url

# len(poem_urls)
# 5720	

poems_html_raw = []
for p in poem_urls:
        # Still may need to be done in steps because of reliance on internet connection and related.
        # The process takes up to an hour.
        f1 = urllib2.urlopen('http://famouspoetsandpoems.com' + p)
        html = f1.read()
        f1.close()
        poem = re.findall('font-size:13px;\"\>\\n\\t{6}(.*?)\\t{6}', html)[0]
        title_author = re.findall('font-size:16px;color:#3C605B;font-family:Times New Roman;\"\>(.*?)\<\/span\>', html)[0]
        title = re.findall('(.*?) \<', title_author)[0]
        author = re.findall('by (.*)', title_author)[0]
        poems_html_raw.append((author, title, poem))

poems_html_raw_u = [(a.decode('utf8'), b.decode('utf8'), c.decode('utf8')) for (a,b,c) in poems_html_raw]
phru = poems_html_raw_u
def exchange_utf_to_ascii(phru):
        phru = [(re.sub(ur'[\u2018\u2019]', '\'', a), re.sub(ur'[\u2018\u2019]', '\'', b), re.sub(ur'[\u2018\u2019]', '\'', c))
                for (a,b,c) in phru] # Change curly single quotes to straight single quotes
        phru = [(re.sub(ur'\u201c|\u201d|\xe2\u20ac\x9d|\xe2\u20ace', '\"', a), re.sub(ur'\u201c|\u201d|\xe2\u20ac\x9d|\xe2\u20ace', '\"', b), re.sub(ur'\u201c|\u201d|\xe2\u20ac\x9d|\xe2\u20ace', '\"', c))
                for (a,b,c) in phru] # Change curly double quotes to straight double quotes
        phru = [(re.sub(ur'[\u2026]', '...', a), re.sub(ur'[\u2026]', '...', b), re.sub(ur'[\u2026]', '...', c))
                for (a,b,c) in phru] # Change epentheses to three dots
        phru = [(re.sub(ur'\xe2\u20ac\u2122', '\'', a), re.sub(ur'\xe2\u20ac\u2122', '\'', b), re.sub(ur'\xe2\u20ac\u2122', '\'', c))
                for (a,b,c) in phru] # Change weird thing to single quote
        phru = [(re.sub(ur'\u2013|\u2014|\xe2\u20ac', '--', a), re.sub(ur'\u2013|\u2014|\xe2\u20ac', '--', b), re.sub(ur'\u2013|\u2014|\xe2\u20ac', '--', c))
                for (a,b,c) in phru] # Change en- and em-dashes to '--'
        phru = [(re.sub(ur'\xc3\xa7|\xe7', 'c', a), re.sub(ur'\xc3\xa7|\xe7', 'c', b), re.sub(ur'\xc3\xa7|\xe7', 'c', c))
                for (a,b,c) in phru] # Change 'c' with cedilla to just 'c'
        phru = [(re.sub(ur'\xc3\xb1|\xf1', 'ny', a), re.sub(ur'\xc3\xb1|\xf1', 'ny', b), re.sub(ur'\xc3\xb1|\xf1', 'ny', c))
                for (a,b,c) in phru] # Change 'n' with tilda to 'ny'
        phru = [(re.sub(ur'[\xe8\xe9\xeb\xe6\u0426\u0153\xea\u043a\u0439\u043b]', 'e', a), re.sub(ur'[\xe8\xe9\xeb\xe6\u0426\u0153\xea\u043a\u0439\u043b]', 'e', b), re.sub(ur'[\xe8\xe9\xeb\xe6\u0426\u0153\xea\u043a\u0439\u043b]', 'e', c))
                for (a,b,c) in phru] # Change various 'e' symbols with diacritics to just 'e'
        phru = [(re.sub(ur'\xc3\xa6', 'e', a), re.sub(ur'\xc3\xa6', 'e', b), re.sub(ur'\xc3\xa6', 'e', c))
                for (a,b,c) in phru] # continuation of above
        phru = [(re.sub(ur'\xf6|\xf4|\xf3|\xc3\xb6|\u0446', 'o', a), re.sub(ur'\xf6|\xf4|\xf3|\xc3\xb6|\u0446', 'o', b), re.sub(ur'\xf6|\xf4|\xf3|\xc3\xb6|\u0446', 'o', c))
                for (a,b,c) in phru] # Change various 'o' symbols with diacritics to just 'o'
        phru = [(re.sub(ur'[\xe0\u0430\xe2]', 'a', a), re.sub(ur'[\xe0\u0430\xe2]', 'a', b), re.sub(ur'[\xe0\u0430\xe2]', 'a', c))
                for (a,b,c) in phru] # Change various 'a' symbols with diacritics to just 'a'
        phru = [(re.sub(ur'[\xef]', 'i', a), re.sub(ur'[\xef]', 'i', b), re.sub(ur'[\xef]', 'i', c))
                for (a,b,c) in phru] # Change various 'i' symbols with diacritics to just 'i'
        phru = [(re.sub(ur'[\xfc]', 'u', a), re.sub(ur'[\xfc]', 'u', b), re.sub(ur'[\xfc]', 'u', c))
                for (a,b,c) in phru] # Change various 'u' symbols with diacritics to just 'u'
        phru = [(re.sub(ur'[\xc6\xc9]', 'E', a), re.sub(ur'[\xc6\xc9]', 'E', b), re.sub(ur'[\xc6\xc9]', 'E', c))
                for (a,b,c) in phru] # Change various 'E' symbols with diacritics to just 'E'
        phru = [(re.sub(ur'[\xc0]', 'A', a), re.sub(ur'[\xc0]', 'A', b), re.sub(ur'[\xc0]', 'A', c))
                for (a,b,c) in phru] # Change various 'A' symbols with diacritics to just 'A'
        phru = [(re.sub(ur'[\xb7\xad]', '', a), re.sub(ur'[\xb7\xad]', '', b), re.sub(ur'[\xb7\xad]', '', c))
                for (a,b,c) in phru] # to nothing
        phru = [(re.sub(ur'\u0436', 'ae', a), re.sub(ur'\u0436', 'ae', b), re.sub(ur'\u0436', 'ae', c))
                for (a,b,c) in phru] # to 'ae'
        phru = [(re.sub(ur'mediaeval', 'medieval', a), re.sub(ur'mediaeval', 'medieval', b), re.sub(ur'mediaeval', 'medieval', c))
                for (a,b,c) in phru] # 'mediaeval' to 'medieval'
        return phru

phru = exchange_utf_to_ascii(phru)

## Extracting specific poems

poems_final = []
for (author, title, poem) in phru:
        poem_list = poem.split('<br>')
        poem_list = [r.strip() for r in poem_list]
        line_nr = 1
        for line in poem_list:
                poems_final.append([line, (author, title, line_nr)])
                line_nr += 1

# len(poems_final)
# 183422
				
f3 = open('C:/Python27/Poetry19cAmer.py', 'w')
for p in poems_final:
	f3.write(str(p)+',\n')
f3.close()

### Ascii encoded, tokenized corpus

poems_final_tok = []
f4 = open('C:/Python27/PoetryTok.py', 'w')
for p in poems_final:
	line = p[0].encode('ascii')
	author = p[1][0].encode('ascii')
	title = p[1][1].encode('ascii')
	nr = p[1][2]
	line = nltk.pos_tag(line)
	if re.findall('by (.*)', author) != []:
		author = re.findall('by (.*)', author)
		author = author[0]
	poems_final_tok.append([line, (author, title, nr)])
	f4.write(str([line, (author, title, nr)]) + ',\n')
f4.close()

ptok = poems_final_tok

# len(ptok)
# 183219


### First, manually delete duplicated poems from PoetryTok, they are:

# Each and All - Ralph Waldo Emerson
# Give All To Love - Ralph Waldo Emerson
# Nine From Eight - Sidney Lanier
# On The Garden Wall - Vachel Lindsay

folder = 'C:/Python27/Poetry/'

author_title = []
for item in ptok:
	author = item[1][0]
	title = item[1][1]
	title = re.sub('\.', '', title)
	file_author = re.sub('[ \.]', '', author)
	file_author = re.sub('[\!\"\'\&\)\(\*\,\.\;\:\?\{\}]', '-', file_author)
	file_title = re.sub('[ \.]', '', title)
	file_title = re.sub('[\!\"\'\&\)\(\*\,\.\;\:\?\{\}]', '-', file_title)
	author_title.append((file_author, file_title, author, title))

at = list(set(author_title))

for a in at:
	with open(folder + a[0] + '_' + a[1] + '.txt', 'a') as f1:
		f1.write('[TITLE] ' + a[3] + '\n')
		f1.write('[AUTHOR] ' + a[2] + '\n')
		
### Write tokenized lines to files

for p in ptok:
	author = p[1][0]
	file_author = re.sub('[ \.]', '', author)
	file_author = re.sub('[\!\"\'\&\)\(\*\,\.\;\:\?\{\}]', '-', file_author)
	title = p[1][1]
	file_title = re.sub('[ \.]', '', title)
	file_title = re.sub('[\!\"\'\&\)\(\*\,\.\;\:\?\{\}]', '-', file_title)
	line = nltk.pos_tag(p[0])
	line_str = ''
	nr = p[1][2]
	for item in line:
		line_str += item[0] + '/' + item[1] + ' '
	line_str = line_str.strip()
	with open(folder + file_author + '_' + file_title + '.txt', 'a') as f1:
		f1.write(str(nr) + ': ' + line_str + '\n')

### Rewrite files
### Fix nltk tokenizer mistake where it didn't separate a final word from its final comma

def getfilenames(input_directory):
    """Returns a list of file names in a directory"""
    filelist = sorted([file for file in os.listdir(input_directory) if file.endswith('.txt')])
    return filelist

filenames = getfilenames('C:/Python27/Poetry/')
	
newfolder = 'C:/Python27/Poetry2/'
for f in filenames:
	with open(folder + f, 'r') as f1:
		text = f1.readlines()
		newtext = []
		for item in text:
			if ',' in item[-8:]:
				last = last = re.findall(r'.+ (\b.+\n)', item)[0]
				last_len = len(last)
				last = re.sub('[,\n]', '', last)
				last = last + ' ,/,\n'
				newitem = item[:-last_len] + last
				with open(newfolder + f, 'a') as f2:
					f2.write(newitem)
			else:
				with open(newfolder + f, 'a') as f2:
					f2.write(item)
					
### Rename by hand .../Poetry2/ to .../Poetry/
### Use the following to create CategorizedTaggedCorpusReader object

# corpus_dir = 'C:/Python27/Poetry/'  # <-- change as necessary
# from nltk.corpus import CategorizedTaggedCorpusReader as CTCR
# poetry = CTCR(corpus_dir, r'.*\.txt', cat_pattern=r'(.*?)\_.*')

# Sample functions:
# poetry.raw()
# poetry.tagged_sents()
# poetry.fileids()
# poetry.categories()

### After all this processing, we ended up with 76 poets, 5645 poems
### For some reason, in the web-scraping process, we obtained a couple extra poems/poets that
### are not 19th century or American, but due to time issues, we did not fix it (and there are very few of them)