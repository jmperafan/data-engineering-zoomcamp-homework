from datetime import date

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
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
        .loc[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]
        .assign(lpep_pickup_date=lambda x: x['lpep_pickup_datetime'].dt.date)
        .rename(columns={
            'VendorID': 'vendor_id',
            'RatecodeID': 'ratecode_id',
            'PULocationID': 'pu_location_id',
            'DOLocationID': 'do_location_id'
        })
    )

@test
def test_output(output, *args) -> None:
    """
    Test the output DataFrame to ensure it meets specified conditions.
    """
    # Check if 'vendor_id' contains only 1 and 2
    assert set(output['vendor_id']) == {1, 2}, "Invalid 'vendor_id' values found."

    # Check if 'passenger_count' is greater than 0 for all rows
    assert (output['passenger_count'] > 0).all(), "'passenger_count' should be greater than 0 for all rows."

    # Check if 'trip_distance' is greater than 0 for all rows
    assert (output['trip_distance'] > 0).all(), "'trip_distance' should be greater than 0 for all rows."

    # Check if the 'lpep_pickup_date' is in months 10, 11, and 12 of 2020
    assert (output['lpep_pickup_date'].min() >= date(2020, 10, 1)), "'lpep_pickup_date' should be after 2020-10-01"
    assert (output['lpep_pickup_date'].max() <= date(2020, 12, 31)), "'lpep_pickup_date' should be before 2020-12-31"
