# TELCO Churn Classification Project
This project uses the TELCO Churn data set to create a classification model that predicts whether or not customers will churn.

## Setup this project
* Dependencies
    1. [utilities.py](https://github.com/david-ryan-alviola/utilities)
        * Use release 1.5.3 or greater
    2. pandas
    3. scipy
    4. sklearn
    5. numpy
* Steps to recreate
    1. Clone this repository
    2. Install `utilities.py` according to the instructions
    3. Setup env.py
        * Remove the .dist extension (should result in `env.py`)
        * Fill in your user_name, password, and host
        * If you did not install `utilities.py` in your cloned repository, put the path in `util_path`
    4. Open `telco_churn_analysis.ipynb` and run the cells
    
## Planning
The Kanban board used for planning is [here](https://trello.com/b/ipr1KRLX).

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
