#Below code should be able to download images to your local from a csv of links
import csv
import urllib
import lxml.html
import requests
connection = urllib.request.urlopen('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events')
with open('events.csv',encoding="latin1") as csvfile:
    csvrows = csv.reader(csvfile, delimiter=',', quotechar='"')
    print("NANI")
    for row in csvrows:
      print("Reading")
      if 'view.php' in row[0]:
        filename = row[1]
        url = row[0]
        locn=row[2]
        print (locn)