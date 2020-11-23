# hindi-spell-checker
nlp assignment hindi spell checker


nlp code1 defines

Due to less standardization in hindi.There are lot of errors , incorrect forms , out of language words etc are widely used in the writtrn form of hindi. हजारों (Incorrect according to Tutor file) occurs with high frequency then the correct हज़ारों (with nukta) .Such things can be handled by using quality corpus.
The file provided for testing is highly corrupted , a large percentage of corrected words are not in Hindi wordnet while some of the errors are there in wordnet.So the distinction between correct and incorrect is doubtful.
Words which consist of two different root words fused together also is in high percentage and obviously they will occur in less frequency.These errors can be attributed to bad design of test file.
example
आचारव्यवहार
गायकगायिकाओं


nlp code2 defines

In this part i modeled the language using bigrams.The approach was to find the nonword in the sentence and for that word create the possible corrected words using earlier edit distance metric.Then search all the possible bigrams in the corpus and replace with that word whose bigram frequency is high.
The spell checker could be made more smart by adding strings which are phoneticaly nearer to error word. Similiar sounds
स श ष
ब भ
र ऋ ऱ
