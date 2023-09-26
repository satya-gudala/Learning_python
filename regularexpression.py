'''import re
str="welcome to satyagudala"#findall()
a=re.findall("a",str)
print(a)
str="sweetygudala"
a=re.findall("e",str)
print(a)
a=re.findall("y",str)
print(a)
a=re.findall(" ",str)
print(a)
a=re.findall("",str)
print(a)
import re
str="vamsikumar gudala"#search()
a=re.search("gu",str)
print(a)
a=re.search("",str)
print(a)
a=re.search("fgt",str)
print(a)
a=re.search("vamsi",str)
print(a.start())
a=re.search("m",str)
print(a.start())
a=re.search("vamsi",str)
print(a.span())
a=re.search("si",str)
print(a.string)
import re
str="bhimavaram institute of engineeering"#split()
a=re.split("bhimavaram",str)
print(a)
a=re.split("",str)
print(a)
a=re.split(" ",str)
print(a)
a=re.split("bhimavaram",str,2)
print(a)
a=re.split("engineering",str,3)
print(a)
a=re.split("bhimavaram",str,1)
print(a)
import re
str="high school"#substuted
a=re.sub("high","low",str)
print(a)
a=re.sub("high","private",str)
print(a)
a=re.sub("school","college",str)
print(a)
a=re.sub("school","company",str)
print(a)

####metacharacters
import re
str="welcome to metacharacters"
a=re.findall("[a]",str)
print(a)
a=re.findall("[ac]",str)
print(a)
a=re.findall("[e]",str)
print(a)
a=re.findall("^we",str)#^startswith
print(a)
a=re.findall("^welcome",str)
print(a)
a=re.findall("ers$",str)#$endswith
print(a)
a=re.findall("we$",str)
print(a)
a=re.findall("we.....",str)#..newline
print(a)
a=re.findall("we...",str)
print(a)
a=re.findall("...we.",str)
print(a)
a=re.findall("meta*",str)# *;0 or more occurance
print(a)
a=re.findall("charcter*",str)
print(a)
a=re.findall("welcome+",str)# +;0 or more occurance
print(a)
a=re.findall("jhf+",str)
print(a)
a=re.findall("e{2}",str)#{}no. of occurance
print(a)
a=re.findall("\s",str)#spacses
print(a)'''


import re
#findall
str='pythonprogramming'
a=re.findall('py',str)
print(a)
a=re.findall('mm',str)
print(a)
a=re.findall('thon',str)
print(a)
a=re.findall('ing',str)
print(a)
s='jsadghujsfhjh'
satya=re.findall('sa',s)
print(satya)
satya=re.findall('fhj',s)
print(satya)
#search
s='satyakrishna'
a=re.search('shna',s)
print(a)

s='pythonprogramming'
a=re.search('ro',s)
print(a)
s='pythonprogramming'
a=re.search('i',s)
print(a.start())
s='kdhfsiufyheriu'
a=re.search('iu',s)
print(a.start())
s='kdhfsiufyheriu'
a=re.search('he',s)
print(a.string)
s='kdhfsiufyheriu'
a=re.search('he',s)
print(a.span())
#spit
a='khfisdufge7yfugtk'
z=re.split('fis',a)
print(z)
x='satya vathi goinig to home'
a=re.split('to',x)
print(a)
d='khd usifje udjqwn'
f=re.split('khd',d)
print(f)
#sub()
s='jkdfhiuef dkeif'
a=re.sub('jkd','satya',s)
print(a)
d='satyavathi vamsikumar chinnu'
s=re.sub('chinnu','harshitha',d)
print(s)


import re
str='python programming'
g=re.findall('thon',str)
print(g)
s='kdjisuhfiuhd'
a=re.findall('uh',s)
print(a)
str='python programming'
a=re.search('gra',str)
print(a.string)
str='python programming'
a=re.search('on',str)
print(a.span())
str='python programming'
a=re.search('mm',str)
print(a.start())
str='python programming'
a=re.split()
















































