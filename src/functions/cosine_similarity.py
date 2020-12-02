#-----------------------------------------------------------------------------------------------------------
#| credit: https://stackoverflow.com/questions/15173225/calculate-cosine-similarity-given-2-sentence-strings|
#------------------------------------------------------------------------------------------------------------


def cosine(text1, text2):
  import math
  import re
  from collections import Counter

  WORD = re.compile(r"\w+")


  def get_cosine(vec1, vec2):
      intersection = set(vec1.keys()) & set(vec2.keys())
      numerator = sum([vec1[x] * vec2[x] for x in intersection])

      sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
      sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
      denominator = math.sqrt(sum1) * math.sqrt(sum2)

      if not denominator:
          return 0.0
      else:
          return float(numerator) / denominator


  def text_to_vector(text):
      words = WORD.findall(text)
      return Counter(words)

  #text1 = "This is a foo bar sentence ."
  #text2 = "This sentence is similar to a foo bar sentence ."


  vector1 = text_to_vector(text1)
  vector2 = text_to_vector(text2)

  cosine = get_cosine(vector1, vector2)

  return cosine
  #print("Cosine:", cosine)

def maxcosine(data):
  maxcosine = '-1.000'
  maxlink = ''
  maxdef = ''
  for x, y in data.items():
    definition = x
    yraw = y.split(',')
    cosine= (yraw[1])
    link = (yraw[0])
    #print(definition," : ", link, " : ",cosine)


    if(float(cosine) > float(maxcosine)):
      maxcosine = cosine
      maxlink = link
      maxdef = definition

  #print("max: ",maxdef," : ", maxlink, " : ",maxcosine)

  num = 1;
  for x,y in data.items():
    if(num == 1):
      firstlink = (y.split(','))[0]
    if(num != 1):
      link = (y.split(','))[0]

    if(link == firstlink):
      pass
    else:
      #print("look at max, not all links are the same")
      return maxlink
    num += 1


  #print("all links r the same")
  #print(firstlink)
  return firstlink