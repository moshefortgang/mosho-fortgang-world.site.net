__author__ = 'student'
from csv import DictReader

dct={'AS':'Asia','EU':'Europe','AF':'Africa','OC':'Oceania','NA':'North America','AN':'Antarctica','SA':'South America'}

with open('countries.csv') as f:
    reader = list(DictReader(f))
    with open('index.html','w')as wirteIndex:
        wirteIndex.write('<ul>\n')

        wirteIndex.write('<p><h1>the list of al</h1></p>')


        for k,v in dct.items():
            wirteIndex.write('\t<li><a href="index{}.html">{}</a>: </li>\n'.format(k,v))
        wirteIndex.write('</ul>\n')

        for k,v in dct.items():
            wirteIndex.write('\t<p><h1>%s</p></h1>'%v)
            wirteIndex.write('<ul>\n')
            print(k)

            for i in reader:

                if k in i['continent']:
                    wirteIndex.write('\t<li><a href="{}.html">{}</a>:</li>\n'.format(i['short_name'],i['name']))
            wirteIndex.write('</ul>\n')

        with open('indexPopultion.html','w')as wirteIndex:
            wirteIndex.write('<ul>\n')
            for i in (sorted(reader, key= lambda x: x['population'],reverse=True)):
                wirteIndex.write('\t<li><a href="{}.html">{}</a>:</li>\n'.format(i['short_name'],i['name']))