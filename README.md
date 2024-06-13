# Data Jobs Analysis

This repository contains the analysis of job postings data scraped from [datajobs.com](https://datajobs.com). The goal of this analysis is to preprocess the data, perform feature engineering, conduct exploratory data analysis (EDA), and select relevant features for further modeling.

## Table of Contents

- [Data Scraping](#data-scraping)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Selection](#feature-selection)
- [Requirements](#requirements)
- [Usage](#usage)
- [License](#license)

## Data Scraping

The data was scraped from [datajobs.com](https://datajobs.com) using a Python script. The script extracts job titles, companies, locations, job links, and job descriptions. Below is the scraping code used:

## Data Preprocessing
After scraping, the data underwent preprocessing steps to handle missing values and clean the data.

Filled missing values in the location column with 'Unknown'.
Feature Engineering
Several new features were engineered from the existing data to enhance the dataset:


### Seniority Level:

Created a seniority column by categorizing job titles into different levels (e.g., Junior, Mid, Senior, Intern).
Key Skills:
Extracted key skills/technologies from the description column.

## Exploratory Data Analysis (EDA)
EDA was performed to understand the data distribution and identify patterns:

#### Distribution of Seniority Levels:
Visualized the distribution of different seniority levels in the job postings.
#### Top Cities for Job Postings:
Identified the cities with the highest number of job postings.
#### Feature Selection
Relevant features were selected to prepare the data for modeling:

## Encoding Categorical Variables:
Converted categorical variables into numerical format using one-hot encoding.
### Corelation Matrix:
Visualized the correlation between different features to identify highly correlated variables.
Highly Correlated Features:

Selected features based on their correlation to ensure the model is built using the most informative features.
## Requirements
The following Python libraries are required to run the code:
- Pandas
- requests
- beautifulsoup4
- matplotlib
- seaborn
- wordcloud
- count

# License

This README file provides a detailed explanation of each step in the analysis process, from data scraping to feature selection, ensuring that anyone can understand and replicate the analysis.
