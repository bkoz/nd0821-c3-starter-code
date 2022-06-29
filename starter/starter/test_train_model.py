"""
Unit tests for data loader and model trainer.

Author: Bob Kozdemba (bkozdemba@gmail.com)
Date: July 2022
"""
import pytest
import numpy as np
import sklearn
import train_model as t_model

def test_load_data() -> None:
    """
    Unit test for loading the data into a pandas data frame.
    """
    assert t_model.data.empty == False

def test_train_data() -> None:
    """
    Unit test for confirming the training set is not null.
    """
    assert type(t_model.X_train) == np.ndarray

def test_train_data() -> None:
    """
    Unit test for confirming the test set is not null.
    """
    assert type(t_model.X_test) == np.ndarray

def test_train_model() -> None:
    """
    Unit test to check for a trained model.
    """
    assert type(t_model.model) == sklearn.ensemble._forest.RandomForestClassifier
