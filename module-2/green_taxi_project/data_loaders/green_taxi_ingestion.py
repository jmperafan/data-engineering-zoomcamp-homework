import io
import pandas as pd
import requests

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

years = [2020]
months = [10,11,12]
base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/'

taxi_dtypes = {
    'VendorID':pd.Int64Dtype(),
    'passenger_count': pd.Int64Dtype(),
    'trip_distance': float,
    'RatecodeID':pd.Int64Dtype(),
    'store_and_fwd_flag':str,
    'PULocationID':pd.Int64Dtype(),
    'DOLocationID':pd.Int64Dtype(),
    'Payment_type': pd.Int64Dtype(),
    'fare_amount':float,
    'extra':float,
    'mta_tax':float,
    'tip_amount':float,
    'tolls_amount':float,
    'improvement_surcharge':float,
    'total_amount': float,
    'congestion_surcharge':float
}

@data_loader
def load_data(base_url: str, years: list, months: list, taxi_dtypes: dict, *args, **kwargs) -> pd.DataFrame:
    """
    Load Green Taxi data for specified years and months from the given base URL.

    Parameters:
    - base_url (str): The base URL for Green Taxi data files.
    - years (list): A list of years for which data needs to be loaded.
    - months (list): A list of months for which data needs to be loaded.
    - taxi_dtypes (dict): A dictionary specifying the data types for each column.

    Returns:
    - pd.DataFrame: A DataFrame containing the loaded Green Taxi data.
    """
    
    return pd.concat(
        [
            pd.read_csv(
                f'{base_url}green_tripdata_{year}-{month:02d}.csv.gz', 
                sep=',',
                compression='gzip',
                dtype=taxi_dtypes, 
                parse_dates['lpep_pickup_datetime', 'lpep_dropoff_datetime']
            )
        for year in years for month in months
        ], 
        ignore_index=True
    )

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'