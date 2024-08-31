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

About the Dataset

The Dataset contains the following fields(ID title	link	code	rank	popularity	members	score	summary	studio	episode	producer	licensor	genre	theme	duration	imgsrc)

Beautfil Soup was used to scrape data from https://myanimelist.net/ ( Data Gathering.ipynb / Data Gathering.ipynb )


- ### Preprocessing  <a name="pp"></a>
   - Removal of empty / unnecessary rows was done after scraping the data in excel
   - Special characters ([,],",',{,}) were removed from columns (genre, producer, theme, licensor, studio, theme) and converted into list
   - Selected feature (genre, licensor, theme) were concatenated into a single feature vector named combined. And then each unique word from the vector was converted into a separate feature represented by 1 or 0
   - Null values in Numeric columns(popularity, episode, duration) were filled using KNN Imputer
   - Numeric columns were converted to categorical by defining a specific range for the particular columns
      - Episode - Ranges [1,2,3-4,5-9,10-14,15-20,21-26,27-30,31-49,50-52,53+]
      - Score - Ranges [5,5-6,6-7,7-8,8+]
      - Duration - Ranges [1-5,6-10,11-15,16-20,21-25,26-35,35+]
      - Popularity - Get MAX value 

- ### Things I tried but did not work  <a name="TT"></a>

  - preprocessing in ['mean_std', 'minmax', 'raw']
  - cnn_type in ['simple','double']
  - conv_layers in [[64,128,128,64], [32, 64, 128,128], [64, 128, 256]]
  - FE in filters on images ['gaussian','laplace',etc]
  - transfer learning ['Vgg16']
  - various custom cnn architecture

- ### Evaluation  <a name="eval"></a>
  The evaluation metric used is Log-Loss (Cross -Entropy)
   ![logloss](https://github.com/ShailadhShinde/CNN/blob/main/assets/eval.JPG)


- ### Architecture <a name="arch"></a>

`

    Input Shape: (75, 75, 3)

    Conv2D (64 filters, 3x3 kernel, ReLU) 
    Conv2D (64 filters, 3x3 kernel, ReLU)
    Conv2D (64 filters, 3x3 kernel, ReLU)
    MaxPooling2D (3x3 pool, strides 2x2)

    Conv2D (128 filters, 3x3 kernel, ReLU)
    Conv2D (128 filters, 3x3 kernel, ReLU)
    Conv2D (128 filters, 3x3 kernel, ReLU)
    MaxPooling2D (2x2 pool, strides 2x2)

    Conv2D (128 filters, 3x3 kernel, ReLU)
    MaxPooling2D (2x2 pool, strides 2x2)

    Conv2D (256 filters, 3x3 kernel, ReLU)
    MaxPooling2D (2x2 pool, strides 2x2)

    Flatten

    Dense (1024 units, ReLU)
    Dropout (0.4)

    Dense (512 units, ReLU)
    Dropout (0.2)

    Dense (1 unit, Sigmoid)
    


----

## ✨ Demo <a name="demo"></a>

Inputs

   <p align="center">
  <img width="60%" height ="40%"  src="https://github.com/ShailadhShinde/CNN/blob/main/assets/1.JPG">
 </p>
   <p align="center">
  <img width="60%" height ="300"  src="https://github.com/ShailadhShinde/CNN/blob/main/assets/2.JPG">
 </p>
   <p align="center">
  <img width="60%" height ="400"  src="https://github.com/ShailadhShinde/CNN/blob/main/assets/ship.png">
 </p>
   <p align="center">
  <img width="60%" height ="400"  src="https://github.com/ShailadhShinde/CNN/blob/main/assets/iceberg.png">
 </p>
 

----
## 💫 Results <a name="results"></a>

  The top score of the competiton was 0.08227 usign 100s of models.
  
  Got a score of 0.15943 using only a single model 😄
  
   <p align="center">
  <img width="60%" src="https://github.com/ShailadhShinde/CNN/blob/main/assets/score.jpg">
 </p>

  
---

## 🚀 Getting Started <a name="gs"></a>

### ✅ Prerequisites <a name="pr"></a>
 
 - <b>Dataset prerequisite for training</b>:
 
 Before starting to train a model, make sure to download the dataset from <a href="https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data" target="_blank">here </a> or add it to your notebook
 ### 🐳 Setting up and Running the project

 Just download/copy the files `iceberg.py / iceberg.ipynb ` and `EDA.ipynb / EDA.py ` and run them

  
