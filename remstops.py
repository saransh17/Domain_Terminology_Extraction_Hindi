import os
def Punctuation(string): 
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for x in string.lower(): 
        if x in punctuations: 
            string = string.replace(x, " ")

    return string

with open('final_stopwords.txt', 'r') as myfile:
  stoplist = myfile.read()
stoplist = stoplist.split(' ')

with open('output.txt','r') as hin_data:
	data = hin_data.read()

hinwords = data.split()
resultwords  = [word for word in hinwords if word not in stoplist]
result = ' '.join(resultwords)


text_file = open("no_stops.txt", "w")
text_file.write(Punctuation(result))
text_file.close()
