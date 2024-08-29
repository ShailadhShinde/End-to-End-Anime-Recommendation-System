#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 300)
import seaborn as sns
import matplotlib.pyplot as plt

from IPython.display import clear_output
clear_output(wait=True)

import gc
gc.collect()


# In[2]:


get_ipython().system('pip install fuzzywuzzy')


# In[50]:


anime= pd.read_csv("anime_details - Copy.csv",dtype={'title':object,'Rank':'int','Popularity':'int32','score':'float',
                                                             'summary':'object','Studio':'object','Episode':'int',
                                                             'Producer':'object','Licensor':'object','Genre':'object',
                                                              'Theme':'object','Duration':'int','imgsrc':'object'   })
anime.drop(columns=['ID','link','code','members','Unnamed: 17','Unnamed: 18'],inplace=True)
anime.reset_index(drop=False, inplace=True)


# In[3]:


anime.dtypes


# In[4]:


len(anime['score'])


# In[11]:


anime['title'].nunique()


# In[26]:


anime['score'].mean()


# In[51]:


anime['genre']=anime['genre'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':''," ":'','[':'',']':''})).split(','))
anime['studio']=anime['studio'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':''," ":''})).split(','))
anime['producer']=anime['producer'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':''," ":''})).split(','))
anime['licensor']=anime['licensor'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':''," ":''})).split(','))
anime['theme']=anime['theme'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':''," ":'','[':'',']':''})).split(','))
anime['summary']=anime['summary'].apply(lambda a:str(a).translate(str.maketrans({'{': '', '}': '','\'':'','[':'',']':''})))


# In[81]:


from collections import Counter

genre_count=Counter(g for genres in anime['genre'] for g in genres)
print(len(genre_count))
genre_count


# In[54]:


genre_count.most_common(5)


# In[58]:


genre_count_df=pd.DataFrame([genre_count]).T.reset_index()
genre_count_df.columns=['genre','count']

sns.barplot(x='genre',y='count',data=genre_count_df.sort_values(by='count',ascending=False),palette='viridis')
plt.xticks(rotation=90)


# In[4]:


sample=anime.select_dtypes(include='number').drop(columns=["index","score","rank"])

anime['combined']=anime['theme']+anime['licensor']+anime['genre']

combined=set(c for combine in anime['combined'] for c in combine)
for a in combined:
    anime[a]=anime.combined.transform(lambda x: int(a in x))
    


# In[5]:


sample=anime.select_dtypes(include='number')


# In[49]:


sample.describe()


# In[51]:


sample.isnull().sum() * 100 / len(sample)


# In[5]:


change_popularity=list(range(0,int(max(anime['popularity'])),150))

def Change_Popularity(x):

    for i in range(0,len(change_popularity)-1):
        if x >= change_popularity[-1]:
            return "great popularity"
        elif x >= change_popularity[i] and x <= change_popularity[i+1]:
            return str(change_popularity[i])+"-"+str(change_popularity[i+1])
        

def Change_duration(x):
    if x >= 1 and x<=5:
        return "1-5"
    if x >= 6 and x<=10:
        return "6-10"
    if x >= 11 and x<=15:
        return "11-15"
    if x >= 16 and x<=20:
        return "16-20"
    if x >= 21 and x<=25:
        return "21-25"
    if x >= 26 and x<=35:
        return "26-35"
    if x >= 35:
        return "35+"
    

def Change_episode(x):
    if x == 1:
        return "1"
    if x == 2:
        return "2"
    if x == 3 or x==4:
        return "3-4"
    if x >= 5 and x<=9:
        return "5-9"
    if x >= 10 and x<=14:
        return "10-14"
    if x >= 15 and x<=20:
        return "15-20"
    if x >= 21 and x <= 26:
        return "21-26"
    if x >= 27 and x <= 30:
        return "27-30"
    if x >= 31 and x <= 49:
        return "31-49"
    if x >= 50 and x <= 52:
        return "50-52"
    if x >= 53:
        return "53"
    
    
def Change_Score(x):
    if x <= 5.0:
        return '5'
    if x > 5.0 and x < 6.0:
        return '5-6'
    if x >=6.0 and x < 7.0:
        return '6-7'
    if x >= 7.0 and x < 8.0:
        return '7-8'
    if x >= 8.0:
        return '8'


# In[224]:


sns.set_theme(rc={'figure.figsize':(11.7,150)})

sns.countplot(data=anime, y='episode', order=anime.episode.value_counts().index)


# In[6]:


from sklearn.impute import KNNImputer
imputer=KNNImputer(n_neighbors=20,weights='uniform',metric='nan_euclidean')
filled_data=imputer.fit_transform(sample)
filled_data=pd.DataFrame(filled_data,columns=sample.columns)
filled_data=filled_data.reset_index()

anime['popularity']=filled_data['popularity']
anime['episode']=filled_data['episode']
anime['duration']=filled_data['duration']



# In[7]:


anime["popularity_ch"]=anime['popularity'].apply(lambda x: Change_Popularity(int(x)))
anime["duration_ch"]=anime['duration'].apply(lambda x: Change_duration(int(x)))
anime["episode_ch"]=anime['episode'].apply(lambda x: Change_episode(int(x)))
anime["score_ch"]=anime['score'].apply(lambda x:Change_Score(x))


# In[8]:


from sklearn.preprocessing import OneHotEncoder

categorical_columns=['popularity_ch','duration_ch','episode_ch','score_ch']

encoder = OneHotEncoder(sparse_output=False)

one_hot_encoded = encoder.fit_transform(anime[categorical_columns])

one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out(categorical_columns))


# In[9]:


drop=['imgsrc','score_ch','popularity_ch','episode_ch','duration_ch','title','rank','popularity','score','summary','episode','duration','studio','producer','licensor','genre','theme','combined','nan']
anime_summary=anime.drop(columns=drop)


# In[59]:


matrix=pd.concat([anime_summary, one_hot_df], axis=1).drop(columns=['index','score_ch_None'])


# In[12]:


matrix


# In[60]:





# In[79]:





# In[14]:


from fuzzywuzzy import process

def anime_finder(name):
    all_titles=anime['title'].tolist()
    match=process.extractOne(name,all_titles)
    return match[0]


# In[15]:


title=anime_finder('Oregairu')
title


# In[11]:


name='91 Days'
movie_index=dict(zip(anime['title'],list(anime.index)))
index=movie_index[name]
index


# In[ ]:





# In[12]:


from sklearn.decomposition import TruncatedSVD

svd = TruncatedSVD(n_components=40,n_iter=20)
q = svd.fit_transform(matrix)

q.shape


# In[13]:


from sklearn.metrics.pairwise import cosine_similarity

cosine_sim=cosine_similarity(q,q)
cosine_sim.shape


# In[61]:


def recommend(name):
    index=movie_index[name]
    n_recommendations=300
    sim_scores=list(enumerate(b[index]))
    sim_scores=sorted(sim_scores, key=lambda x:x[1],reverse=True)
    sim_scores=sim_scores[1:(n_recommendations+1)]

    recommended_anime=[i[0] for i in sim_scores]

    list1=set(anime.iloc[index]['theme'])

    recommendation=[]

    list1=set(anime.iloc[index]['theme'])
    list1.discard('nan')
    print(list1)
    if list1:
        for j in sim_scores:
            list2=set(anime.iloc[j[0]]['theme'])
            list2.discard('nan')
            if list2:
                common = set(list1).intersection(set(list2))
                if (len(common)==len(list2)) and common:
                    recommendation.append(j[0])

    else :
        list1=set(anime.iloc[index]['genre'])
        list1.discard('nan')

        for j in sim_scores:
            list2=set(anime.iloc[j[0]]['genre'])
            list2.discard('nan')
            if list2:
                common= set(list1).intersection(set(list2))
                if (len(common)==len(list2)) and common:
                    recommendation.append(j[0])
                    
    print(anime['title'].iloc[recommendation][:15])


# In[62]:


recommend('91 Days')


# In[ ]:





# In[52]:


dump=anime[['index','title','theme','genre','imgsrc']]


# In[53]:


dump


# In[ ]:


b = np.float16(cosine_sim)


# In[48]:


import pickle


# In[55]:


pickle.dump(dump,open('anime.pkl','wb'))


# In[42]:


pickle.dump(b,open('ssimilarity.pkl','wb'))


# In[ ]:




