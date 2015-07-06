__author__ = 'student'
from csv import DictReader
from math import radians, cos, sin, asin, sqrt




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

with open('countries.csv')as index:
    index = DictReader(index)
    with open('index.html','w')as wirteIndex:
        wirteIndex.write('<ul>\n')
        wirteIndex.write('<body background ="P.JPG" t>')
        for i in index:
            distance= (haversine(34.75,31.5,float(i['lon']),float(i['lat'])))
            wirteIndex.write('\t<li><a href="{}.html">{}</a>: {:,d} km</li>\n'.format(i['short_name'],i['name'],int(distance)))
        wirteIndex.write('<ul>\n')



with open('countries.csv') as f:
    reader = DictReader(f)
    for i in reader:
       with open('%s.html'%i['short_name'], 'w') as myFile:
          myFile.write('<html>\n')
          myFile.write('<head>\n')
          myFile.write('\t<title>%s</title>\n'% i['name']);
          myFile.write('</head>\n')
          myFile.write('<body>\n')
          myFile.write(' <body style="background-color:#ff0000;">')
          myFile.write('<h1>%s<h1>\n'%i['name'])
          myFile.write('<dl>\n')
          myFile.write('\t<dt>Capital</dt>\n')
          myFile.write('\t<dd>%s</dd>\n'%i['capital'])
          myFile.write('\t<dt>Population</dt>\n')
          myFile.write('\t<dd>%s</dd>\n'%i['population'])
          myFile.write('\t<dt>%skm<sup>2</sup></dt>\n'%i['land'])
          myFile.write('\t<dd>%s</dd>\n'% i['continent'])
          myFile.write('\t<bb><a href="indexA.html"><em>back to the index</em></a>: </bb>\n')
          myFile.write('</dl>\n')

          myFile.write('</body>\n')

          myFile.write('</html>\n')


    #for i in reader:
   #     print('israel', i['name'],'  ',haversine(float(i['lat']),float(i['lon']),float(31.5),float(34.75)))


# d['short name']
# d['name']
# d['capital']
# d['lat']
# d['lon']
# d['continent']
# d['subcontinent']
# d['population']
# d['land']
# d['languages']
# d['gov_url']




