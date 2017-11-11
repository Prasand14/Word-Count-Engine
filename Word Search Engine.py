import string

def word_count_engine(document):
  #REMOVE PUNCTUATION
  no_punctuation = document.translate(string.maketrans("",""), string.punctuation)
  
  counts = dict() #CREATING DICTIONARY
  words = no_punctuation.lower().split() #CONVERT TO LOWERCASE
  
  #WORD-OCCURENCE-COUNT DICTIONARY
  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  
  #UNIQUE WORD LIST
  uniqueWords = []
  for i in words:
      if not i in uniqueWords:
          uniqueWords.append(i)
  
  new_list=[] #NESTED LIST
  indi = 0 #INDEX COUNT
  
  #CREATING NESTED LIST OF WORD,OCCURENCE #, INDEX #
  for word in uniqueWords:
    new_list.append([word] + [counts[word]] + [indi])
    indi += 1
  
  #SORTING THE LIST BASED ON 1)OCCURENCE # AND 2)INDEX #
  new_list = sorted(sorted(new_list, key = lambda x : x[2]), key = lambda x : x[1], reverse = True)
  
  #REMOVING INDEX ELEMENT AND CONVERT OCCURENCE # TYPE TO STRING
  for i in new_list:
    del i[-1]
    i[-1]=str(i[-1])
  
  return new_list

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(document)