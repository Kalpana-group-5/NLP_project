

# <a name="top"></a> Spotify Natural Language Processing Project
![]()
### Kalpana group 5
by: Daniel Ford, Glady Barrios, Kevin Smith

<p>
  <a href="https://github.com/DanielFordHUB" target="_blank">
    <img alt="Daniel" src="https://img.shields.io/github/followers/DanielFordHUB?label=Follow_Daniel&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/GladyBarrios" target="_blank">
    <img alt="Glady" src="https://img.shields.io/github/followers/GladyBarrios?label=Follow_Glady&style=social" />
  </a>
</p>

<p>
  <a href="https://github.com/kevin-mal-smith" target="_blank">
    <img alt="Kevin" src="https://img.shields.io/github/followers/kevin-mal-smith?label=Follow_Kevin&style=social" />
  </a>
</p>

***
[[Project Description](#project_description)]
[[Project Goal](#project_goal)]
[[Project Planning](#planning)]
[[Key Findings](#findings)]
[[Data Dictionary](#dictionary)]
[[Data Acquire and Prep](#wrangle)]
[[Data Exploration](#explore)]
[[Modeling](#model)]
[[Conclusion](#conclusion)]
___


## <a name="project_description"></a>Project Description:

In our project we have collected 100 README files from GitHub and used Machine Learning classification Models to predict the primary programming language when using the search term "Spotify". Our main goal is to identify terms for predicting a readme's primary language on GitHub.

This project involves Data cleaning, Preparation, Exploration and Modeling.



[[Back to top](#top)]

***
## <a name="project_goal"></a>Project Goal:
The goal of this project is to use natural language processing and classification models to identify terms for predicting a readme's primary language on Github.

[[Back to top](#top)]


***
## <a name="planning"></a>Project Planning: 
[[Back to top](#top)]

### Project Outline:
### Initial Questions
 - What are the top 5 programming languages when searching for 'Spotify' repos on github?
 - What are the most common words we would see when searching for spotify README's
 - From these top 5 programing languages what are the most common words from these languages 
 - What are some common bigrams in the languages when using these bigrams


### Need to haves (Deliverables):

- Here is a link to our Canva Presentaion 
    - This is a short 5 minuite presentaion 
- Our final Notebook contaning specific details of the code necessary for our presentaion 

***

## <a name="findings"></a>Executive Summary:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]


| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
|Repo|The username of the REPO |Object|
|readme_contents|What is inside the readme|Object|
|language|the programming language|Object|
|lemmatized|prepared data|Object|

***

## <a name="wrangle"></a>Data Acquisition and Preparation

### Acquiring the Data 

- To acquire the data first we needed to scrape the links for the individual repos from github by iterating through the pages of search results and grabbing the 10 links from each page.

- Once this step was completed we were able to populate a dataframe with the name of the repo, the main coding language, and the contents of the README file associated with the repo by utilizing different functions that gathered those pieces of data from the github API.

- Both process were wrapped in a TQDM progress bar because the acquisition took about 45 minutes altogether, and having a progress bar allowed us to know if the function was still working, or if it had timed out.

### Preparing/Wrangling the Data

[[Back to top](#top)]

![]()


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - acquire.py 
    - prepare.py


### Takeaways from exploration:

__The top 5 Programing languages are__
- JavaScript
- Python
- TypeScript
- Shell
- C#

__The most commonly used top ten words have between 770 and nearly 3000 specific uses, respectively__


__Each of the top 5 programing languages have relatively specific bigrams when looking at most used__

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:
### Models Used:
- Will run the following Classification models:
  - Logistic Regression Model
  - Random Forest
  - Stochastic Gradient Descent (SGD)   
  -  
## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Accuracy (Train) | Accuracy (Test) | Diffrence |
| ---- | ----| ---- |---- |
| Logistic Regression Model | 0.82 | 0.61 |  0.21|
| Stochastic Gradient Descent (SGD) | 0.97 | 0.58 |0.39| 
| Random Forest | 0.87 | 0.62| 0.25| 

### Model 1: Logistic Regression Model

- Model 1 accuracy results:
      - 82% accuracy on Train


### Model 2 : Stochastic Gradient Descent (SGD)

- Model 2 results:
  - 97% accuracy on Train
  
  
### Model 3 : Random Forest

- Model 3 results:   
  - 87% accuracy on Train
  - 62% accuracy on Test
  
***

## - Random Forest Performed the Best @ 62% Test Accuracy

***

# <a name="conclusion"></a>Conclusion: 

## Key Items

- After testing multiple models, our best performer turned out to be random forest at 62%

- Through exploration we found that each programming language does have its own unique distribution of words

## Recomendations

- For the time being this model should be implemented until a better model can be implemented at a later date

## What's Next?

- With a many model approach based on each language as a target variable we may be able to create a model with much more accuracy at pinpointing select programming languages based on README text.

- through the use of many models we may better be able to make models detect more obscure languages along with the more commonly used ones.