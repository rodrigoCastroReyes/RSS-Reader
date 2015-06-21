
import urllib.request
import feedparser
import random

class Feed:
    id= 0
    title= ''
    link= ''
    fecha= ''
    descripcion= ''


    def __init__(self, id, tit, link, fecha, desc):
        self.id= id
        self.title= tit
        self.link = link
        self.fecha = fecha
        self.descripcion= desc

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def getFecha(self):
        return self.fecha

    def getDescripcion(self):
        return self.descripcion

    def setTitle(self, title):
        self.title = title

    def setLink(self, link):
        self.link = link

    def setFecha(self, fecha):
        self.fecha = fecha

    def setDescripcion(self, descrip):
        self.descripcion =  descrip

    def setAll(self, t, d, l, f):
        self.descripcion =  d
        self.fecha = f
        self.title = t
        self.link = l

    # Da formato a los elementos del feed y los deja listos para ser impresos
    def getAlltoPrint(self):
        return self.fecha + ' >> ' + self.title + '\n\t' + self.descripcion + '\n' + self.link+ '\n\n'

########################################### CLASE PROVIDER #####################################################3

# Clase de proveedores de feeds
class Provider:
    id=0
    url = ''
    maxFeeds=0 #cuantos feeds se trae el hilo por cada fetch al proveedor
    feedsList= []

    # contructor

    def __init__(self, id, url, maxFeeds):
        self.id = id
        self.url = url
        self.maxFeeds = maxFeeds
        self.feedsList = []

    def getId(self):
        return self.id

    def getUrl(self):
        return self.url

    def getMaxFeeds(self):
        return self.maxFeeds

    def getFeeds(self):
        return self.feedsList

    def setUrl(self, url):
        self.url = url

    def setMaxFeeds(self, max):
        self.maxFeeds = max

    def setAll(self, url, feeds):
        self.url = url
        self.feeds = feeds

    def addFeed(self, Feed):
        self.feedsList.append(Feed)

    def cleanFeedsList(self):
        self.feedsList = []

    def cargaFeeds(self):
        i = self.maxFeeds
        self.cleanFeedsList()
        c = 0
        # Dada una url me devuelvo objeto Feed con título, link, info y fecha de publicación
        try:
            x= urllib.request.urlopen(self.url)
            d = feedparser.parse(x.read())
            while i > 0:
                feed = Feed(c, d.entries[c].title, d.entries[c].link, d.entries[c].published, d.entries[c].description)
                self.addFeed(feed)
                i-=1
                c+=1
        except Exception as e:
            print("Tenemos Inconvenientes: " + str(e))

    def getNews(self):
        return self.getFeeds()[random.randrange(0,len(self.feedsList)-1)].getAlltoPrint()

    def printFeedsList(self):

        for i in range (1, len(self.feedsList)):
            print(self.getFeeds()[i-1].getAlltoPrint())
          #  print(self.getFeeds()[2].getTitle() + ' LINK >>' + p.getFeeds()[2].getLink())
           # print(p.getFeeds()[3].getTitle() + ' LINK >>' + p.getFeeds()[3].getLink())
          #  print(p.getFeeds()[4].getTitle() + ' LINK >>' + p.getFeeds()[4].getLink())








