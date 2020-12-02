def stemmer(word):
  try:
    import nltk
    from nltk.stem.lancaster import LancasterStemmer
  except:
    import os
    os.system("pip install nltk")
    import nltk
    from nltk.stem.lancaster import LancasterStemmer
  
  st = LancasterStemmer()
  return st.stem(word)


def lemm(index, strsent):
  from functions.grammar import classify_grammar
  pos  = {
  'CC':	'Coordinating conjunction'
  ,'CD':	'Cardinal number'
  ,'DT':	'Determiner'
  ,'EX':	'Existential there'
  ,'FW':	'Foreign word'
  ,'IN':	'Preposition or subordinating conjunction'
  ,'JJ':	'a'
  ,'JJR':	'a'
  ,'JJS':	'a'
  ,'LS':	'List item marker'
  ,'MD':	'Modal'
  ,'NN':	'n'
  ,'NNS':	'n'
  ,'NNP':	'n'
  ,'NNPS':	'n'
  ,'PDT':	'Predeterminer'
  ,'POS':	'Possessive ending'
  ,'PRP':	'Personal pronoun'
  ,'PRP$':'Possessive pronoun'
  ,'RB':'a'
  ,'RBR':'a'
  ,'RBS':'a'
  ,'RP':'Particle'
  ,'SYM':'Symbol'
  ,'TO':'to'
  ,'UH':'Interjection'
  ,'VB':'v'
  ,'VBD':'v'
  ,'VBG':'v'
  ,'VBN':'v'
  ,'VBP':'v'
  ,'VBZ':'v'
  ,'WDT':'Wh-determiner'
  ,'WP':'Wh-pronoun'
  ,'WP$':'Possessive wh-pronoun'
  ,'WRB':'a'
  }


  pos2 = classify_grammar(strsent)
  x = pos[pos2[index][1]]
  y = pos2[index][0]
  #print(y," : ", x)

  if(len(x)>1):return 0
  #make sure we only accept adjectives, adverbs, verbs, and nouns
  #if none of the above, then return 0

  try:
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
  except:
    import os
    os.system('pip install nltk')
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
  try:
    return(lemmatizer.lemmatize(y, pos = x))
  except:
    import nltk
    nltk.download('wordnet')
    return(lemmatizer.lemmatize(y, pos = x))