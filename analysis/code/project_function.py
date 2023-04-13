import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import code.project_function


def load_and_process(path):
    df4=(pd.read_csv('../../project-group-group45C/data/raw/day.csv')
     .dropna(axis=0) 
    )
    df5=(df4
    .drop(columns=['weathersit','temp','atemp','hum','windspeed','casual','registered','instant'])
    )
    return df5

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .code import project_function
else:
    import sys
    sys.path.append("./code")
    import project_function
    
def dropsth(path):
    df5=(pd.read_csv('../../project-group-group45C/data/raw/day.csv')
         .drop(columns=['weathersit','temp','atemp','hum','windspeed','casual','registered','instant'])
    )
    return df5

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .code import project_function
else:
    import sys
    sys.path.append("./code")
    import project_function



