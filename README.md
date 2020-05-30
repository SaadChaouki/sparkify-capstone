# Sparkify Capstone Project

## Description
This project is the final project of the Udacity Data Science nanodegree. The projects deals with the data of a fictional music streaming called Sparkify. A dataset was provided that contains the actions of users on the website in terms of pages visited, songs, time, and whether the users have downgraded (churn).

The goal of the project is to train a model that can predict whether a user is likely to churn using PySpark to handle the large amount of data as well as an app using Flask and Plotly to visualise the change of data overtime.

## Getting Started
### Prerequisite

* PySpark
* Flask
* Plotly
* Pandas
* Numpy

### Files

* **run.py**: Flask app with data visualisation.
* **sparkify.ipynb**: Exploration code to load, create features, and train different models to predict churn.


### Cloning

To run the code, clone this GIT repository:

`git clone https://github.com/SaadChaouki/sparkify-capstone.git`

### Executing

1. Run the following command in the app's directory to run your web app.
    `python run.py`

2. Go to http://127.0.0.1:5000

### Web Application

Screenshots of the application are included [here](https://github.com/SaadChaouki/sparkify-capstone/tree/master/screenshots).

## Project Summary

In this project, we looked at the use of PySpark to load, clean, engineer features, and train a model. Using PySpark gives the possibility to handle large volumes of data. The dataset that was used is a sample of a larger dataset that contains the interactions of users in a fictional music service similar to Spotify. Based on their behaviour, we needed to predict whether a user is going to churn or not.

### Feature Engineering

After cleaning the data to remove the rows that did not have any user assigned to them, we engineered a new set of features that show the change of behaviour of a user 2 weeks prior to their churn.

To achieve this, we set a 'date selection' for each user to extract their data. For the users who churned, this week was their last week using the service. For the users who stayed with Sparkify, the date was a random week. By doing this, we were able to see 2 weeks behaviour of users before they churned and compare it to users that did not churn. The predictions become more precise as we are predicting if a user is likely to churn in a week's time.

The reason why I followed this methodology is that simply grouping the variables by user will lead to a bias as users who churned are likely to have less interactions, therefore, we will be including some of the information that happened after the user left into the model.

### Modelling

For the modelling, we transformed the features into a vector before standardising them. The column 'label' is the output (churn) and the column 'features' is the features that we engineered. After doing that, the set was split into training, testing, and validation. However, one thing to consider here is that this made the training set even smaller than it already is.

We selected a logistic regression, decision tree, random forest, and gradient boosting tree as the models of choice. The best model was a gradient boosting and achieved an F1 score of 85% on the validation set.

### Areas for Improvement

Even though the results of the initial runs look promising, we need to take into consideration the number of data points that are used for this. We won't be able to get a good representation until we use the large dataset and train the model. We also need to include the validation set in the cross validation model as the model was overfitting and reached an almost perfect F-score on the training set while dropping the performance on the validation set.

Once using the larger data, we might start seeing a decline in the performance as we will have more variance. However, we can tackle this by looking into new models and tune the model even further.


## Author

* [Saad Chaouki](https://www.linkedin.com/in/schaouki/)

## Acknowledgements

* [Udacity](https://www.udacity.com/)
* [W3 School](https://www.w3schools.com/w3css/w3css_templates.asp)
