#!/usr/bin/env python
# coding: utf-8

# In[1]:


url='https://myanimelist.net/anime.php'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
#r=requests.get(url,headers)
#soup=BeautifulSoup(r.text,'html.parser')
#response = requests.post(url, data=post_fields, timeout=timeout)
#print(response.elapsed.total_seconds())


# In[13]:


import requests
from bs4 import BeautifulSoup
import string
import re
from bs4 import BeautifulSoup, NavigableString, Tag
import time  
import csv
import itertools


# In[23]:


import pandas as pd
d=pd.read_csv('anime_details - Copy.csv',sep=',')
d.head(d)


# In[3]:


def reviews(code,morereviews):
    #print('passed: '+morereviews)
    #print("review start")
    r=requests.get(morereviews,headers)
    soup=BeautifulSoup(r.text,'html.parser')
    T=30
    #print('P1')
    while r.status_code!=200:
            print("status czode")
            print(r.status_code)
            time.sleep(T)
            r=requests.get(morereviews,headers)
            #print(r.text)
            soup=BeautifulSoup(r.text,'html.parser')
            T=T+20
            print(morereviews)       
            if T>350:
                break
            
    a=soup.find_all('div',{'class':'review-element js-review-element'})
    k=morereviews
    try:
        for i in soup.find_all('div',{'class':'ml4 mb8'}):
            morereviews=i.find('a')['href']
            break
        else:       
            morereviews=''
    except:
        morereviews=''
    review={}
    for i in a:
        review[i.find('div',{'class':'username'}).text]=i.find('div',{'class':'text'}).text
        
    Allreviews[code]=review 
    if morereviews!='' and k!=morereviews:
       
        reviews(code,morereviews)
        #print('empty')


# In[4]:


def Letterswisesearch(Detailscounter,details):
    Alphabets=('T','U','V','W','X','Y','Z')

    
    for alpha in Alphabets:
        r=requests.get(url+'?letter='+alpha,headers)
        #print("main status code")
        #print(r.status_code)

        soup=BeautifulSoup(r.text,'html.parser')
        T=30
        while(r.status_code!=200):
            print("status code")
            print(r.status_code)
            time.sleep(T)
            T=T+20
            r=requests.get(url+'?letter='+alpha,headers)
            soup=BeautifulSoup(r.text,'html.parser')

       # print(soup.prettify)
        table=soup.find('div',{'class':'js-categories-seasonal'}).find_all('tr')

        #re.sub('[^0-9]', '-',pageno.get_attribute("innerText"))).split("-")
        #num=list(re.sub('[^0-9]','',num[0]))
        substring='anime/'
        for i in table:
            innerdict={}

            for j in i.find_all('a',{'class':'hoverinfo_trigger fw-b fl-l'}):
                names.append(j.text)
                href.append(j['href'])
                innerdict['title']=j.text 
                innerdict['link']=j['href']
                Detailscounter=Detailscounter+1
                index=j['href'].index(substring)+len(substring)
                code=''  
                while(j['href'][index]!='/'):
                    code=code+j['href'][index]
                    index=index+1

                innerdict['code']=code
                details[Detailscounter]=innerdict    

               # print(alpha)
                Animedetails(Detailscounter,j['href'],details)
                #print('main one: '+j['href'])


                print(details[Detailscounter]['title'])
                #print("Reviews start")
              #  reviews(int(code),j['href']+'/reviews?sort=suggested&filter_check=&filter_hide=&preliminary=on&spoiler=on&p=1')

                #print(alpha+"Animereviews")

                #innerdict.clear()
                #print(Detailscounter)

        EverysinglePage(findtotalpage(soup),Detailscounter,alpha,50,details,count=1)   

        #print(alpha+" "+str(numi)+"Animedetails")
       

        Allreviews={}



# In[5]:


def findtotalpage(soup):
    num=0
    pages=soup.find_all('span',{'class':'bgColor1'})
    
    for i in pages:
        if i.text[-2]==' ':
            num=int(i.text[-1])
        elif i.text[-3]==' ' and i.text!=' ':
            num=int(i.text[-2]+i.text[-1])
    
    return num


# In[6]:


def EverysinglePage(num,Detailscounter,alpha,previousnum,details,count):
    
    startnum=previousnum
    pagelist=range(startnum,num*50,50)
    

    #pagelist=range(50,100,50)
    for numi in pagelist:
        #headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
        if count==3:
            count=0
            print("sleeping")
            time.sleep(30)
        count+=1
        T=30
        r=requests.get(url+'?letter='+alpha+'&show='+str(numi),headers)
        #print("status code")
        #print(r.status_code)
        while r.status_code!=200:
            
            print("sleeping")
            time.sleep(T)
            r=requests.get(url+'?letter='+alpha+'&show='+str(numi),headers)
           
            T=T+20
            print("status code")
            print(r.status_code)
        soup=BeautifulSoup(r.text,'html.parser')
       # print(numi)
        global z
        z=soup
        #print(numi)
        table=soup.find('div',{'class':'js-categories-seasonal'}).find_all('tr')
        substring='anime/'
       # print(alpha+" "+str(numi))
        for i in table:
            innerdict={}
            for j in i.find_all('a',{'class':'hoverinfo_trigger fw-b fl-l'}):
              #  names.append(j.text)
               # href.append(j['href'])
                innerdict['title']=j.text 
                innerdict['link']=j['href']
                index=j['href'].index(substring)+len(substring)
                code=''  
                while(j['href'][index]!='/'):
                    code=code+j['href'][index]
                    index=index+1
                
                innerdict['code']=code
                
                Detailscounter=Detailscounter+1
                details[Detailscounter]=innerdict
                Animedetails(Detailscounter,j['href'],details)
                print(details[Detailscounter]['title'])
                #print(alpha+" "+str(numi)+"Animedetails")
                #reviews(int(code),j['href']+'/reviews?sort=suggested&filter_check=&filter_hide=&preliminary=on&spoiler=on&p=1')
               # print(alpha+" "+str(numi)+"Animereviews")
                #print(details[Detailscounter])
                #innerdict.clear()
       # print('OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
       # print(details[Detailscounter])
       # print('numi   num')
       # print(str(numi)+str(num))
        store(details)
        details.clear()
    NUM=findtotalpage(soup)
    if num < NUM:
        previousnum=num
        #print("once")
        EverysinglePage(NUM,Detailscounter,alpha,previousnum*50,details,count) 
    


# In[7]:


def Animedetails(key,url,details):
    t=30
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.text,'html.parser')
    while(r.status_code!=200):
        print("status code")
        print(r.status_code)
        time.sleep(t)
        t=t+20
        r=requests.get(url,headers)
        soup=BeautifulSoup(r.text,'html.parser')
        
    print("status code")
    print(r.status_code)
    #print(soup.find_all('span',{'class':'numbers ranked'}))
    for i in soup.find_all('span',{'class':'numbers ranked'}):
        details[key]['Rank']=re.sub('[^0-9]','',i.text)
    for i in soup.find_all('span',{'class':'numbers popularity'}):
        details[key]['Popularity']=re.sub('[^0-9]','',i.text)
    for i in soup.find_all('span',{'class':'numbers members'}):
        details[key]['Members']=re.sub('[^0-9]','',i.text)
    for i in soup.find_all('span',{'itemprop':'ratingValue'}):
        details[key]['Score']=i.text
    for i in soup.find_all('p',{'itemprop':'description'}):
        details[key]['summary']=i.text
    for i in soup.find_all('span',{'class':'information studio author'}):
        details[key]['Studio']=i.text


    for i in soup.find_all('div',{'class':'spaceit_pad'}):
        if 'Episodes:' in i.text:
             details[key]['Episode']=re.sub('[^0-9]','',i.text)
        elif 'Producers' in i.text:
            a=set(i.text.replace(' ','-').replace('Producers:','').replace('\n','').replace('-','').split(','))
            a.discard('addsome')
            if 'Nonefound' in a:
                details[key]['Producer']=''
            else:
                details[key]['Producer']=a
        elif 'Licensors:' in i.text:
            a=set(i.text.replace(' ','-').replace('Licensors:','').replace('\n','').replace('-','').split(','))
            a.discard('addsome')
            if 'Nonefound' in a:
                details[key]['Licensor:']=''
            else:
                details[key]['Licensor:']=a
            
        elif 'Studios:' in i.text:
            a=set(i.text.replace(' ','-').replace('Studios:','').replace('\n','').replace('-','').split(','))
            a.discard('addsome')
            if 'Nonefound' in a:
                details[key]['Studio']=''
            else:
                details[key]['Studio']=a
        elif 'Genres:' in i.text:
            a=''
            for j in i.find_all('a'):
                a=a+' '+j.text
            m=set(a.split(' '))
            details[key]['Genre']=m-{''}
        elif 'Theme:' in i.text:
            a=''
            for j in i.find_all('a'):
                a=a+''+j.text
            m=set(a.split(' '))
            details[key]['Theme']=m-{''}
        elif 'Duration:' in i.text:
            details[key]['Duration']=re.sub('[^0-9]','',i.text)
      
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.text,'html.parser')

    t=30

    while(r.status_code!=200):
        print("status code")
        print(r.status_code)
        time.sleep(t)
        t=t+20
        r=requests.get(url,headers)
        soup=BeautifulSoup(r.text,'html.parser')

    src=''
    try:
        for i in soup.find_all('h1',{'class':'title-name h1_bold_none'}):

            src=str(i.text)

        image=soup.find_all('img',{'alt':src})
        ind=str(image).index("data-src")+len('data-src')+2
        image=str(image)
        src=''
        while image[ind]!='"':
            src=src+image[ind]
            ind+=1
        details[key]['imgsrc']=src
    except:
        print("Nameeeeeeeeeee:")
        print(src)
        print('url')
        print(url)
        print(soup.find_all('h1',{'class':'title-name h1_bold_none'}))



# In[8]:


def store(details):
    print("first")
    print(list(details)[0])
    print("last")
    print(list(details)[-1])
    previous=details
    csvfile(details)
            #reviewst(Allreviews)
    print('clearrrrrrrrr')
    details.clear()
    print(details)


# In[ ]:





# In[12]:


Letterswisesearch(Detailscounter,details)


# In[9]:


def mergedict(a,b):
    a.update(b)
    return a

 
def csvfile(details):
    field_names = ['Id','title', 'link','code', 'Rank','Popularity','Members','Score','summary','Studio','Episode','Producer','Licensor:','Genre','Theme','Duration','imgsrc'] 
    print("doneeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    
    with open("anime_details.csv","a",encoding="utf-8") as f:
        w = csv.DictWriter( f, field_names )
        w.writeheader()
        for k,d in sorted(details.items()):
            w.writerow(mergedict({'Id': k},d))
            
    


# In[10]:


def reviewst(reviews):
    fields = ['code','username','summary'] 
    with open("review_details.csv","a",encoding="utf-8") as f:
        w = csv.DictWriter(f, fields )
        w.writeheader()
        for key,val in sorted(reviews.items()):
            for k,v in val.items():
                w.writerow({'code':key,'username':k,'summary':v})  


# In[ ]:





# In[11]:


names=[]
href=[]
details={}
Allreviews={}
    
Detailscounter=0


# In[ ]:





# In[ ]:





# In[ ]:




