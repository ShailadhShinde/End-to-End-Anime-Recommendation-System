# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```



<div align="center">

![logo](https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/header.png)  
<h1 align="center"><strong>Anime Recommender<h6 align="center">A Recommendation System (CV) project</h6></strong></h1>

![Python - Version](https://img.shields.io/badge/PYTHON-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)

</div>




This project focuses on:

- Exploratory Data Analysis
- 
-
-

#### -- Project Status: [Completed]

#### -- time_series.py / time_Series.ipynb - Contains code for the project

#### -- eda-time-series.ipynb / EDA.py - Exploratory Data Analysis [Click to view](https://www.kaggle.com/code/shailadh/eda-time-series?scriptVersionId=190759981)

----

## [📚 Project Documentation 📚](http://smp.readthedocs.io/)

### 📋 Table of Contents
- [Overview](#overview)
  - [About the Dataset](#atd)
  - [Preprocessing](#pp)
  - [Things I tried but did not work](#TT)
  - [Evaluation](#eval)
  - [Architecture](#arch)
- [Demo](#demo)
- [Results](#results)
- [Getting Started](#gs)
  - [Prerequisites](#pr)


###  📌 Project Overview  <a name="overview"></a>

This project is an End to End Anime(a style of Japanese film and television animation, typically aimed at adults as well as children) Recommendation System.
Content Based Filtering is used to recommend other similar anime. The Cosine similarity metric was used to generate a similarity score between one anime and another.
Streamlit framework was used to built the web app.

- ### About the Dataset

The Dataset contains the following fields (ID title	link	code	rank	popularity	members	score	summary	studio	episode	producer	licensor	genre	theme	duration	imgsrc)

Beautfil Soup was used to scrape data from https://myanimelist.net/ ( Data Gathering.ipynb / Data Gathering.ipynb )


- ### Preprocessing  <a name="pp"></a>

   - Removal of empty / unnecessary rows was done after scraping the data in excel
   - Special characters ([,],",',{,}) were removed from columns (genre, producer, theme, licensor, studio, theme) and converted into list
   - Selected feature (genre, licensor, theme) were concatenated into a single feature vector named combined. And then each unique word from the vector was converted into a separate feature represented by 1 or 0
   - Null values in Numeric columns(popularity, episode, duration) were filled using KNN Imputer
   - Numeric columns were converted to categorical by defining a specific range for the particular columns
      - episode - Ranges [1,2,3-4,5-9,10-14,15-20,21-26,27-30,31-49,50-52,53+]
      - score - Ranges [5,5-6,6-7,7-8,8+]
      - duration - Ranges [1-5,6-10,11-15,16-20,21-25,26-35,35+]
      - popularity - Get MAX value and split the list having a static range of 150 between numbers (0-150, 151-300, 301-450 , ....)
   - After changing numeric-categorical applied one-hot Encoding and concatenated the one hot encoded matrix to rest of the dataset
   - Drop columns not having 1s or 0s as their value converting it into a matrix
   - Used Truncated SVD to reduce the dimensionality of the matrix

- ### Things I tried but did not work  <a name="TT"></a>

  - using Columns [rank,members,summary,producer] and their unique combination like genre+theme, theme+genre etc.
  - raw numeric columns [episode,score,duration,popularity]

  
- ### Evaluation  <a name="eval"></a>

   Since the Content Based filtering is a way to solve the cold start problem and the data was scraped from the internet I did not use any evaluvation metric.
  Also I am familiar with most of the anime to test the model.  

- ### Model <a name="arch"></a>

   Cosine similarity measure was used to get the similarity matrix . Yes, it works on binary data as aswell.

  Streamlit was used to create thw web app ()

- ### Post-Processing

  Converted matrix form float64 to float16 as Streamlit has restriction of 1 GB RAM 
  
   
----

## ✨ Demo - 💫 Results <a name="results"></a> <a name="demo"></a>

[Live Demonstration](https://sanime-recommendations.streamlit.app/)

Home
   <p align="center">
  <img width="60%" height ="40%"  src="https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/home.JPG">
 </p>

 Romance Anime
   <p align="center">
  <img width="60%" height ="100%"  src="https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/romance.JPG">
 </p>

 Crime Anime
   <p align="center">
  <img width="60%" height ="100%"  src="https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/crime.JPG">
 </p>

 Isekai Anime
   <p align="center">
  <img width="60%" height ="100%"  src="https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/isekai.JPG">
 </p>
 

----

## 🚀 Getting Started <a name="gs"></a>

### ✅ Prerequisites <a name="pr"></a>
 
 - <b>Dataset prerequisite for training</b>:
 
 Before starting to train a model, make sure to download the dataset from <a href="https://github.com/ShailadhShinde/RecommendationSystems/blob/main/assets/anime_details%20-%20Copy.csv" target="_blank"> here </a> or add it to your notebook
 
 ### 🐳 Setting up and Running the project

To Scrape Data - Download/copy the files `Data Gathering.py / Data Gathering.ipynb ` and run them 

To create model - Download/copy the files `anime.py / anime.ipynb ` and run them 

                                 OR

To Run thw Web App - 

1. Clone the git Repository 
2. Create account on Streamlit Community Cloud > Login > Create New App > add your Repository and Save

   


 

  
