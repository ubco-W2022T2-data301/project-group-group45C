import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path):
    df4=(pd.read_csv('../../project-group-group45C/data/raw/day.csv')
     .dropna(axis=0) 
    )
    df5=(df4
    .drop(columns=['weathersit','temp','atemp','hum','windspeed','casual','registered','instant'])
    )
    return df5

import sys
    sys.path.append("./code")
    import project_function