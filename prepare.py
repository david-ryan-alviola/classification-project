import pandas as pd
import numpy as np

from utilities import split_dataframe

def prepare_telco_data(df):
    telco_df = df.copy()
    prepped_telco_data = {}

    def clean_telco(telco_df):

        # Change empty strings to np.nan so that we can fillna
        telco_df.total_charges.replace(" ", np.nan, inplace = True)

        # Replace nan total charges to monthly charges
        telco_df.total_charges.fillna(value=telco_df.monthly_charges, inplace=True)

        # These columns are redundant or provide no useful information
        drop_columns = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'multiple_lines']
        telco_df.drop(columns=drop_columns, inplace=True)

        # Convert total_charges to float
        telco_df.total_charges = telco_df.total_charges.astype(float)
        
        # Simplify related columns by combining them
        telco_df['internet_extras'] = (telco_df.online_backup == "Yes") | (telco_df.online_security == "Yes") | (telco_df.device_protection == "Yes") | (telco_df.tech_support == "Yes")
        telco_df['streaming_entertainment'] = (telco_df.streaming_movies == "Yes") | (telco_df.streaming_tv == "Yes")
        telco_df['family'] = (telco_df.partner == "Yes") | (telco_df.dependents == "Yes")

        # Drop combined columns
        telco_df.drop(columns=['online_backup', 'online_security', 'device_protection', 'tech_support', 'streaming_movies', 'streaming_tv', 'partner', 'dependents'], inplace=True)

        # These columns need to be encoded
        drop_first_true = ['gender', 'phone_service', 'paperless_billing', 'churn']
        drop_first_false = ['contract_type', 'internet_service_type', 'payment_type']

        dummies_df1 = pd.get_dummies(telco_df[drop_first_true], dummy_na=False, drop_first=True)
        dummies_df2 = pd.get_dummies(telco_df[drop_first_false], dummy_na=False, drop_first=False)

        # Merge dummies with telco_df
        telco_df = pd.concat([telco_df, dummies_df1, dummies_df2], axis=1)

        # Drop columns that are now encoded
        telco_df.drop(columns=drop_first_false, inplace=True)
        telco_df.drop(columns=drop_first_true, inplace=True)

        # Remove spaces from encoded column names
        telco_df.rename(columns={'contract_type_One year' : 'contract_type_One_year',
                            'contract_type_Two year' : 'contract_type_Two_year',
                            'internet_service_type_Fiber optic' : 'internet_service_type_Fiber_optic',
                            'payment_type_Bank transfer (automatic)' : 'payment_type_Bank_transfer',
                            'payment_type_Credit card (automatic)' : 'payment_type_Credit_card',
                            'payment_type_Electronic check' : 'payment_type_Electronic_check',
                            'payment_type_Mailed check' : 'payment_type_Mailed_check'}, inplace=True)
        
        return telco_df

    prepped_telco_data['population'] = clean_telco(telco_df)
    prepped_telco_data['samples'] = split_dataframe(prepped_telco_data['population'], stratify_by="churn_Yes")

    return prepped_telco_data