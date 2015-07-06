__author__ = 'student'
from csv import DictReader

dct={'AS':'Asia','EU':'Europe','AF':'Africa','OC':'Oceania','NA':'North America','AN':'Antarctica','SA':'South America'}

with open('indexA.html' ,'w')as wirteIndex:
    wirteIndex.write('<ul>\n')
    wirteIndex.write('<p><h1>the list of al</h1></p>')
    for k,v in dct.items():
            wirteIndex.write('\t<li><a href="index{}.html">{}</a>: </li>\n'.format(k,v))
    wirteIndex.write('<ul>\n')



with open('countries.csv')as index:
    index = list(DictReader(index))
    for k,v in dct.items():
        with open('index%s.html'%k ,'w')as wirteIndex:
            wirteIndex.write('<ul>\n')
            wirteIndex.write('<h1>%s</h1>'%v)
            for i in index:
                if i['continent']== k:
                    wirteIndex.write('\t<li><a href="{}.html">{}</a>: </li>\n'.format(i['short_name'],i['name']))
            wirteIndex.write('\t<li><a href="indexA.html"><em>to the index</em></a>: </li>\n')
            wirteIndex.write('<ul>\n')
for k,v in dct.items():
    with open('index%s.html'%k, 'r') as myFile:
        for i in myFile:
            print(i)
