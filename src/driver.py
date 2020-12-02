from functions.scraper import getlink, options
from functions.sentence import seperate
from functions.grammar import homonyms, classify_grammar
from functions.cosine_similarity import cosine, maxcosine
from functions.remove_tense import stemmer, lemm
from voice_functions.stt import stt
from functions.video import download_video,combinevideo
import os
from os import startfile
import time

try:
	try:
		os.rmdir("clips")
	except:
		import shutil
		shutil.rmtree("clips", ignore_errors=True)
		#os.rmdir("clips")
except:
	pass


#sent = input("sentence: ")
sent = stt("1.wav")
print(sent)
sep_sent = seperate(sent)

original_sent = sent


#filter
import json 
with open('FILTER.json') as json_file: 
    data = json.load(json_file) 
fsep_sent = sep_sent
bdict = {}
for i in data['filter']:
  bdict.update(i)
for x in range(len(sep_sent)):
  i = sep_sent[x]
  word = i.lower()
  try:
    #print(bdict[i],":", word)
    if(bdict[word] == "IGNORE"):
      fsep_sent[x] = ""
  except KeyError:
    #print("NOTHING :",word)
    pass
fsent = ""
for i in fsep_sent:
  if(i != ""):
    fsent = fsent+ i+" "
sent = fsent
print("filtering words")
print(sent) # filtered
sep_sent = sent.split(" ")
sep_sent.pop()


videonumber = 1
skip = False
os.mkdir("clips")


import timeit
start = timeit.default_timer()



for j in range( len(sep_sent)):

  if(skip == False):

    print("videonum: ",videonumber)
    i = sep_sent[j]
  

    #-------------------------------
    #|try to get link with tenses|
    #--------------------------------



    #--------------------------------------------------------------------------------------
    #| get next word in sentence for phrases before looking for individual words ( tense)
    #--------------------------------------------------------------------------------------

    try: 
      nextword = sep_sent[j+1]

      res2 = getlink(i + " "+ nextword)
      #print("it is a phrase")


      if type(res2) is str:
        
        print(i + " " + nextword + " : "+ res2)
        print('')
        skip = True

        todownload = res2
        download_video(todownload, videonumber)
        print("downloading... \n \n")
        videonumber += 1

        continue


      if type(res2) is dict:
        #print("nextword: ",nextword)
        print(i + " "+ nextword+" : "+res2[list(res2)[0]])
        print('')
        skip = True

        todownload = res2[list(res2)[0]]
        download_video(todownload, videonumber)
        print("downloading... \n \n")
        videonumber += 1

        continue

    except Exception as a:

      #print(a)
      pass


    result = (getlink(i))
    try:
            if type(result) is dict:


              #---------------------------------------------------------------
              #| iterate through each choice, use cosine similarity ( tense)|
              #------------------------------------------------------------------
              print(i, " has ",str(len(result.items())), " choices")
              def_in_context = homonyms(original_sent, i)
              print(def_in_context)


              data = {}

              for x, y in result.items():
                print(i, " : ",x," : ", y)
                print("cosine similarity: ", cosine(x, def_in_context))
                data[x] = str(y)+" ,"+str(cosine(x,def_in_context))


              todownload = maxcosine(data)
              download_video(todownload, videonumber)
              print("download:", todownload)
              print("downloading... \n \n")
              videonumber += 1
              

              print('')
              #print(len(result.items()))
              if(len(result.items())> 0):
                continue
              elif(len(result.items()) == 0):
                pass
                print("there are no signs with the tense, removing tense ")

              #-----------------------------------------------------
              #| there are no signs with the tense, removing tense |
              #-----------------------------------------------------



            else:
              print(i," : ",result)
              print('')

              todownload = result
              download_video(todownload, videonumber)
              print("downloading... \n \n")
              videonumber += 1
          
              continue
    except:
            pass


    #-----------------
    #| remove tenses |
    #-----------------

    i2 = lemm(j,sent)
    if(i2 != 0):
      i=i2  

    #--------------------------------------------------------------------------------------
    #| get next word in sentence for phrases before looking for individual words (no tense)|
    #---------------------------------------------------------------------------------------

    try: 
      nextword = sep_sent[j+1]

      res2 = getlink(i + " "+ nextword)

      #print("it is a phrase")


      if type(res2) is str:
        print(i + " " + nextword + " : "+ res2)
        print('')
        skip = True

        todownload = res2
        download_video(todownload, videonumber)
        print("downloading... \n \n")
        videonumber += 1
        
        continue;

      if type(res2) is dict:
        #print("nextword: ",nextword)
        print(i + " "+ nextword+" : "+res2[list(res2)[0]])
        print('')
        skip = True

        todownload = res2[list(res2)[0]]
        download_video(todownload, videonumber)
        print("downloading... \n \n")
        videonumber += 1

        continue;

    except Exception as a:
      #print(a)
      pass


    result = (getlink(i))
    if type(result) is dict:



      #----------------------------------------------------------------
      #| iterate through each choice, use cosine similarity(no tense) |
      #----------------------------------------------------------------
      print(i, " has ",str(len(result.items())), " choices")
      def_in_context = homonyms(original_sent, i)
      print(def_in_context)

      data = {}


      for x, y in result.items():
        print(i, " : ",x," : ", y)
        print("cosine similarity: ", cosine(x, def_in_context))
        data[x] = str(y)+" ,"+str(cosine(x,def_in_context))

      todownload = maxcosine(data)
      download_video(todownload, videonumber)
      print("download:", todownload)
      print("downloading... \n \n")
      videonumber += 1
      
      


      print('')
      if(len(result.items())> 0):
        continue
      elif(len(result.items()) == 0):
        pass

    else:
      print(i," : ",result)
      print('')

      todownload = result
      download_video(todownload, videonumber)
      print("downloading... \n \n")
      videonumber += 1


      continue

  skip = False
  
combinevideo(videonumber -1)


stop = timeit.default_timer()
print(' \n Runtime: ', stop - start)  



try:
	os.rmdir("clips")
except:
	import shutil
	shutil.rmtree("clips", ignore_errors=True)
	#os.rmdir("clips")
	
	
startfile("finalvideo.mp4")
