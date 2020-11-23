# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re, collections
import unicodedata
import re
import regex
import codecs

def words(text): return text

##def train(features):
##    model = collections.defaultdict(lambda: 1)
##    for f in features:
##        model[f] += 1
##    return model

##NWORDS = train(words(file('corpus.txt').read()))

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates=set()
    candidates=set(known([word])) |set(known(edits1(word))) | set([word])
    z={}
    for x in candidates:
       w={x:NWORDS.get(x)}
       z.update(w)
    suggestions=sorted(z.items(), key=lambda x:x[1],reverse=True)
    return (suggestions[0][0])
       
      

alphabet = 'ी','ि','ु','े','ै','ो','ौ','़','्','ं','ँ','आ','अ','ए','ऐ','ओ','औ','इ','ई' ,'ी','ा','ू''ि','ु','े','़','्','ं','ँ'
a= codecs.open("unigram.txt", "r", "utf-8")
a=a.readlines()
NWORDS = collections.defaultdict(lambda: 1)
for i in range(len(a)):
    truth=a[i].split()
    dict={truth[0]:truth[1]}
    NWORDS.update(dict)
b= open("validation.txt", "r")
b=b.readlines()
total=0
hit=0
for i in range(len(b)):
   words=re.split(r'[:]',b[i])
   wrong=words[1].strip().decode("utf-8")
   truth=words[0]
   total=total+1
   print ("checking",i,"word...")
   cor=correct(wrong)
   if(truth.strip().decode("utf-8")==cor):
      hit=hit+1
print (hit,total)












