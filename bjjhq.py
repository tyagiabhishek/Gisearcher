import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import yagmail

def linkmmahq(soup):
    headings = soup.findAll('h1')
    saleitem = headings[0].string
    return('https://www.mmahq.com/',saleitem)
def linkbjjhq(soup):
    headings = soup.findAll('h1')
    saleitem = headings[0].string
    return('https://www.bjjhq.com/',saleitem)
def linkbjjfanatics(soup):
    productsonpage = soup.find_all('div',class_ = "product-card__name")
    dailysaleitem = productsonpage[-1].string
    links = soup.find_all("a",class_="product-card")
    linkforsaleitem = links[-1]
    linkforsaleitem = "https://bjjfanatics.com"+linkforsaleitem["href"]
    return (linkforsaleitem,dailysaleitem)

def get_link_name(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    if "bjjhq" in url:
        return linkbjjhq(soup)
    elif "bjjfanatics" in url:
        return linkbjjfanatics(soup)
    elif "mmahq" in url:
        return linkmmahq(soup)
    
sender_email = "leo7279bot@gmail.com"
receiver_email = "tyagiabhishek13@gmail.com"
message = "The following Gi is on sale: "
yag = yagmail.SMTP("leo7279bot@gmail.com")
Gionsale = set()
urls = [ 'https://www.bjjhq.com/','https://bjjfanatics.com/' ]

#working loop
while True:
    for url in urls:
        link,saleitem = get_link_name(url)
        if re.search('gi',saleitem,re.IGNORECASE):
            if not saleitem in Gionsale:
                Gionsale.add(saleitem)
                message = "The following Gi is on sale: "
                message+= saleitem +"\n"
                message += "Get in on: "+link
                yag.send(to = receiver_email,subject = "BOT NOTIFICATION: Gi on sale",contents=message)
                
                print("New Gi on sale "+saleitem)
    time.sleep(5*60)




    
