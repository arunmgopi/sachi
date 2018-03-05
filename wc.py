openfile = open('joyal.txt','w')
content = openfile.write('hai joyal how are you i am fine joyal thank you')
openfile.close()


a = open('joyal.txt','r')
contents = a.read()
words = contents.split(' ')
length = len(words)
print('the total length of words is ',length)
print(' the word count of each words is....')
noDuplicate= list(set(words))
print ( '{0:15}  {1:5}'.format('word','count'))

for word in noDuplicate:
 print ( '{0:15}  {1:5}'.format(word,words.count(word)))
a.close()



