import os
import sys
import dill # This is used to create pickle file. Pickel file stores data object in a serialized form.

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    

# This utils.py file typically contains helper functions or common code that can be reused across different parts of the poject.
# It's a way to keep your code clean