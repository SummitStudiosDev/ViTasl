## Problems


### 1. Homonyms
##### Problem: The word "A" is a homonyms, so when we make a request to the website, it will result in no media links because we need to select the correct one, then make another request.
##### Solution 1: (may not work all the time)
1. Look for List (find possible choices' defintion)
2. Iterate through sentence (find if there are any words that are in choice's defintion that are also in sent)
3. Pick that one
##### Solution 2:
1. AI (idk how)
##### Solution 3: (prob will work)
1. Look for List (find possible choices' defintion)
2. Find defintion of word in context
Links: https://www.nltk.org/book/ch01.html
http://www.nltk.org/howto/wsd.html
https://stackoverflow.com/questions/58802653/how-to-identify-the-correct-definition-of-a-word-in-a-sentence-python
3. If the example/defintion has the word in it, put through lesk algorithm and get sysnet. Compare through context sysnet definition
(example: in RUN AWAY (as in "run away")) put sentence "run away" and "away" in lesk algorithm
4. if tht doesnt work, iterate through sentence and look for synonyms and stuff
5. if that doesnt work, use cosine similarity
https://www.geeksforgeeks.org/python-measure-similarity-between-two-sentences-using-cosine-similarity/
5. Pick that one

##### Status: Resolved
|
|
|
### 2. Proper Grammar in ASL
##### Problem: ASL has a special grammar structure, unlike normal english structure.
##### Solution 1:
1. Create a map or something and find all parts of speech.
Links:
https://www.nltk.org/book/ch05.html (2.3)
https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
https://www.oreilly.com/content/how-do-you-find-the-parts-of-speech-in-a-sentence-using-python/?afsrc=1
https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
https://en.wikipedia.org/wiki/American_Sign_Language_grammar#:~:text=The%20full%20sentence%20structure%20in,subject%2Dpronoun%2Dtag%5D.
2. Reorder sentence on parts of speech

##### Status: Unresolved
|
|
|
### 3. Complex Sentences/Compound
##### Problem: complex sentences wont work with solution of problem 2
##### Solution 1:
1. divide compund/complex sentences into individual lists

##### Status: Unresolved
|
|
|
### 4. tenses
##### Problem: Sometimes unable to get video because of tenses (tenses mess up search)
##### Solution 1:
1. use a lemmatizer to remove tense to get base form

##### Status: Resolved
|
|
|
### 5. tenses require part of speech
##### Problem: in order to use the lemmatizer correctly, you need to pass in the part of speech or else it will consider it as a noun, and that will cause problems
##### Solution 1:
1. classify the sentence by part of speech (Penn treebank)
2. create a dictionary that replaces adjectives, adverbs, nouns, and verbs with (a, n, and v (which is the format for the arguments))
3. with the index, take the penn treebank pos, put in dictionary, get out correct format to pass into lemmatizer 
4. pass in POS to lemmatizer  

##### Status: Resolved
|
|
|
### 6. some tenses can be searched
##### Problem: some tenses (like "are") have a different form then their base tense (is)
##### Solution 1:
1. first search for original tense
2. if there is a problem, lemmanize and then search again

##### Status: Resolved
|
|
|
### 7. Two-word phrases
##### Problem: some phrases like "run away" and "every thursday" have their own signs
##### Solution 1:
1. before we get the video, we add the current word  + nextword to get a string
2. we scrape the website using that string
3. if it returns  successful, we download and continue
4. if not, pass

##### Status: Resolved
|
|
|
### 8. Options Problem
##### Problem: if getlink goes into options mode, it only returns the website, not the video link
##### Solution 1:
1. after we get the link, we put getlink on the website link

##### Status: Resolved
|
|
|
#### 9. Some options have the same video/signs
##### Problem: For example, the two options of "a" are the same 
#### Solution 1: 
1. loop thru links
2. have a var that tracks the first link and compares it to the one that is being pointed after
3. if same, continue
4. if different, stop looping and return highest cosine

##### Status: Resolved