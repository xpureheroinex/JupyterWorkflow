from workflow.data import get_data
import pandas as pd

def test_get_data():
    data = get_data()
    assert all(data.columns == ['East', 'West', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
