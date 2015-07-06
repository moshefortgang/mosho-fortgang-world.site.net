__author__ = 'student'
from math import radians, cos, sin, asin, sqrt
from csv import DictReader


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def sortContry(lon1,lat1):
    with open('countries.csv')as index:
        index = list(DictReader(index))
        lst=[]
        for i in index:
            distance= (haversine(float(lon1),float(lat1),float(i['lon']),float(i['lat'])))
            lst.append((i['short_name'], distance))
        a = sorted(lst, key=lambda x: x[1])

        return a[1:16]
dct={'AS':'Asia','EU':'Europe','AF':'Africa','OC':'Oceania','NA':'North America','AN':'Antarctica','SA':'South America'}
with open('countries.csv') as f:
    reader = list(DictReader(f))
    for i in reader:
        with open('%s.html'%i['short_name'], 'w') as myFile:
            myFile.write('<html>\n')
            myFile.write('<head>\n')
            myFile.write('\t<title>%s</title>\n'% i['name']);
            myFile.write('</head>\n')

            a = i['short_name']
            myFile.write('<img src="http://www.crwflags.com/fotw/images/{}/{}.gif">\n'.format(a[0].lower(),a.lower()))

            myFile.write('<h1>%s</h1>\n'%i['name'])
            myFile.write('<dl>\n')
            myFile.write('\t<dt>Capital</dt>\n')
            myFile.write('\t<dd>%s</dd>\n'%i['capital'])
            myFile.write('\t<dt>Population</dt>\n')
            myFile.write('\t<dd>%s</dd>\n'%i['population'])
            myFile.write('\t<dt>%skm<sup>2</sup></dt>\n'%i['land'])
            myFile.write('\t<dd>%s</dd>\n'% i['continent'])
            myFile.write('<p></p>\n')
            myFile.write('<h1>Closet countries:</h1>')
            myFile.write('<ol>')
            s = sortContry(i['lon'],i['lat'])
            for j in s:
                for a in reader:
                    if j[0] == a['short_name']:
                        myFile.write('\t<li><dd><a href="{0}.html">{1} </a>: {2} </dd></li>\n'.format(a['short_name'],a['name'],j[1]))


            myFile.write('</ol>')
            myFile.write('<p><h1>all continents:</h1></p>')

            myFile.write('<ul>\n')
            for k,v in dct.items():
                myFile.write('\t<li><a href="index{}.html">{}</a>: </li>\n'.format(k,v))
            myFile.write('<ul>\n')
            myFile.write('\t<bb><a href="indexA.html"><em>back to the index</em></a>: </bb>\n')


            myFile.write('</dl>\n')
            myFile.write('</body>\n')
            myFile.write('</html>\n')

print(sortContry(34.75,31.5))
