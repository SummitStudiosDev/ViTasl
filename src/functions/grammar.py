def classify_grammar(str_sent):
  try: 
    import nltk
    from nltk.tokenize import word_tokenize
  except:
    import os
    os.system("pip install nltk")
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    from nltk.tokenize import word_tokenize


  try:
    text = word_tokenize(str_sent)
    return (nltk.pos_tag(text))
  except:
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    text = word_tokenize(str_sent)
    return (nltk.pos_tag(text))

  

def homonyms(sentence, word):
  try:
    import nltk
    from nltk.wsd import lesk
    from nltk.corpus import wordnet as wn
  except:
    import os
    os.system("pip install nltk")
    import nltk
    nltk.download('wordnet')
    from nltk.wsd import lesk
    from nltk.corpus import wordnet as wn


  #print("word "+word) 
  try: 
    def_label = lesk(sentence, word)
    if def_label is None:
      return "None"
    return (def_label.definition())

  except:
    nltk.download('wordnet')
    def_label = lesk(sentence, word)
    if def_label is None:
      return "None"
    return (def_label.definition())

