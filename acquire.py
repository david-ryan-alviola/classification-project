from env import user, password, host
from utilities import generate_db_url, generate_df

def acquire_telco_churn_data():
    
    telco_query = """
    SELECT *
        FROM customers
            JOIN contract_types USING(contract_type_id)
            JOIN internet_service_types USING(internet_service_type_id)
            JOIN payment_types USING(payment_type_id);
    """

    return generate_df("telco_churn.csv", telco_query, generate_db_url(user, password, host, "telco_churn"))