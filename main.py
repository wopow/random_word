import random

outfile=open('new.txt','w')
outfile1=open('new1.txt','w')
file=open('english\\1.txt','r',encoding='utf-8')
words=file.readlines()
word_dict={}
for i in words:
    word_dict[i.split(':')[0]]=i.split(':')[1].replace('\n', '')
word_dict_key=list(word_dict.keys())
random.shuffle(word_dict_key)
new_word_dict={}
for key in word_dict_key:
    new_word_dict[key] = word_dict.get(key)
    new_line=word_dict.get(key).ljust(len(key)+len(word_dict.get(key))+10,'_')
    outfile1.write(word_dict.get(key)+' :'+key+'\n')
    outfile.write(new_line+'\n')
outfile1.close()
outfile.close()
file.close()
