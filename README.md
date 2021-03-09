# TELCO churn classification project:  A hit with customers overall, but misses with key groups
This project uses the TELCO Churn data set to create a classification model that predicts whether or not customers will churn.

## Goals
1. Identify possible drivers of churn for TELCO customers
2. Create a machine learning model that is used to predict customer churn
3. Provide a technical report on the process, findings, and recommendations

## Setup this project
* Dependencies
    1. [utilities.py](https://github.com/david-ryan-alviola/utilities/releases)
        * Use release 1.5.3 or greater
    2. python
    3. pandas
    4. scipy
    5. sklearn
    6. numpy
* Steps to recreate
    1. Clone this repository
    2. Install `utilities.py` according to the instructions
    3. Setup env.py
        * Remove the .dist extension (should result in `env.py`)
        * Fill in your user_name, password, and host
        * If you did not install `utilities.py` in your cloned repository, replace the "/path/to/utilities" string with the path to where `utilities.py` is installed
    4. Open `telco_churn_analysis.ipynb` and run the cells
    
## Key Findings
1. Low churn rate overall, but significant increase in churn for month-to-month and fiber optic customers
2. Possible drivers are the above average monthly charges for month-to-month and fiber optic customers
3. Churned customers tend to last only 18 months and even less for month-to-month and fiber optic customers.
4. We can predict churn with 76% accuracy.
    
## The Plan
The Kanban board used for planning is [here](https://trello.com/b/ipr1KRLX).

We wanted to examine these four possibilities:
1. Dependency between month-to-month contracts and churn
2. Dependency between fiber and churn
3. Correlation between tenure and monthly charges
4. Month-to-month fiber customers and monthly charges

Data will be acquired from the *telco_churn* database and prepared accordingly based on initial examination.

After preparation, we will explore the data by performing statistical testing to support or reject our alternative hypotheses and evaluate the results with `utilities.py`. Visual exploration will be performed with `explore.py`.

We will select features for modeling based on the results from our hypothesis testing and from our exploration. A baseline accuracy will be established by selecting the most common churn value of our training data and finding its occurence. Four classification models will be evaluated:
1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors
4. Logistic Regression

The best performing model in terms of accuracy, churn recall, and false negative rate will be selected for fine tuning and validation.

We will select the model that best maximizes overall accuracy and churn recall while minimizing the false negative rate. This model will be evaluated with the test data.

## Data Dictionary

Name | Description | Type
:---: | :---: | :---:
senior_citizen | Indicates if customer is a senior citizen | int
tenure | Months customer has subscribed to service | int
monthly_charges | Dollar cost per month | float
total_charges | Dollar cost accumulated during tenure | float
internet_extras | Indicates if customer pays for internet add-ons | int
streaming_entertainment | Indicates if customer has streaming movies or tv | int
family | Indicates if customer has dependents or partner | int
gender_Male | Indicates if customer identifies as male | int
phone_service_Yes | Indicates if customer has at least 1 phone line | int
paperless_billing_Yes | Indicates if customer uses paperless billing | int
churn_Yes | Indicates if customer has left the company | int
contract_type_Month-to-month | Indicates if customer pays on a monthly basis | int
contract_type_One_year | Indicates if customer pays annually | int
contract_type_Two_year | Indicates if customer pays bi-annually | int
internet_service_type_DSL | Indicates if customer has DSL internet | int
internet_service_type_Fiber_optic | Indicates if customer has fiber optic internet | int
internet_service_type_None | Indicates if customer does not have internet | int
payment_type_Bank_transfer | Indicates if customer pays using a bank account | int
payment_type_Credit_card | Indicates if customer pays using a credit card | int
payment_type_Electronic_check | Indicates if customer pays using e-check | int
payment_type_Mailed_check | Indicates if customer pays using paper check | int

## Results
Original results are found [here](https://drive.google.com/file/d/18vnvnSJPfsEhv2MpF-X3bKvr3kAHr6uX/view?usp=sharing).

## Recommendations
1. Reduce monthly cost and incentivize tenure
2. Continue fine tuning model
3. Explore other features
