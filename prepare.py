import pandas as pd
import numpy as np

from utilities import split_dataframe

def prepare_telco_data(telco_df):

    # Change empty strings to np.nan so that we can fillna
    telco_df.total_charges.replace(" ", np.nan, inplace = True)

    # Replace nan total charges to monthly charges
    telco_df.total_charges.fillna(value=telco_df.monthly_charges, inplace=True)

    # These columns are redundant or provide no useful information
    drop_columns = ['Unnamed: 0', 'payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id']
    telco_df.drop(columns=drop_columns, inplace=True)

    # Replace No internet service or No phone service to No since they are pretty much the same
    telco_df.replace(to_replace="No phone service", value="No", inplace=True)
    telco_df.replace(to_replace="No internet service", value="No", inplace=True)

    # Convert total_charges to float
    telco_df.total_charges = telco_df.total_charges.astype(float)

    # These columns need to be encoded
    encode_dict = {'gender' : True,
                'partner' : True,
                'dependents' : True,
                'phone_service' : True,
                'multiple_lines' : True,
                'online_security' : True,
                'online_backup' : True,
                'device_protection' : True,
                'tech_support' : True,
                'streaming_tv' : True,
                'streaming_movies' : True,
                'paperless_billing' : True,
                'churn' : True,
                'contract_type' : False,
                'internet_service_type' : False,
                'payment_type' : False
                }
    dummies_df = pd.get_dummies(telco_df[list(encode_dict.keys())], dummy_na=False, drop_first=list(encode_dict.values()))

    # Merge dummies with telco_df
    telco_df = pd.concat([telco_df, dummies_df], axis=1)

    # Drop columns that are now encoded
    telco_df.drop(columns=list(encode_dict.keys()), inplace=True)

    return split_dataframe(telco_df, stratify_by="churn_Yes")