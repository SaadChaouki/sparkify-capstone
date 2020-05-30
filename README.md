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

`git clone https://github.com/SaadChaouki/disaster-response-project.git`

### Executing

1. Run the following command in the app's directory to run your web app.
    `python run.py`

2. Go to http://127.0.0.1:5000

### Web Application

Screenshots of the application are included [here]().

### Conclusions

In this project, we looked at the use of PySpark to load, clean, engineering features, and train a model. Using PySpark gives the possibility to handle large volumes of data. The dataset that was used is a sample of a larger dataset that contains the interactions of users in a fictional music service similar to Spotify. Based on their behaviour, we needed to predict whether a use is going to churn or not.

After cleaning the data to remove the rows that did not have any user assigned to them, we engineering a new set o features that show the behaviour changes of users 2 weeks before churning. To achieve this, we set a 'date selection' for each user to extract their data. For the users who churned, this week was their last week using the services. For the users who stayed with Sparkify, the date was a random week. By doing this, we were able to see 2 weeks behaviour of users before they churned and compare it to users that did not churn. The predictions become more precise as we are predicting if a user is likely to churn in a week's time.


### Author

* [Saad Chaouki](https://www.linkedin.com/in/schaouki/)

### Acknowledgements

* [Udacity](https://www.udacity.com/)
* [W3 School](https://www.w3schools.com/w3css/w3css_templates.asp)
