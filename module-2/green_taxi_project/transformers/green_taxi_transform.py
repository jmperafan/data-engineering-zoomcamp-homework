if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
    """
    This function does 3 transformation steps to the data:
    - Filters the data (no trips without distance or without passengers).
    - Transforms lpep_pickup_datetime into a date.
    - Modifies the colnames that were in camelcase into snake case. 

    Parameters:
    - data (pd.DataFrame): Input DataFrame containing Green Taxi data.
    """
    return (
        data
        .loc[(data[passenger_col] > 0) & (data[distance_col] > 0)]
        .assign(lpep_pickup_date=lambda x: x['lpep_pickup_datetime'].dt.date)
        .rename(columns={
            'VendorID': 'vendor_id',
            'RatecodeID': 'ratecode_id',
            'PULocationID': 'pu_location_id',
            'DOLocationID': 'do_location_id'
        })
    )

@test
def test_output(output: pd.DataFrame, *args) -> None:
    """
    Test the output DataFrame to ensure it meets specified conditions.
    """
    # Check if 'vendor_id' contains only 1 and 2
    assert set(output['vendor_id']) == {1, 2}, "Invalid 'vendor_id' values found."

    # Check if 'passenger_count' is greater than 0 for all rows
    assert (output['passenger_count'] > 0).all(), "'passenger_count' should be greater than 0 for all rows."

    # Check if 'trip_distance' is greater than 0 for all rows
    assert (output['trip_distance'] > 0).all(), "'trip_distance' should be greater than 0 for all rows."