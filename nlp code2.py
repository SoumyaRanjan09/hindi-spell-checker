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
    return (suggestions)
       
      

alphabet = 'ी','ि','ु','े','ै','ो','ौ','़','्','ं','ँ','आ','अ','ए','ऐ','ओ','औ','इ','ई' ,'ी','ा','ू''ि','ु','े','़','्','ं','ँ'
a= codecs.open("unigram.txt", "r", "utf-8")
a=a.readlines()
NWORDS = collections.defaultdict(lambda: 1)
for i in range(len(a)):
    truth=a[i].split()
    dict={truth[0]:truth[1]}
    NWORDS.update(dict)
b= codecs.open("bigrams.txt", "r", "utf-8")
b=b.readlines()
BWORDS = collections.defaultdict(lambda: 1)
for i in range(len(b)):
    truth=b[i].split()
    #print len(truth)
    bi=truth[0]+" "+truth[1]
    s=len(truth)-1
    dict={bi:truth[s]}
    BWORDS.update(dict)
c= codecs.open("sentences.txt", "r", "utf-8")
c=c.readlines()
for line in c:
   words=line.split()
   error=list()
   for i in words:
      if(int(NWORDS[i])<100):
         error.append(i) 
   for k in error:
      possible=correct(k)
      maxi=0
      correction=""
      for i in possible:
         #print i[0]
         position=words.index(k)
         if(position==0):
             b2="<s>"+" "+words[position]
             strength=int(BWORDS[b2])
             print (strength)
         if(position==len(words)-1):
             b1=words[position]+"</s>"
             strength=int(BWORDS[b1])
             print (strength)
         else:
            b1=words[position-1]+" "+i[0]
            b2=i[0]+" "+words[position+1]
            strength=int(BWORDS[b1])*int(BWORDS[b2])
            #print strength
         if(strength>maxi):
            maxi=strength
            correction=i
      print (correction)
         






