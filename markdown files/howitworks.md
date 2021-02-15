## ViTasl: A Translator Between Spoken English and ASL

Vitasl is a novel concept translator between spoken english and asl. Today, I will be going through a detailed explanation of how the concept works.

To start off, Vitasl will be programmed in Python, HtmlCSSJs, and Node.js. Python will be used as the backend programming language, processing and returning the data. Node.js will be used to interface with the electron framework. Electron is a framework that allows us to create desktop applications using HtmlCSSJs. HtmllCSSJss will allow us to create a user friendly interface.

To start off, in the user interface, you will click record and say the message that you want to translate to ASL. After you record, the program will kick in and use speech to text recognition to translate that into text. The program will then seperate that into a array, with each word in its own index. Now we need to reorder the sentence to have proper ASL sentence structure. To do this, we will tag each word with its part of speech. To tag each word with its part of speech, we will use the NLTK pos tagger, which uses the Penn Treebank POS Tags. We will then recorder the array depending on its tags. 

Next we will need to get the ASL signs. To do this, we will make a request with a query to signingsavy. Then, we take the html code of the website and search for source tags. This is where the video link is stored. 

We then will have a filter to filter out any unnecessary words in ASL such as "is", and other words.

However, it is not all that easy. There are cases of homonyms. If there have been no media links scraped, we will then search through the html code for list tags. This is where the defintions of the homonyms were. We will then use a lesk algorithm to find out the defintion of the word in context. This is an example of word sense disambugation. We take the array and the word we are looking for and we put it through the lesk algorithm. This returns us with an entry from the princeton wordnet. We then take that entry and we get the defintion. Then we compare the defintions in the website and the defintion we got and we pick the right one. We then get the link of the correct sign and we scrape the media link. 

We then download all the videos in the right order and then combine them using moviepy. 

Finally, we show the video on the user interface. and we are done!