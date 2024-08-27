import streamlit as st
import pickle

st.title('Anime Recommendation System')

anime_list = pickle.load(open("anime.pkl",'rb'))
anime_data=anime_list
anime_list = anime_list['title'].values
movie_index=dict(zip(anime_data['title'],list(anime_data.index)))


option = st.selectbox("select",anime_list)
cosine_sim = pickle.load(open("ssimilarity.pkl","rb"))


def recommend(name):
        
    index=movie_index[name]
    n_recommendations=300
    sim_scores=list(enumerate(cosine_sim[index]))
    sim_scores=sorted(sim_scores, key=lambda x:x[1],reverse=True)
    sim_scores=sim_scores[1:(n_recommendations+1)]

    recommended_anime=[i[0] for i in sim_scores]

    list1=set(anime_data.iloc[index]['theme'])

    recommendation=[]

    list1=set(anime_data.iloc[index]['theme'])
    list1.discard('nan')

    if list1:
        for j in sim_scores:
            list2=set(anime_data.iloc[j[0]]['theme'])
            list2.discard('nan')
        
            if list2:
                common = set(list1).intersection(set(list2))
          
                if common:
                    recommendation.append(j[0])

    else :

        list1=set(anime_data.iloc[index]['genre'])
        list1.discard('nan')

        if list1:
            for j in sim_scores:
                list2=set(anime_data.iloc[j[0]]['genre'])
                list2.discard('nan')
             
                if list2:
                    common= set(list1).intersection(set(list2))
          
                    if common:
                        recommendation.append(j[0])
    return(recommendation[:15])


col1, col2, col3 = st.columns(3)


if st.button('Recommend'):
    recommendations=recommend(option)

    for i in range(0,len(recommendations)-3,3):
        
        with col1:
            st.write(anime_data.iloc[recommendations[i]]['title'])
            st.image(anime_data.iloc[recommendations[i]]['imgsrc'],width=200)
       

        with col2:
            st.write(anime_data.iloc[recommendations[i+1]]['title'])
            st.image(anime_data.iloc[recommendations[i+1]]['imgsrc'],width=200)

        
        with col3:
            st.write(anime_data.iloc[recommendations[i+2]]['title'])
            st.image(anime_data.iloc[recommendations[i+2]]['imgsrc'],width=200)

            

