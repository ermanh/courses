##### i256 Final Project
##### Etymology Component
##### Team members: Kyle Booten & Herman Leung
##### Code written by: Herman Leung

import re, nltk
from collections import Counter
wnl = nltk.WordNetLemmatizer()

###########################################
##### Edinburgh Associative Thesaurus #####
###########################################

##### stimulus-response #####

print "File: eat-stimulus-response.xml"
f1 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/EAT/eat-stimulus-response.xml", "r")
text1 = f1.read()
stimulus_list = re.findall(r'\<stimulus((.|\n)*?)\<\/stimulus\>', text1)
print "Stimulus words: " + str(len(stimulus_list))

word_list1 = []
for item in stimulus_list:
    word_list1 += re.findall(r'word\=\"(.*?)\"', item[0])
print "Unique response words: " + str(len(list(set(word_list1)))) + '\n'
word_list1 = list(set(word_list1))

f1.close()

##### response-stimulus #####

print "File: eat-response-stimulus.xml"
f2 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/EAT/eat-response-stimulus.xml", "r")
text2 = f2.read()
response_list = re.findall(r'\<response((.|\n)*?)\<\/response\>', text2)
print "Response words: " + str(len(response_list))

word_list2 = []
for item in response_list:
    word_list2 += re.findall(r'word\=\"(.*?)\"', item[0])
print "Unique stimulus words: " + str(len(list(set(word_list2))))
word_list2 = list(set(word_list2))

f2.close()

################################
##### Etymological WordNet #####
################################

print "\nFile: etymwn_eng.txt"
f3 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/etymwn.tsv", "r")
text3 = f3.read()
english = re.findall(r'eng\:.*?rel\:etymology.*?\n', text3)
english_fullwords = []
for e in english:
    if '-' not in e:
        english_fullwords.append(e)

etym_dict = {}
for e in english_fullwords:
    word = re.findall(r'eng: (.*)\trel', e)[0]
    code = re.findall(r'rel:etymology\t(.*?)\:', e)[0]  # code = language code
    source = re.findall(r'rel:etymology\t.{5}(.*)', e)[0]
    etym_dict[word] = {}
    etym_dict[word]['code'] = code
    etym_dict[word]['source'] = source
	
# len(etym_dict)
# 96240

iso_codes = []
for e in english_fullwords:
    code = re.findall(r'rel:etymology\t(.*?)\:', e)[0]
    iso_codes.append(code)
iso_counter = Counter(iso_codes)
iso_codes = list(set(iso_codes))    # 239

f3.close()

##### getting iso-639-3 codes #####

f4 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/iso-639-3/iso-639-3.tab", "r")
text4 = f4.read()
iso_list = re.findall(r'.*?\n', text4)
f4.close()

iso_list.pop(0)     # the first line is column titles
iso_dict = {}
for i in iso_list:
    code = i[:3]
    lang = re.findall('.*?\t.*?\t.*?\t.*?\t.*?\t.*?\t(.*?)\t', i)[0]
    if code in iso_codes:
        iso_dict[code] = lang
iso_dict['wit'] = 'Wintu'
iso_dict['p_sla'] = 'Proto-Slavic'
iso_dict['nah'] = 'Nahuatl'

iso_counter_list = iso_counter.items()
iso_counter_list.sort(key=lambda tup: tup[1], reverse=True)

f5 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/etym_count.txt", "w")
for (i,j) in iso_counter_list:
    f5.write(str(i) + '\t' + str(j) + '\t' + str(iso_dict[i]) + '\n')
f5.close()


tok = nltk.word_tokenize('He walks lonely as a cloud')

def show_etym(sentence):
	tok = nltk.word_tokenize(sentence)
	for t in tok:
		if t in etym_dict.keys():
			print str(t), etym_dict[t]
		elif t.lower() in etym_dict.keys():
			print str(t), etym_dict[t.lower()]
		elif wnl.lemmatize(t.lower()) in etym_dict.keys():
			print str(t), etym_dict[wnl.lemmatize(t.lower())]
		else:
			print str(t), 'NONE'

			
#####################
##### EXPANSION #####
#####################

f6 = open("C:/Users/Herman/My Documents/UC Berkeley/Fall 2013/i256/etymwn_eng.txt", "r")
ety_en = f6.readlines()
f6.close()

ety_en = [e.split('\t') for e in ety_en]
ety_en_clean = []
for e in ety_en:
	item1 = e[0][5:]
	item2 = e[1][4:]
	item3 = e[2][:3]
	item4 = e[2][5:-1]
	ety_en_clean.append([item1, item2, item3, item4])

ety_en_clean2 = []		
for e in ety_en_clean:
	if (e[3][0] != '-' and e[0][0] != '-' and			# Delete entries that start/end with a hyphen (in either first or last slot)
			e[3][-1] != '-' and e[0][-1] != '-' and
			re.search('[0-9]', e[0]) == None and		# Delete entries that contain a digit (in the first slot)
			len(re.sub('[a-z\'\-]', '', e[0])) == 0 and	# Delete entries that contain special characters (so, only a-z, apostrophe, and internal hyphens) (in the first slot)
			' ' not in e[3].strip()):					# Delete entries that are more than one word (in last slot)
		ety_en_clean2.append(e)

# len(ety_en_clean2)
# 599446

###keys = etym_dict.keys()
###new_assess = []
###for e in ety_en_clean2:
###	if e[0] not in keys:
###		new_assess.append(e)

# len(new_assess)
# 337277



#['is_derived_from', 'has_derived_form', 'etymological_origin_of', 'etymology', 'variant:orthography', 'etymologically_related']
		
l_isderived, l_hasderived, l_origin, l_etymology, l_variant, l_related = [], [], [], [], [], []
d_isderived, d_hasderived, d_origin, d_etymology, d_variant, d_related = {}, {}, {}, {}, {}, {}

for e in ety_en_clean2:
	if e[1] == 'is_derived_from':
		l_isderived.append(e)
	elif e[1] == 'has_derived_form':
		l_hasderived.append(e)
	elif e[1] == 'etymological_origin_of':
		l_origin.append(e)
	elif e[1] == 'etymology':
		l_etymology.append(e)
	elif e[1] == 'variant:orthography':
		l_variant.append(e)
	elif e[1] == 'etymologically_related':
		l_related.append(e)

# len(l_isderived), len(l_hasderived), len(l_origin), len(l_etymology), len(l_variant), len(l_related)
# (171525, 171926, 84130, 100333, 7305, 64227)
# len(l_isderived) + len(l_hasderived) + len(l_origin) + len(l_etymology) + len(l_variant) + len(l_related)
# 599446

def create_dict(LIST):
	DICT = {}
	for l in LIST:
		if l[0] in DICT.keys():
			DICT[l[0]]['lex'].append(l[3])
			DICT[l[0]]['ori'].append(l[2])
		else:
			DICT[l[0]] = {'rel':l[1], 'ori':[l[2]], 'lex':[l[3].strip()]}
	return DICT

d_isderived = create_dict(l_isderived)
d_hasderived = create_dict(l_hasderived)
d_origin = create_dict(l_origin)
d_etymology = create_dict(l_etymology)
d_variant = create_dict(l_variant)
d_related = create_dict(l_related)


# len(d_isderived), len(d_hasderived), len(d_origin), len(d_etymology), len(d_variant), len(d_related)
# (169251, 106227, 30693, 90564, 7264, 37675)
# len(d_isderived) + len(d_hasderived) + len(d_origin) + len(d_etymology) + len(d_variant) + len(d_related)
# 441674
# len(list(set(d_isderived.keys() + d_hasderived.keys() + d_origin.keys() + d_etymology.keys() + d_variants.keys() + d_related.keys())))
# 322997

newdict = dict(d_etymology)
newdictkeys = newdict.keys()
def create_newdict(DICT):
	'''for dicts where the etymological source is in "lex"'''
	returndict = {}
	for d in DICT.items():
		if d[0] not in newdictkeys:
			for item in d[1]['lex']:
				if item in newdictkeys:
					if d[0] not in returndict.keys():
						returndict[d[0]] = {}
						returndict[d[0]]['rel'] = 'root_etymology'
						returndict[d[0]]['ori'] = newdict[item]['ori']
						returndict[d[0]]['lex'] = [item] # may need to toggle [] list operator
					else:
						returndict[d[0]]['ori'] += newdict[item]['ori']
						returndict[d[0]]['lex'] += [item]
	return returndict

newdict_isderived = create_newdict(d_isderived)
newdict.update(newdict_isderived)

# len(newdict)
# 158496

newdictkeys = newdict.keys()
def create_newdict_from(DICT):
	'''for dicts where the etymological source are the keys'''
	returndict = {}
	for d in DICT.items():
		for item in d[1]['lex']:
			if item not in newdictkeys:
				returndict[item] = {}
				if d[0] in newdictkeys:
					returndict[item]['rel'] = 'root_etymology'
					returndict[item]['ori'] = newdict[d[0]]['ori']
					returndict[item]['lex'] = newdict[d[0]]['lex']
				else:
					returndict[item]['rel'] = 'root_etymology'
					returndict[item]['ori'] = ['eng']
					returndict[item]['lex'] = d[0]
	return returndict
	
newdict_hasderived = create_newdict_from(d_hasderived)
newdict.update(newdict_hasderived)

newdict_variant = create_newdict(d_variant)
newdict.update(newdict_variant)