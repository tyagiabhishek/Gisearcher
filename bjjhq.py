import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import smtplib,ssl

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

port = 465   
smtp_server = "smtp.gmail.com"
sender_email = "leo7279bot@gmail.com"
receiver_email = "tyagiabhishek13@gmail.com"
password = input()
Gionsale = set()
urls = [ 'https://www.bjjhq.com/','https://bjjfanatics.com/collections/daily-deals','https://www.mmahq.com/' ]
context = ssl.create_default_context()
#working loop
while True:
    for url in urls:
        link,saleitem = get_link_name(url)
        if re.search('gi',saleitem,re.IGNORECASE):
            if not saleitem in Gionsale:
                Gionsale.add(saleitem)
                message = "Subject: BOT NOTIFICATION Gi On Sale\n"
                message = "The following Gi is on sale: "
                message+= saleitem +"\n"
                message += "Get in on: "+link
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
                
                print("New Gi on sale "+saleitem)
    time.sleep(5*60)




    
