from bs4 import BeautifulSoup
import urllib
import urllib2
import urlparse
import os

output = []
url = "http://apps1.eere.energy.gov/buildings/energyplus/cfm/weather_data3.cfm/region=4_north_and_central_america_wmo_region_4/country=1_usa/cname=USA"
site = urllib2.urlopen(url).read()

links = []

for link in BeautifulSoup(site).find_all('a'):
    links.append(urlparse.urljoin(url,link.get('href')))

zips = []
for link in links:
    if link[-4:] == '.zip':
        zips.append(link)
        
for zip in zips:
    name = zip.split("/")[len(zip.split("/"))-1]
    urllib.urlretrieve(zip, "./weatherfiles/" + name)
    
for filename in os.listdir("./weatherfiles/"):
    os.system("unzip " + "./weatherfiles/" + filename + " -d ./weatherfiles/")
    
os.system("rm ./weatherfiles/*.zip ./weatherfiles/*.ddy ./weatherfiles/*.stat")