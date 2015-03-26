##### i256 Final Project
##### Sound Component
##### Team members: Kyle Booten & Herman Leung
##### Code written by: Herman Leung

from nltk.corpus import cmudict
import re, nltk
cmuwords = cmudict.words()

def get_perfect_rhyme(word):
    if word in cmuwords:
        pronun_list = cmudict.dict()[word][0]
        if '1' in str(pronun_list):
            for i in range(len(pronun_list)):
                if '1' in pronun_list[i]:
                    stressed_pos = i
            rhyme_list = [pronun_list[stressed_pos]]
            for j in range(len(pronun_list) - stressed_pos -1):
                stressed_pos += 1
                rhyme_list.append(pronun_list[stressed_pos])
            return rhyme_list
        else:
            print str(word) + ' not rhymable'
            return None
    else:
        print str(word) + ' not in cmudict'
        return None

def get_last_rhyme(word):
    if word in cmuwords:
        pronun_list = cmudict.dict()[word][0]
        for i in range(len(pronun_list)):
            if re.search('[AEIOU]', pronun_list[i]):
                final_vowel_pos = i
        rhyme_list = [pronun_list[final_vowel_pos]]
        for j in range(len(pronun_list) - final_vowel_pos -1):
            final_vowel_pos += 1
            rhyme_list.append(pronun_list[final_vowel_pos])
        return rhyme_list
    else:
        print str(word) + ' not in cmudict'
        return None

def get_initial(word):
    if word in cmuwords:
        pronun_list = cmudict.dict()[word][0]
        if re.search('[AEIOU]', pronun_list[0]):
            print str(word) + ' starts with a vowel'
            return None
        else:
            for i in range(len(pronun_list)-1, -1, -1):
                if re.search('[AEIOU]', pronun_list[i]):
                    first_vowel_pos = i
            initial = pronun_list[:first_vowel_pos]
        return initial
    else:
        print str(word) + ' not in cmudict'
        return None


### Function not completed/in progress
    
#def detect_alliteration(line):
#    line = nltk.word_tokenize(line)
#    line = [word.lower() for word in line]
#    initial_list = [get_initial(word) for word in line]
#    return initial_list
