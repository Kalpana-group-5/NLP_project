

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

### Nice to haves (With more time):



***

## <a name="findings"></a>Key Findings:
[[Back to top](#top)]




***

## <a name="dictionary"></a>Data Dictionary  
[[Back to top](#top)]

### Data Used
---
| Attribute | Definition | Data Type |
| ----- | ----- | ----- |
| | | |
| | | |
| | | |
| | | |
| | | |
| | | |

***

## <a name="wrangle"></a>Data Acquisition and Preparation
[[Back to top](#top)]

![]()


### Wrangle steps: 


*********************

## <a name="explore"></a>Data Exploration:
[[Back to top](#top)]
- Python files used for exploration:
    - acquire.py 
    - prepare.py


### Takeaways from exploration:

***

## <a name="model"></a>Modeling:
[[Back to top](#top)]

### Model Preparation:

### Baseline
    
- Baseline Results: 
    

- Selected features to input into models:
    - features = []

***

### Models and R<sup>2</sup> Values:
- Will run the following regression models:

    

- Other indicators of model performance with breif defiition and why it's important:

    
    
#### Model 1: Linear Regression (OLS)


- Model 1 results:



### Model 2 : Lasso Lars Model


- Model 2 results:


### Model 3 : Tweedie Regressor (GLM)

- Model 3 results:


### Model 4: Quadratic Regression Model

- Model 4 results:


## Selecting the Best Model:

### Use Table below as a template for all Modeling results for easy comparison:

| Model | Validation/Out of Sample RMSE | R<sup>2</sup> Value |
| ---- | ----| ---- |
| Baseline | 0.167366 | 2.2204 x 10<sup>-16</sup> |
| Linear Regression (OLS) | 0.166731 | 2.1433 x 10<sup>-3</sup> |  
| Tweedie Regressor (GLM) | 0.155186 | 9.4673 x 10<sup>-4</sup>|  
| Lasso Lars | 0.166731 | 2.2204 x 10<sup>-16</sup> |  
| Quadratic Regression | 0.027786 | 2.4659 x 10<sup>-3</sup> |  


- {} model performed the best


## Testing the Model

- Model Testing Results

***

## <a name="conclusion"></a>Conclusion:
[[Back to top](#top)]
