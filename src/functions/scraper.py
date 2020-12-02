def getlink(query):
  try:
    from bs4 import BeautifulSoup
  except:
    import os
    os.system("pip install BeautifulSoup4")
    from bs4 import BeautifulSoup
  import requests
  webpageLink = 'https://www.signingsavvy.com/search/'+query
  page = requests.get(webpageLink)

  imagelist=[]
  soup = BeautifulSoup(page.content, 'html.parser')
  match = soup.findAll("source")


  if len(match)==1:
    tag=match[0]
  elif len(match) < 1:
    #raise RuntimeError("Too little media links were scraped")
    return options(query)
  elif len(match) >1:
    raise RuntimeError("Too many media links were scraped")
  else:
    raise RuntimeError("Unknown Error")

  relativelink = tag['src']
  vidlink = "https://www.signingsavvy.com/" + relativelink
  return vidlink



def options(query):

  try:
    from bs4 import BeautifulSoup
  except:
    import os
    os.system("pip install BeautifulSoup4")
    from bs4 import BeautifulSoup
  import requests
  webpageLink = 'https://www.signingsavvy.com/search/'+query
  page = requests.get(webpageLink)


  imagelist=[]
  soup = BeautifulSoup(page.content, 'html.parser')
  match = soup.findAll("li")

  ahrefs = []


  for i in match:
    toparse = '<!DOCTYPE html><html><head><title>Express</title><link rel="stylesheet" href="/stylesheets/style.css"></head><body>'+str(i)+'</body></html>'
    soup2 = BeautifulSoup(toparse, 'html.parser')
    #print(soup2.prettify())
    match2 = soup2.findAll('a')

    if len(match2)==1:
      tag2=match2[0]
    elif len(match2) < 1:
      raise RuntimeError("Too little media links were scraped")
    elif len(match2) >1:
      raise RuntimeError("Too many media links were scraped")
    else:
      raise RuntimeError("Unknown Error")


    try:
      href = tag2['href']
      ahrefs.append(href)
    except:
      #no hrefs were found, ignore
      pass

      
  
  good_ahrefs = []
  for i in ahrefs:
    if(i.startswith('sign/')):
      good_ahrefs.append("https://www.signingsavvy.com/"+i)
  good_descs = []
  for i in match:
    toparse = '<!DOCTYPE html><html><head><title>Express</title><link rel="stylesheet" href="/stylesheets/style.css"></head><body>'+str(i)+'</body></html>'
    soup2 = BeautifulSoup(toparse, 'html.parser')


    match3 = soup2.find('em')
    try:
      if len(match3)==1:
        description = (match3.getText()).replace('&quot','')
        description = description.replace('(','')
        description = description.replace(')','')
        description = description.replace('"','')
        good_descs.append(description)
    except:
      pass
  


  #print(len(good_ahrefs), " : ", len(good_descs))

  choices = {}
  if(len(good_ahrefs) <= len(good_descs)):
    raise RuntimeError("Unknown Error")
  if((len(good_ahrefs)-1) == len(good_descs)):
    for i in range(len(good_descs)):
      #print(good_descs[i]," : ",good_ahrefs[i])
      websitelink = (good_ahrefs[i]).replace(' ', '%20')
      choices[good_descs[i]] = raw_getlink(websitelink)
  
  return choices



def raw_getlink(link):
  try:
    from bs4 import BeautifulSoup
  except:
    import os
    os.system("pip install BeautifulSoup4")
    from bs4 import BeautifulSoup
  import requests
  webpageLink = link
  page = requests.get(webpageLink)

  imagelist=[]
  soup = BeautifulSoup(page.content, 'html.parser')
  match = soup.findAll("source")
  #print(match)


  if len(match)==1:
    tag=match[0]
  elif len(match) < 1:
    #raise RuntimeError("Too little media links were scraped")
    return options(query)
  elif len(match) >1:
    raise RuntimeError("Too many media links were scraped")
  else:
    raise RuntimeError("Unknown Error")

  relativelink = tag['src']
  vidlink = "https://www.signingsavvy.com/" + relativelink
  return vidlink
