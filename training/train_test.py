import lightgbm
import numpy as np
import pandas as pd

# functions to test are imported from train.py
from train import split_data, train_model, get_model_metrics

"""
A set of simple unit tests for protecting against regressions in train.py
"""


def test_split_data():
    """
    This function tests the split_data function.
    
    prints
    -------
    The test results.
    
    execution
    ---------
    test_data: dict
        The test data.
        
    data_df: DataFrame
        The test data in a DataFrame.
        
    data: tuple
        The split data.
    """
    test_data = {
        'id': [0, 1, 2, 3, 4],
        'target': [0, 0, 1, 0, 1],
        'col1': [1, 2, 3, 4, 5],
        'col2': [2, 1, 1, 2, 1]
        }

    data_df = pd.DataFrame(data=test_data)
    data = split_data(data_df)

    # verify that columns were removed correctly
    assert "target" not in data[0].data.columns
    assert "id" not in data[0].data.columns
    assert "col1" in data[0].data.columns

    # verify that data was split as desired
    assert data[0].data.shape == (4, 2)
    assert data[1].data.shape == (1, 2)


def test_train_model():
    """
    This function trains the model.
    
    execution
    ---------
    data: tuple
        The split data.
        
    params: dict
        The parameters for the model.
        
    model: object
        The trained model.
    """
    data = __get_test_datasets()

    params = {
        "learning_rate": 0.05,
        "metric": "auc",
        "min_data": 1
    }

    model = train_model(data, params)

    # verify that parameters are passed in to the model correctly
    for param_name in params.keys():
        assert param_name in model.params
        assert params[param_name] == model.params[param_name]


def test_get_model_metrics():
    """
    This function tests the get_model_metrics function.
    """
    class MockModel:

        @staticmethod
        def predict(data):
            return np.array([0, 0])

    data = __get_test_datasets()

    metrics = get_model_metrics(MockModel(), data)

    # verify that metrics is a dictionary containing the auc value.
    assert "auc" in metrics
    auc = metrics["auc"]
    np.testing.assert_almost_equal(auc, 0.5)


def __get_test_datasets():
    """
    This is a helper function to set up some test data
    """
    X_train = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)
    y_train = np.array([1, 1, 0, 1, 0, 1])
    X_test = np.array([7, 8]).reshape(-1, 1)
    y_test = np.array([0, 1])

    train_data = lightgbm.Dataset(X_train, y_train)
    valid_data = lightgbm.Dataset(X_test, y_test)
    data = (train_data, valid_data)
    return data
